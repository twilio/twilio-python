import unittest
from mock import Mock, patch
from nose.tools import assert_equal, assert_true
from tests.tools import create_mock_json
from twilio.rest.resources.trunking.ip_access_control_lists import (
    IpAccessControlLists
)

ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
AUTH = (ACCOUNT_SID, "auth_token")
BASE_URI = "https://trunking.twilio.com/v1/Trunks/TK11111111111111111111111111111111"


class IpAccessControlListsTest(unittest.TestCase):

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get_ip_access_control_lists(self, request):
        resp = create_mock_json('tests/resources/trunking/ip_access_control_lists_list.json')
        resp.status_code = 200
        request.return_value = resp

        ip_access_control_lists = IpAccessControlLists(BASE_URI, AUTH)
        result = ip_access_control_lists.list()

        assert_equal(len(result), 1)
        assert_equal(result[0].sid, 'ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        assert_equal(result[0].account_sid, 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        assert_equal(result[0].trunk_sid, "TK11111111111111111111111111111111")
        assert_equal(result[0].friendly_name, "Test")
        assert_equal(result[0].url, "{0}/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(BASE_URI))

        request.assert_called_with(
            "GET",
            "{0}/IpAccessControlLists".format(BASE_URI),
            auth=AUTH,
            params={},
            use_json_extension=False,
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get_ip_access_control_lists_instance(self, request):
        resp = create_mock_json('tests/resources/trunking/ip_access_control_lists_instance.json')
        resp.status_code = 200
        request.return_value = resp

        ip_access_control_lists = IpAccessControlLists(BASE_URI, AUTH)
        result = ip_access_control_lists.get('ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        assert_equal(result.sid, "ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        assert_equal(result.account_sid, "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        assert_equal(result.trunk_sid, "TK11111111111111111111111111111111")
        assert_equal(result.friendly_name, "Test")
        assert_equal(result.url, "{0}/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(BASE_URI))

        request.assert_called_with(
            "GET",
            "{0}/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_associate_ip_access_control_lists_instance(self, request):
        resp = create_mock_json('tests/resources/trunking/ip_access_control_lists_instance.json')
        resp.status_code = 201
        request.return_value = resp

        ip_access_control_lists = IpAccessControlLists(BASE_URI, AUTH)
        result = ip_access_control_lists.create('ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        assert_equal(result.sid, "ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        assert_equal(result.account_sid, "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        assert_equal(result.trunk_sid, "TK11111111111111111111111111111111")
        assert_equal(result.friendly_name, "Test")
        assert_equal(result.url, "{0}/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(BASE_URI))

        data_dict = dict()
        data_dict['IpAccessControlListSid'] = 'ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        request.assert_called_with(
            "POST",
            "{0}/IpAccessControlLists".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False,
            data=data_dict,
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_disassociate_ip_access_control_lists_instance(self, request):
        resp = Mock()
        resp.status_code = 204
        request.return_value = resp

        ip_access_control_lists = IpAccessControlLists(BASE_URI, AUTH)
        result = ip_access_control_lists.delete('ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        assert_true(result)

        request.assert_called_with(
            "DELETE",
            "{0}/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False
        )
