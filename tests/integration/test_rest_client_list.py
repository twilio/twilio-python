import unittest
from twilio.ext.holodeck import holodeck
from twilio.rest.client import TwilioRestClient
from twilio.rest.exceptions import TwilioRestException


class TwilioRestClientTest(unittest.TestCase):

    def setUp(self):
        self.client = TwilioRestClient('AC' + 'a' * 32, 'AUTHTOKEN')
        holodeck.activate()

    def tearDown(self):
        holodeck.deactivate()

    def test_list_top_level(self):
        for conference in self.client.conferences.list().execute()[0:1]:
            conference.participants.list().execute()

        self.client.authorized_connect_apps.list().execute()
        self.client.applications.list().execute()
        self.client.caller_ids.list().execute()

        for call in self.client.calls.list().execute()[0:1]:
            call.notifications.list().execute()
            call.recordings.list().execute()

            try:
                call.feedback.get()
            except TwilioRestException as e:
                if e.status != 404:
                    raise e

        self.client.connect_apps.list().execute()
        for message in self.client.messages.list().execute()[0:1]:
            if int(message.num_media) > 0:
                message.media_list.list().execute()

        self.client.notifications.list().execute()
        self.client.phone_numbers.list().execute()
        self.client.phone_numbers.available_phone_numbers.list().execute()
        self.client.phone_numbers.available_phone_numbers.list(type='mobile').execute()
        self.client.phone_numbers.available_phone_numbers.list(type='tollfree').execute()
        self.client.phone_numbers.available_phone_numbers.list(country='US').execute()

        for queue in self.client.queues.list().execute()[0:1]:
            queue.queue_members.list().execute()

        self.client.recordings.list().execute()

        for domain in self.client.sip.domains.list().execute()[0:1]:
            self.client.sip.ip_access_control_list_mappings(domain.name)
            self.client.sip.credential_list_mappings(domain.name)

        for cred_list in self.client.sip.credential_lists.list().execute()[0:1]:
            self.client.sip.credentials(cred_list.name)
            cred_list.credentials.list().execute()

        self.client.sip.ip_access_control_lists.list().execute()
        self.client.sms.messages.list().execute()
        self.client.sms.short_codes.list().execute()
        self.client.transcriptions.list().execute()
        self.client.usage.records.list().execute()
        self.client.usage.triggers.list().execute()

    def test_list_accounts(self):
        accounts = self.client.accounts.list().execute()
        for account in accounts[-1:]:
            account.calls.list().execute()
            account.conferences.list().execute()
            account.incoming_phone_numbers.list().execute()
            account.messages.list().execute()
            account.notifications.list().execute()
            account.outgoing_caller_ids.list().execute()
            account.queues.list().execute()
            account.recordings.list().execute()
            account.sip.credential_lists.list().execute()
            account.sip.domains.list().execute()
            account.sip.ip_access_control_lists.list().execute()
            account.sms.messages.list().execute()
            account.sms.short_codes.list().execute()
            account.transcriptions.list().execute()
            account.usage_records.list().execute()
            account.usage_records.daily.list().execute()
            account.usage_records.last_month.list().execute()
            account.usage_records.monthly.list().execute()
            account.usage_records.this_month.list().execute()
            account.usage_records.today.list().execute()
            account.usage_triggers.list().execute()
