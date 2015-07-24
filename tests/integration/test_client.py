from tests.integration.base_integration_test import BaseIntegrationTest
from twilio.rest.exceptions import TwilioRestException


class TwilioRestClientTest(BaseIntegrationTest):

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
        self.client.tokens.create(ttl=30)
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
