from twilio.rest.resources import InstanceResource, ListResource
from twilio.rest.resources.media import MediaList
from twilio.rest.resources.util import normalize_dates, parse_date


class Message(InstanceResource):
    subresources = [MediaList]


class Messages(ListResource):
    name = "Messages"
    key = "messages"
    instance = Message

    def create(self, from_=None, **kwargs):
        """
        Create and send a Message.

        :param string to: The destination phone number.
        :param string `from_`: The phone number sending this message
            (must be a verified Twilio number)
        :param string body: The message you want to send,
            limited to 1600 characters.
        :param list media_url: A list of URLs of images to include in the
            message.
        :param status_callback: A URL that Twilio will POST to when
            your message is processed.
        :param string application_sid: The 34 character sid of the application
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

    def update(self, sid, **kwargs):
        """ Updates the message for the given sid
        :param sid: The sid of the message to update.
        """
        return self.update_instance(sid, kwargs)

