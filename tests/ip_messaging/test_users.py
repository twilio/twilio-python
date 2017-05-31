import unittest
from mock import patch, Mock
from twilio.rest.resources.ip_messaging import Users, User
from tests.tools import create_mock_json

BASE_URI = "https://ip-messaging.twilio.com/v1/Services/ISxxx"
ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
AUTH = (ACCOUNT_SID, "token")
USER_SID = "USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

list_resource = Users(BASE_URI, AUTH)


class UserTest(unittest.TestCase):

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_create_user(self, mock):
        resp = create_mock_json("tests/resources/ip_messaging/user_instance.json")
        resp.status_code = 201
        mock.return_value = resp

        uri = "%s/Users" % (BASE_URI)
        list_resource.create('test_id')
        exp_params = {
            'Identity': "test_id"
        }

        mock.assert_called_with("POST", uri, data=exp_params, auth=AUTH,
                                use_json_extension=False)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_get(self, mock):
        resp = create_mock_json("tests/resources/ip_messaging/user_instance.json")
        mock.return_value = resp

        uri = "%s/Users/%s" % (BASE_URI, USER_SID)
        list_resource.get(USER_SID)

        mock.assert_called_with("GET", uri, auth=AUTH,
                                use_json_extension=False)

    @patch("twilio.rest.resources.base.Resource.request")
    def test_delete(self, req):
        """ Deleting a call should work """
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        req.return_value = resp, {}

        app = User(list_resource, "US123")
        app.delete()
        uri = "%s/Users/US123" % (BASE_URI)
        req.assert_called_with("DELETE", uri)
