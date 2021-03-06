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


class BrandsInformationTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.trusted_comms.brands_information().fetch(if_none_match="if_none_match")

        headers = {'If-None-Match': "if_none_match", }
        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/TrustedComms/BrandsInformation',
            headers=headers,
        ))

    def test_fetch_results_with_etag_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "update_time": "2020-05-19T19:47:51Z",
                "file_link": "https://www.twilio.com",
                "file_link_ttl_in_seconds": "900",
                "url": "https://preview.twilio.com/TrustedComms/BrandsInformation"
            }
            '''
        ))

        actual = self.client.preview.trusted_comms.brands_information().fetch()

        self.assertIsNotNone(actual)
