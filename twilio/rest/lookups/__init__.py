from twilio.rest.resources.lookups.phone_numbers import PhoneNumbers
from twilio.rest.lookups.client import RestClient as TwilioLookupsClientBase


class TwilioLookupsClient(TwilioLookupsClientBase):
    """
    A client for accessing the Twilio Lookups API.

    The Twilio Lookups API provides information about phone numbers,
    including non-Twilio numbers. For more information, see the
    `Lookups API documentation <https://www.twilio.com/docs/XXX>`_.

    :param str account: Your Account Sid from `your dashboard
        <https://www.twilio.com/user/account>`_
    :param str token: Your Auth Token from `your dashboard
        <https://www.twilio.com/user/account>`_
    :param float timeout: The socket and read timeout for requests to Twilio
    """

    def __init__(self, *args, **kwargs):
        super(TwilioLookupsClient, self).__init__(*args, **kwargs)

        self.phone_numbers = PhoneNumbers(self.version_uri, self.auth, self.timeout)
