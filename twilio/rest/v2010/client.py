# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.base import TwilioClient
from twilio.rest.resources import UNSET_TIMEOUT
from twilio.rest.v2010.account import Accounts
from account.address import Addresses
from account.application import Applications
from account.authorized_connect_app import AuthorizedConnectApps
from account.available_phone_number import AvailablePhoneNumberCountries
from account.call import Calls
from account.conference import Conferences
from account.connect_app import ConnectApps
from account.incoming_phone_number import IncomingPhoneNumbers
from account.message import Messages
from account.notification import Notifications
from account.outgoing_caller_id import OutgoingCallerIds
from account.queue import Queues
from account.recording import Recordings
from account.sandbox import Sandboxes
from account.sip import Sip
from account.sms import Sms
from account.token import Tokens
from account.transcription import Transcriptions
from account.usage import Usage


class V2010Client(TwilioClient):
    """
    A client for accessing the Twilio V2010 API.
    
    :param str account: :param str account: Your Account SID from `your
    dashboard
        <https://twilio.com/user/account>`_
    :param str timeout: :param float timeout: The socket connect and read
    timeout
        for requests to Twilio
    :param str token: :param str account: Your Account SID from `your dashboard
        <https://twilio.com/user/account>`_
    """

    def __init__(self, account=None, token=None, base="https://api.twilio.com",
                 version="2010-04-01", timeout=UNSET_TIMEOUT, client=None):
        super(V2010Client, self).__init__(account, token, base, version, timeout, client)
        
        self.version_uri = "{}/{}".format(base, version)
        self.accounts = Accounts(self.client, self.version_uri, self.auth, self.timeout)
        
        account_sid = account
        if account_sid:
            base_instance_uri = "{}/Accounts/{}.json".format(self.version_uri, account_sid)
            self.addresses = Addresses(self.client, base_instance_uri, self.auth, self.timeout)
            self.applications = Applications(self.client, base_instance_uri, self.auth, self.timeout)
            self.authorized_connect_apps = AuthorizedConnectApps(self.client, base_instance_uri, self.auth, self.timeout)
            self.available_phone_numbers = AvailablePhoneNumberCountries(self.client, base_instance_uri, self.auth, self.timeout)
            self.calls = Calls(self.client, base_instance_uri, self.auth, self.timeout)
            self.conferences = Conferences(self.client, base_instance_uri, self.auth, self.timeout)
            self.connect_apps = ConnectApps(self.client, base_instance_uri, self.auth, self.timeout)
            self.incoming_phone_numbers = IncomingPhoneNumbers(self.client, base_instance_uri, self.auth, self.timeout)
            self.messages = Messages(self.client, base_instance_uri, self.auth, self.timeout)
            self.notifications = Notifications(self.client, base_instance_uri, self.auth, self.timeout)
            self.outgoing_caller_ids = OutgoingCallerIds(self.client, base_instance_uri, self.auth, self.timeout)
            self.queues = Queues(self.client, base_instance_uri, self.auth, self.timeout)
            self.recordings = Recordings(self.client, base_instance_uri, self.auth, self.timeout)
            self.sandbox = Sandboxes(self.client, base_instance_uri, self.auth, self.timeout)
            self.sip = Sip(self.client, base_instance_uri, self.auth, self.timeout)
            self.sms = Sms(self.client, base_instance_uri, self.auth, self.timeout)
            self.tokens = Tokens(self.client, base_instance_uri, self.auth, self.timeout)
            self.transcriptions = Transcriptions(self.client, base_instance_uri, self.auth, self.timeout)
            self.usage = Usage(self.client, base_instance_uri, self.auth, self.timeout)
