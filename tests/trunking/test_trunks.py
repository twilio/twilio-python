import unittest
from mock import Mock, patch
from nose.tools import assert_equal, assert_true
from tests.tools import create_mock_json
from twilio.rest.resources.trunking.trunks import (
    Trunks
)

ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
AUTH = (ACCOUNT_SID, "auth_token")
BASE_URI = "https://trunking.twilio.com/v1"
TRUNK_SID = "TK11111111111111111111111111111111"


class TrunksTest(unittest.TestCase):

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get_trunks_lists(self, request):
        resp = create_mock_json('tests/resources/trunking/trunks_list.json')
        resp.status_code = 200
        request.return_value = resp

        trunks = Trunks(BASE_URI, AUTH)
        result = trunks.list()

        assert_equal(len(result), 1)
        assert_equal(result[0].sid, 'TK11111111111111111111111111111111')
        assert_equal(result[0].account_sid, 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        assert_equal(result[0].domain_name, "test-trunk.pstn.twilio.com")
        assert_equal(result[0].friendly_name, "Test")
        assert_equal(result[0].recording,
                     {"trim": "do-not-trim",
                      "mode": "record-from-ringing"})

        assert_equal(result[0].auth_type, "CREDENTIAL_LIST")
        assert_equal(result[0].auth_type_set, ["CREDENTIAL_LIST"])
        TRUNK_INSTANCE_BASE_URI = "{0}/{1}/{2}".format(BASE_URI, "Trunks",
                                                       TRUNK_SID)

        assert_equal(result[0].url, TRUNK_INSTANCE_BASE_URI)

        assert_equal(result[0].links['origination_urls'],
                     "{0}/OriginationUrls".format(TRUNK_INSTANCE_BASE_URI))
        assert_equal(result[0].links['credential_lists'],
                     "{0}/CredentialLists".format(TRUNK_INSTANCE_BASE_URI))
        assert_equal(result[0].links['ip_access_control_lists'],
                     "{0}/IpAccessControlLists".format(TRUNK_INSTANCE_BASE_URI))
        assert_equal(result[0].links['phone_numbers'],
                     "{0}/PhoneNumbers".format(TRUNK_INSTANCE_BASE_URI))

        request.assert_called_with(
            "GET",
            "{0}/Trunks".format(BASE_URI),
            auth=AUTH,
            params={},
            use_json_extension=False,
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get_trunks_instance(self, request):
        resp = create_mock_json('tests/resources/trunking/trunks_instance.json')
        resp.status_code = 200
        request.return_value = resp

        trunks = Trunks(BASE_URI, AUTH)
        result = trunks.get('TK11111111111111111111111111111111')

        assert_equal(result.sid, 'TK11111111111111111111111111111111')
        assert_equal(result.account_sid, 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        assert_equal(result.domain_name, "test-trunk.pstn.twilio.com")
        assert_equal(result.friendly_name, "Test")
        assert_equal(result.recording,
                     {"trim": "do-not-trim",
                      "mode": "record-from-ringing"})

        assert_equal(result.auth_type, "CREDENTIAL_LIST")
        assert_equal(result.auth_type_set, ["CREDENTIAL_LIST"])
        TRUNK_INSTANCE_BASE_URI = "{0}/{1}/{2}".format(BASE_URI, "Trunks",
                                                       TRUNK_SID)

        assert_equal(result.url, TRUNK_INSTANCE_BASE_URI)

        assert_equal(result.links['origination_urls'],
                     "{0}/OriginationUrls".format(TRUNK_INSTANCE_BASE_URI))
        assert_equal(result.links['credential_lists'],
                     "{0}/CredentialLists".format(TRUNK_INSTANCE_BASE_URI))
        assert_equal(result.links['ip_access_control_lists'],
                     "{0}/IpAccessControlLists".format(TRUNK_INSTANCE_BASE_URI))
        assert_equal(result.links['phone_numbers'],
                     "{0}/PhoneNumbers".format(TRUNK_INSTANCE_BASE_URI))

        request.assert_called_with(
            "GET",
            "{0}/Trunks/TK11111111111111111111111111111111".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_create_trunk_instance(self, request):
        resp = create_mock_json('tests/resources/trunking/trunks_instance.json')
        resp.status_code = 201
        request.return_value = resp

        trunks = Trunks(BASE_URI, AUTH)
        kwargs = {
            'FriendlyName': 'Test',
            'DomainName': 'test-trunk.pstn.twilio.com'
        }
        result = trunks.create(**kwargs)

        assert_equal(result.sid, 'TK11111111111111111111111111111111')
        assert_equal(result.account_sid, 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        assert_equal(result.domain_name, "test-trunk.pstn.twilio.com")
        assert_equal(result.friendly_name, "Test")
        assert_equal(result.recording,
                     {"trim": "do-not-trim",
                      "mode": "record-from-ringing"})

        assert_equal(result.auth_type, "CREDENTIAL_LIST")
        assert_equal(result.auth_type_set, ["CREDENTIAL_LIST"])
        TRUNK_INSTANCE_BASE_URI = "{0}/{1}/{2}".format(BASE_URI, "Trunks",
                                                       TRUNK_SID)

        assert_equal(result.url, TRUNK_INSTANCE_BASE_URI)

        assert_equal(result.links['origination_urls'],
                     "{0}/OriginationUrls".format(TRUNK_INSTANCE_BASE_URI))
        assert_equal(result.links['credential_lists'],
                     "{0}/CredentialLists".format(TRUNK_INSTANCE_BASE_URI))
        assert_equal(result.links['ip_access_control_lists'],
                     "{0}/IpAccessControlLists".format(TRUNK_INSTANCE_BASE_URI))
        assert_equal(result.links['phone_numbers'],
                     "{0}/PhoneNumbers".format(TRUNK_INSTANCE_BASE_URI))

        data_dict = dict()
        data_dict['FriendlyName'] = 'Test'
        data_dict['DomainName'] = 'test-trunk.pstn.twilio.com'

        request.assert_called_with(
            "POST",
            "{0}/Trunks".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False,
            data=data_dict,
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_update_trunk_instance(self, request):
        resp = create_mock_json('tests/resources/trunking/trunks_instance.json')
        resp.status_code = 200
        request.return_value = resp

        trunks = Trunks(BASE_URI, AUTH)
        result = trunks.update('TK11111111111111111111111111111111', {'FriendlyName': 'Test'})

        assert_equal(result.sid, 'TK11111111111111111111111111111111')
        assert_equal(result.account_sid, 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        assert_equal(result.domain_name, "test-trunk.pstn.twilio.com")
        assert_equal(result.friendly_name, "Test")
        assert_equal(result.recording,
                     {"trim": "do-not-trim",
                      "mode": "record-from-ringing"})

        assert_equal(result.auth_type, "CREDENTIAL_LIST")
        assert_equal(result.auth_type_set, ["CREDENTIAL_LIST"])
        TRUNK_INSTANCE_BASE_URI = "{0}/{1}/{2}".format(BASE_URI, "Trunks",
                                                       TRUNK_SID)

        assert_equal(result.url, TRUNK_INSTANCE_BASE_URI)

        assert_equal(result.links['origination_urls'],
                     "{0}/OriginationUrls".format(TRUNK_INSTANCE_BASE_URI))
        assert_equal(result.links['credential_lists'],
                     "{0}/CredentialLists".format(TRUNK_INSTANCE_BASE_URI))
        assert_equal(result.links['ip_access_control_lists'],
                     "{0}/IpAccessControlLists".format(TRUNK_INSTANCE_BASE_URI))
        assert_equal(result.links['phone_numbers'],
                     "{0}/PhoneNumbers".format(TRUNK_INSTANCE_BASE_URI))

        data_dict = dict()
        data_dict['FriendlyName'] = 'Test'

        request.assert_called_with(
            "POST",
            "{0}/Trunks/TK11111111111111111111111111111111".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False,
            data=data_dict
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_delete_trunk_instance(self, request):
        resp = Mock()
        resp.status_code = 204
        request.return_value = resp

        trunks = Trunks(BASE_URI, AUTH)
        result = trunks.delete('TK11111111111111111111111111111111')

        assert_true(result)

        request.assert_called_with(
            "DELETE",
            "{0}/Trunks/TK11111111111111111111111111111111".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False
        )
