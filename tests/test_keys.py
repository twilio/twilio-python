from mock import patch, Mock
from twilio.rest.resources.keys import Keys, Key
from tests.tools import create_mock_json

ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
AUTH = (ACCOUNT_SID, "token")
BASE_URL = "https://api.twilio.com/2010-04-01/Accounts/{0}".format(ACCOUNT_SID)
KEY_SID = "SKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

list_resource = Keys(BASE_URL, AUTH)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_get_key(mock):
    resp = create_mock_json("tests/resources/keys_instance.json")
    mock.return_value = resp

    url = BASE_URL + "/Keys/{0}".format(KEY_SID)
    list_resource.get(KEY_SID)

    mock.assert_called_with("GET", url, auth=AUTH, use_json_extension=True)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_create_key(mock):
    resp = create_mock_json("tests/resources/keys_instance.json")
    resp.status_code = 201
    mock.return_value = resp

    url = BASE_URL + "/Keys"
    list_resource.create(friendly_name="Fuzzy Lumpkins' SigningKey")
    params = {
        'FriendlyName': "Fuzzy Lumpkins' SigningKey"
    }

    mock.assert_called_with("POST", url, data=params, auth=AUTH, use_json_extension=True)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_update_key(mock):
    resp = create_mock_json("tests/resources/keys_instance.json")
    mock.return_value = resp

    url = BASE_URL + "/Keys/{0}".format(KEY_SID)
    list_resource.update(sid=KEY_SID, friendly_name="Fuzzy Lumpkins' SigningKey")
    params = {
        'FriendlyName': "Fuzzy Lumpkins' SigningKey"
    }

    mock.assert_called_with("POST", url, data=params, auth=AUTH, use_json_extension=True)


@patch("twilio.rest.resources.base.Resource.request")
def test_delete_key(mock):
    resp = Mock()
    resp.content = ""
    resp.status_code = 204
    mock.return_value = resp, {}

    key = Key(list_resource, KEY_SID)
    key.delete()

    url = BASE_URL + "/Keys/{0}".format(KEY_SID)
    mock.assert_called_with("DELETE", url)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_list_keys(mock):
    resp = create_mock_json("tests/resources/keys_list.json")
    mock.return_value = resp

    url = BASE_URL + "/Keys"
    list_resource.list()

    mock.assert_called_with("GET", url, params={}, auth=AUTH, use_json_extension=True)
