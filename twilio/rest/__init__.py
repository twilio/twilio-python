import logging
import os
import platform
from ..exceptions import TwilioException
from .. import __version__ as LIBRARY_VERSION
from .resources import (
    make_request,
    Accounts,
    Applications,
    AuthorizedConnectApps,
    CallerIds,
    Calls,
    Conferences,
    ConnectApps,
    Connection,
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
    Transcriptions,
    UNSET_TIMEOUT,
    Usage,
    CallFeedbackFactory,
    CallFeedback,
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


class TwilioRestClient(object):
    """
    A client for accessing the Twilio REST API

    :param str account: Your Account SID from `your dashboard
        <https://twilio.com/user/account>`_
    :param str token: Your Auth Token from `your dashboard
        <https://twilio.com/user/account>`_
    :param float timeout: The socket and read timeout for requests to Twilio
    """

    def __init__(self, account=None, token=None, base="https://api.twilio.com",
                 version="2010-04-01", client=None, timeout=UNSET_TIMEOUT):
        """
        Create a Twilio REST API client.
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
        auth = (account, token)
        version_uri = "%s/%s" % (base, version)
        account_uri = "%s/%s/Accounts/%s" % (base, version, account)

        self.accounts = Accounts(version_uri, auth, timeout)
        self.applications = Applications(account_uri, auth, timeout)
        self.authorized_connect_apps = AuthorizedConnectApps(
            account_uri,
            auth,
            timeout
        )
        self.calls = Calls(account_uri, auth, timeout)
        self.caller_ids = CallerIds(account_uri, auth, timeout)
        self.connect_apps = ConnectApps(account_uri, auth, timeout)
        self.notifications = Notifications(account_uri, auth, timeout)
        self.recordings = Recordings(account_uri, auth, timeout)
        self.transcriptions = Transcriptions(account_uri, auth, timeout)
        self.sms = Sms(account_uri, auth, timeout)
        self.phone_numbers = PhoneNumbers(account_uri, auth, timeout)
        self.conferences = Conferences(account_uri, auth, timeout)
        self.queues = Queues(account_uri, auth, timeout)
        self.sandboxes = Sandboxes(account_uri, auth, timeout)
        self.usage = Usage(account_uri, auth, timeout)
        self.messages = Messages(account_uri, auth, timeout)
        self.media = MediaList(account_uri, auth, timeout)
        self.sip = Sip(account_uri, auth, timeout)

        self.auth = auth
        self.account_uri = account_uri
        self.timeout = timeout

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
