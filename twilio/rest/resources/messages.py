from .media import MediaList
from .util import normalize_dates, parse_date

from twilio.rest.v2010.account.message import (
    Message as BaseMessage,
    Messages as BaseMessages
)

class Message(BaseMessage):

    subresources = [MediaList]

    def redact(self):
        """Redact this Message's `body` field from Twilio while preserving
        the record itself and related metadata.
        """
        return self.parent.redact(self.sid)


class Messages(BaseMessages):
    instance = Message

    def create(self, from_=None, **kwargs):
        """
        Create and send a Message.

        :param str to: The destination phone number.
        :param str `from_`: The phone number sending this message
            (must be a verified Twilio number)
        :param str body: The message you want to send,
            limited to 1600 characters.
        :param list media_url: A list of URLs of images to include in the
            message.
        :param status_callback: A URL that Twilio will POST to when
            your message is processed.
        :param str application_sid: The 34 character sid of the application
            Twilio should use to handle this phone call.
        """
        kwargs["from"] = from_
        return self.create_instance(kwargs)

    @normalize_dates
    def list(self, from_=None, before=None, after=None, date_sent=None, **kw):
        """
        Returns a page of :class:`Message` resources as a list. For
        paging information see :class:`ListResource`.

        :param to: Only show messages to this phone number.
        :param from_: Only show messages from this phone number.
        :param date after: Only list messages sent after this date.
        :param date before: Only list message sent before this date.
        :param date date_sent: Only list message sent on this date.
        :param `from_`: Only show messages from this phone number.
        :param date after: Only list messages logged after this datetime
        :param date before: Only list messages logged before this datetime
        """
        kw["From"] = from_
        kw["DateSent<"] = before
        kw["DateSent>"] = after
        kw["DateSent"] = parse_date(date_sent)
        return self.get_instances(kw)

    def redact(self, sid):
        """Redact the specified Message record's Body field."""
        return self.update_instance(sid, {'Body': ''})
