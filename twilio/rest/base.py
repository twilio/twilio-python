import os

from twilio.exceptions import TwilioException
from twilio.rest.http import HttpClient
from twilio.rest.resources import Connection
from twilio.rest.resources import UNSET_TIMEOUT


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
                 timeout=UNSET_TIMEOUT,
                 client=None):
        """
        Create a Twilio API client.
        """
        if not client:
            client = HttpClient()

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
        self.client = client
        self.timeout = timeout
        self.account_uri = "{0}/{1}/Accounts/{2}".format(base,
                                                         version, account)
