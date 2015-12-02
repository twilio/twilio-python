import unittest
from mock import patch, Mock
from twilio.rest.resources.ip_messaging import Credentials, Credential
from tests.tools import create_mock_json

BASE_URI = "https://ip-messaging.twilio.com/v1"
ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
AUTH = (ACCOUNT_SID, "token")
CREDENTIAL_SID = "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

list_resource = Credentials(BASE_URI, AUTH)


class CredentialTest(unittest.TestCase):

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_create_credential(self, mock):
        resp = create_mock_json("tests/resources/ip_messaging/credential_instance.json")
        resp.status_code = 201
        mock.return_value = resp

        uri = "%s/Credentials" % (BASE_URI)
        list_resource.create('apn')
        exp_params = {
            'Type': "apn"
        }

        mock.assert_called_with("POST", uri, data=exp_params, auth=AUTH,
                                use_json_extension=False)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_get(self, mock):
        resp = create_mock_json("tests/resources/ip_messaging/credential_instance.json")
        mock.return_value = resp

        uri = "%s/Credentials/%s" % (BASE_URI, CREDENTIAL_SID)
        list_resource.get(CREDENTIAL_SID)

        mock.assert_called_with("GET", uri, auth=AUTH,
                                use_json_extension=False)

    @patch("twilio.rest.resources.base.Resource.request")
    def test_delete(self, req):
        """ Deleting a call should work """
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        req.return_value = resp, {}

        app = Credential(list_resource, "IS123")
        app.delete()
        uri = "https://ip-messaging.twilio.com/v1/Credentials/IS123"
        req.assert_called_with("DELETE", uri)
