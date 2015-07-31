from tests.integration import config
from tests.integration.api_responses import (
    NextGenGETRequestHandler as GRH,
)
from tests.integration.base_integration_test import BaseIntegrationTest
from tests.integration.test_rest_client_list import RESPONSE_HANDLERS
from twilio.rest import TwilioLookupsClient


class TwilioLookupsClientTest(BaseIntegrationTest):

    def setUp(self, base_uri=config.lookups_uri,
              response_handlers=RESPONSE_HANDLERS):
        super(TwilioLookupsClientTest, self).setUp(
            base_uri=base_uri, response_handlers=response_handlers)

        self.client = TwilioLookupsClient(config.account_sid,
                                          config.auth_token,
                                          base_uri)

    def test_lookups_phone_number(self):
        self.response_handlers = [
            GRH('/PhoneNumbers/+15108675309', 'lookups/phone_number_instance.json')
        ]

        self.client.phone_numbers.get('+15108675309')
