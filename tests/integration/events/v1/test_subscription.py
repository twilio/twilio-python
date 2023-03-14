# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base import serialize
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class SubscriptionTestCase(IntegrationTestCase):
    def test_list_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.events.v1.subscriptions.list()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://events.twilio.com/v1/Subscriptions",
            )
        )

    def test_read_empty_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "subscriptions": [],
                "meta": {
                    "page": 0,
                    "page_size": 10,
                    "first_page_url": "https://events.twilio.com/v1/Subscriptions?PageSize=10&Page=0",
                    "previous_page_url": null,
                    "url": "https://events.twilio.com/v1/Subscriptions?PageSize=10&Page=0",
                    "next_page_url": null,
                    "key": "subscriptions"
                }
            }
            """,
            )
        )

        actual = self.client.events.v1.subscriptions.list()

        self.assertIsNotNone(actual)

    def test_read_results_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "subscriptions": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:01:33Z",
                        "sid": "DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sink_sid": "DGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "description": "A subscription",
                        "url": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "subscribed_events": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedEvents"
                        }
                    },
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:01:33Z",
                        "sid": "DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                        "sink_sid": "DGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "description": "Another subscription",
                        "url": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                        "links": {
                            "subscribed_events": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab/SubscribedEvents"
                        }
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 20,
                    "first_page_url": "https://events.twilio.com/v1/Subscriptions?PageSize=20&Page=0",
                    "previous_page_url": null,
                    "url": "https://events.twilio.com/v1/Subscriptions?PageSize=20&Page=0",
                    "next_page_url": null,
                    "key": "subscriptions"
                }
            }
            """,
            )
        )

        actual = self.client.events.v1.subscriptions.list()

        self.assertIsNotNone(actual)

    def test_read_results_filtered_by_sink_sid_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "subscriptions": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:01:33Z",
                        "sid": "DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sink_sid": "DGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "description": "A subscription",
                        "url": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "subscribed_events": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedEvents"
                        }
                    },
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:01:33Z",
                        "sid": "DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                        "sink_sid": "DGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "description": "Another subscription",
                        "url": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                        "links": {
                            "subscribed_events": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab/SubscribedEvents"
                        }
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 10,
                    "first_page_url": "https://events.twilio.com/v1/Subscriptions?SinkSid=DGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=10&Page=0",
                    "previous_page_url": null,
                    "url": "https://events.twilio.com/v1/Subscriptions?SinkSid=DGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=10&Page=0",
                    "next_page_url": null,
                    "key": "subscriptions"
                }
            }
            """,
            )
        )

        actual = self.client.events.v1.subscriptions.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.events.v1.subscriptions(
                "DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).fetch()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://events.twilio.com/v1/Subscriptions/DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_fetch_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:01:33Z",
                "sid": "DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sink_sid": "DGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "description": "A subscription",
                "url": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "subscribed_events": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedEvents"
                }
            }
            """,
            )
        )

        actual = self.client.events.v1.subscriptions(
            "DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).fetch()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.events.v1.subscriptions.create(
                description="description",
                sink_sid="DGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                types=[{}],
            )

        values = {
            "Description": "description",
            "SinkSid": "DGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "Types": serialize.map([{}], lambda e: serialize.object(e)),
        }

        self.holodeck.assert_has_request(
            Request(
                "post",
                "https://events.twilio.com/v1/Subscriptions",
                data=values,
            )
        )

    def test_create_response(self):
        self.holodeck.mock(
            Response(
                201,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:01:33Z",
                "sid": "DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sink_sid": "DGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "description": "A subscription",
                "url": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "subscribed_events": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedEvents"
                }
            }
            """,
            )
        )

        actual = self.client.events.v1.subscriptions.create(
            description="description",
            sink_sid="DGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            types=[{}],
        )

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.events.v1.subscriptions(
                "DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).update()

        self.holodeck.assert_has_request(
            Request(
                "post",
                "https://events.twilio.com/v1/Subscriptions/DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_update_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2020-07-30T20:01:33Z",
                "sid": "DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sink_sid": "DGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                "description": "Updated description",
                "url": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "subscribed_events": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedEvents"
                }
            }
            """,
            )
        )

        actual = self.client.events.v1.subscriptions(
            "DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).update()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.events.v1.subscriptions(
                "DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).delete()

        self.holodeck.assert_has_request(
            Request(
                "delete",
                "https://events.twilio.com/v1/Subscriptions/DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_delete_response(self):
        self.holodeck.mock(
            Response(
                204,
                None,
            )
        )

        actual = self.client.events.v1.subscriptions(
            "DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).delete()

        self.assertTrue(actual)
