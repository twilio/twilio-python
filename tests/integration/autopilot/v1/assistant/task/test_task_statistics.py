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


class TaskStatisticsTestCase(IntegrationTestCase):
    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.autopilot.v1.assistants(
                "UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).tasks("UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").statistics().fetch()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://autopilot.twilio.com/v1/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Tasks/UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Statistics",
            )
        )

    def test_fetch_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/UDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "assistant_sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "task_sid": "UDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "samples_count": 0,
                "fields_count": 0
            }
            """,
            )
        )

        actual = (
            self.client.autopilot.v1.assistants("UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .tasks("UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .statistics()
            .fetch()
        )

        self.assertIsNotNone(actual)
