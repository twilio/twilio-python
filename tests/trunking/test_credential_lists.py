import unittest
from mock import Mock, patch
from nose.tools import assert_equal, assert_true
from tests.tools import create_mock_json
from twilio.rest.resources.trunking.credential_lists import CredentialLists

ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
AUTH = (ACCOUNT_SID, "auth_token")
BASE_URI = "https://trunking.twilio.com/v1/Trunks/TK11111111111111111111111111111111"


class CredentialListsTest(unittest.TestCase):

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get_credential_lists(self, request):
        resp = create_mock_json('tests/resources/trunking/credential_lists_list.json')
        resp.status_code = 200
        request.return_value = resp

        credential_lists = CredentialLists(BASE_URI, AUTH)
        result = credential_lists.list()

        assert_equal(len(result), 1)
        assert_equal(result[0].sid, 'CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        assert_equal(result[0].account_sid, 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        assert_equal(result[0].trunk_sid, "TK11111111111111111111111111111111")
        assert_equal(result[0].friendly_name, "Test list")
        assert_equal(result[0].url, "{0}/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(BASE_URI))

        request.assert_called_with(
            "GET",
            "{0}/CredentialLists".format(BASE_URI),
            auth=AUTH,
            params={},
            use_json_extension=False,
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get_credential_lists_instance(self, request):
        resp = create_mock_json('tests/resources/trunking/credential_lists_instance.json')
        resp.status_code = 200
        request.return_value = resp

        credential_lists = CredentialLists(BASE_URI, AUTH)
        result = credential_lists.get('CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        assert_equal(result.sid, "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        assert_equal(result.account_sid, "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        assert_equal(result.trunk_sid, "TK11111111111111111111111111111111")
        assert_equal(result.friendly_name, "Test")
        assert_equal(result.url, "{0}/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(BASE_URI))

        request.assert_called_with(
            "GET",
            "{0}/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_create_credential_lists_instance(self, request):
        resp = create_mock_json('tests/resources/trunking/credential_lists_instance.json')
        resp.status_code = 201
        request.return_value = resp

        credential_lists = CredentialLists(BASE_URI, AUTH)
        result = credential_lists.create('CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        assert_equal(result.sid, "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        assert_equal(result.account_sid, "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        assert_equal(result.trunk_sid, "TK11111111111111111111111111111111")
        assert_equal(result.friendly_name, "Test")
        assert_equal(result.url, "{0}/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(BASE_URI))

        data_dict = dict()
        data_dict['CredentialListSid'] = 'CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        request.assert_called_with(
            "POST",
            "{0}/CredentialLists".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False,
            data=data_dict,
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_delete_credential_lists_instance(self, request):
        resp = Mock()
        resp.status_code = 204
        request.return_value = resp

        credential_lists = CredentialLists(BASE_URI, AUTH)
        result = credential_lists.delete('CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        assert_true(result)

        request.assert_called_with(
            "DELETE",
            "{0}/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False
        )
