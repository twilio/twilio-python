from twilio.rest.base import TwilioClient
from twilio.rest.resources import UNSET_TIMEOUT
from twilio.rest.resources.pricing import (
    PhoneNumbers,
    Voice,
    Messaging,
)


class TwilioPricingClient(TwilioClient):
    """
    A client for accessing the Twilio Pricing API.

    :param str account: Your Account SID from `your dashboard
        <https://twilio.com/user/account>`_
    :param str token: Your Auth Token from `your dashboard
        <https://twilio.com/user_account>`_
    :param float timeout: The socket connect and read timeout for requests
    to Twilio
    """

    def __init__(self, account=None, token=None,
                 base="https://pricing.twilio.com", version="v1",
                 timeout=UNSET_TIMEOUT):
        super(TwilioPricingClient, self).__init__(account, token, base,
                                                  version, timeout)

        self.uri_base = "{}/{}".format(base, version)

        self.voice = Voice(self.uri_base, self.auth, self.timeout)
        self.phone_numbers = PhoneNumbers(self.uri_base, self.auth,
                                          self.timeout)
        self.messaging = Messaging(self.uri_base, self.auth, self.timeout)
