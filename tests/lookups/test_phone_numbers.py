from mock import patch

from nose.tools import assert_equal

from tests.tools import create_mock_json
from twilio.rest.resources.lookups.phone_numbers import PhoneNumbers


AUTH = ('AC123', 'foobar')
TIMEOUT = 30


@patch("twilio.rest.resources.base.make_twilio_request")
def test_get_phone_number(request):
    resp = create_mock_json(
        "tests/resources/lookups/phone_number_instance.json",
    )
    request.return_value = resp

    phone_numbers = PhoneNumbers('/v1', AUTH, TIMEOUT)
    pn = phone_numbers.get('+15108675309')
    assert_equal(pn.phone_number, '+15108675309')
    request.assert_called_with('GET', '/v1/PhoneNumbers/+15108675309',
                               auth=AUTH, timeout=TIMEOUT, params={},
                               use_json_extension=False)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_get_carrier_info(request):
    resp = create_mock_json(
        "tests/resources/lookups/phone_number_instance.json",
    )
    request.return_value = resp

    phone_numbers = PhoneNumbers('/v1', AUTH, TIMEOUT)
    pn = phone_numbers.get('+15108675309', include_carrier_info=True)
    assert_equal(pn.phone_number, '+15108675309')
    request.assert_called_with('GET', '/v1/PhoneNumbers/+15108675309',
                               auth=AUTH, timeout=TIMEOUT,
                               params={'Type': 'carrier'},
                               use_json_extension=False)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_get_with_country_code(request):
    resp = create_mock_json(
        "tests/resources/lookups/phone_number_instance.json",
    )
    request.return_value = resp

    phone_numbers = PhoneNumbers('/v1', AUTH, TIMEOUT)
    pn = phone_numbers.get('510-867-5309', country_code='US')
    assert_equal(pn.phone_number, '+15108675309')
    request.assert_called_with('GET', '/v1/PhoneNumbers/510-867-5309',
                               auth=AUTH, timeout=TIMEOUT,
                               params={'CountryCode': 'US'},
                               use_json_extension=False)
