from datetime import date
from mock import patch
from nose.tools import raises, assert_true
from twilio.rest.resources import Calls
from tools import create_mock_json

BASE_URI = "https://api.twilio.com/2010-04-01/Accounts/AC123"
ACCOUNT_SID = "AC123"
AUTH = (ACCOUNT_SID, "token")
CALL_SID = "CA47e13748ed59a5733d2c1c1c69a83a28"

list_resource = Calls(BASE_URI, AUTH)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_create_call(mock):
    resp = create_mock_json("tests/resources/calls_instance.json")
    resp.status_code = 201
    mock.return_value = resp

    uri = "%s/Calls" % (BASE_URI)
    list_resource.create("TO", "FROM", "url", record=True, application_sid='APPSID')
    exp_params = {
        'To': "TO",
        'From': "FROM",
        'Url': "url",
        'Record': "true",
        'ApplicationSid': 'APPSID',
        }

    mock.assert_called_with("POST", uri, data=exp_params, auth=AUTH)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_paging(mock):
    resp = create_mock_json("tests/resources/calls_list.json")
    mock.return_value = resp

    uri = "%s/Calls" % (BASE_URI)
    list_resource.list(started_before=date(2010, 12, 5))
    exp_params = {'StartTime<': '2010-12-05'}

    mock.assert_called_with("GET", uri, params=exp_params, auth=AUTH)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_get(mock):
    resp = create_mock_json("tests/resources/calls_instance.json")
    mock.return_value = resp

    uri = "%s/Calls/%s" % (BASE_URI, CALL_SID)
    list_resource.get(CALL_SID)

    mock.assert_called_with("GET", uri, auth=AUTH)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_hangup(mock):
    resp = create_mock_json("tests/resources/calls_instance.json")
    resp.status_code = 204
    mock.return_value = resp

    uri = "%s/Calls/%s" % (BASE_URI, CALL_SID)
    r = list_resource.hangup(CALL_SID)
    exp_data = {"Status": "completed"}

    mock.assert_called_with("POST", uri, data=exp_data, auth=AUTH)
    assert_true(r)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_cancel(mock):
    resp = create_mock_json("tests/resources/calls_instance.json")
    resp.status_code = 204
    mock.return_value = resp

    uri = "%s/Calls/%s" % (BASE_URI, CALL_SID)
    r = list_resource.cancel(CALL_SID)
    exp_data = {"Status": "canceled"}

    mock.assert_called_with("POST", uri, data=exp_data, auth=AUTH)
    assert_true(r)


@raises(AttributeError)
def test_create():
    list_resource.delete
