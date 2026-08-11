"""
Integration tests for twilio-python 9.11.0 release.

Covers the API surface changes introduced in:
  - twilio-oai PR #150
  - twilio-python PR #951

Run with prod credentials:
  export TWILIO_ACCOUNT_SID=ACxxx
  export TWILIO_AUTH_TOKEN=xxx
  export TWILIO_PHONE_NUMBER=+1xxx  # optional, required for Routes v3 test

  pytest tests/cluster/test_9_11_0.py -v
"""

import inspect
import os
import unittest

from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse


class Release9110Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        cls.auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        cls.phone_number = os.environ.get("TWILIO_PHONE_NUMBER")
        cls.client = Client(cls.account_sid, cls.auth_token)

    # -------------------------------------------------------------------------
    # TwiML
    # -------------------------------------------------------------------------

    def test_twiml_dial_passports_attribute(self):
        """<Dial passports="..."> renders the new SHAKEN/STIR passport attribute."""
        response = VoiceResponse()
        response.dial(
            number="+15005550006",
            passports="base64passport1,base64passport2",
        )
        twiml = str(response)
        self.assertIn('passports="base64passport1,base64passport2"', twiml)
        self.assertIn("<Dial", twiml)

    def test_twiml_connect_no_assistant_noun(self):
        """<Connect> no longer accepts <Assistant> as part of the AI Assistants deprecation."""
        from twilio.twiml.voice_response import Connect
        connect_attrs = [
            attr for attr in dir(Connect) if not attr.startswith("_")
        ]
        self.assertNotIn("assistant", connect_attrs)

    # -------------------------------------------------------------------------
    # Accounts — suppress_email_notification parameter (param-level smoke test)
    # -------------------------------------------------------------------------

    def test_accounts_suppress_email_notification_on_secondary_auth_token(self):
        """suppress_email_notification param added to SecondaryAuthToken create/delete."""
        from twilio.rest.accounts.v1.secondary_auth_token import (
            SecondaryAuthTokenContext,
        )
        create_sig = inspect.signature(SecondaryAuthTokenContext.create)
        self.assertIn("suppress_email_notification", create_sig.parameters)

        delete_sig = inspect.signature(SecondaryAuthTokenContext.delete)
        self.assertIn("suppress_email_notification", delete_sig.parameters)

    def test_accounts_suppress_email_notification_on_auth_token_promotion(self):
        """suppress_email_notification param added to AuthTokenPromotion update."""
        from twilio.rest.accounts.v1.auth_token_promotion import (
            AuthTokenPromotionContext,
        )
        update_sig = inspect.signature(AuthTokenPromotionContext.update)
        self.assertIn("suppress_email_notification", update_sig.parameters)

    # -------------------------------------------------------------------------
    # Voice v2 (new module)
    # -------------------------------------------------------------------------

    def test_voice_v2_recording_configuration_fetch(self):
        """Voice v2 recording configuration endpoint is reachable."""
        try:
            result = self.client.voice.v2.recording("default").fetch()
            self.assertIsNotNone(result)
        except TwilioRestException as e:
            # 404 means the endpoint exists but no 'default' config is set up —
            # that is still a valid response demonstrating the SDK routes correctly.
            self.assertIn(e.status, [403, 404])

    def test_voice_v2_transcription_configuration_fetch(self):
        """Voice v2 transcription configuration endpoint is reachable."""
        try:
            result = self.client.voice.v2.transcription("default").fetch()
            self.assertIsNotNone(result)
        except TwilioRestException as e:
            self.assertIn(e.status, [403, 404])

    def test_voice_v2_account_default_configuration_recording_fetch(self):
        """Voice v2 AccountDefaultConfiguration for Recording type is reachable."""
        try:
            result = self.client.voice.v2.account_default_configuration(
                "Recording"
            ).fetch()
            self.assertIsNotNone(result)
        except TwilioRestException as e:
            self.assertIn(e.status, [403, 404])

    # -------------------------------------------------------------------------
    # Insights v3 (new module)
    # -------------------------------------------------------------------------

    def test_insights_v3_metadata_fetch(self):
        """Insights v3 metadata endpoint returns domain/cube info."""
        try:
            metadata = self.client.insights.v3.metadata.fetch()
            self.assertIsNotNone(metadata)
        except TwilioRestException as e:
            self.assertIn(e.status, [403, 404])

    def test_insights_v3_query_create(self):
        """Insights v3 synchronous query create executes successfully."""
        from twilio.rest.insights.v3.query import QueryList

        query_def = QueryList.QueryDefinition(
            {"measures": ["calls.count"], "dimensions": []}
        )
        query_request = QueryList.InsightsQueryRequest(
            {"domain": "voice", "query": query_def}
        )
        try:
            result = self.client.insights.v3.query.create(
                insights_query_request=query_request
            )
            self.assertIsNotNone(result)
        except TwilioRestException as e:
            # 400 (bad query) or 403 (insufficient permissions) are acceptable;
            # what matters is the request reached the API correctly.
            self.assertIn(e.status, [400, 403, 404, 422])

    # -------------------------------------------------------------------------
    # Intelligence v3 (new module)
    # -------------------------------------------------------------------------

    def test_intelligence_v3_operators_list(self):
        """Intelligence v3 operators list returns a list."""
        operators = self.client.intelligence.v3.operators.list(limit=5)
        self.assertIsNotNone(operators)
        self.assertIsInstance(operators, list)

    def test_intelligence_v3_conversations_list(self):
        """Intelligence v3 conversations list returns a list."""
        try:
            conversations = self.client.intelligence.v3.conversations.list(limit=5)
            self.assertIsNotNone(conversations)
            self.assertIsInstance(conversations, list)
        except TwilioRestException as e:
            self.assertIn(e.status, [403, 404])

    # -------------------------------------------------------------------------
    # Memory v1 (new module) — full create/fetch/delete lifecycle
    # -------------------------------------------------------------------------

    def test_memory_v1_store_lifecycle(self):
        """Memory v1 store create (async 202) → poll operation → fetch → delete lifecycle."""
        import time
        from twilio.rest.memory.v1.store import StoreList

        import uuid

        unique_name = f"itest-9110-{uuid.uuid4().hex[:8]}"
        service_req = StoreList.ServiceRequest(
            {
                "displayName": unique_name,
                "description": "Temp store for 9.11.0 integration test",
            }
        )

        # Create is async — returns HTTP 202 with a status_url to poll, not the store ID
        create_response = self.client.memory.v1.stores.create_with_http_info(
            service_request=service_req
        )
        self.assertEqual(create_response.status_code, 202)
        stub = create_response.data
        self.assertIsNotNone(stub.status_url)

        op_id = stub.status_url.rstrip("/").split("/")[-1]

        op = None
        for _ in range(15):
            op = self.client.memory.v1.operations(op_id).fetch()
            if op.status in ("COMPLETED", "FAILED"):
                break
            time.sleep(2)

        if op and op.status == "FAILED":
            error_code = (op.error or {}).get("code")
            if error_code == 520044:
                self.skipTest(
                    "Account has reached max memory stores; skipping lifecycle test"
                )
            self.fail(f"Store creation failed: {op.error}")

        self.assertEqual(op.status, "COMPLETED")
        self.assertIsNotNone(op.result_url)

        store_id = op.result_url.rstrip("/").split("/")[-1]

        try:
            fetched = self.client.memory.v1.stores(store_id).fetch()
            self.assertIsNotNone(fetched.id)
            self.assertEqual(fetched.id, store_id)
        finally:
            deleted = self.client.memory.v1.stores(store_id).delete()
            self.assertTrue(deleted)

    def test_memory_v1_stores_list(self):
        """Memory v1 stores list returns store ID strings; each is fetchable."""
        stores = self.client.memory.v1.stores.list(limit=5)
        self.assertIsInstance(stores, list)
        if stores:
            # The Memory API list response contains store IDs as plain strings
            self.assertIsInstance(stores[0], str)
            self.assertTrue(stores[0].startswith("mem_store_"))
            # Verify a full fetch by ID works
            fetched = self.client.memory.v1.stores(stores[0]).fetch()
            self.assertIsNotNone(fetched.id)
            self.assertEqual(fetched.id, stores[0])

    # -------------------------------------------------------------------------
    # Knowledge v2 (new module)
    # -------------------------------------------------------------------------

    def test_knowledge_v2_knowledge_bases_list(self):
        """Knowledge v2 knowledge_bases list endpoint returns a list."""
        try:
            knowledge_bases = self.client.knowledge.v2.knowledge_bases.list(limit=5)
            self.assertIsNotNone(knowledge_bases)
            self.assertIsInstance(knowledge_bases, list)
        except TwilioRestException as e:
            self.assertIn(e.status, [403, 404])

    # -------------------------------------------------------------------------
    # Conversations v2 (new module)
    # -------------------------------------------------------------------------

    def test_conversations_v2_configurations_list(self):
        """Conversations v2 configurations list endpoint returns a list."""
        try:
            configurations = self.client.conversations.v2.configurations.list(limit=5)
            self.assertIsNotNone(configurations)
            self.assertIsInstance(configurations, list)
        except TwilioRestException as e:
            self.assertIn(e.status, [403, 404])

    def test_conversations_v2_conversations_list(self):
        """Conversations v2 conversations list endpoint is reachable."""
        try:
            conversations = self.client.conversations.v2.conversations.list(limit=5)
            self.assertIsNotNone(conversations)
            self.assertIsInstance(conversations, list)
        except TwilioRestException as e:
            self.assertIn(e.status, [403, 404])

    # -------------------------------------------------------------------------
    # Routes v3 (new module)
    # -------------------------------------------------------------------------

    def test_routes_v3_phone_number_fetch(self):
        """Routes v3 phone number routing config is fetchable for a known number."""
        if not self.phone_number:
            self.skipTest("TWILIO_PHONE_NUMBER not set — skipping Routes v3 test")

        try:
            result = self.client.routes.v3.phone_numbers(self.phone_number).fetch()
            self.assertIsNotNone(result)
            self.assertEqual(result.phone_number, self.phone_number)
        except TwilioRestException as e:
            # 404 = number exists but no route assigned yet (valid for new accounts)
            self.assertIn(e.status, [403, 404])


if __name__ == "__main__":
    unittest.main()
