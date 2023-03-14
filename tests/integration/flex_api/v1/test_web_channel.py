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


class WebChannelTestCase(IntegrationTestCase):
    def test_list_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.flex_api.v1.web_channel.list()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://flex-api.twilio.com/v1/WebChannels",
            )
        )

    def test_read_full_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://flex-api.twilio.com/v1/WebChannels?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://flex-api.twilio.com/v1/WebChannels?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "flex_chat_channels"
                },
                "flex_chat_channels": [
                    {
                        "flex_flow_sid": "FOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2016-08-01T22:10:40Z",
                        "date_updated": "2016-08-01T22:10:40Z",
                        "url": "https://flex-api.twilio.com/v1/WebChannels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            """,
            )
        )

        actual = self.client.flex_api.v1.web_channel.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://flex-api.twilio.com/v1/WebChannels?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://flex-api.twilio.com/v1/WebChannels?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "flex_chat_channels"
                },
                "flex_chat_channels": []
            }
            """,
            )
        )

        actual = self.client.flex_api.v1.web_channel.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.flex_api.v1.web_channel(
                "CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).fetch()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://flex-api.twilio.com/v1/WebChannels/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_fetch_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "flex_flow_sid": "FOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2016-08-01T22:10:40Z",
                "date_updated": "2016-08-01T22:10:40Z",
                "url": "https://flex-api.twilio.com/v1/WebChannels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            """,
            )
        )

        actual = self.client.flex_api.v1.web_channel(
            "CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).fetch()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.flex_api.v1.web_channel.create(
                flex_flow_sid="FOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                identity="identity",
                customer_friendly_name="customer_friendly_name",
                chat_friendly_name="chat_friendly_name",
            )

        values = {
            "FlexFlowSid": "FOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "Identity": "identity",
            "CustomerFriendlyName": "customer_friendly_name",
            "ChatFriendlyName": "chat_friendly_name",
        }

        self.holodeck.assert_has_request(
            Request(
                "post",
                "https://flex-api.twilio.com/v1/WebChannels",
                data=values,
            )
        )

    def test_create_response(self):
        self.holodeck.mock(
            Response(
                201,
                """
            {
                "flex_flow_sid": "FOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2016-08-01T22:10:40Z",
                "date_updated": "2016-08-01T22:10:40Z",
                "url": "https://flex-api.twilio.com/v1/WebChannels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            """,
            )
        )

        actual = self.client.flex_api.v1.web_channel.create(
            flex_flow_sid="FOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            identity="identity",
            customer_friendly_name="customer_friendly_name",
            chat_friendly_name="chat_friendly_name",
        )

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.flex_api.v1.web_channel(
                "CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).update()

        self.holodeck.assert_has_request(
            Request(
                "post",
                "https://flex-api.twilio.com/v1/WebChannels/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_update_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "flex_flow_sid": "FOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2016-08-01T22:10:40Z",
                "date_updated": "2016-08-01T22:10:40Z",
                "url": "https://flex-api.twilio.com/v1/WebChannels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            """,
            )
        )

        actual = self.client.flex_api.v1.web_channel(
            "CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).update()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.flex_api.v1.web_channel(
                "CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).delete()

        self.holodeck.assert_has_request(
            Request(
                "delete",
                "https://flex-api.twilio.com/v1/WebChannels/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_delete_response(self):
        self.holodeck.mock(
            Response(
                204,
                None,
            )
        )

        actual = self.client.flex_api.v1.web_channel(
            "CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).delete()

        self.assertTrue(actual)
