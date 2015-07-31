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

        countries = VoiceCountries(BASE_URI, AUTH)
        result = countries.list()

        assert_equal(result[0].iso_country, "AD")
        assert_equal(len(result), 50)

        request.assert_called_with(
            "GET",
            "{0}/Voice/Countries".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False,
            params={},
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_voice_country(self, request):
        resp = create_mock_json('tests/resources/pricing/voice_country_instance.json')
        resp.status_code = 200
        request.return_value = resp

        countries = VoiceCountries(BASE_URI, AUTH)
        country = countries.get('AU')

        assert_equal(country.country, "Australia")
        assert_equal(
            country.inbound_call_prices[0],
            {
                'number_type': 'local',
                'current_price': '0.0075',
                'base_price': '0.0075'
            },
        )

        request.assert_called_with(
            "GET",
            "{0}/Voice/Countries/AU".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False,
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_voice_number(self, request):
        resp = create_mock_json('tests/resources/pricing/voice_number_instance.json')
        resp.status_code = 200
        request.return_value = resp

        numbers = VoiceNumbers(BASE_URI, AUTH)
        result = numbers.get('+14089673429')

        assert_equal(result.number, '+14089673429')
        assert_equal(result.price_unit, 'usd')

        request.assert_called_with(
            "GET",
            "{0}/Voice/Numbers/+14089673429".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False,
        )
