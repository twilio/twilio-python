import logging
import os
import platform

from ..exceptions import TwilioException
from .. import __version__ as LIBRARY_VERSION
from .resources import (
    make_request,
    Accounts,
    Activities,
    Events,
    Applications,
    AuthorizedConnectApps,
    CallerIds,
    Calls,
    Conferences,
    ConnectApps,
    Connection,
    DependentPhoneNumbers,
    MediaList,
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
    UNSET_TIMEOUT,
    Usage,
    CallFeedbackFactory,
    CallFeedback,
    Reservations,
    TaskQueues,
    Tasks,
    Workers,
    Workflows,
    Workspaces,
)


def find_credentials(environ=None):
    """
    Look in the current environment for Twilio credentials

    :param environ: the environment to check
    """
    environment = environ or os.environ
    try:
        account = environment["TWILIO_ACCOUNT_SID"]
        token = environment["TWILIO_AUTH_TOKEN"]
        return account, token
    except KeyError:
        return None, None


def set_twilio_proxy(proxy_url, proxy_port):
    Connection.set_proxy_info(proxy_url, proxy_port)


class TwilioClient(object):
    def __init__(self, account=None, token=None, base="https://api.twilio.com",
                 version="2010-04-01",
                 timeout=UNSET_TIMEOUT):
        """
        Create a Twilio API client.
        """

        # Get account credentials
        if not account or not token:
            account, token = find_credentials()
            if not account or not token:
                raise TwilioException("""
Twilio could not find your account credentials. Pass them into the
TwilioRestClient constructor like this:

    client = TwilioRestClient(account='AC38135355602040856210245275870',
                              token='2flnf5tdp7so0lmfdu3d')

Or, add your credentials to your shell environment. From the terminal, run

    echo "export TWILIO_ACCOUNT_SID=AC3813535560204085626521" >> ~/.bashrc
    echo "export TWILIO_AUTH_TOKEN=2flnf5tdp7so0lmfdu3d7wod" >> ~/.bashrc

and be sure to replace the values for the Account SID and auth token with the
values from your Twilio Account at https://www.twilio.com/user/account.
""")

        self.base = base
        self.auth = (account, token)
        self.timeout = timeout
        self.account_uri = "{0}/{1}/Accounts/{2}".format(base,
                                                         version, account)

    def dependent_phone_numbers(self, address_sid):
        """
        Return a :class:`DependentPhoneNumbers
        <twilio.rest.resources.DependentPhoneNumbers>` instance for the
        :class:`Address <twilio.rest.resources.Address>` with the given
        address_sid
        """
        base_uri = "%s/Addresses/%s" % (self.account_uri, address_sid)
        return DependentPhoneNumbers(base_uri, self.auth, self.timeout)

    def request(self, path, method=None, vars=None):
        """sends a request and gets a response from the Twilio REST API

        .. deprecated:: 3.0

        :param path: the URL (relative to the endpoint URL, after the /v1
        :param url: the HTTP method to use, defaults to POST
        :param vars: for POST or PUT, a dict of data to send

        :returns: Twilio response in XML or raises an exception on error
        :raises: a :exc:`ValueError` if the path is invalid
        :raises: a :exc:`NotImplementedError` if the method is unknown

        This method is only included for backwards compatability reasons.
        It will be removed in a future version
        """
        logging.warning(":meth:`TwilioRestClient.request` is deprecated and "
                        "will be removed in a future version")

        vars = vars or {}
        params = None
        data = None

        if not path or len(path) < 1:
            raise ValueError('Invalid path parameter')
        if method and method not in ['GET', 'POST', 'DELETE', 'PUT']:
            raise NotImplementedError(
                'HTTP %s method not implemented' % method)

        if path[0] == '/':
            uri = self.base + path
        else:
            uri = self.base + '/' + path

        if method == "GET":
            params = vars
        elif method == "POST" or method == "PUT":
            data = vars

        user_agent = "twilio-python %s (python-%s)" % (
            LIBRARY_VERSION,
            platform.python_version(),
        )

        headers = {
            "User-Agent": user_agent,
            "Accept-Charset": "utf-8",
        }

        resp = make_request(method, uri, auth=self.auth, data=data,
                            params=params, headers=headers)

        return resp.content


