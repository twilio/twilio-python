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


class CallTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .calls.create(to="+15558675310", from_="+15017122661")

        values = {'To': "+15558675310", 'From': "+15017122661", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Calls.json',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "annotation": null,
                "answered_by": null,
                "api_version": "2010-04-01",
                "caller_name": null,
                "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",
                "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",
                "direction": "inbound",
                "duration": "15",
                "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",
                "forwarded_from": "+141586753093",
                "from": "+14158675308",
                "from_formatted": "(415) 867-5308",
                "group_sid": null,
                "parent_call_sid": null,
                "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "price": "-0.03000",
                "price_unit": "USD",
                "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
                "status": "completed",
                "subresource_uris": {
                    "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                    "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Feedback.json",
                    "feedback_summaries": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/FeedbackSummary.json"
                },
                "to": "+14158675309",
                "to_formatted": "(415) 867-5309",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls.create(to="+15558675310", from_="+15017122661")

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .calls(sid="CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Calls/CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls(sid="CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .calls(sid="CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Calls/CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "annotation": null,
                "answered_by": null,
                "api_version": "2010-04-01",
                "caller_name": null,
                "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",
                "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",
                "direction": "inbound",
                "duration": "15",
                "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",
                "forwarded_from": "+141586753093",
                "from": "+14158675308",
                "from_formatted": "(415) 867-5308",
                "group_sid": null,
                "parent_call_sid": null,
                "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "price": "-0.03000",
                "price_unit": "USD",
                "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
                "status": "completed",
                "subresource_uris": {
                    "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"
                },
                "to": "+14158675309",
                "to_formatted": "(415) 867-5309",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls(sid="CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .calls.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Calls.json',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "calls": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "annotation": null,
                        "answered_by": null,
                        "api_version": "2010-04-01",
                        "caller_name": "",
                        "date_created": "Fri, 04 Sep 2015 22:48:30 +0000",
                        "date_updated": "Fri, 04 Sep 2015 22:48:35 +0000",
                        "direction": "outbound-api",
                        "duration": "0",
                        "end_time": "Fri, 04 Sep 2015 22:48:35 +0000",
                        "forwarded_from": null,
                        "from": "kevin",
                        "from_formatted": "kevin",
                        "group_sid": null,
                        "parent_call_sid": null,
                        "phone_number_sid": "",
                        "price": null,
                        "price_unit": "USD",
                        "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "start_time": "Fri, 04 Sep 2015 22:48:31 +0000",
                        "status": "failed",
                        "subresource_uris": {
                            "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"
                        },
                        "to": "sip:kevin@example.com",
                        "to_formatted": "sip:kevin@example.com",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                    }
                ],
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?PageSize=1&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 1,
                "previous_page_uri": null,
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?PageSize=1&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "calls": [],
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?PageSize=1&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 1,
                "previous_page_uri": null,
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?PageSize=1&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .calls(sid="CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Calls/CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "annotation": null,
                "answered_by": null,
                "api_version": "2010-04-01",
                "caller_name": null,
                "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",
                "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",
                "direction": "inbound",
                "duration": "15",
                "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",
                "forwarded_from": "+141586753093",
                "from": "+14158675308",
                "from_formatted": "(415) 867-5308",
                "group_sid": null,
                "parent_call_sid": null,
                "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "price": "-0.03000",
                "price_unit": "USD",
                "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
                "status": "completed",
                "subresource_uris": {
                    "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                    "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Feedback.json",
                    "feedback_summaries": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/FeedbackSummary.json"
                },
                "to": "+14158675309",
                "to_formatted": "(415) 867-5309",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls(sid="CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_cancel_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "annotation": null,
                "answered_by": null,
                "api_version": "2010-04-01",
                "caller_name": null,
                "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",
                "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",
                "direction": "inbound",
                "duration": "15",
                "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",
                "forwarded_from": "+141586753093",
                "from": "+14158675308",
                "from_formatted": "(415) 867-5308",
                "group_sid": null,
                "parent_call_sid": null,
                "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "price": "-0.03000",
                "price_unit": "USD",
                "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
                "status": "canceled",
                "subresource_uris": {
                    "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                    "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Feedback.json",
                    "feedback_summaries": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/FeedbackSummary.json"
                },
                "to": "+14158675309",
                "to_formatted": "(415) 867-5309",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls(sid="CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_posttwiml_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "annotation": null,
                "answered_by": null,
                "api_version": "2010-04-01",
                "caller_name": null,
                "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",
                "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",
                "direction": "inbound",
                "duration": "15",
                "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",
                "forwarded_from": "+141586753093",
                "from": "+14158675308",
                "from_formatted": "(415) 867-5308",
                "group_sid": null,
                "parent_call_sid": null,
                "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "price": "-0.03000",
                "price_unit": "USD",
                "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
                "status": "canceled",
                "subresource_uris": {
                    "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                    "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Feedback.json",
                    "feedback_summaries": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/FeedbackSummary.json"
                },
                "to": "+14158675309",
                "to_formatted": "(415) 867-5309",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls(sid="CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)
