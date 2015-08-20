import unittest
from tests.integration import config
from tests.integration.api_responses import (
    NextGenGETRequestHandler as GRH,
)
from twilio.ext.holodeck import holodeck
from twilio.rest import TwilioLookupsClient


class TwilioLookupsClientTest(unittest.TestCase):

    def setUp(self):
        self.client = TwilioLookupsClient(config.account_sid,
                                          config.auth_token)
        holodeck.activate()

    def tearDown(self):
        holodeck.deactivate()

    def test_lookups_phone_number(self):
        self.client.phone_numbers.get('+15108675309')
