import json
from typing import Any

from twilio.base.exceptions import TwilioServiceException
from twilio.base.version import Version
from twilio.http.response import Response


class ApiV1Version(Version):
    """
    Represents an API version with RFC-9457 compliant error handling.

    This class extends Version to provide support for RFC-9457 (Problem Details for HTTP APIs)
    error responses. When a service returns an RFC-9457 compliant error, it will be wrapped
    in a TwilioServiceException.
    """

    @classmethod
    def exception(
        cls, method: str, uri: str, response: Response, error_payload: Any = None
    ) -> TwilioServiceException:
        """
        Wraps an exceptional response in a `TwilioServiceException`

        Response should be RFC-9457 compliant (contains 'type', 'title', 'status', and 'code' fields),
        returns a TwilioServiceException.

        :param method: HTTP method used for the request
        :param uri: URI that was requested
        :param response: HTTP response object
        :param error_payload: Pre-parsed error payload
        :return: TwilioServiceException
        """
        return TwilioServiceException(
            type_uri=error_payload["type"],
            title=error_payload["title"],
            status=error_payload["status"],
            code=error_payload["code"],
            detail=error_payload.get("detail"),
            instance=error_payload.get("instance"),
            errors=error_payload.get("errors"),
            method=method,
            uri=uri,
        )

    def _parse_fetch(self, method: str, uri: str, response: Response) -> Any:
        """
        Parses fetch response JSON with RFC-9457 error handling
        """
        # Note that 3XX response codes are allowed for fetches.
        if response.status_code < 200 or response.status_code >= 400:
            # Try to parse error payload
            error_payload = None
            try:
                error_payload = json.loads(response.text)
            except Exception:
                pass

            raise self.exception(method, uri, response, error_payload)

        return json.loads(response.text)

    def _parse_update(self, method: str, uri: str, response: Response) -> Any:
        """
        Parses update response JSON with RFC-9457 error handling
        """
        if response.status_code < 200 or response.status_code >= 300:
            # Try to parse error payload
            error_payload = None
            try:
                error_payload = json.loads(response.text)
            except Exception:
                pass

            raise self.exception(method, uri, response, error_payload)

        return json.loads(response.text)

    def _parse_delete(self, method: str, uri: str, response: Response) -> bool:
        """
        Parses delete response with RFC-9457 error handling
        """
        if response.status_code < 200 or response.status_code >= 300:
            # Try to parse error payload
            error_payload = None
            try:
                error_payload = json.loads(response.text)
            except Exception:
                pass

            raise self.exception(method, uri, response, error_payload)

        return True  # if response code is 2XX, deletion was successful

    def _parse_create(self, method: str, uri: str, response: Response) -> Any:
        """
        Parse create response JSON with RFC-9457 error handling
        """
        if response.status_code < 200 or response.status_code >= 300:
            # Try to parse error payload
            error_payload = None
            try:
                error_payload = json.loads(response.text)
            except Exception:
                pass

            raise self.exception(method, uri, response, error_payload)

        return json.loads(response.text)
