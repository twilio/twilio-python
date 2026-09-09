import unittest
from unittest.mock import Mock

from twilio.rest.api.v2010.account.message import MessageInstance
from twilio.rest.messaging.v2.channels_sender import ChannelsSenderInstance
from twilio.rest.memory.v1.recall import RecallInstance


def _build_base_message_payload():
    return {
        "body": "Hello, World!",
        "num_segments": "1",
        "direction": "outbound-api",
        "from": "+15558881111",
        "to": "+15559992222",
        "date_updated": "Thu, 30 Jul 2015 20:00:00 +0000",
        "price": "-0.00750",
        "error_message": None,
        "uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json",
        "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "num_media": "0",
        "status": "sent",
        "messaging_service_sid": "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "sid": "SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "date_sent": "Thu, 30 Jul 2015 20:00:00 +0000",
        "date_created": "Thu, 30 Jul 2015 20:00:00 +0000",
        "error_code": None,
        "price_unit": "USD",
        "api_version": "2010-04-01",
        "subresource_uris": {
            "media": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media.json"
        },
    }


def _build_base_channels_sender_payload():
    return {
        "sid": "XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "status": "ONLINE",
        "sender_id": "whatsapp:+15558881111",
        "friendly_name": "My WhatsApp Sender",
        "configuration": {
            "waba_id": "WABA123",
            "verification_method": "sms",
            "verification_code": None,
            "voice_application_sid": None,
            "account_type": None,
        },
        "webhook": {
            "callback_url": "https://example.com/callback",
            "callback_method": "POST",
            "fallback_url": "https://example.com/fallback",
            "fallback_method": "POST",
            "status_callback_url": "https://example.com/status",
            "status_callback_method": "POST",
        },
        "profile": {
            "name": "My Business",
            "about": "We sell things",
            "address": "123 Main St",
            "description": "A business",
            "logo_url": "https://example.com/logo.png",
            "banner_url": None,
            "privacy_url": "https://example.com/privacy",
            "terms_of_service_url": None,
            "accent_color": "#FF0000",
            "use_case": "TRANSACTIONAL",
            "vertical": "Shopping and Retail",
            "websites": [{"website": "https://example.com", "label": "Main"}],
            "emails": [{"email": "info@example.com", "label": "Info"}],
            "phone_numbers": [{"phone_number": "+15558881111", "label": "Support"}],
        },
        "properties": {
            "quality_rating": "GREEN",
            "messaging_limit": "1000",
        },
        "offline_reasons": [
            {
                "code": "12345",
                "message": "Some offline reason",
                "more_info": "https://example.com/error",
            }
        ],
        "compliance": {
            "registration_sid": "CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "countries": [
                {
                    "country": "US",
                    "registration_sid": "CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                    "status": "APPROVED",
                    "carriers": [{"name": "Verizon", "status": "APPROVED"}],
                }
            ],
        },
        "url": "https://messaging.twilio.com/v2/Channels/Senders/XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    }


def _build_base_recall_payload():
    return {
        "observations": [
            {
                "content": "User prefers email communication",
                "occurredAt": "2025-01-15T10:30:00Z",
                "source": "conversation-analysis",
                "conversationIds": ["conv_123"],
                "id": "obs_001",
                "createdAt": "2025-01-15T10:30:00Z",
                "updatedAt": "2025-01-15T10:30:00Z",
                "score": 0.95,
            }
        ],
        "summaries": [
            {
                "source": "auto-summarizer",
                "content": "Customer discussed billing concerns",
                "occurredAt": "2025-01-14T09:00:00Z",
                "conversationId": "conv_456",
                "id": "sum_001",
                "createdAt": "2025-01-14T09:00:00Z",
                "updatedAt": "2025-01-14T09:00:00Z",
                "score": 0.88,
            }
        ],
        "communications": [
            {
                "id": "comm_001",
                "channelId": "CH123",
                "content": {"text": "Hello, how can I help?"},
                "createdAt": "2025-01-15T10:00:00Z",
                "updatedAt": "2025-01-15T10:00:00Z",
                "author": {
                    "id": "agent_001",
                    "name": "Agent Smith",
                    "type": "HUMAN_AGENT",
                    "profileId": "prof_001",
                    "address": "+15558881111",
                    "channel": "sms",
                },
                "recipients": [
                    {
                        "id": "cust_001",
                        "name": "John Doe",
                        "type": "CUSTOMER",
                        "profileId": "prof_002",
                        "address": "+15559992222",
                        "channel": "sms",
                        "deliveryStatus": "delivered",
                    }
                ],
            }
        ],
        "meta": {
            "queryTime": 42,
        },
    }


