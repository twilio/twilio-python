from twilio.rest.resources.util import normalize_dates, parse_date
from twilio.rest.resources import InstanceResource, ListResource


class ShortCode(InstanceResource):

    def update(self, **kwargs):
        return self.parent.update(self.name, **kwargs)


class ShortCodes(ListResource):

    name = "ShortCodes"
    key = "short_codes"
    instance = ShortCode

    def list(self, **kwargs):
        """
        Returns a page of :class:`ShortCode` resources as a list. For
        paging information see :class:`ListResource`.

        :param short_code: Only show the ShortCode resources that match this
                           pattern. You can specify partial numbers and use '*'
                           as a wildcard for any digit.
        :param friendly_name: Only show the ShortCode resources with friendly
                              names that exactly match this name.
        """
        return self.get_instances(kwargs)

    def update(self, sid, url=None, method=None, fallback_url=None,
               fallback_method=None, **kwargs):
        """
        Update a specific :class:`ShortCode`, by specifying the sid.

        :param friendly_name: Description of the short code, with maximum
                              length 64 characters.
        :param api_version: SMSs to this short code will start a new TwiML
                            session with this API version.
        :param url: The URL that Twilio should request when somebody sends an
                    SMS to the short code.
        :param method: The HTTP method that should be used to request the url.
        :param fallback_url: A URL that Twilio will request if an error occurs
                             requesting or executing the TwiML at the url.
        :param fallback_method: The HTTP method that should be used to request
                                the fallback_url.
        """
        kwargs["sms_url"] = kwargs.get("sms_url", url)
        kwargs["sms_method"] = kwargs.get("sms_method", method)
        kwargs["sms_fallback_url"] = \
            kwargs.get("sms_fallback_url", fallback_url)
        kwargs["sms_fallback_method"] = \
            kwargs.get("sms_fallback_method", fallback_method)
        return self.update_instance(sid, kwargs)


class Sms(object):
    """
    Holds all the specific SMS list resources
    """

    name = "SMS"
    key = "sms"

    def __init__(self, base_uri, auth):
        self.uri = "%s/SMS" % base_uri
        self.messages = SmsMessages(self.uri, auth)
        self.short_codes = ShortCodes(self.uri, auth)


class SmsMessage(InstanceResource):
    pass


class SmsMessages(ListResource):

    name = "Messages"
    key = "sms_messages"
    instance = SmsMessage

    def create(self, from_=None, **kwargs):
        """
        Create and send a SMS Message.

        :param string to: The destination phone number.
        :param string `from_`: The phone number sending this message
            (must be a verified Twilio number)
        :param string body: The message you want to send,
            limited to 160 characters.
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
        Returns a page of :class:`SMSMessage` resources as a list. For
        paging informtion see :class:`ListResource`.

        :param to: Only show SMS messages to this phone number.
        :param from_: Only show SMS messages from this phone number.
        :param date after: Only list SMS messages sent after this date.
        :param date before: Only list SMS message sent before this date.
        :param date date_sent: Only list SMS message sent on this date.
        :param `from_`: Only show SMS messages from this phone number.
        :param date after: Only list recordings logged after this datetime
        :param date before: Only list recordings logged before this datetime
        """
        kw["From"] = from_
        kw["DateSent<"] = before
        kw["DateSent>"] = after
        kw["DateSent"] = parse_date(date_sent)
        return self.get_instances(kw)
