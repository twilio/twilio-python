from tests.integration import config
from tests.integration.api_responses import (
    GETRequestHandler as GRH,
    POSTRequestHandler as PRH,
    DELETERequestHandler as DRH,
)
from tests.integration.base_integration_test import BaseIntegrationTest
from twilio.rest.client import TwilioRestClient


class TwilioRestClientTest(BaseIntegrationTest):

    def setUp(self, base_uri=config.base_uri):
        super(TwilioRestClientTest, self).setUp(base_uri=base_uri)
        self.client = TwilioRestClient(config.post_account_sid,
                                       config.auth_token,
                                       base_uri)

    def test_calls(self):
        self.response_handlers = [
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Calls',
                'calls_instance.json', {
                    'From': config.post_account_outgoing_pn,
                    'To': '+14105551234',
                    'Url': 'http://example.com/foo.xml'
                }),
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Calls/CA47e13748ed59a5733d2c1c1c69a83a28',
                'calls_instance.json', {
                    'Status': 'canceled'
                }),
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Calls/CA47e13748ed59a5733d2c1c1c69a83a28',
                'calls_instance.json', {
                    'Status': 'completed'
                }),
            DRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Calls/CA47e13748ed59a5733d2c1c1c69a83a28')
        ]
        call = self.client.calls.create('+14105551234',
                                        config.post_account_outgoing_pn,
                                        'http://example.com/foo.xml')
        call.cancel()
        call.hangup()
        call.delete()

    def test_message(self):
        self.response_handlers = [
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Messages',
                'messages_instance.json', {
                    'From': config.post_account_outgoing_pn,
                    'To': config.post_account_outgoing_pn,
                    'Body': 'a'
                }),
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Messages/SM5fe343f4d8fd43b38de8497f8d633b65',
                'messages_instance.json', {
                    'Body': ''
                }),
            DRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Messages/SM5fe343f4d8fd43b38de8497f8d633b65')
        ]
        message = self.client.messages.create(config.post_account_outgoing_pn,
                                              to=config.post_account_outgoing_pn,
                                              body='a')
        message.redact()
        message.delete()

    def test_sms(self):
        self.response_handlers = [
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SMS/Messages',
                'sms_messages_instance.json', {
                    'From': config.post_account_outgoing_pn,
                    'To': config.post_account_outgoing_pn,
                    'Body': 'a'
                }),
            DRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SMS/Messages/SM6144a547ed59a5733d2c1c1c69a83a28')
        ]
        sms = self.client.sms.messages.create(config.post_account_outgoing_pn,
                                              to=config.post_account_outgoing_pn,
                                              body='a')
        sms.delete()

    def test_tokens(self):
        self.response_handlers = [
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Tokens',
                'tokens.json', {'Ttl': 30})
        ]
        self.client.tokens.create(ttl=30)

    def test_accounts(self):
        self.response_handlers = [
            PRH('/Accounts', 'accounts_instance.json', {
                'FriendlyName': "test_sub_account"
            }),
            PRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28', 'accounts_instance.json', {
                'Status': "suspended"
            }),
            PRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28', 'accounts_instance.json', {
                'Status': "active"
            }),
            PRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28', 'accounts_instance.json', {
                'Status': "closed"
            }),
        ]
        account = self.client.accounts.create(friendly_name='test_sub_account')
        account.suspend()
        account.activate()
        account.close()

    def test_available_phone_numbers(self):
        self.response_handlers = [
            GRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/AvailablePhoneNumbers/US/Local',
                'available_phone_numbers_us_local.json',
                auth=(config.post_account_sid, config.auth_token)),
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/IncomingPhoneNumbers',
                'incoming_phone_numbers_instance.json', {
                    'PhoneNumber': '+141586753092'
                })
        ]
        phone_numbers = self.client.phone_numbers.available_phone_numbers.list()
        phone_numbers[0].purchase()

    def test_sip_domain(self):
        self.response_handlers = [
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP/Domains',
                'sip/sip_domain_instance.json', {
                    'DomainName': 'domain'
                }),
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP/Domains/SD27f0288630a668bdfbf177f8e22f5ccc',
                'sip/sip_domain_instance.json', {}),
            DRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP/Domains/SD27f0288630a668bdfbf177f8e22f5ccc'),
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP'
                '/Domains/SD27f0288630a668bdfbf177f8e22f5ccc/CredentialListMappings',
                'sip/sip_credential_list_mapping_instance.json', {
                    'CredentialListSid': 'credsid'
                }),
            DRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP/Domains/SD27f0288630a668bdfbf177f8e22f5ccc'
                '/CredentialListMappings/CL32a3c49700934481addd5ce1659f04d2'),
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP'
                '/Domains/SD27f0288630a668bdfbf177f8e22f5ccc/IpAccessControlListMappings',
                'sip/sip_ip_access_control_list_mapping_instance.json', {
                    'IpAccessControlListSid': 'listsid'
                }),
            DRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP/Domains/SD27f0288630a668bdfbf177f8e22f5ccc'
                '/IpAccessControlListMappings/ALasdfasfasdf'),
        ]

        domain = self.client.sip.domains.create('domain')
        domain.update()

        cred = domain.credential_list_mappings.create('credsid')
        cred.delete()
        cred = self.client.sip.credential_list_mappings('SD27f0288630a668bdfbf177f8e22f5ccc').create('credsid')
        cred.delete()

        control = domain.ip_access_control_list_mappings.create('listsid')
        control.delete()
        control = self.client.sip.ip_access_control_list_mappings(
            'SD27f0288630a668bdfbf177f8e22f5ccc').create('listsid')
        control.delete()

        domain.delete()

    def test_sip_credential_lists(self):
        self.response_handlers = [
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP/CredentialLists',
                'sip/sip_credential_list_instance.json', {
                    'FriendlyName': 'friendlyname'
                }),
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP'
                '/CredentialLists/CL1e9949149f055138a8c215fb7ccd5b64',
                'sip/sip_credential_list_instance.json', {
                    'FriendlyName': 'blah'
                }),
            DRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP'
                '/CredentialLists/CL1e9949149f055138a8c215fb7ccd5b64'),

            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP/CredentialLists'
                '/CL1e9949149f055138a8c215fb7ccd5b64/Credentials',
                'sip/sip_credential_instance.json', {
                    'Username': 'username',
                    'Password': 'password'
                }),
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP'
                '/CredentialLists/CL1e9949149f055138a8c215fb7ccd5b64'
                '/Credentials/SC9dc76ca0b355dd39f0f52788b2e008c6',
                'sip/sip_credential_instance.json', {
                    'Username': 'blah',
                    'Password': 'foo'
                }),
            DRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP'
                '/CredentialLists/CL1e9949149f055138a8c215fb7ccd5b64'
                '/Credentials/SC9dc76ca0b355dd39f0f52788b2e008c6')
        ]

        cred_list = self.client.sip.credential_lists.create('friendlyname')
        cred_list.update(friendly_name='blah')

        credentials = cred_list.credentials.create('username', 'password')
        credentials.update(username='blah', password='foo')
        credentials.delete()

        credentials = self.client.sip.credentials(
            'CL1e9949149f055138a8c215fb7ccd5b64').create('username', 'password')
        credentials.update(username='blah', password='foo')
        credentials.delete()

        cred_list.delete()

    def test_sip_control_list(self):
        self.response_handlers = [
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP/IpAccessControlLists',
                'sip/sip_ip_access_control_list_instance.json', {
                    'FriendlyName': 'friendlyname'
                }),
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP'
                '/IpAccessControlLists/AL123',
                'sip/sip_ip_access_control_list_instance.json', {
                    'FriendlyName': 'blah'
                }),
            DRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP'
                '/IpAccessControlLists/AL123'),

            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP'
                '/IpAccessControlLists/AL123/IpAddresses',
                'sip/sip_ip_access_control_list_instance.json', {
                    'FriendlyName': 'friendlyname',
                    'IpAddress': '127.0.0.1'
                }),
            PRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP'
                '/IpAccessControlLists/AL123/IpAddresses/AL123',
                'sip/sip_ip_access_control_list_instance.json', {
                    'FriendlyName': 'blah',
                    'IpAddress': 'localhost'
                }),
            DRH('/Accounts/ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/SIP'
                '/IpAccessControlLists/AL123/IpAddresses/AL123'),
        ]
        control = self.client.sip.ip_access_control_lists.create('friendlyname')
        control.update(friendly_name='blah')

        ip = control.ip_addresses.create('friendlyname', '127.0.0.1')
        ip.update(friendly_name='blah', ip_address='localhost')
        ip.delete()

        ip = self.client.sip.ip_addresses('AL123').create('friendlyname', '127.0.0.1')
        ip.update(friendly_name='blah', ip_address='localhost')
        ip.delete()

        control.delete()
