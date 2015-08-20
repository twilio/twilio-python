import unittest
from tests.integration import config
from twilio.ext.holodeck import holodeck
from twilio.rest.client import TwilioRestClient


class TwilioRestClientTest(unittest.TestCase):

    def setUp(self):
        self.client = TwilioRestClient('AC' + 'a' * 32, 'AUTHTOKEN')
        holodeck.activate()

    def tearDown(self):
        holodeck.deactivate()

    def test_calls(self):
        call = self.client.calls.create('+321', '+123',
                                        'http://www.example.com').execute()
        call.delete().execute()

    def test_message(self):
        message = self.client.messages.create('+123',
                                              to='+321',
                                              body='body').execute()
        message.delete().execute()

    def test_sms(self):
        sms = self.client.sms.messages.create('+123',
                                              to='+321',
                                              body='body').execute()
        sms.delete().execute()

    def test_tokens(self):
        self.client.tokens.create().execute()

    def test_accounts(self):
        account = self.client.accounts.create().execute()
        account.update().execute()

    def test_available_phone_numbers(self):
        phone_numbers = self.client.phone_numbers.available_phone_numbers\
            .list().execute()
        phone_numbers[0].purchase().execute()

    def test_sip_domain(self):
        domain = self.client.sip.domains.create('domain_name').execute()
        domain.update().execute()

        cred = domain.credential_list_mappings.create('CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').execute()
        cred.delete().execute()
        cred = self.client.sip.credential_list_mappings(
            'SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').create('CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').execute()
        cred.delete().execute()

        control = domain.ip_access_control_list_mappings.create('ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').execute()
        control.delete().execute()
        control = self.client.sip.ip_access_control_list_mappings(
            'SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').create('ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').execute()
        control.delete().execute()

        domain.delete().execute()

    def test_sip_credential_lists(self):
        cred_list = self.client.sip.credential_lists.create('friendly_name').execute()
        cred_list.update(friendly_name='friendly_name').execute()

        credentials = cred_list.credentials.create('username', 'password').execute()
        credentials.update(username='username', password='password').execute()
        credentials.delete().execute()

        credentials = self.client.sip.credentials(
            'CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').create('username', 'password').execute()
        credentials.update(username='username', password='password').execute()
        credentials.delete().execute()

        cred_list.delete().execute()

    def test_sip_control_list(self):
        control = self.client.sip.ip_access_control_lists.create('friendly_name').execute()
        control.update(friendly_name='friendly_name').execute()

        ip = control.ip_addresses.create('friendly_name', '127.0.0.1').execute()
        ip.update(ip_address='127.0.0.1').execute()
        ip.delete().execute()

        ip = self.client.sip.ip_addresses('ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')\
            .create('friendly_name', '127.0.0.1').execute()
        ip.update(ip_address='127.0.0.1').execute()
        ip.delete().execute()

        control.delete().execute()
