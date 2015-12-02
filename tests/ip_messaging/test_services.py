import unittest
from mock import patch, Mock
from twilio.rest.resources.ip_messaging import Services, Service
from tests.tools import create_mock_json

BASE_URI = "https://ip-messaging.twilio.com/v1"
ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
AUTH = (ACCOUNT_SID, "token")
SERVICE_SID = "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

list_resource = Services(BASE_URI, AUTH)


class ServiceTest(unittest.TestCase):

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_create_service(self, mock):
        resp = create_mock_json("tests/resources/ip_messaging/service_instance.json")
        resp.status_code = 201
        mock.return_value = resp

        uri = "%s/Services" % (BASE_URI)
        list_resource.create('TestService')
        exp_params = {
            'FriendlyName': "TestService"
        }

        mock.assert_called_with("POST", uri, data=exp_params, auth=AUTH,
                                use_json_extension=False)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_get(self, mock):
        resp = create_mock_json("tests/resources/ip_messaging/service_instance.json")
        mock.return_value = resp

        uri = "%s/Services/%s" % (BASE_URI, SERVICE_SID)
        list_resource.get(SERVICE_SID)

        mock.assert_called_with("GET", uri, auth=AUTH,
                                use_json_extension=False)

    @patch("twilio.rest.resources.base.Resource.request")
    def test_delete(self, req):
        """ Deleting a call should work """
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        req.return_value = resp, {}

        app = Service(list_resource, "IS123")
        app.delete()
        uri = "https://ip-messaging.twilio.com/v1/Services/IS123"
        req.assert_called_with("DELETE", uri)
