from mock import patch, Mock
from nose.tools import raises
from twilio.rest.resources import Transcriptions, Transcription
from tests.tools import create_mock_json

BASE_URI = "https://api.twilio.com/2010-04-01/Accounts/AC123"
ACCOUNT_SID = "AC123"
AUTH = (ACCOUNT_SID, "token")

transcriptions = Transcriptions(BASE_URI, AUTH)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_paging(mock):
    resp = create_mock_json("tests/resources/transcriptions_list.json")
    mock.return_value = resp

    uri = "%s/Transcriptions" % (BASE_URI)
    transcriptions.list(page=2)

    mock.assert_called_with("GET", uri, params={"Page": 2}, auth=AUTH,
                            use_json_extension=True)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_get(mock):
    resp = create_mock_json("tests/resources/transcriptions_instance.json")
    mock.return_value = resp

    uri = "%s/Transcriptions/TR123" % (BASE_URI)
    transcriptions.get("TR123")

    mock.assert_called_with("GET", uri, auth=AUTH,
                            use_json_extension=True)


@patch("twilio.rest.resources.base.Resource.request")
def test_delete_transcription(req):
    """ Deleting a transcription should work """
    resp = Mock()
    resp.content = ""
    resp.status_code = 204
    req.return_value = resp, {}

    app = Transcription(transcriptions, "TR123")
    app.delete()
    uri = "https://api.twilio.com/2010-04-01/Accounts/AC123/Transcriptions/TR123"
    req.assert_called_with("DELETE", uri)


@raises(AttributeError)
def test_create():
    transcriptions.create


@raises(AttributeError)
def test_update():
    transcriptions.update
