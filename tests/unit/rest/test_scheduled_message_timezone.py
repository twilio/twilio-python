"""Scheduled messages must preserve the instant of timezone-aware SendAt values."""

import datetime
import unittest
from unittest.mock import Mock

from twilio.http.response import Response
from twilio.rest import Client


class ScheduledMessageTimezoneTest(unittest.TestCase):
    """Exercise serialization through the public messages.create method."""

    def assert_send_at(self, value, expected):
        """Capture a request without sending it to Twilio."""
        http_client = Mock()
        http_client.request.return_value = Response(201, '{"sid":"SM123"}')
        client = Client("AC123", "test-token", http_client=http_client)
        client.messages.create(
            to="+15555550123",
            messaging_service_sid="MG" + "0" * 32,
            schedule_type="fixed",
            body="test",
            send_at=value,
        )
        self.assertEqual(
            expected, http_client.request.call_args.kwargs["data"]["SendAt"]
        )

    def test_positive_offset_crosses_previous_day(self):
        """Convert a fractional positive offset before adding the UTC suffix."""
        value = datetime.datetime(
            2030,
            1,
            2,
            1,
            30,
            tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)),
        )
        self.assert_send_at(value, "2030-01-01T20:00:00Z")

    def test_negative_offset_crosses_next_day(self):
        """Convert a negative offset across midnight."""
        value = datetime.datetime(
            2030, 1, 2, 23, 30, tzinfo=datetime.timezone(datetime.timedelta(hours=-7))
        )
        self.assert_send_at(value, "2030-01-03T06:30:00Z")

    def test_utc_unchanged(self):
        """Keep an already UTC timestamp unchanged."""
        value = datetime.datetime(2030, 1, 2, 3, 4, 5, tzinfo=datetime.timezone.utc)
        self.assert_send_at(value, "2030-01-02T03:04:05Z")

    def test_naive_unchanged(self):
        """Preserve the existing naive datetime interpretation."""
        self.assert_send_at(
            datetime.datetime(2030, 1, 2, 3, 4, 5), "2030-01-02T03:04:05Z"
        )

    def test_date_unchanged(self):
        """Preserve date-only serialization."""
        self.assert_send_at(datetime.date(2030, 1, 2), "2030-01-02T00:00:00Z")

    def test_string_unchanged(self):
        """Preserve callers' preformatted timestamp strings."""
        self.assert_send_at("2030-01-02T03:04:05+02:00", "2030-01-02T03:04:05+02:00")
