import os
from tests.integration import config
from tests.integration.api_responses import (
    GETRequestHandler as GRH,
    POSTRequestHandler as PRH,
)
from tests.integration.base_integration_test import BaseIntegrationTest
from twilio.rest.client import TwilioRestClient
from twilio.rest.exceptions import TwilioRestException


RESPONSE_HANDLERS = [
    GRH('/Accounts', 'accounts_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28', 'accounts_instance.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Calls', 'calls_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Calls'
        '/CA24388be8ed59a5733d2c1c1c69a83a28/Notifications',
        'notifications_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Calls'
        '/CA24388be8ed59a5733d2c1c1c69a83a28/Recordings',
        'recordings_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Conferences',
        'conferences_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/IncomingPhoneNumbers',
        'incoming_phone_numbers_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Messages',
        'messages_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Notifications',
        'notifications_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/OutgoingCallerIds',
        'outgoing_caller_ids_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Queues',
        'queues_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Queues/QU1b9faddec3d54ec18488f86c83019bf0/Members',
        'members_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Recordings',
        'recordings_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/SIP/Domains',
        os.path.join('sip', 'sip_domain_list.json')),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/SIP/CredentialLists',
        os.path.join('sip', 'sip_credential_list_list.json')),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/'
        'SIP/CredentialLists/CL1e9949149f055138a8c215fb7ccd5b64/Credentials',
        os.path.join('sip', 'sip_credential_list.json')),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/SIP/IpAccessControlLists',
        os.path.join('sip', 'sip_ip_access_control_list_list.json')),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/SMS/Messages',
        'sms_messages_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/SMS/ShortCodes',
        'sms_short_codes_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Transcriptions',
        'transcriptions_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Usage/Records',
        'usage_records_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Usage/Records/Daily',
        'usage_records_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Usage/Records/LastMonth',
        'usage_records_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Usage/Records/Monthly',
        'usage_records_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Usage/Records/ThisMonth',
        'usage_records_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Usage/Records/Today',
        'usage_records_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Usage/Triggers',
        'usage_triggers_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/AuthorizedConnectApps',
        'authorized_connect_apps.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Applications',
        'applications_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Conferences'
        '/CFf2fe8498ed59a5733d2c1c1c69a83a28/Participants',
        'participants_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/ConnectApps',
        'connect_apps_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/AvailablePhoneNumbers/US/Local',
        'available_phone_numbers_us_local.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/AvailablePhoneNumbers/US/Mobile',
        'available_phone_numbers_us_local.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/AvailablePhoneNumbers/US/TollFree',
        'available_phone_numbers_us_tollfree.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/AvailablePhoneNumbers/CA/Local',
        'available_phone_numbers_ca_local.json'),
]


class TwilioRestClientTest(BaseIntegrationTest):

    def setUp(self, base_uri=config.base_uri,
              response_handlers=RESPONSE_HANDLERS):
        super(TwilioRestClientTest, self).setUp(
            base_uri=base_uri, response_handlers=response_handlers)
        self.client = TwilioRestClient(config.account_sid,
                                       config.auth_token,
                                       base_uri)

    def test_list_top_level(self):
        for conference in self.client.conferences.list()[0:1]:
            conference.participants.list()

        self.client.authorized_connect_apps.list()
        self.client.applications.list()
        self.client.caller_ids.list()

        for call in self.client.calls.list()[0:1]:
            call.notifications.list()
            call.recordings.list()

            try:
                call.feedback.get()
            except TwilioRestException as e:
                if e.status != 404:
                    raise e

        self.client.connect_apps.list()
        for message in self.client.messages.list()[0:1]:
            message.media_list.list()

        self.client.notifications.list()
        self.client.phone_numbers.list()
        self.client.phone_numbers.available_phone_numbers.list()
        self.client.phone_numbers.available_phone_numbers.list(type='mobile')
        self.client.phone_numbers.available_phone_numbers.list(type='tollfree')
        self.client.phone_numbers.available_phone_numbers.list(country='CA')

        for queue in self.client.queues.list()[0:1]:
            queue.queue_members.list()

        self.client.recordings.list()

        for domain in self.client.sip.domains.list()[0:1]:
            self.client.sip.ip_access_control_list_mappings(domain.name)
            self.client.sip.credential_list_mappings(domain.name)

        for cred_list in self.client.sip.credential_lists.list()[0:1]:
            self.client.sip.credentials(cred_list.name)
            cred_list.credentials.list()

        self.client.sip.ip_access_control_lists.list()
        self.client.sms.messages.list()
        self.client.sms.short_codes.list()
        self.client.transcriptions.list()
        self.client.usage.records.list()
        self.client.usage.triggers.list()

    def test_list_accounts(self):
        accounts = self.client.accounts.list()
        for account in accounts[-1:]:
            account.calls.list()
            account.conferences.list()
            account.incoming_phone_numbers.list()
            account.messages.list()
            account.notifications.list()
            account.outgoing_caller_ids.list()
            account.queues.list()
            account.recordings.list()
            account.sip.credential_lists.list()
            account.sip.domains.list()
            account.sip.ip_access_control_lists.list()
            account.sms.messages.list()
            account.sms.short_codes.list()
            account.transcriptions.list()
            account.usage_records.list()
            account.usage_records.daily.list()
            account.usage_records.last_month.list()
            account.usage_records.monthly.list()
            account.usage_records.this_month.list()
            account.usage_records.today.list()
            account.usage_triggers.list()
