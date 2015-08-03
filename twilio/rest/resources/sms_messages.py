from .util import normalize_dates, parse_date

from twilio.rest.v2010.account.sms.short_code import (
    ShortCode,
    ShortCodes as BaseShortCodes,
)
from twilio.rest.v2010.account.sms import Sms as BaseSms
from twilio.rest.v2010.account.sms.sms_message import (
    SmsMessage,
    SmsMessages as BaseSmsMessages,
)


class ShortCodes(BaseShortCodes):

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


class SmsMessages(BaseSmsMessages):

    def create(self, from_=None, **kwargs):
        """
        Create and send a SMS Message.

        :param str to: The destination phone number.
        :param str `from_`: The phone number sending this message
            (must be a verified Twilio number)
        :param str body: The message you want to send,
            limited to 160 characters.
        :param status_callback: A URL that Twilio will POST to when
            your message is processed.
        :param str application_sid: The 34 character sid of the application
            Twilio should use to handle this phone call.

        Usage:

        .. code-block::python

            message = client.sms.messages.create(to="+12316851234",
                from_="+15555555555",
                body="Hello there!")

        """
        return super(SmsMessages, self).create(from_=from_, **kwargs)

    @normalize_dates
    def list(self, from_=None, before=None, after=None, date_sent=None, **kw):
        """
        Returns a page of :class:`~twilio.rest.resources.SmsMessage` resources
        as a list. For paging information see :class:`ListResource`.

        :param to: Only show SMS messages to this phone number.
        :param from_: Only show SMS messages from this phone number.
        :param date after: Only list SMS messages sent after this date.
        :param date before: Only list SMS message sent before this date.
        :param date date_sent: Only list SMS message sent on this date.
        :param `from_`: Only show SMS messages from this phone number.
        :param date after: Only list SMS messages logged after this datetime
        :param date before: Only list SMS messages logged before this datetime
        """
        return super(SmsMessages, self).list(from_=from_,
                                             date_sent=date_sent,
                                             date_sent_before=before,
                                             date_sent_after=after)


class Sms(BaseSms):
    def __init__(self, base_uri, auth, timeout):
        self.messages = SmsMessages(base_uri, auth, timeout)
        self.short_codes = ShortCodes(base_uri, auth, timeout)
