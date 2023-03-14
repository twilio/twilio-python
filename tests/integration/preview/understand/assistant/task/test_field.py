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


class FieldTestCase(IntegrationTestCase):
    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.preview.understand.assistants(
                "UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).tasks("UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fields(
                "UEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).fetch()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://preview.twilio.com/understand/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Tasks/UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Fields/UEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_fetch_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "url": "https://preview.twilio.com/understand/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/UDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Fields/UEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique_name",
                "date_updated": "2015-07-30T20:00:00Z",
                "assistant_sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "task_sid": "UDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "sid": "UEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "field_type": "field_type"
            }
            """,
            )
        )

        actual = (
            self.client.preview.understand.assistants(
                "UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            )
            .tasks("UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .fields("UEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .fetch()
        )

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.preview.understand.assistants(
                "UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).tasks("UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fields.list()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://preview.twilio.com/understand/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Tasks/UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Fields",
            )
        )

    def test_read_empty_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "fields": [],
                "meta": {
                    "page": 0,
                    "first_page_url": "https://preview.twilio.com/understand/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/UDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Fields?PageSize=50&Page=0",
                    "url": "https://preview.twilio.com/understand/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/UDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Fields?PageSize=50&Page=0",
                    "key": "fields",
                    "next_page_url": null,
                    "previous_page_url": null,
                    "page_size": 50
                }
            }
            """,
            )
        )

        actual = (
            self.client.preview.understand.assistants(
                "UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            )
            .tasks("UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .fields.list()
        )

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "fields": [
                    {
                        "url": "https://preview.twilio.com/understand/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/UDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Fields/UEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "unique_name": "unique_name",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "assistant_sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "task_sid": "UDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T20:00:00Z",
                        "sid": "UEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "field_type": "field_type"
                    }
                ],
                "meta": {
                    "page": 0,
                    "first_page_url": "https://preview.twilio.com/understand/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/UDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Fields?PageSize=50&Page=0",
                    "url": "https://preview.twilio.com/understand/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/UDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Fields?PageSize=50&Page=0",
                    "key": "fields",
                    "next_page_url": null,
                    "previous_page_url": null,
                    "page_size": 50
                }
            }
            """,
            )
        )

        actual = (
            self.client.preview.understand.assistants(
                "UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            )
            .tasks("UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .fields.list()
        )

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.preview.understand.assistants(
                "UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).tasks("UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fields.create(
                field_type="field_type", unique_name="unique_name"
            )

        values = {
            "FieldType": "field_type",
            "UniqueName": "unique_name",
        }

        self.holodeck.assert_has_request(
            Request(
                "post",
                "https://preview.twilio.com/understand/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Tasks/UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Fields",
                data=values,
            )
        )

    def test_create_response(self):
        self.holodeck.mock(
            Response(
                201,
                """
            {
                "url": "https://preview.twilio.com/understand/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/UDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Fields/UEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique_name",
                "date_updated": "2015-07-30T20:00:00Z",
                "assistant_sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "task_sid": "UDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "sid": "UEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "field_type": "field_type"
            }
            """,
            )
        )

        actual = (
            self.client.preview.understand.assistants(
                "UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            )
            .tasks("UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .fields.create(field_type="field_type", unique_name="unique_name")
        )

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.preview.understand.assistants(
                "UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).tasks("UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fields(
                "UEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).delete()

        self.holodeck.assert_has_request(
            Request(
                "delete",
                "https://preview.twilio.com/understand/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Tasks/UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Fields/UEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_delete_response(self):
        self.holodeck.mock(
            Response(
                204,
                None,
            )
        )

        actual = (
            self.client.preview.understand.assistants(
                "UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            )
            .tasks("UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .fields("UEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .delete()
        )

        self.assertTrue(actual)
