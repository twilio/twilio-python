# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class UserTestCase(IntegrationTestCase):
    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.frontline_api.v1.users("sid").fetch()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://frontline-api.twilio.com/v1/Users/sid",
            )
        )

    def test_fetch_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "sid": "USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "identity": "john@example.com",
                "friendly_name": "John Doe",
                "avatar": "https://example.com/profile.png",
                "state": "active",
                "is_available": true,
                "url": "https://frontline-api.twilio.com/v1/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            """,
            )
        )

        actual = self.client.frontline_api.v1.users("sid").fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.frontline_api.v1.users("sid").update()

        self.holodeck.assert_has_request(
            Request(
                "post",
                "https://frontline-api.twilio.com/v1/Users/sid",
            )
        )

    def test_update_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "sid": "USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "identity": "john@example.com",
                "friendly_name": "John Doe",
                "avatar": "https://example.com/profile.png",
                "state": "active",
                "is_available": true,
                "url": "https://frontline-api.twilio.com/v1/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            """,
            )
        )

        actual = self.client.frontline_api.v1.users("sid").update()

        self.assertIsNotNone(actual)
