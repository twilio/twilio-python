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


class StreamTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .streams.create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Calls/CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Streams.json',
        ))

    def test_create_no_args_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "MZaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "name": null,
                "status": "in-progress",
                "date_updated": "Thu, 30 Jul 2015 20:00:00 +0000"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .streams.create()

        self.assertIsNotNone(actual)

    def test_create_with_args_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "MZaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "name": "myName",
                "status": "in-progress",
                "date_updated": "Thu, 30 Jul 2015 20:00:00 +0000"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .streams.create()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .streams("MZXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(status="stopped")

        values = {'Status': "stopped", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Calls/CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Streams/MZXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
            data=values,
        ))

    def test_update_by_sid_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "MZaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "name": null,
                "status": "stopped",
                "date_updated": "Thu, 30 Jul 2015 20:00:00 +0000"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .streams("MZXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(status="stopped")

        self.assertIsNotNone(actual)

    def test_update_by_name_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "MZaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "name": "myStream",
                "status": "stopped",
                "date_updated": "Thu, 30 Jul 2015 20:00:00 +0000"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .streams("MZXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(status="stopped")

        self.assertIsNotNone(actual)
