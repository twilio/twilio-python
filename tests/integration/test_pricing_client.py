from tests.integration import config
from tests.integration.api_responses import (
    NextGenGETRequestHandler as GRH
)
from tests.integration.base_integration_test import BaseIntegrationTest
from twilio.rest.pricing import TwilioPricingClient

RESPONSE_HANDLERS = []


class TwilioPricingClientTest(BaseIntegrationTest):

    def setUp(self, base_uri=config.pricing_uri,
              response_handlers=RESPONSE_HANDLERS):
        super(TwilioPricingClientTest, self).setUp(
            base_uri=base_uri, response_handlers=response_handlers)
        self.client = TwilioPricingClient(config.account_sid,
                                          config.auth_token,
                                          base_uri)

    def test_voice_list(self):
        self.response_handlers = [
            GRH('/Voice/Countries', 'pricing/voice_countries_list.json'),
            GRH('/Voice/Countries/AU', 'pricing/voice_country_instance.json', params=None),
            GRH('/Voice/Numbers/14089673429', 'pricing/voice_number_instance.json', params=None),
        ]

        self.client.voice.countries.list()
        self.client.voice.countries.get('AU')
        self.client.voice.numbers.get('14089673429')

    def test_phone_numbers_list(self):
        self.response_handlers = [
            GRH('/PhoneNumbers/Countries', 'pricing/phone_number_country_list.json'),
            GRH('/PhoneNumbers/Countries/EE', 'pricing/phone_number_country_instance.json', params=None)
        ]

        self.client.phone_numbers.countries.list()
        self.client.phone_numbers.countries.get('EE')
