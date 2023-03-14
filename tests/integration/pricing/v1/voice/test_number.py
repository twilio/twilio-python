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


class NumberTestCase(IntegrationTestCase):
    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.pricing.v1.voice.numbers("+15017122661").fetch()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://pricing.twilio.com/v1/Voice/Numbers/+15017122661",
            )
        )

    def test_fetch_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "country": "Iran",
                "inbound_call_price": {
                    "base_price": null,
                    "current_price": null,
                    "number_type": null
                },
                "iso_country": "IR",
                "number": "+987654321",
                "outbound_call_price": {
                    "base_price": "0.255",
                    "current_price": "0.255"
                },
                "price_unit": "USD",
                "url": "https://pricing.twilio.com/v1/Voice/Numbers/+987654321"
            }
            """,
            )
        )

        actual = self.client.pricing.v1.voice.numbers("+15017122661").fetch()

        self.assertIsNotNone(actual)