class TwilioRestClient(TwilioClient):
    """
    A client for accessing the Twilio REST API

    :param str account: Your Account SID from `your dashboard
        <https://twilio.com/user/account>`_
    :param str token: Your Auth Token from `your dashboard
        <https://twilio.com/user/account>`_
    :param float timeout: The socket and read timeout for requests to Twilio
    """

    def __init__(self, account=None, token=None, base="https://api.twilio.com",
                 version="2010-04-01", timeout=UNSET_TIMEOUT):
        """
        Create a Twilio REST API client.
        """
        super(TwilioRestClient, self).__init__(account, token, base, version,
                                               timeout)

        version_uri = "%s/%s" % (base, version)

        self.accounts = Accounts(version_uri, self.auth, timeout)
        self.applications = Applications(self.account_uri, self.auth, timeout)
        self.authorized_connect_apps = AuthorizedConnectApps(
            self.account_uri,
            self.auth,
            timeout
        )
        self.calls = Calls(self.account_uri, self.auth, timeout)
        self.caller_ids = CallerIds(self.account_uri, self.auth, timeout)
        self.connect_apps = ConnectApps(self.account_uri, self.auth, timeout)
        self.notifications = Notifications(self.account_uri, self.auth,
                                           timeout)
        self.recordings = Recordings(self.account_uri, self.auth, timeout)
        self.transcriptions = Transcriptions(self.account_uri, self.auth,
                                             timeout)
        self.sms = Sms(self.account_uri, self.auth, timeout)
        self.phone_numbers = PhoneNumbers(self.account_uri, self.auth, timeout)
        self.conferences = Conferences(self.account_uri, self.auth, timeout)
        self.queues = Queues(self.account_uri, self.auth, timeout)
        self.sandboxes = Sandboxes(self.account_uri, self.auth, timeout)
        self.usage = Usage(self.account_uri, self.auth, timeout)
        self.messages = Messages(self.account_uri, self.auth, timeout)
        self.media = MediaList(self.account_uri, self.auth, timeout)
        self.sip = Sip(self.account_uri, self.auth, timeout)
        self.tokens = Tokens(self.account_uri, self.auth, timeout)

    def participants(self, conference_sid):
        """
        Return a :class:`~twilio.rest.resources.Participants` instance for the
        :class:`~twilio.rest.resources.Conference` with given conference_sid
        """
        base_uri = "%s/Conferences/%s" % (self.account_uri, conference_sid)
        return Participants(base_uri, self.auth, self.timeout)

    def members(self, queue_sid):
        """
        Return a :class:`Members <twilio.rest.resources.Members>` instance for
        the :class:`Queue <twilio.rest.resources.Queue>` with the
        given queue_sid
        """
        base_uri = "%s/Queues/%s" % (self.account_uri, queue_sid)
        return Members(base_uri, self.auth, self.timeout)

    def feedback(self, call_sid):
        """
        Return a :class:`CallFeedback <twilio.rest.resources.CallFeedback>`
        instance for the :class:`Call <twilio.rest.resources.calls.Call>`
        with the given call_sid
        """
        base_uri = "%s/Calls/%s/Feedback" % (self.account_uri, call_sid)
        call_feedback_list = CallFeedbackFactory(
            base_uri,
            self.auth,
            self.timeout
        )
        return CallFeedback(call_feedback_list)


class TwilioTaskRouterClient(TwilioClient):
    """
    A client for accessing the Twilio TaskRouter API

    :param str account: Your Account SID from `your dashboard
        <https://twilio.com/user/account>`_
    :param str token: Your Auth Token from `your dashboard
        <https://twilio.com/user/account>`_
    :param float timeout: The socket and read timeout for requests to Twilio
    """

    def __init__(self, account=None, token=None,
                 base="https://taskrouter.twilio.com", version="v1",
                 timeout=UNSET_TIMEOUT):
        """
        Create a Twilio REST API client.
        """
        super(TwilioTaskRouterClient, self).__init__(account, token, base,
                                                     version, timeout)
        self.base_uri = "{0}/{1}".format(base, version)
        self.workspace_uri = "{0}/Workspaces".format(self.base_uri)

        self.workspaces = Workspaces(self.base_uri, self.auth, timeout)

    def activities(self, workspace_sid):
        """
        Return a :class:`Activities` instance for the :class:`Activity`
        with the given workspace_sid
        """
        base_uri = "{0}/{1}".format(self.workspace_uri, workspace_sid)
        return Activities(base_uri, self.auth, self.timeout)

    def events(self, workspace_sid):
        """
        Return a :class:`Events` instance for the :class:`Event` with the given
        workspace_sid
        """
        base_uri = "{0}/{1}".format(self.workspace_uri, workspace_sid)
        return Events(base_uri, self.auth, self.timeout)

    def reservations(self, workspace_sid, task_sid):
        """
        Return a :class:`Reservations` instance for the :class:`Reservation`
        with the given workspace_sid ans task_sid
        """
        base_uri = "{0}/{1}/Tasks/{2}".format(self.workspace_uri,
                                              workspace_sid, task_sid)
        return Reservations(base_uri, self.auth, self.timeout)

    def task_queues(self, workspace_sid):
        """
        Return a :class:`TaskQueues` instance for the :class:`TaskQueue` with
        the given workspace_sid
        """
        base_uri = "{0}/{1}".format(self.workspace_uri, workspace_sid)
        return TaskQueues(base_uri, self.auth, self.timeout)

    def tasks(self, workspace_sid):
        """
        Return a :class:`Tasks` instance for the :class:`Task` with the given
        workspace_sid
        """
        base_uri = "{0}/{1}".format(self.workspace_uri, workspace_sid)
        return Tasks(base_uri, self.auth, self.timeout)

    def workers(self, workspace_sid):
        """
        Return a :class:`Workers` instance for the :class:`Worker` with the
        given workspace_sid
        """
        base_uri = "{0}/{1}".format(self.workspace_uri, workspace_sid)
        return Workers(base_uri, self.auth, self.timeout)

    def workflows(self, workspace_sid):
        """
        Return a :class:`Workflows` instance for the :class:`Workflow` with the
        given workspace_sid
        """
        base_uri = "{0}/{1}".format(self.workspace_uri, workspace_sid)
        return Workflows(base_uri, self.auth, self.timeout)
