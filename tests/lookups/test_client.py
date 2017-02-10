import urllib.parse

from mock import patch

from tests.tools import create_mock_json
from twilio.rest import TwilioLookupsClient


@patch("twilio.rest.resources.base.make_twilio_request")
def test_phone_numbers(mock):
    client = TwilioLookupsClient("ACCOUNT_SID", "AUTH_TOKEN")
    resp = create_mock_json("tests/resources/lookups/phone_number_instance.json")
    mock.return_value = resp
    number_encode = urllib.parse.quote('+15108675309')
    client.phone_numbers.get('+15108675309')
    uri = "https://lookups.twilio.com/v1/PhoneNumbers/{}".format(number_encode)
    mock.assert_called_with("GET", uri, params={}, auth=("ACCOUNT_SID", "AUTH_TOKEN"),
                            use_json_extension=False)
