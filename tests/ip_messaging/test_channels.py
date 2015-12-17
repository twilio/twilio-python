import unittest
from mock import patch, Mock
from twilio.rest.resources.ip_messaging import Channels, Channel
from tests.tools import create_mock_json

BASE_URI = "https://ip-messaging.twilio.com/v1/Services/ISxxx"
ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
AUTH = (ACCOUNT_SID, "token")
CHANNEL_SID = "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

list_resource = Channels(BASE_URI, AUTH)


class ChannelTest(unittest.TestCase):

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_create_channel(self, mock):
        resp = create_mock_json("tests/resources/ip_messaging/channel_instance.json")
        resp.status_code = 201
        mock.return_value = resp

        uri = "%s/Channels" % (BASE_URI)
        list_resource.create(friendly_name='TestChannel', unique_name='Unique')
        exp_params = {
            'FriendlyName': "TestChannel",
            'UniqueName': 'Unique'
        }

        mock.assert_called_with("POST", uri, data=exp_params, auth=AUTH,
                                use_json_extension=False)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_get(self, mock):
        resp = create_mock_json("tests/resources/ip_messaging/channel_instance.json")
        mock.return_value = resp

        uri = "%s/Channels/%s" % (BASE_URI, CHANNEL_SID)
        list_resource.get(CHANNEL_SID)

        mock.assert_called_with("GET", uri, auth=AUTH,
                                use_json_extension=False)

    @patch("twilio.rest.resources.base.Resource.request")
    def test_delete(self, req):
        """ Deleting a call should work """
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        req.return_value = resp, {}

        app = Channel(list_resource, "CH123")
        app.delete()
        uri = "%s/Channels/CH123" % (BASE_URI)
        req.assert_called_with("DELETE", uri)
