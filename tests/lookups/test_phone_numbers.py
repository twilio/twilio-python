import urllib

try:
    import urllib.parse
except ImportError:
    import urllib

from mock import patch

from nose.tools import assert_equal

from tests.tools import create_mock_json
from twilio.rest.resources.lookups.phone_numbers import PhoneNumbers

AUTH = ('AC123', 'foobar')
TIMEOUT = 30
NUMBER = '+15108675309'
try:
    NUMBER_ENCODED = urllib.quote_plus(NUMBER)
except:
    NUMBER_ENCODED = urllib.parse.quote_plus(NUMBER)

print(NUMBER_ENCODED)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_get_phone_number(request):
    resp = create_mock_json(
        "tests/resources/lookups/phone_number_instance.json",
    )
    request.return_value = resp

    phone_numbers = PhoneNumbers('/v1', AUTH, TIMEOUT)
    pn = phone_numbers.get(NUMBER)
    assert_equal(pn.phone_number, NUMBER)
    request.assert_called_with('GET',
                               '/v1/PhoneNumbers/{0}'.format(NUMBER_ENCODED),
                               auth=AUTH, timeout=TIMEOUT, params={},
                               use_json_extension=False)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_get_carrier_info(request):
    resp = create_mock_json(
        "tests/resources/lookups/phone_number_instance.json",
    )
    request.return_value = resp

    phone_numbers = PhoneNumbers('/v1', AUTH, TIMEOUT)
    pn = phone_numbers.get(NUMBER, include_carrier_info=True)
    assert_equal(pn.phone_number, NUMBER)
    request.assert_called_with('GET',
                               '/v1/PhoneNumbers/{0}'.format(NUMBER_ENCODED),
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
    assert_equal(pn.phone_number, NUMBER)
    request.assert_called_with('GET', '/v1/PhoneNumbers/510-867-5309',
                               auth=AUTH, timeout=TIMEOUT,
                               params={'CountryCode': 'US'},
                               use_json_extension=False)
