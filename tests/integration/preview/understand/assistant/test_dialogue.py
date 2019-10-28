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


class DialogueTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.understand.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .dialogues(sid="UKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/understand/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Dialogues/UKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "assistant_sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "UKkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",
                "url": "https://preview.twilio.com/understand/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Dialogues/UKkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",
                "data": {}
            }
            '''
        ))

        actual = self.client.preview.understand.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                               .dialogues(sid="UKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)
