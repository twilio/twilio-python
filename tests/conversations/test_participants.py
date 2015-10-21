import unittest

from mock import patch

from tests.tools import create_mock_json
from twilio.rest.resources.conversations.participants import Participants


AUTH = ("AC123", "token")
BASE_URI = "https://conversations.twilio.com/v1"
CONVERSATION_SID = "CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
PARTICIPANT_SID = "PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


class ParticipantTest(unittest.TestCase):
    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get(self, request):
        resp = create_mock_json('tests/resources/conversations/participant_instance.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{0}/Conversations/{1}".format(BASE_URI, CONVERSATION_SID)
        expected = "{0}/Participants/{1}".format(uri, PARTICIPANT_SID)
        list_resource = Participants(uri, AUTH)
        list_resource.get(PARTICIPANT_SID)
        request.assert_called_with("GET", expected, use_json_extension=False, auth=AUTH)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_list_in_progress(self, request):
        resp = create_mock_json('tests/resources/conversations/participant_list.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{0}/Conversations/{1}".format(BASE_URI, CONVERSATION_SID)
        expected = "{0}/Participants".format(uri)
        list_resource = Participants(uri, AUTH)
        list_resource.list()
        request.assert_called_with("GET", expected, params={}, auth=AUTH, use_json_extension=False)
