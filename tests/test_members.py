from mock import patch
from tests.tools import create_mock_json
from twilio.rest.resources import Members

QUEUE_SID = "QU1b9faddec3d54ec18488f86c83019bf0"
ACCOUNT_SID = "AC123"
AUTH = (ACCOUNT_SID, "token")
CALL_SID = "CAaaf2e9ded94aba3e57c42a3d55be6ff2"
BASE_URI = "https://api.twilio.com/2010-04-01/Accounts/AC123/Queues/%s" % (
    QUEUE_SID)
TWIML_URL = "example_twiml_url"

list_resource = Members(BASE_URI, AUTH)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_members_list(mock):
    resp = create_mock_json("tests/resources/members_list.json")
    mock.return_value = resp

    uri = "%s/Members" % (BASE_URI)
    list_resource.list()

    mock.assert_called_with("GET", uri, params={}, auth=AUTH,
                            use_json_extension=True)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_members_dequeue_front(mock):
    resp = create_mock_json("tests/resources/members_instance.json")
    mock.return_value = resp

    uri = "%s/Members/Front" % (BASE_URI)
    list_resource.dequeue(TWIML_URL)

    mock.assert_called_with("POST", uri, data={"Url": TWIML_URL}, auth=AUTH,
                            use_json_extension=True)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_members_dequeue_call(mock):
    resp = create_mock_json("tests/resources/members_instance.json")
    mock.return_value = resp

    uri = "%s/Members/%s" % (BASE_URI, CALL_SID)
    list_resource.dequeue(TWIML_URL, call_sid=CALL_SID)

    mock.assert_called_with("POST", uri, data={"Url": TWIML_URL}, auth=AUTH,
                            use_json_extension=True)
