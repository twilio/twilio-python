# -*- coding: utf-8 -*-
import sys
from typing import Optional, List, Dict


class TwilioException(Exception):
    pass


class TwilioRestException(TwilioException):
    """A generic 400 or 500 level exception from the Twilio API

    :param int status: the HTTP status that was returned for the exception
    :param str uri: The URI that caused the exception
    :param str msg: A human-readable message for the error
    :param int|None code: A Twilio-specific error code for the error. This is
         not available for all errors.
    :param method: The HTTP method used to make the request
    :param details: Additional error details returned for the exception
    """

    def __init__(
        self,
        status: int,
        uri: str,
        msg: str = "",
        code: Optional[int] = None,
        method: str = "GET",
        details: Optional[object] = None,
    ):
        self.uri = uri
        self.status = status
        self.msg = msg
        self.code = code
        self.method = method
        self.details = details

    def __str__(self) -> str:
        """Try to pretty-print the exception, if this is going on screen."""

        def red(words: str) -> str:
            return "\033[31m\033[49m%s\033[0m" % words

        def white(words: str) -> str:
            return "\033[37m\033[49m%s\033[0m" % words

        def blue(words: str) -> str:
            return "\033[34m\033[49m%s\033[0m" % words

        def teal(words: str) -> str:
            return "\033[36m\033[49m%s\033[0m" % words

        def get_uri(code: int) -> str:
            return "https://www.twilio.com/docs/errors/{0}".format(code)

        # If it makes sense to print a human readable error message, try to
        # do it. The one problem is that someone might catch this error and
        # try to display the message from it to an end user.
        if hasattr(sys.stderr, "isatty") and sys.stderr.isatty():
            msg = (
                "\n{red_error} {request_was}\n\n{http_line}"
                "\n\n{twilio_returned}\n\n{message}\n".format(
                    red_error=red("HTTP Error"),
                    request_was=white("Your request was:"),
                    http_line=teal("%s %s" % (self.method, self.uri)),
                    twilio_returned=white("Twilio returned the following information:"),
                    message=blue(str(self.msg)),
                )
            )
            if self.code:
                msg = "".join(
                    [
                        msg,
                        "\n{more_info}\n\n{uri}\n\n".format(
                            more_info=white("More information may be available here:"),
                            uri=blue(get_uri(self.code)),
                        ),
                    ]
                )
            return msg
        else:
            return "HTTP {0} error: {1}".format(self.status, self.msg)


class TwilioServiceException(TwilioException):
    """An RFC-9457 compliant exception from a Twilio service

    This exception follows the Problem Details for HTTP APIs specification
    (RFC-9457). See https://www.rfc-editor.org/rfc/rfc9457.html

    :param str type: A URI reference that identifies the problem type
    :param str title: A short, human-readable summary of the problem type
    :param int status: The HTTP status code for this occurrence of the problem
    :param int code: Twilio-specific error code
    :param str|None detail: A human-readable explanation specific to this occurrence
    :param str|None instance: A URI reference identifying the specific occurrence
    :param list|None errors: Array of validation errors with detail and pointer fields
    :param str method: The HTTP method used to make the request
    :param str uri: The URI that caused the exception
    """

    def __init__(
        self,
        type_uri: str,
        title: str,
        status: int,
        code: int,
        detail: Optional[str] = None,
        instance: Optional[str] = None,
        errors: Optional[List[Dict[str, str]]] = None,
        method: str = "GET",
        uri: str = "",
    ):
        self.type = type_uri
        self.title = title
        self.status = status
        self.code = code
        self.detail = detail
        self.instance = instance
        self.errors = errors or []
        self.method = method
        self.uri = uri

    def __str__(self) -> str:
        """Pretty-print the exception for terminal output."""

        def red(words: str) -> str:
            return "\033[31m\033[49m%s\033[0m" % words

        def white(words: str) -> str:
            return "\033[37m\033[49m%s\033[0m" % words

        def blue(words: str) -> str:
            return "\033[34m\033[49m%s\033[0m" % words

        def teal(words: str) -> str:
            return "\033[36m\033[49m%s\033[0m" % words

        def yellow(words: str) -> str:
            return "\033[33m\033[49m%s\033[0m" % words

        # Check if we're in a TTY for colored output
        if hasattr(sys.stderr, "isatty") and sys.stderr.isatty():
            msg_parts = [
                "\n{red_error} {request_was}\n\n{http_line}\n\n{twilio_returned}\n".format(
                    red_error=red("HTTP Error"),
                    request_was=white("Your request was:"),
                    http_line=(
                        teal("%s %s" % (self.method, self.uri))
                        if self.uri
                        else teal("(no URI)")
                    ),
                    twilio_returned=white("Twilio returned the following information:"),
                )
            ]

            # Title and detail
            msg_parts.append(
                "\n{title_label}: {title}\n".format(
                    title_label=white("Title"),
                    title=blue(self.title),
                )
            )

            if self.detail:
                msg_parts.append(
                    "{detail_label}: {detail}\n".format(
                        detail_label=white("Detail"),
                        detail=blue(self.detail),
                    )
                )

            # Code and status
            msg_parts.append(
                "{code_label}: {code} | {status_label}: {status}\n".format(
                    code_label=white("Error Code"),
                    code=blue(str(self.code)),
                    status_label=white("Status"),
                    status=blue(str(self.status)),
                )
            )

            # Validation errors if present
            if self.errors:
                msg_parts.append(
                    "\n{validation_label}:\n".format(
                        validation_label=white("Validation Errors"),
                    )
                )
                for error in self.errors:
                    msg_parts.append(
                        "  {pointer}: {detail}\n".format(
                            pointer=yellow(error.get("pointer", "(unknown field)")),
                            detail=error.get("detail", "(no detail)"),
                        )
                    )

            # Documentation link
            msg_parts.append(
                "\n{more_info}\n\n{uri}\n\n".format(
                    more_info=white("More information may be available here:"),
                    uri=blue(self.type),
                )
            )

            return "".join(msg_parts)
        else:
            # Plain text output for non-TTY
            msg = "HTTP {0} error: {1}".format(self.status, self.title)
            if self.detail:
                msg += " - {0}".format(self.detail)
            if self.errors:
                msg += " | Validation errors: {0}".format(
                    ", ".join(
                        "{0} ({1})".format(e.get("pointer", "?"), e.get("detail", "?"))
                        for e in self.errors
                    )
                )
            return msg
