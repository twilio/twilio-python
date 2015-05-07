from mock import patch

from tests.tools import create_mock_json
from twilio.rest.monitor import TwilioMonitorClient


@patch("twilio.rest.resources.base.make_twilio_request")
def test_events(mock):
    client = TwilioMonitorClient("ACCOUNT_SID", "AUTH_TOKEN")
    resp = create_mock_json("tests/resources/monitor/events_instance.json")
    mock.return_value = resp
    client.events.get("AEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    uri = "https://monitor.twilio.com/v1/Events/AEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    mock.assert_called_with("GET", uri, auth=("ACCOUNT_SID", "AUTH_TOKEN"), use_json_extension=False)
