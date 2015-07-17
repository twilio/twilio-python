import unittest
from mock import patch, Mock

from tests.tools import create_mock_json
from twilio.rest.resources.sip.domains import (
    CredentialListMappings,
    CredentialListMapping
)
from twilio.rest.resources.util import UNSET_TIMEOUT


class SipCredentialListMappingTest(unittest.TestCase):
    ACCOUNT_SID = 'AC123'
    AUTH = (ACCOUNT_SID, 'token')
    API_URI = 'https://api.twilio.com/2010-04-01'
    SID = 'CL32a3c49700934481addd5ce1659f04d2'
    DOMAIN_SID = 'SD27f0288630a668bdfbf177f8e22f5ccc'
    BASE_URI = '%s/Accounts/%s/SIP/Domains/%s' % (API_URI, ACCOUNT_SID,
                                                  DOMAIN_SID)

    def setUp(self):
        self.list_resource = CredentialListMappings(self.BASE_URI,
                                                    self.AUTH, UNSET_TIMEOUT)
        self.instance_resource = CredentialListMapping(self.list_resource,
                                                       self.SID)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_load(self, mock):
        resp = create_mock_json('tests/resources/sip/'
                                'sip_credential_list_mapping_list.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/CredentialListMappings' % (self.BASE_URI)
        self.list_resource.list()

        mock.assert_called_with("GET", uri, params={}, auth=self.AUTH,
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_create(self, mock):
        resp = create_mock_json('tests/resources/sip/'
                                'sip_credential_list_mapping_instance.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/CredentialListMappings' % (self.BASE_URI)
        self.list_resource.create('cred_sid')

        data = {
            'CredentialListSid': 'cred_sid'
        }
        mock.assert_called_with("POST", uri, data=data,
                                auth=self.AUTH, use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_fetch(self, mock):
        resp = create_mock_json('tests/resources/sip/'
                                'sip_credential_list_mapping_instance.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/CredentialListMappings/%s' % (self.BASE_URI, self.SID)
        self.list_resource.get(self.SID)

        mock.assert_called_with("GET", uri, auth=self.AUTH,
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_delete(self, mock):
        resp = Mock()
        resp.status_code = 204
        mock.return_value = resp

        uri = '%s/CredentialListMappings/%s' % (self.BASE_URI, self.SID)
        self.list_resource.delete(self.SID)

        mock.assert_called_with("DELETE", uri, auth=self.AUTH,
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_instance_delete(self, mock):
        resp = Mock()
        resp.status_code = 204
        mock.return_value = resp

        uri = '%s/CredentialListMappings/%s' % (self.BASE_URI, self.SID)
        self.instance_resource.delete()

        mock.assert_called_with("DELETE", uri,
                                auth=self.AUTH,
                                use_json_extension=True)
