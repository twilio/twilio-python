from mock import patch

from tests.tools import create_mock_json
from twilio.rest.conversations import TwilioConversationsClient


@patch("twilio.rest.resources.base.make_twilio_request")
def test_conversations(mock):
    client = TwilioConversationsClient("ACCOUNT_SID", "AUTH_TOKEN")
    resp = create_mock_json("tests/resources/conversations/conversation_instance.json")
    mock.return_value = resp
    client.conversations.get("CV4bbc4afc943cd2a5d29f0ce01c5656db")
    uri = "https://conversations.twilio.com/v1/Conversations/CV4bbc4afc943cd2a5d29f0ce01c5656db"
    mock.assert_called_with("GET", uri, auth=("ACCOUNT_SID", "AUTH_TOKEN"), use_json_extension=False)
