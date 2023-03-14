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


class SettingTestCase(IntegrationTestCase):
    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.insights.v1.settings().fetch()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://insights.twilio.com/v1/Voice/Settings",
            )
        )

    def test_fetch_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "voice_trace": true,
                "advanced_features": true,
                "url": "https://insights.twilio.com/v1/Voice/Settings"
            }
            """,
            )
        )

        actual = self.client.insights.v1.settings().fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.insights.v1.settings().update()

        self.holodeck.assert_has_request(
            Request(
                "post",
                "https://insights.twilio.com/v1/Voice/Settings",
            )
        )

    def test_update_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "voice_trace": true,
                "advanced_features": true,
                "url": "https://insights.twilio.com/v1/Voice/Settings"
            }
            """,
            )
        )

        actual = self.client.insights.v1.settings().update()

        self.assertIsNotNone(actual)
