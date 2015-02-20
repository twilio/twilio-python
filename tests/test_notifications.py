from datetime import date
from mock import patch
from nose.tools import raises, assert_true
from twilio.rest.resources import Notifications
from tests.tools import create_mock_json

BASE_URI = "https://api.twilio.com/2010-04-01/Accounts/AC123"
ACCOUNT_SID = "AC123"
AUTH = (ACCOUNT_SID, "token")

RE_SID = "RE19e96a31ed59a5733d2c1c1c69a83a28"

list_resource = Notifications(BASE_URI, AUTH)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_paging(mock):
    resp = create_mock_json("tests/resources/notifications_list.json")
    mock.return_value = resp

    uri = "%s/Notifications" % (BASE_URI)
    list_resource.list(before=date(2010, 12, 5))
    exp_params = {'MessageDate<': '2010-12-05'}

    mock.assert_called_with("GET", uri, params=exp_params, auth=AUTH,
                            use_json_extension=True)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_get(mock):
    resp = create_mock_json("tests/resources/notifications_instance.json")
    mock.return_value = resp

    uri = "%s/Notifications/%s" % (BASE_URI, RE_SID)
    list_resource.get(RE_SID)

    mock.assert_called_with("GET", uri, auth=AUTH,
                            use_json_extension=True)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_get2(mock):
    resp = create_mock_json("tests/resources/notifications_instance.json")
    resp.status_code = 204
    mock.return_value = resp

    uri = "%s/Notifications/%s" % (BASE_URI, RE_SID)
    r = list_resource.delete(RE_SID)

    mock.assert_called_with("DELETE", uri, auth=AUTH,
                            use_json_extension=True)
    assert_true(r)


@raises(AttributeError)
def test_create():
    list_resource.create


@raises(AttributeError)
def test_update():
    list_resource.update
