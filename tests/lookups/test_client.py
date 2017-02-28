try:
    import urllib.parse
except ImportError:
    import urllib

try:
    NUMBER_ENCODED = urllib.quote_plus('+15108675309')
except:
    NUMBER_ENCODED = urllib.parse.quote_plus('+15108675309')

from mock import patch

from tests.tools import create_mock_json
from twilio.rest import TwilioLookupsClient


@patch("twilio.rest.resources.base.make_twilio_request")
def test_phone_numbers(mock):
    client = TwilioLookupsClient("ACCOUNT_SID", "AUTH_TOKEN")
    resp = create_mock_json(
        "tests/resources/lookups/phone_number_instance.json")
    mock.return_value = resp
    client.phone_numbers.get('+15108675309')
    uri = "https://lookups.twilio.com/v1/PhoneNumbers/{0}".format(
        NUMBER_ENCODED)
    mock.assert_called_with("GET", uri, params={},
                            auth=("ACCOUNT_SID", "AUTH_TOKEN"),
                            use_json_extension=False)
