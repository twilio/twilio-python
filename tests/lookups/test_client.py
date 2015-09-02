from mock import patch
from tests.tools import create_mock_json
from twilio.rest import TwilioLookupsClient
from twilio.rest.http import HttpClient


@patch("twilio.rest.resources.base.make_twilio_request")
def test_phone_numbers(mock):
    http_client = HttpClient()
    client = TwilioLookupsClient("ACCOUNT_SID", "AUTH_TOKEN", client=http_client)
    resp = create_mock_json("tests/resources/lookups/phone_number_instance.json")
    mock.return_value = resp
    client.phone_numbers.get("+15108675309").execute()
    uri = "https://lookups.twilio.com/v1/PhoneNumbers/+15108675309"
    mock.assert_called_with("GET", uri, auth=("ACCOUNT_SID", "AUTH_TOKEN"),
                            use_json_extension=False,
                            client=http_client)
