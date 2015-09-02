from twilio.rest.v2010.client import V2010Client
from twilio.rest.resources import (
    UNSET_TIMEOUT,
    Accounts,
    Applications,
    AuthorizedConnectApps,
    CallFeedback,
    CallFeedbackFactory,
    CallerIds,
    Calls,
    Conferences,
    ConnectApps,
    DependentPhoneNumbers,
    Members,
    Messages,
    Notifications,
    Participants,
    PhoneNumbers,
    Queues,
    Recordings,
    Sandboxes,
    Sip,
    Sms,
    Tokens,
    Transcriptions,
    Usage,
)


class TwilioRestClient(V2010Client):
    """
    A client for accessing the Twilio REST API

    :param str account: Your Account SID from `your dashboard
        <https://twilio.com/user/account>`_
    :param str token: Your Auth Token from `your dashboard
        <https://twilio.com/user/account>`_
    :param float timeout: The socket and read timeout for requests to Twilio
    """

    def __init__(self, account=None, token=None, base="https://api.twilio.com",
                 version="2010-04-01", timeout=UNSET_TIMEOUT, client=None):
        """
        Create a Twilio REST API client.
        """
        super(TwilioRestClient, self).__init__(account, token, base, version,
                                               timeout, client)

        self.accounts = Accounts(
            self.client, self.version_uri, self.auth, timeout
        )
        self.applications = Applications(
            self.client, self.account_uri, self.auth, timeout
        )
        self.authorized_connect_apps = AuthorizedConnectApps(
            self.client,
            self.account_uri,
            self.auth,
            timeout
        )
        self.calls = Calls(self.client, self.account_uri, self.auth, timeout)
        self.caller_ids = CallerIds(
            self.client, self.account_uri, self.auth, timeout
        )
        self.notifications = Notifications(
            self.client, self.account_uri, self.auth, timeout
        )
        self.recordings = Recordings(
            self.client, self.account_uri, self.auth, timeout
        )
        self.sms = Sms(self.client, self.account_uri, self.auth, timeout)
        self.phone_numbers = PhoneNumbers(
            self.client, self.account_uri, self.auth, timeout
        )
        self.conferences = Conferences(
            self.client, self.account_uri, self.auth, timeout
        )
        self.queues = Queues(
            self.client, self.account_uri, self.auth, timeout
        )
        self.sandboxes = self.sandbox

        self.messages = Messages(
            self.client, self.account_uri, self.auth, timeout
        )
        self.sip = Sip(
            self.client, self.account_uri, self.auth, timeout
        )
        self.tokens = Tokens(
            self.client, self.account_uri, self.auth, timeout
        )

    def participants(self, conference_sid):
        """
        Return a :class:`~twilio.rest.resources.Participants` instance for the
        :class:`~twilio.rest.resources.Conference` with given conference_sid
        """
        base_uri = "%s/Conferences/%s" % (self.account_uri, conference_sid)
        return Participants(self.client, base_uri, self.auth, self.timeout)

    def members(self, queue_sid):
        """
        Return a :class:`Members <twilio.rest.resources.Members>` instance for
        the :class:`Queue <twilio.rest.resources.Queue>` with the
        given queue_sid
        """
        base_uri = "%s/Queues/%s" % (self.account_uri, queue_sid)
        return Members(self.client, base_uri, self.auth, self.timeout)

    def feedback(self, call_sid):
        """
        Return a :class:`CallFeedback <twilio.rest.resources.CallFeedback>`
        instance for the :class:`Call <twilio.rest.resources.calls.Call>`
        with the given call_sid
        """
        base_uri = "%s/Calls/%s/Feedback" % (self.account_uri, call_sid)
        call_feedback_list = CallFeedbackFactory(
            self.client,
            base_uri,
            self.auth,
            self.timeout
        )
        return CallFeedback(call_feedback_list)

    def dependent_phone_numbers(self, address_sid):
        """
        Return a :class:`DependentPhoneNumbers
        <twilio.rest.resources.DependentPhoneNumbers>` instance for the
        :class:`Address <twilio.rest.resources.Address>` with the given
        address_sid
        """
        base_uri = "%s/Addresses/%s" % (self.account_uri, address_sid)
        return DependentPhoneNumbers(
            self.client, base_uri, self.auth, self.timeout
        )
