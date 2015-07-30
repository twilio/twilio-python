from tests.integration import config
from tests.integration.api_responses import (
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
        account = self.client.accounts.create(friendly_name='test_sub_account')
        account.suspend()
        account.activate()
        account.close()
