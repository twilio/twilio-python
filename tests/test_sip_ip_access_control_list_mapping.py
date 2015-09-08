import unittest
from mock import patch, Mock

from tests.tools import create_mock_json
from twilio.rest.http import HttpClient
from twilio.rest.resources.sip.domains import (
    IpAccessControlListMapping,
    IpAccessControlListMappings
)
from twilio.rest.resources.util import UNSET_TIMEOUT


class SipIPAccessControlListMappingTest(unittest.TestCase):
    ACCOUNT_SID = 'AC123'
    AUTH = (ACCOUNT_SID, 'token')
    API_URI = 'https://api.twilio.com/2010-04-01'
    SID = 'CL32'
    DOMAIN_SID = 'SD27'
    BASE_URI = '%s/Accounts/%s/SIP/Domains/%s' % (API_URI, ACCOUNT_SID,
                                                  DOMAIN_SID)

    def setUp(self):
        self.client = HttpClient()
        self.list_resource = IpAccessControlListMappings(
            self.client, self.BASE_URI, self.AUTH, UNSET_TIMEOUT)
        self.instance_resource = IpAccessControlListMapping(
            self.list_resource, self.SID)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_load(self, mock):
        resp = create_mock_json('tests/resources/sip/'
                                'sip_ip_access_control_list_mapping_list.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/IpAccessControlListMappings' % (self.BASE_URI)
        self.list_resource.list().execute()

        mock.assert_called_with("GET", uri, auth=self.AUTH,
                                use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_create(self, mock):
        resp = create_mock_json('tests/resources/sip/'
                                'sip_ip_access_control_list_mapping_instance.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/IpAccessControlListMappings' % (self.BASE_URI)
        self.list_resource.create('cred_sid').execute()

        data = {
            'IpAccessControlListSid': 'cred_sid'
        }
        mock.assert_called_with("POST", uri, data=data,
                                auth=self.AUTH, use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_fetch(self, mock):
        resp = create_mock_json('tests/resources/sip/'
                                'sip_ip_access_control_list_mapping_instance.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/IpAccessControlListMappings/%s' % (self.BASE_URI, self.SID)
        self.list_resource.get(self.SID).execute()

        mock.assert_called_with("GET", uri, auth=self.AUTH,
                                use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_delete(self, mock):
        resp = Mock()
        resp.status_code = 204
        mock.return_value = resp

        uri = '%s/IpAccessControlListMappings/%s' % (self.BASE_URI, self.SID)
        self.list_resource.delete(self.SID).execute()

        mock.assert_called_with("DELETE", uri, auth=self.AUTH,
                                use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_instance_delete(self, mock):
        resp = Mock()
        resp.status_code = 204
        mock.return_value = resp

        uri = '%s/IpAccessControlListMappings/%s' % (self.BASE_URI, self.SID)
        self.instance_resource.delete().execute()

        mock.assert_called_with("DELETE", uri,
                                auth=self.AUTH,
                                use_json_extension=True,
                                client=self.client)
