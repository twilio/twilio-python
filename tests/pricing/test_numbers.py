import unittest
from nose.tools import assert_equal

from mock import patch
from tests.tools import create_mock_json

from twilio.rest.resources.pricing.phone_numbers import PhoneNumberCountries


AUTH = ("AC123", "token")
BASE_URI = "https://pricing.twilio.com/v1"


class NumbersTest(unittest.TestCase):

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_number_countries(self, request):
        resp = create_mock_json('tests/resources/pricing/phone_number_country_list.json')
        resp.status_code = 200
        request.return_value = resp

        countries = PhoneNumberCountries(BASE_URI + "/PhoneNumbers", AUTH)
        result = countries.list()

        assert_equal(result[0].iso_country, "AC")
        assert_equal(len(result), 3)

        request.assert_called_with(
            "GET",
            "{0}/PhoneNumbers/Countries".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False,
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_number_country(self, request):
        resp = create_mock_json('tests/resources/pricing/phone_number_country_instance.json')
        resp.status_code = 200
        request.return_value = resp

        countries = PhoneNumberCountries(BASE_URI + "/PhoneNumbers", AUTH)
        country = countries.get('EE')

        assert_equal(country.country, "Estonia")
        assert_equal(
            country.phone_number_prices,
            [
                {
                    'type': 'mobile',
                    'base_price': 3.00,
                    'current_price': 3.00,
                },
                {
                    'type': 'national',
                    'base_price': 1.00,
                    'current_price': 1.00,
                }
            ],
        )

        request.assert_called_with(
            "GET",
            "{0}/PhoneNumbers/Countries/EE".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False,
        )
