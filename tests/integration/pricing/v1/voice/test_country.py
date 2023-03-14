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


class CountryTestCase(IntegrationTestCase):
    def test_list_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.pricing.v1.voice.countries.list()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://pricing.twilio.com/v1/Voice/Countries",
            )
        )

    def test_read_full_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "countries": [
                    {
                        "country": "Andorra",
                        "iso_country": "AD",
                        "url": "https://pricing.twilio.com/v1/Voice/Countries/AD"
                    }
                ],
                "meta": {
                    "first_page_url": "https://pricing.twilio.com/v1/Voice/Countries?PageSize=50&Page=0",
                    "key": "countries",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://pricing.twilio.com/v1/Voice/Countries?PageSize=50&Page=0"
                }
            }
            """,
            )
        )

        actual = self.client.pricing.v1.voice.countries.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "countries": [],
                "meta": {
                    "first_page_url": "https://pricing.twilio.com/v1/Voice/Countries?PageSize=50&Page=0",
                    "key": "countries",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://pricing.twilio.com/v1/Voice/Countries?PageSize=50&Page=0"
                }
            }
            """,
            )
        )

        actual = self.client.pricing.v1.voice.countries.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.pricing.v1.voice.countries("US").fetch()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://pricing.twilio.com/v1/Voice/Countries/US",
            )
        )

    def test_fetch_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "country": "United States",
                "inbound_call_prices": [
                    {
                        "current_price": "0.0085",
                        "number_type": "local",
                        "base_price": "0.0085"
                    },
                    {
                        "current_price": "0.022",
                        "number_type": "toll free",
                        "base_price": "0.022"
                    }
                ],
                "iso_country": "US",
                "outbound_prefix_prices": [
                    {
                        "prefixes": [
                            "1907"
                        ],
                        "current_price": "0.090",
                        "friendly_name": "Programmable Outbound Minute - United States - Alaska",
                        "base_price": "0.090"
                    }
                ],
                "price_unit": "USD",
                "url": "https://pricing.twilio.com/v1/Voice/Countries/US"
            }
            """,
            )
        )

        actual = self.client.pricing.v1.voice.countries("US").fetch()

        self.assertIsNotNone(actual)
