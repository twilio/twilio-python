import unittest
from mock import patch, Mock
from twilio.rest.resources.ip_messaging import Members, Member
from tests.tools import create_mock_json

BASE_URI = "https://ip-messaging.twilio.com/v1/Services/ISxxx/Channels/CHxxx"
ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
AUTH = (ACCOUNT_SID, "token")
MEMBER_SID = "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

list_resource = Members(BASE_URI, AUTH)


class MemberTest(unittest.TestCase):

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_create_member(self, mock):
        resp = create_mock_json("tests/resources/ip_messaging/member_instance.json")
        resp.status_code = 201
        mock.return_value = resp

        uri = "%s/Members" % (BASE_URI)
        list_resource.create('test_identity')
        exp_params = {
            'Identity': "test_identity"
        }

        mock.assert_called_with("POST", uri, data=exp_params, auth=AUTH,
                                use_json_extension=False)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_get(self, mock):
        resp = create_mock_json("tests/resources/ip_messaging/member_instance.json")
        mock.return_value = resp

        uri = "%s/Members/%s" % (BASE_URI, MEMBER_SID)
        list_resource.get(MEMBER_SID)

        mock.assert_called_with("GET", uri, auth=AUTH,
                                use_json_extension=False)

    @patch("twilio.rest.resources.base.Resource.request")
    def test_delete(self, req):
        """ Deleting a call should work """
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        req.return_value = resp, {}

        app = Member(list_resource, "MB123")
        app.delete()
        uri = "%s/Members/MB123" % (BASE_URI)
        req.assert_called_with("DELETE", uri)
