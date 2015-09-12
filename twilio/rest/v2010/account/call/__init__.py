# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.resources.util import (
    parse_date,
    parse_iso_date,
)
from twilio.rest.resources.base import InstanceResource
from twilio.rest.v2010.account.call.recording import (
    Recording,
    Recordings,
)
from twilio.rest.v2010.account.call.notification import (
    Notification,
    Notifications,
)
from twilio.rest.v2010.account.call.feedback import (
    Feedback,
    Feedbacks,
)
from twilio.rest.resources.base import ListResource
from twilio.rest.v2010.account.call.feedback_summary import (
    FeedbackSummaries,
    FeedbackSummary,
)


class Call(InstanceResource):
    """
    .. attribute:: account_sid
    
        The unique id of the Account responsible for creating this Call
    
    .. attribute:: annotation
    
        The annotation provided for the Call
    
    .. attribute:: answered_by
    
        If this call was initiated with answering machine detection, either
        `human` or `machine`. Empty otherwise.
    
    .. attribute:: api_version
    
        The API Version the Call was created through
    
    .. attribute:: caller_name
    
        If this call was an incoming call to a phone number with Caller ID
        Lookup enabled, the caller's name. Empty otherwise.
    
    .. attribute:: date_created
    
        The date that this resource was created
    
    .. attribute:: date_updated
    
        The date that this resource was last updated
    
    .. attribute:: direction
    
        A string describing the direction of the call. `inbound` for inbound
        calls, `outbound-api` for calls initiated via the REST API or
        `outbound-dial` for calls initiated by a `<Dial>` verb.
    
    .. attribute:: duration
    
        The duration
    
    .. attribute:: end_time
    
        The end time of the Call. Null if the call did not complete
        successfully.
    
    .. attribute:: forwarded_from
    
        If this Call was an incoming call forwarded from another number, the
        forwarding phone number (depends on carrier supporting forwarding).
        Empty otherwise.
    
    .. attribute:: from
    
        The phone number, SIP address or Client identifier that made this Call.
        Phone numbers are in E.164 format (e.g. +16175551212). SIP addresses are
        formatted as `name@company.com`. Client identifiers are formatted
        `client:name`.
    
    .. attribute:: from_formatted
    
        The phone number, SIP address or Client identifier that made this Call.
        Formatted for display.
    
    .. attribute:: group_sid
    
        A 34 character Group Sid associated with this Call. Empty if no Group is
        associated with the Call.
    
    .. attribute:: parent_call_sid
    
        A 34 character string that uniquely identifies the Call that created
        this leg.
    
    .. attribute:: phone_number_sid
    
        If the call was inbound, this is the Sid of the IncomingPhoneNumber that
        received the call. If the call was outbound, it is the Sid of the
        OutgoingCallerId from which the call was placed.
    
    .. attribute:: price
    
        The charge for this call, in the currency associated with the account.
        Populated after the call is completed. May not be immediately available.
    
    .. attribute:: price_unit
    
        The currency in which `Price` is measured.
    
    .. attribute:: sid
    
        A 34 character string that uniquely identifies this resource.
    
    .. attribute:: start_time
    
        The start time of the Call. Null if the call has not yet been dialed.
    
    .. attribute:: status
    
        The status
    
    .. attribute:: subresource_uris
    
        A Map of various subresources available for the given Call Instance
    
    .. attribute:: to
    
        The phone number, SIP address or Client identifier that received this
        Call. Phone numbers are in E.164 format (e.g. +16175551212). SIP
        addresses are formatted as `name@company.com`. Client identifiers are
        formatted `client:name`.
    
    .. attribute:: to_formatted
    
        The phone number, SIP address or Client identifier that received this
        Call. Formatted for display.
    
    .. attribute:: uri
    
        The URI for this resource, relative to `https://api.twilio.com`
    """
    id_key = "sid"
    ANSWERED = "answered"
    BUSY = "busy"
    CANCELED = "canceled"
    COMPLETED = "completed"
    FAILED = "failed"
    IN_PROGRESS = "in-progress"
    INITIATED = "initiated"
    NO_ANSWER = "no-answer"
    QUEUED = "queued"
    RINGING = "ringing"
    subresources = [
        Recordings,
        Notifications,
        Feedbacks
    ]

    def load(self, *args, **kwargs):
        super(Call, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)
        
        if hasattr(self, "end_time") and self.end_time:
            self.end_time = parse_iso_date(self.end_time)
        
        if hasattr(self, "start_time") and self.start_time:
            self.start_time = parse_iso_date(self.start_time)

    def delete(self):
        """
        Once the record is deleted, it will no longer appear in the API and Account Portal logs.
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()

    def update(self, **kwargs):
        """
        Initiates a call redirect or terminates a call
        
        :param call.status status: Either `canceled` or `completed`. Specifying
            `canceled` will attempt to hangup calls that are queued or ringing but not
            affect calls already in progress. Specifying `completed` will attempt to hang up
            a call even if it's already in progress.
        :param str fallback_method: The HTTP method that Twilio should use to request
            the `FallbackUrl`. Must be either `GET` or `POST`. Defaults to `POST`.
        :param str fallback_url: A URL that Twilio will request if an error occurs
            requesting or executing the TwiML at `Url`.
        :param str method: The HTTP method Twilio should use when requesting the URL.
            Defaults to `POST`.
        :param str status_callback: A URL that Twilio will request when the call ends to
            notify your app.
        :param str status_callback_method: The HTTP method that Twilio should use to
            request the `StatusCallback`. Defaults to `POST`.
        :param str url: A valid URL that returns TwiML. Twilio will immediately redirect
            the call to the new TwiML upon execution.
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Call`
        """
        return self.update_instance(kwargs)

    def redirect_to(self, url, **kwargs):
        """ Route the call to another url """
        return self.update(url=url, **kwargs)

    def cancel(self, **kwargs):
        """
        Cancel the call
        
        If the called is queued or ringing, cancel the calls. Will not affect in
        progress calls.
        """
        return self.update(status='canceled', **kwargs)

    def hangup(self, **kwargs):
        """
        Hangup the call
        
        If this call is currently active, hang up the call. If this call is scheduled to
        be made, remove the call from the queue. Will not affect in progress calls.
        """
        return self.update(status='completed', **kwargs)


class Calls(ListResource):
    name = "Calls"
    mount_name = "calls"
    key = "calls"
    instance = Call

    def __init__(self, *args, **kwargs):
        super(Calls, self).__init__(*args, **kwargs)
        self.feedback_summaries = FeedbackSummaries(*args, **kwargs)

    def create(self, to, from_, **kwargs):
        """
        Create a new outgoing call to phones, SIP-enabled endpoints or Twilio Client connections
        
        :param bool record: Set this parameter to true to record the entirety of a phone
            call. The RecordingUrl will be sent to the StatusCallback URL. Defaults to
            false.
        :param str application_sid: The 34 character sid of the application Twilio
            should use to handle this phone call. If this parameter is present, Twilio will
            ignore all of the voice URLs passed and use the URLs set on the application.
        :param str fallback_method: The HTTP method that Twilio should use to request
            the `FallbackUrl`. Must be either `GET` or `POST`. Defaults to `POST`. If an
            `ApplicationSid` was provided, this parameter is ignored.
        :param str fallback_url: A URL that Twilio will request if an error occurs
            requesting or executing the TwiML at `Url`. If an `ApplicationSid` was provided,
            this parameter is ignored.
        :param str from_: The phone number or client identifier to use as the caller id.
            If using a phone number, it must be a Twilio number or a Verified outgoing
            caller id for your account.
        :param str if_machine: Tell Twilio to try and determine if a machine (like
            voicemail) or a human has answered the call. Possible value are `Continue` and
            `Hangup`.
        :param str method: The HTTP method Twilio should use when requesting the URL.
            Defaults to `POST`. If an `ApplicationSid` was provided, this parameter is
            ignored.
        :param str send_digits: A string of keys to dial after connecting to the number.
            Valid digits in the string include: any digit (`0`-`9`), '`#`', '`*`' and '`w`'
            (to insert a half second pause). For example, if you connected to a company
            phone number, and wanted to pause for one second, dial extension 1234 and then
            the pound key, use `ww1234#`.
        :param str status_callback: A URL that Twilio will request when the call ends to
            notify your app. If an `ApplicationSid` was provided, this parameter is ignored.
        :param str status_callback_method: The HTTP method that Twilio should use to
            request the `StatusCallback`. Defaults to `POST`. If an `ApplicationSid` was
            provided, this parameter is ignored.
        :param str timeout: The integer number of seconds that Twilio should allow the
            phone to ring before assuming there is no answer. Default is `60` seconds, the
            maximum is `999` seconds. Note, you could set this to a low value, such as `15`,
            to hangup before reaching an answering machine or voicemail.
        :param str to: The phone number, SIP address or client identifier to call.
        :param str url: The fully qualified URL that should be consulted when the call
            connects. Just like when you set a URL on a phone number for handling inbound
            calls.
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Call`
        """
        kwargs["To"] = to
        kwargs["From"] = from_
        return self.create_instance(kwargs)

    def delete(self, sid):
        """
        Delete a call record from your account.
        
        Once the record is deleted, it will no longer appear in the API and Account
        Portal logs.
        
        :param str sid: The Call Sid that uniquely identifies the Call to delete
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def get(self, sid):
        """
        Fetch the Call specified by the provided Call Sid
        
        :param str sid: The Call Sid that uniquely identifies the Call to fetch
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Call`
        :returns: A placeholder for a :class:`Call` resource
        """
        return self.get_instance(sid)

    def list(self, **kwargs):
        """
        Retrieves a collection of Calls made to and from your account
        
        :param date end_time: Only show call that ended on this date
        :param date end_time_after: Only show calls that ended after this date
        :param date end_time_before: Only show calls that ended before this date
        :param date start_time: Only show calls that started on this date
        :param date start_time_after: Only show calls that started after this date
        :param date start_time_before: Only show calls that started before this date
        :param feedback_summary.status status: Only show calls currently in this status
        :param str from_: Only show calls from this phone number or Client identifier
        :param str parent_call_sid: Only show calls spawned by the call with this Sid
        :param str to: Only show calls to this phone number or Client identifier
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Call`
        """
        if "from_" in kwargs:
            kwargs["From"] = kwargs["from_"]
            del kwargs["from_"]
        if "start_time_before" in kwargs:
            kwargs["StartTime<"] = parse_date(kwargs["start_time_before"])
            del kwargs["start_time_before"]
        if "start_time_after" in kwargs:
            kwargs["StartTime>"] = parse_date(kwargs["start_time_after"])
            del kwargs["start_time_after"]
        if "start_time" in kwargs:
            kwargs["StartTime"] = parse_date(kwargs["start_time"])
            del kwargs["start_time"]
        if "end_time_before" in kwargs:
            kwargs["EndTime<"] = parse_date(kwargs["end_time_before"])
            del kwargs["end_time_before"]
        if "end_time_after" in kwargs:
            kwargs["EndTime>"] = parse_date(kwargs["end_time_after"])
            del kwargs["end_time_after"]
        if "end_time" in kwargs:
            kwargs["EndTime"] = parse_date(kwargs["end_time"])
            del kwargs["end_time"]
        return self.get_instances(kwargs)

    def update(self, sid, **kwargs):
        """
        Initiates a call redirect or terminates a call
        
        :param feedback_summary.status status: Either `canceled` or `completed`.
            Specifying `canceled` will attempt to hangup calls that are queued or ringing
            but not affect calls already in progress. Specifying `completed` will attempt to
            hang up a call even if it's already in progress.
        :param str fallback_method: The HTTP method that Twilio should use to request
            the `FallbackUrl`. Must be either `GET` or `POST`. Defaults to `POST`.
        :param str fallback_url: A URL that Twilio will request if an error occurs
            requesting or executing the TwiML at `Url`.
        :param str method: The HTTP method Twilio should use when requesting the URL.
            Defaults to `POST`.
        :param str sid: The Call Sid that uniquely identifies the Call to update
        :param str status_callback: A URL that Twilio will request when the call ends to
            notify your app.
        :param str status_callback_method: The HTTP method that Twilio should use to
            request the `StatusCallback`. Defaults to `POST`.
        :param str url: A valid URL that returns TwiML. Twilio will immediately redirect
            the call to the new TwiML upon execution.
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`Call`
        """
        return self.update_instance(sid, kwargs)

    def iter(self, **kwargs):
        """
        Retrieves a collection of Calls made to and from your account
        
        :param date end_time: Only show call that ended on this date
        :param date end_time_after: Only show calls that ended after this date
        :param date end_time_before: Only show calls that ended before this date
        :param date start_time: Only show calls that started on this date
        :param date start_time_after: Only show calls that started after this date
        :param date start_time_before: Only show calls that started before this date
        :param feedback_summary.status status: Only show calls currently in this status
        :param str from_: Only show calls from this phone number or Client identifier
        :param str parent_call_sid: Only show calls spawned by the call with this Sid
        :param str to: Only show calls to this phone number or Client identifier
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Call`
        """
        if "from_" in kwargs:
            kwargs["From"] = kwargs["from_"]
            del kwargs["from_"]
        if "start_time_before" in kwargs:
            kwargs["StartTime<"] = parse_date(kwargs["start_time_before"])
            del kwargs["start_time_before"]
        if "start_time_after" in kwargs:
            kwargs["StartTime>"] = parse_date(kwargs["start_time_after"])
            del kwargs["start_time_after"]
        if "start_time" in kwargs:
            kwargs["StartTime"] = parse_date(kwargs["start_time"])
            del kwargs["start_time"]
        if "end_time_before" in kwargs:
            kwargs["EndTime<"] = parse_date(kwargs["end_time_before"])
            del kwargs["end_time_before"]
        if "end_time_after" in kwargs:
            kwargs["EndTime>"] = parse_date(kwargs["end_time_after"])
            del kwargs["end_time_after"]
        if "end_time" in kwargs:
            kwargs["EndTime"] = parse_date(kwargs["end_time"])
            del kwargs["end_time"]
        return super(Calls, self).iter(**kwargs)

    def make(self, to, from_, url, **kwargs):
        """ An alias to create """
        return self.create(to=to, from_=from_, url=url, **kwargs)

    def redirect_to(self, sid, url, **kwargs):
        """ Route the call to another url """
        return self.update(sid, url=url, **kwargs)

    def cancel(self, sid, **kwargs):
        """
        Cancel the call
        
        If the called is queued or ringing, cancel the calls. Will not affect in
        progress calls.
        """
        return self.update(sid, status='canceled', **kwargs)

    def hangup(self, sid, **kwargs):
        """
        Hangup the call
        
        If this call is currently active, hang up the call. If this call is scheduled to
        be made, remove the call from the queue. Will not affect in progress calls.
        """
        return self.update(sid, status='completed', **kwargs)
