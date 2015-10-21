import unittest

from mock import patch

from tests.tools import create_mock_json
from twilio.rest.resources.conversations.conversations import ConversationsRoot


AUTH = ("AC123", "token")
BASE_URI = "https://conversations.twilio.com/v1"
CONVERSATION_SID = "CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


class ConversationTest(unittest.TestCase):
    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get(self, request):
        resp = create_mock_json('tests/resources/conversations/conversation_instance.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{0}/Conversations/{1}".format(BASE_URI, CONVERSATION_SID)
        list_resource = ConversationsRoot(BASE_URI, AUTH)
        list_resource.get(CONVERSATION_SID)
        request.assert_called_with("GET", uri, use_json_extension=False, auth=AUTH)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_list_in_progress(self, request):
        resp = create_mock_json('tests/resources/conversations/conversation_list.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{0}/Conversations/InProgress".format(BASE_URI)
        list_resource = ConversationsRoot(BASE_URI, AUTH)
        list_resource.in_progress.list()
        request.assert_called_with("GET", uri, params={}, auth=AUTH, use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_list_completed(self, request):
        resp = create_mock_json('tests/resources/conversations/conversation_list.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{0}/Conversations/Completed".format(BASE_URI)
        list_resource = ConversationsRoot(BASE_URI, AUTH)
        list_resource.completed.list()
        request.assert_called_with("GET", uri, params={}, auth=AUTH, use_json_extension=False)
