import unittest
from nose.tools import assert_equal

from mock import patch
from tests.tools import create_mock_json

from twilio.rest.resources.pricing.voice import (
    VoiceCountries,
    VoiceNumbers,
)


AUTH = ("AC123", "token")
BASE_URI = "https://pricing.twilio.com/v1"


class VoiceTest(unittest.TestCase):

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_voice_countries(self, request):
        resp = create_mock_json('tests/resources/pricing/voice_countries_list.json')
        resp.status_code = 200
        request.return_value = resp

        countries = VoiceCountries(BASE_URI + "/Voice", AUTH)
        result = countries.list()

        assert_equal(result[0].iso_country, "AC")
        assert_equal(len(result), 3)

        request.assert_called_with(
            "GET",
            "{0}/Voice/Countries".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False,
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_voice_country(self, request):
        resp = create_mock_json('tests/resources/pricing/voice_country_instance.json')
        resp.status_code = 200
        request.return_value = resp

        countries = VoiceCountries(BASE_URI + "/Voice", AUTH)
        country = countries.get('EE')

        assert_equal(country.country, "Estonia")
        assert_equal(
            country.inbound_call_prices[0],
            {
                'number_type': 'mobile',
                'call_base_price': 0.0075,
                'call_current_price': 0.0070
            },
        )

        request.assert_called_with(
            "GET",
            "{0}/Voice/Countries/EE".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False,
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_voice_number(self, request):
        resp = create_mock_json('tests/resources/pricing/voice_number_instance.json')
        resp.status_code = 200
        request.return_value = resp

        numbers = VoiceNumbers(BASE_URI + "/Voice", AUTH)
        result = numbers.get('+14089673429')

        assert_equal(result.number, '+14089673429')
        assert_equal(result.price_unit, 'usd')

        request.assert_called_with(
            "GET",
            "{0}/Voice/Numbers/+14089673429".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False,
        )
