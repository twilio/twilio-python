import unittest
from mock import patch, Mock

from tests.tools import create_mock_json
from twilio.rest.http import HttpClient
from twilio.rest.resources.sip.credential_lists import Credential, Credentials
from twilio.rest.resources.util import UNSET_TIMEOUT


class SipCredentialTest(unittest.TestCase):
    ACCOUNT_SID = 'AC123'
    AUTH = (ACCOUNT_SID, 'token')
    API_URI = 'https://api.twilio.com/2010-04-01'
    CRED_SID = 'CL1e9949149f055138a8c215fb7ccd5b64'
    SID = 'SC9dc76ca0b355dd39f0f52788b2e008c6'
    BASE_URI = '%s/Accounts/%s/SIP/CredentialLists/%s' % (API_URI,
                                                          ACCOUNT_SID,
                                                          CRED_SID)

    def setUp(self):
        self.client = HttpClient()
        self.list_resource = Credentials(self.client, self.BASE_URI, self.AUTH, UNSET_TIMEOUT)
        self.instance_resource = Credential(self.list_resource, self.SID)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_load(self, mock):
        resp = create_mock_json('tests/resources/sip/sip_credential_list.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/Credentials' % (self.BASE_URI)
        self.list_resource.list().execute()

        mock.assert_called_with("GET", uri, params={}, auth=self.AUTH,
                                use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_create(self, mock):
        resp = create_mock_json('tests/resources/sip/sip_credential_instance.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/Credentials' % (self.BASE_URI)
        self.list_resource.create(username='username',
                                  password='password').execute()

        data = {
            'Username': 'username',
            'Password': 'password'
        }
        mock.assert_called_with("POST", uri, data=data,
                                auth=self.AUTH, use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_fetch(self, mock):
        resp = create_mock_json('tests/resources/sip/sip_credential_instance.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/Credentials/%s' % (self.BASE_URI, self.SID)
        self.list_resource.get(self.SID).execute()

        mock.assert_called_with("GET", uri, auth=self.AUTH,
                                use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_delete(self, mock):
        resp = Mock()
        resp.status_code = 204
        mock.return_value = resp

        uri = '%s/Credentials/%s' % (self.BASE_URI, self.SID)
        self.list_resource.delete(self.SID).execute()

        mock.assert_called_with("DELETE", uri, auth=self.AUTH,
                                use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_update(self, mock):
        resp = create_mock_json('tests/resources/sip/sip_credential_instance.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/Credentials/%s' % (self.BASE_URI, self.SID)
        self.list_resource.update(self.SID, username='username',
                                  password='password').execute()

        data = {
            'Username': 'username',
            'Password': 'password'
        }
        mock.assert_called_with("POST", uri,
                                data=data,
                                auth=self.AUTH,
                                use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_instance_update(self, mock):
        resp = create_mock_json('tests/resources/sip/sip_credential_instance.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/Credentials/%s' % (self.BASE_URI, self.SID)
        self.instance_resource.update(username='username',
                                      password='password').execute()

        data = {
            'Username': 'username',
            'Password': 'password'
        }
        mock.assert_called_with("POST", uri, data=data,
                                auth=self.AUTH,
                                use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_instance_delete(self, mock):
        resp = Mock()
        resp.status_code = 204
        mock.return_value = resp

        uri = '%s/Credentials/%s' % (self.BASE_URI, self.SID)
        self.instance_resource.delete().execute()

        mock.assert_called_with("DELETE", uri,
                                auth=self.AUTH,
                                use_json_extension=True,
                                client=self.client)
