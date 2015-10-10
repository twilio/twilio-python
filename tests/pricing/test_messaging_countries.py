import unittest
from mock import patch
from nose.tools import assert_equal
from tests.tools import create_mock_json
from twilio.rest.resources.pricing.messaging_countries import (
    MessagingCountries
)

AUTH = ("AC123", "token")
BASE_URI = "https://pricing.twilio.com/v1"


class MessagingCountriesTest(unittest.TestCase):

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_messaging_countries(self, request):
        resp = create_mock_json(
            'tests/resources/pricing/messaging_countries_list.json')
        resp.status_code = 200
        request.return_value = resp

        countries = MessagingCountries(BASE_URI + "/Messaging", AUTH)
        result = countries.list()

        assert_equal(result[0].iso_country, "AT")
        assert_equal(len(result), 2)

        request.assert_called_with(
            "GET",
            "{0}/Messaging/Countries".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False,
            params={}
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_messaging_country(self, request):
        resp = create_mock_json(
            'tests/resources/pricing/messaging_countries_instance.json')
        resp.status_code = 200
        request.return_value = resp

        countries = MessagingCountries(BASE_URI + "/Messaging", AUTH)
        result = countries.get('US')

        assert_equal(result.iso_country, "US")
        assert_equal(result.price_unit, "usd")
        assert_equal(result.outbound_sms_prices[0]['mcc'], "311")
        assert_equal(result.outbound_sms_prices[0]['mnc'], "484")
        assert_equal(result.outbound_sms_prices[0]['carrier'], "Verizon")
        prices = result.outbound_sms_prices[0]['prices']

        assert_equal(prices[0]['number_type'], "mobile")
        assert_equal(prices[0]['base_price'], "0.0075")
        assert_equal(prices[0]['current_price'], "0.0070")

        assert_equal(prices[1]['number_type'], "local")
        assert_equal(prices[1]['base_price'], "0.0075")
        assert_equal(prices[1]['current_price'], "0.0070")

        assert_equal(prices[2]['number_type'], "shortcode")
        assert_equal(prices[2]['base_price'], "0.01")
        assert_equal(prices[2]['current_price'], "0.01")

        assert_equal(prices[3]['number_type'], "toll-free")
        assert_equal(prices[3]['base_price'], "0.0075")
        assert_equal(prices[3]['current_price'], "0.0075")

        inbound_sms_prices = result.inbound_sms_prices

        assert_equal(inbound_sms_prices[0]['number_type'], "local")
        assert_equal(inbound_sms_prices[0]['base_price'], "0.0075")
        assert_equal(inbound_sms_prices[0]['current_price'], "0.0075")

        assert_equal(inbound_sms_prices[1]['number_type'], "shortcode")
        assert_equal(inbound_sms_prices[1]['base_price'], "0.0075")
        assert_equal(inbound_sms_prices[1]['current_price'], "0.005")

        assert_equal(inbound_sms_prices[2]['number_type'], "toll-free")
        assert_equal(inbound_sms_prices[2]['base_price'], "0.0075")
        assert_equal(inbound_sms_prices[2]['current_price'], "0.0075")

        request.assert_called_with(
            "GET",
            "{0}/Messaging/Countries/US".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False,
        )
