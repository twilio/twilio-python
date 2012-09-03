from datetime import date
from mock import patch
from nose.tools import raises, assert_equals, assert_true
from twilio.rest.resources import Recordings
from tools import create_mock_json

BASE_URI = "https://api.twilio.com/2010-04-01/Accounts/AC123"
ACCOUNT_SID = "AC123"
AUTH = (ACCOUNT_SID, "token")

RE_SID = "RE19e96a31ed59a5733d2c1c1c69a83a28"

recordings = Recordings(BASE_URI, AUTH)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_paging(mock):
    resp = create_mock_json("tests/resources/recordings_list.json")
    mock.return_value = resp

    uri = "%s/Recordings" % (BASE_URI)
    recordings.list(call_sid="CA123", before=date(2010, 12, 5))
    exp_params = {'CallSid': 'CA123', 'DateCreated<': '2010-12-05'}

    mock.assert_called_with("GET", uri, params=exp_params, auth=AUTH)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_get(mock):
    resp = create_mock_json("tests/resources/recordings_instance.json")
    mock.return_value = resp

    uri = "%s/Recordings/%s" % (BASE_URI, RE_SID)
    r = recordings.get(RE_SID)

    mock.assert_called_with("GET", uri, auth=AUTH)

    truri = "%s/Recordings/%s/Transcriptions" % (BASE_URI, RE_SID)
    assert_equals(r.transcriptions.uri, truri)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_get2(mock):
    resp = create_mock_json("tests/resources/recordings_instance.json")
    resp.status_code = 204
    mock.return_value = resp

    uri = "%s/Recordings/%s" % (BASE_URI, RE_SID)
    r = recordings.delete(RE_SID)

    mock.assert_called_with("DELETE", uri, auth=AUTH)
    assert_true(r)


@raises(AttributeError)
def test_create():
    recordings.create


@raises(AttributeError)
def test_update():
    recordings.update
