from mock import patch, Mock
from twilio.rest.resources.ip_messaging import Roles, Role
from tests.tools import create_mock_json

BASE_URI = "https://ip-messaging.twilio.com/v1/Services/ISxxx"
ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
AUTH = (ACCOUNT_SID, "token")
ROLE_SID = "ROaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

list_resource = Roles(BASE_URI, AUTH)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_get(mock):
    resp = create_mock_json("tests/resources/ip_messaging/role_instance.json")
    mock.return_value = resp

    uri = "%s/Roles/%s" % (BASE_URI, ROLE_SID)
    list_resource.get(ROLE_SID)

    mock.assert_called_with("GET", uri, auth=AUTH,
                            use_json_extension=False)


@patch("twilio.rest.resources.base.Resource.request")
def test_delete(req):
    """ Deleting a call should work """
    resp = Mock()
    resp.content = ""
    resp.status_code = 204
    req.return_value = resp, {}

    app = Role(list_resource, "RO123")
    app.delete()
    uri = "%s/Roles/RO123" % (BASE_URI)
    req.assert_called_with("DELETE", uri)
