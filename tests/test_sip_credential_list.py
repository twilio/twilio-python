import unittest
from mock import patch, Mock

from tests.tools import create_mock_json
from twilio.rest.resources.sip import Sip
from twilio.rest.resources.sip_credential_lists import SipCredentialList
from twilio.rest.resources.util import UNSET_TIMEOUT


class SipCredentialListTest(unittest.TestCase):
    ACCOUNT_SID = 'AC123'
    AUTH = (ACCOUNT_SID, 'token')
    BASE_URI = 'https://api.twilio.com/2010-04-01/Accounts/' + ACCOUNT_SID
    SID = 'CL1e9949149f055138a8c215fb7ccd5b64'

    def setUp(self):
        self.sip = Sip(self.BASE_URI, self.AUTH, UNSET_TIMEOUT)
        self.list_resource = self.sip.credential_lists
        self.instance_resource = SipCredentialList(
            self.list_resource, self.SID)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_load(self, mock):
        resp = create_mock_json('tests/resources/sip/sip_credential_list_list.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/SIP/CredentialLists' % (self.BASE_URI)
        self.list_resource.list()

        mock.assert_called_with("GET", uri, params={}, auth=self.AUTH,
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_create(self, mock):
        resp = create_mock_json('tests/resources/sip/sip_credential_list_instance.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/SIP/CredentialLists' % (self.BASE_URI)
        self.list_resource.create('cred')

        mock.assert_called_with("POST", uri, data={'FriendlyName': 'cred'},
                                auth=self.AUTH, use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_fetch(self, mock):
        resp = create_mock_json('tests/resources/sip/sip_credential_list_instance.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/SIP/CredentialLists/%s' % (self.BASE_URI, self.SID)
        self.list_resource.get(self.SID)

        mock.assert_called_with("GET", uri, auth=self.AUTH,
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_delete(self, mock):
        resp = Mock()
        resp.status_code = 204
        mock.return_value = resp

        uri = '%s/SIP/CredentialLists/%s' % (self.BASE_URI, self.SID)
        self.list_resource.delete(self.SID)

        mock.assert_called_with("DELETE", uri, auth=self.AUTH,
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_update(self, mock):
        resp = create_mock_json('tests/resources/sip/sip_credential_list_instance.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/SIP/CredentialLists/%s' % (self.BASE_URI, self.SID)
        self.list_resource.update(self.SID, friendly_name='cred')

        mock.assert_called_with("POST", uri,
                                data={'FriendlyName': 'cred'},
                                auth=self.AUTH,
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_instance_update(self, mock):
        resp = create_mock_json('tests/resources/sip/sip_credential_list_instance.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/SIP/CredentialLists/%s' % (self.BASE_URI, self.SID)
        self.instance_resource.update(friendly_name='cred')

        mock.assert_called_with("POST", uri, data={'FriendlyName': 'cred'},
                                auth=self.AUTH,
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_instance_delete(self, mock):
        resp = Mock()
        resp.status_code = 204
        mock.return_value = resp

        uri = '%s/SIP/CredentialLists/%s' % (self.BASE_URI, self.SID)
        self.instance_resource.delete()

        mock.assert_called_with("DELETE", uri,
                                auth=self.AUTH,
                                use_json_extension=True)
