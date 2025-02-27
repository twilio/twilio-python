import os
import unittest

from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse


class ClusterTest(unittest.TestCase):
    def setUp(self):
        self.from_number = os.environ["TWILIO_FROM_NUMBER"]
        self.to_number = os.environ["TWILIO_TO_NUMBER"]
        self.api_key = os.environ["TWILIO_API_KEY"]
        self.api_secret = os.environ["TWILIO_API_SECRET"]
        self.account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        self.assistant_id = os.environ["ASSISTANT_ID"]
        self.client = Client(
            username=self.api_key,
            password=self.api_secret,
            account_sid=self.account_sid,
        )
        self.voice_twiml = VoiceResponse()

    def test_send_text_message(self):
        msg = self.client.messages.create(
            to=self.to_number, from_=self.from_number, body="hello world"
        )
        self.assertEqual(msg.to, self.to_number)
        self.assertEqual(msg.from_, self.from_number)
        self.assertEqual(msg.body, "hello world")
        self.assertIsNotNone(msg.sid)

    def test_list_incoming_numbers(self):
        incoming_phone_numbers = self.client.incoming_phone_numbers.list()
        self.assertIsNotNone(incoming_phone_numbers)
        self.assertGreaterEqual(len(incoming_phone_numbers), 2)

    def test_list_an_incoming_number(self):
        incoming_phone_numbers = self.client.incoming_phone_numbers.list(limit=1)
        self.assertIsNotNone(incoming_phone_numbers)
        self.assertEqual(len(incoming_phone_numbers), 1)

    def test_allow_special_characters_for_friendly_and_identity_name(self):
        friendly_name = "service|friendly&name"
        identity_name = "user|identity&string"
        conversation = self.client.conversations.v1.conversations.create(
            friendly_name=friendly_name
        )
        participant = self.client.conversations.v1.conversations(
            conversation.sid
        ).participants.create(identity=identity_name)

        self.assertIsNotNone(conversation)
        self.assertIsNotNone(participant)
        self.assertEqual(conversation.friendly_name, friendly_name)
        self.assertEqual(participant.identity, identity_name)

        remove_conversation = self.client.conversations.v1.conversations(
            conversation.sid
        ).delete()
        self.assertIsNotNone(remove_conversation)

    def test_list_available_numbers(self):
        toll_free_numbers = self.client.available_phone_numbers("US").toll_free.list(
            limit=2
        )
        self.assertIsNotNone(toll_free_numbers)
        self.assertEqual(len(toll_free_numbers), 2)

    def test_fetch_assistant(self):
        assistant = self.client.assistants.v1.assistants(self.assistant_id).fetch()
        self.assertIsNotNone(assistant)
        self.assertEqual(assistant.account_sid, self.account_sid)

    def test_calling_twiml_string(self):
        call = self.client.calls.create(
            to=self.to_number, from_=self.from_number, twiml=str(self.voice_twiml)
        )
        self.assertIsNotNone(call.sid)

    def test_calling_twiml_object(self):
        call = self.client.calls.create(
            to=self.to_number, from_=self.from_number, twiml=self.voice_twiml
        )
        self.assertIsNotNone(call.sid)
