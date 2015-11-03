import unittest
from mock import Mock, patch
from nose.tools import assert_equal, assert_true
from tests.tools import create_mock_json
from twilio.rest.resources.trunking.origination_urls import (
    OriginationUrls
)

ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
AUTH = (ACCOUNT_SID, "auth_token")
BASE_URI = "https://trunking.twilio.com/v1/Trunks/TK11111111111111111111111111111111"


class OriginationUrlsTest(unittest.TestCase):

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get_origination_urls_lists(self, request):
        resp = create_mock_json('tests/resources/trunking/origination_urls_list.json')
        resp.status_code = 200
        request.return_value = resp

        origination_urls = OriginationUrls(BASE_URI, AUTH)
        result = origination_urls.list()

        assert_equal(len(result), 1)
        assert_equal(result[0].sid, 'OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        assert_equal(result[0].account_sid, 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        assert_equal(result[0].trunk_sid, "TK11111111111111111111111111111111")
        assert_equal(result[0].friendly_name, "Name")
        assert_equal(result[0].sip_url, "sip:169.10.1.35")
        assert_equal(result[0].weight, 10)
        assert_equal(result[0].priority, 20)
        assert_true(result[0].enabled)
        assert_equal(result[0].url, "{0}/OriginationUrls/OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(BASE_URI))

        request.assert_called_with(
            "GET",
            "{0}/OriginationUrls".format(BASE_URI),
            auth=AUTH,
            params={},
            use_json_extension=False,
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get_origination_urls_instance(self, request):
        resp = create_mock_json('tests/resources/trunking/origination_urls_instance.json')
        resp.status_code = 200
        request.return_value = resp

        origination_urls = OriginationUrls(BASE_URI, AUTH)
        result = origination_urls.get('OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        assert_equal(result.sid, "OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        assert_equal(result.account_sid, "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        assert_equal(result.trunk_sid, "TK11111111111111111111111111111111")
        assert_equal(result.friendly_name, "Name")
        assert_equal(result.sip_url, "sip:169.10.1.35")
        assert_equal(result.weight, 10)
        assert_equal(result.priority, 20)
        assert_true(result.enabled)
        assert_equal(result.url, "{0}/OriginationUrls/OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(BASE_URI))

        request.assert_called_with(
            "GET",
            "{0}/OriginationUrls/OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_create_origination_urls_instance(self, request):
        resp = create_mock_json('tests/resources/trunking/origination_urls_instance.json')
        resp.status_code = 201
        request.return_value = resp

        origination_urls = OriginationUrls(BASE_URI, AUTH)
        result = origination_urls.create('Name', 'sip:169.10.1.35')

        assert_equal(result.sid, "OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        assert_equal(result.account_sid, "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        assert_equal(result.trunk_sid, "TK11111111111111111111111111111111")
        assert_equal(result.friendly_name, "Name")
        assert_equal(result.sip_url, "sip:169.10.1.35")
        assert_equal(result.weight, 10)
        assert_equal(result.priority, 20)
        assert_true(result.enabled)
        assert_equal(result.url, "{0}/OriginationUrls/OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(BASE_URI))

        data_dict = dict()
        data_dict['FriendlyName'] = 'Name'
        data_dict['SipUrl'] = 'sip:169.10.1.35'
        data_dict['Priority'] = 10
        data_dict['Weight'] = 10
        data_dict['Enabled'] = 'true'

        request.assert_called_with(
            "POST",
            "{0}/OriginationUrls".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False,
            data=data_dict,
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_update_origination_urls_instance(self, request):
        resp = create_mock_json('tests/resources/trunking/origination_urls_instance.json')
        resp.status_code = 200
        request.return_value = resp

        origination_urls = OriginationUrls(BASE_URI, AUTH)
        result = origination_urls.update('OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', {'Priority': 10})

        assert_equal(result.sid, "OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        assert_equal(result.account_sid, "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        assert_equal(result.trunk_sid, "TK11111111111111111111111111111111")
        assert_equal(result.friendly_name, "Name")
        assert_equal(result.sip_url, "sip:169.10.1.35")
        assert_equal(result.weight, 10)
        assert_equal(result.priority, 20)
        assert_true(result.enabled)
        assert_equal(result.url, "{0}/OriginationUrls/OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(BASE_URI))

        data_dict = dict()
        data_dict['Priority'] = 10

        request.assert_called_with(
            "POST",
            "{0}/OriginationUrls/OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False,
            data=data_dict
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_delete_origination_urls_instance(self, request):
        resp = Mock()
        resp.status_code = 204
        request.return_value = resp

        origination_urls = OriginationUrls(BASE_URI, AUTH)
        result = origination_urls.delete('OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        assert_true(result)

        request.assert_called_with(
            "DELETE",
            "{0}/OriginationUrls/OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False
        )