class TestMessageForwardCompatibility(unittest.TestCase):
    """MessageResource (flat) forward compatibility tests."""

    def setUp(self):
        self.mock_version = Mock()

    def test_add_field_at_parent_level(self):
        payload = _build_base_message_payload()
        payload["new_unknown_field"] = "some-value"
        payload["another_future_field"] = 12345

        instance = MessageInstance(
            self.mock_version,
            payload,
            account_sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            sid="SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        self.assertEqual(instance.body, "Hello, World!")
        self.assertEqual(instance.sid, "SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        self.assertEqual(instance.status, "sent")
        self.assertEqual(instance.direction, "outbound-api")
        self.assertEqual(instance.from_, "+15558881111")
        self.assertEqual(instance.to, "+15559992222")
        self.assertEqual(instance.num_segments, "1")
        self.assertEqual(instance.price, "-0.00750")
        self.assertEqual(instance.price_unit, "USD")

    def test_remove_field_at_parent_level(self):
        payload = _build_base_message_payload()
        del payload["error_message"]
        del payload["price"]
        del payload["num_media"]

        instance = MessageInstance(
            self.mock_version,
            payload,
            account_sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            sid="SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        self.assertEqual(instance.body, "Hello, World!")
        self.assertEqual(instance.sid, "SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        self.assertIsNone(instance.error_message)
        self.assertIsNone(instance.price)
        self.assertIsNone(instance.num_media)
        self.assertEqual(instance.status, "sent")

    def test_unknown_enum_value_at_parent_level(self):
        payload = _build_base_message_payload()
        payload["status"] = "future_unknown_status"
        payload["direction"] = "outbound-future"

        instance = MessageInstance(
            self.mock_version,
            payload,
            account_sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            sid="SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        self.assertEqual(instance.status, "future_unknown_status")
        self.assertEqual(instance.direction, "outbound-future")
        self.assertEqual(instance.body, "Hello, World!")
        self.assertEqual(instance.sid, "SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    def test_empty_response_body(self):
        payload = {}

        instance = MessageInstance(
            self.mock_version,
            payload,
            account_sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            sid="SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        self.assertIsNone(instance.body)
        self.assertIsNone(instance.sid)
        self.assertIsNone(instance.status)
        self.assertIsNone(instance.direction)
        self.assertIsNone(instance.from_)
        self.assertIsNone(instance.to)


class TestChannelsSenderForwardCompatibility(unittest.TestCase):
    """ChannelsSenderResource (nested, top-level) forward compatibility tests."""

    def setUp(self):
        self.mock_version = Mock()

    def test_add_field_at_nested_level(self):
        payload = _build_base_channels_sender_payload()
        payload["configuration"]["future_config_field"] = "new-value"
        payload["profile"]["future_profile_field"] = "new-profile-value"
        payload["webhook"]["future_webhook_field"] = True
        payload["properties"]["future_properties_field"] = 999
        payload["offline_reasons"][0]["future_offline_field"] = "extra"
        payload["compliance"]["future_compliance_field"] = "extra"
        payload["compliance"]["countries"][0]["future_country_field"] = "extra"

        instance = ChannelsSenderInstance(
            self.mock_version,
            payload,
            sid="XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        self.assertEqual(instance.sid, "XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        self.assertEqual(instance.status, "ONLINE")
        self.assertIsNotNone(instance.configuration)
        self.assertEqual(instance.configuration["waba_id"], "WABA123")
        self.assertIsNotNone(instance.webhook)
        self.assertEqual(
            instance.webhook["callback_url"], "https://example.com/callback"
        )
        self.assertIsNotNone(instance.profile)
        self.assertEqual(instance.profile["name"], "My Business")
        self.assertIsNotNone(instance.properties)
        self.assertEqual(instance.properties["quality_rating"], "GREEN")
        self.assertEqual(len(instance.offline_reasons), 1)
        self.assertEqual(instance.offline_reasons[0]["code"], "12345")

    def test_remove_field_inside_nested_object(self):
        payload = _build_base_channels_sender_payload()
        del payload["configuration"]["waba_id"]
        del payload["configuration"]["verification_method"]
        del payload["profile"]["logo_url"]
        del payload["profile"]["accent_color"]
        del payload["webhook"]["fallback_url"]
        del payload["webhook"]["fallback_method"]

        instance = ChannelsSenderInstance(
            self.mock_version,
            payload,
            sid="XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        self.assertEqual(instance.sid, "XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        self.assertIsNotNone(instance.configuration)
        self.assertNotIn("waba_id", instance.configuration)
        self.assertNotIn("verification_method", instance.configuration)
        self.assertIsNotNone(instance.profile)
        self.assertNotIn("logo_url", instance.profile)
        self.assertNotIn("accent_color", instance.profile)
        self.assertIsNotNone(instance.webhook)
        self.assertNotIn("fallback_url", instance.webhook)
        self.assertEqual(
            instance.webhook["callback_url"], "https://example.com/callback"
        )

    def test_remove_whole_nested_object(self):
        payload = _build_base_channels_sender_payload()
        payload["configuration"] = None
        payload["webhook"] = None
        payload["profile"] = None
        payload["properties"] = None
        payload["offline_reasons"] = None
        payload["compliance"] = None

        instance = ChannelsSenderInstance(
            self.mock_version,
            payload,
            sid="XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        self.assertEqual(instance.sid, "XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        self.assertEqual(instance.status, "ONLINE")
        self.assertIsNone(instance.configuration)
        self.assertIsNone(instance.webhook)
        self.assertIsNone(instance.profile)
        self.assertIsNone(instance.properties)
        self.assertIsNone(instance.offline_reasons)
        self.assertIsNone(instance.compliance)

    def test_new_item_appended_to_nested_list(self):
        payload = _build_base_channels_sender_payload()
        payload["offline_reasons"].append(
            {
                "code": "67890",
                "message": "Another reason",
                "more_info": "https://example.com/error2",
                "brand_new_field": "surprise",
            }
        )
        payload["profile"]["websites"].append(
            {
                "website": "https://other.example.com",
                "label": "Other",
                "future_field": "unexpected",
            }
        )
        payload["compliance"]["countries"].append(
            {
                "country": "GB",
                "registration_sid": "CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                "status": "APPROVED",
                "carriers": [
                    {"name": "EE", "status": "APPROVED"},
                    {"name": "Three", "status": "CARRIER_REVIEW"},
                ],
            }
        )

        instance = ChannelsSenderInstance(
            self.mock_version,
            payload,
            sid="XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        self.assertEqual(len(instance.offline_reasons), 2)
        self.assertEqual(instance.offline_reasons[0]["code"], "12345")
        self.assertEqual(instance.offline_reasons[1]["code"], "67890")
        self.assertEqual(instance.offline_reasons[1]["message"], "Another reason")

        self.assertEqual(len(instance.profile["websites"]), 2)
        self.assertEqual(
            instance.profile["websites"][0]["website"], "https://example.com"
        )
        self.assertEqual(
            instance.profile["websites"][1]["website"], "https://other.example.com"
        )

        self.assertEqual(len(instance.compliance["countries"]), 2)
        self.assertEqual(instance.compliance["countries"][1]["country"], "GB")
        self.assertEqual(len(instance.compliance["countries"][1]["carriers"]), 2)

    def test_unknown_enum_value_at_nested_level_and_inside_list_item(self):
        payload = _build_base_channels_sender_payload()
        payload["status"] = "FUTURE_UNKNOWN_STATUS"
        payload["compliance"]["countries"][0]["status"] = "FUTURE_COUNTRY_STATUS"
        payload["compliance"]["countries"][0]["carriers"][0][
            "status"
        ] = "FUTURE_CARRIER_STATUS"

        instance = ChannelsSenderInstance(
            self.mock_version,
            payload,
            sid="XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        self.assertEqual(instance.status, "FUTURE_UNKNOWN_STATUS")
        self.assertEqual(instance.sid, "XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        self.assertEqual(instance.sender_id, "whatsapp:+15558881111")
        self.assertEqual(instance.configuration["waba_id"], "WABA123")
        self.assertEqual(
            instance.compliance["countries"][0]["status"], "FUTURE_COUNTRY_STATUS"
        )
        self.assertEqual(
            instance.compliance["countries"][0]["carriers"][0]["status"],
            "FUTURE_CARRIER_STATUS",
        )


class TestRecallForwardCompatibility(unittest.TestCase):
    """RecallCreateResource (nested, operation-specific) forward compatibility tests."""

    def setUp(self):
        self.mock_version = Mock()

    def test_add_field_at_parent_and_nested_level(self):
        payload = _build_base_recall_payload()
        payload["future_top_level_field"] = "extra-top"
        payload["observations"][0]["future_obs_field"] = "extra-obs"
        payload["summaries"][0]["future_sum_field"] = "extra-sum"
        payload["communications"][0]["future_comm_field"] = "extra-comm"
        payload["communications"][0]["author"]["future_author_field"] = "extra-author"
        payload["communications"][0]["recipients"][0][
            "future_recipient_field"
        ] = "extra-recipient"
        payload["communications"][0]["content"][
            "future_content_field"
        ] = "extra-content"
        payload["meta"]["future_meta_field"] = 999

        instance = RecallInstance(
            self.mock_version,
            payload,
            store_id="store_001",
            profile_id="prof_001",
        )

        self.assertEqual(len(instance.observations), 1)
        self.assertEqual(
            instance.observations[0]["content"], "User prefers email communication"
        )
        self.assertEqual(instance.observations[0]["score"], 0.95)

        self.assertEqual(len(instance.summaries), 1)
        self.assertEqual(
            instance.summaries[0]["content"], "Customer discussed billing concerns"
        )

        self.assertEqual(len(instance.communications), 1)
        self.assertEqual(instance.communications[0]["id"], "comm_001")
        self.assertEqual(instance.communications[0]["author"]["name"], "Agent Smith")
        self.assertEqual(
            instance.communications[0]["recipients"][0]["name"], "John Doe"
        )

        self.assertIsNotNone(instance.meta)
        self.assertEqual(instance.meta["queryTime"], 42)

    def test_remove_field_at_parent_and_inside_nested_object(self):
        payload = _build_base_recall_payload()
        del payload["observations"][0]["score"]
        del payload["observations"][0]["conversationIds"]
        del payload["summaries"][0]["source"]
        del payload["summaries"][0]["score"]
        del payload["communications"][0]["channelId"]
        del payload["communications"][0]["updatedAt"]
        del payload["communications"][0]["author"]["profileId"]
        del payload["communications"][0]["recipients"][0]["deliveryStatus"]
        del payload["communications"][0]["recipients"][0]["profileId"]
        del payload["communications"][0]["content"]["text"]

        instance = RecallInstance(
            self.mock_version,
            payload,
            store_id="store_001",
            profile_id="prof_001",
        )

        self.assertEqual(len(instance.observations), 1)
        self.assertEqual(
            instance.observations[0]["content"], "User prefers email communication"
        )
        self.assertNotIn("score", instance.observations[0])
        self.assertNotIn("conversationIds", instance.observations[0])

        self.assertEqual(len(instance.summaries), 1)
        self.assertEqual(
            instance.summaries[0]["content"], "Customer discussed billing concerns"
        )
        self.assertNotIn("source", instance.summaries[0])
        self.assertNotIn("score", instance.summaries[0])

        self.assertEqual(len(instance.communications), 1)
        self.assertNotIn("channelId", instance.communications[0])
        self.assertNotIn("updatedAt", instance.communications[0])
        self.assertNotIn("profileId", instance.communications[0]["author"])
        self.assertNotIn("deliveryStatus", instance.communications[0]["recipients"][0])
        self.assertNotIn("profileId", instance.communications[0]["recipients"][0])
        self.assertNotIn("text", instance.communications[0]["content"])

    def test_unknown_enum_value_inside_nested_list_item(self):
        payload = _build_base_recall_payload()
        payload["communications"][0]["author"]["type"] = "FUTURE_AGENT_TYPE"
        payload["communications"][0]["recipients"][0]["type"] = "FUTURE_RECIPIENT_TYPE"

        instance = RecallInstance(
            self.mock_version,
            payload,
            store_id="store_001",
            profile_id="prof_001",
        )

        self.assertEqual(len(instance.communications), 1)
        self.assertEqual(
            instance.communications[0]["author"]["type"], "FUTURE_AGENT_TYPE"
        )
        self.assertEqual(
            instance.communications[0]["recipients"][0]["type"],
            "FUTURE_RECIPIENT_TYPE",
        )
        self.assertEqual(instance.communications[0]["author"]["name"], "Agent Smith")
        self.assertEqual(
            instance.communications[0]["recipients"][0]["name"], "John Doe"
        )
        self.assertEqual(instance.communications[0]["id"], "comm_001")


if __name__ == "__main__":
    unittest.main()
