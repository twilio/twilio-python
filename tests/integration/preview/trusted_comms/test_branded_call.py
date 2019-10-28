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


class BrandedCallTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.trusted_comms.branded_calls.create(from_="from", to="to", reason="reason")

        values = {'From': "from", 'To': "to", 'Reason': "reason", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/TrustedComms/Business/BrandedCalls',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "bg_color": "#fff",
                "caller": "Owl Bank",
                "created_at": "2019-05-01T20:00:00Z",
                "font_color": "#000",
                "from": "+15000000000",
                "logo": "https://www.twilio.com/marketing/bundles/company/img/logos/red/twilio-logo-red.png",
                "reason": "Hello Jhon, your appointment has been confirmed.",
                "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "unknown",
                "to": "+573000000000",
                "use_case": "conversational",
                "url": "https://preview.twilio.com/TrustedComms/Business/BrandedCalls"
            }
            '''
        ))

        actual = self.client.preview.trusted_comms.branded_calls.create(from_="from", to="to", reason="reason")

        self.assertIsNotNone(actual)
