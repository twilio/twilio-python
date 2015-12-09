import unittest
from mock import patch, Mock
from twilio.rest.resources.ip_messaging import Messages, Message
from tests.tools import create_mock_json

BASE_URI = "https://ip-messaging.twilio.com/v1/Services/ISxxx/Channels/CHxxx"
ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
AUTH = (ACCOUNT_SID, "token")
MESSAGE_SID = "MSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

list_resource = Messages(BASE_URI, AUTH)


class MessageTest(unittest.TestCase):

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_create_message(self, mock):
        resp = create_mock_json("tests/resources/ip_messaging/message_instance.json")
        resp.status_code = 201
        mock.return_value = resp

        uri = "%s/Messages" % (BASE_URI)
        list_resource.create('TestBody')
        exp_params = {
            'Body': "TestBody"
        }

        mock.assert_called_with("POST", uri, data=exp_params, auth=AUTH,
                                use_json_extension=False)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_get(self, mock):
        resp = create_mock_json("tests/resources/ip_messaging/message_instance.json")
        mock.return_value = resp

        uri = "%s/Messages/%s" % (BASE_URI, MESSAGE_SID)
        list_resource.get(MESSAGE_SID)

        mock.assert_called_with("GET", uri, auth=AUTH,
                                use_json_extension=False)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_update(self, mock):
        resp = create_mock_json("tests/resources/ip_messaging/message_instance.json")
        mock.return_value = resp

        update_params = {
            'UniqueName': 'unique'
        }

        uri = "%s/Messages/%s" % (BASE_URI, MESSAGE_SID)
        list_resource.update(MESSAGE_SID, unique_name='unique')

        mock.assert_called_with("POST", uri, data=update_params, auth=AUTH,
                                use_json_extension=False)

    @patch("twilio.rest.resources.base.Resource.request")
    def test_delete(self, req):
        """ Deleting a call should work """
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        req.return_value = resp, {}

        app = Message(list_resource, "MS123")
        app.delete()
        uri = "%s/Messages/MS123" % (BASE_URI)
        req.assert_called_with("DELETE", uri)
