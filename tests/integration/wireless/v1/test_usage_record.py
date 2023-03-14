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


class UsageRecordTestCase(IntegrationTestCase):
    def test_list_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.wireless.v1.usage_records.list()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://wireless.twilio.com/v1/UsageRecords",
            )
        )

    def test_fetch_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "usage_records": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "commands": {
                            "billing_units": "USD",
                            "billed": 0,
                            "total": 3,
                            "from_sim": 1,
                            "to_sim": 2,
                            "home": {
                                "billing_units": "USD",
                                "billed": 0,
                                "total": 3,
                                "from_sim": 1,
                                "to_sim": 2
                            },
                            "national_roaming": {
                                "billing_units": "USD",
                                "billed": 0,
                                "total": 0,
                                "from_sim": 0,
                                "to_sim": 0
                            },
                            "international_roaming": []
                        },
                        "data": {
                            "billing_units": "USD",
                            "billed": 0.35,
                            "total": 3494609,
                            "upload": 731560,
                            "download": 2763049,
                            "units": "bytes",
                            "home": {
                                "billing_units": "USD",
                                "billed": 0.35,
                                "total": 3494609,
                                "upload": 731560,
                                "download": 2763049,
                                "units": "bytes"
                            },
                            "national_roaming": {
                                "billing_units": "USD",
                                "billed": 0,
                                "total": 0,
                                "upload": 0,
                                "download": 0,
                                "units": "bytes"
                            },
                            "international_roaming": []
                        },
                        "period": {
                            "start": "2015-07-30T20:00:00Z",
                            "end": "2015-07-30T20:00:00Z"
                        }
                    },
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "commands": {},
                        "data": {},
                        "period": {}
                    }
                ],
                "meta": {
                    "first_page_url": "https://wireless.twilio.com/v1/UsageRecords?Start=2015-07-30T20%3A00%3A00Z&End=2015-07-30T20%3A00%3A00Z&PageSize=50&Page=0",
                    "key": "usage_records",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://wireless.twilio.com/v1/UsageRecords?Start=2015-07-30T20%3A00%3A00Z&End=2015-07-30T20%3A00%3A00Z&PageSize=50&Page=0"
                }
            }
            """,
            )
        )

        actual = self.client.wireless.v1.usage_records.list()

        self.assertIsNotNone(actual)
