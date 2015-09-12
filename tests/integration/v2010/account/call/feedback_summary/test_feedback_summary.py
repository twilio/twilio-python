# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

import unittest
from datetime import datetime
from twilio.ext.holodeck import Holodeck
from twilio.rest.v2010.client import V2010Client
from twilio.rest.http import Response
from twilio.rest.resources.util import parse_iso_date


class FeedbackSummaryIntegrationTest(unittest.TestCase):

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "call_count": 10200,
            "call_feedback_count": 729,
            "end_date": "2014-01-31",
            "issues": [
                {
                    "count": 45,
                    "description": "imperfect-audio",
                    "percentage_of_total_calls": "0.04%"
                }
            ],
            "quality_score_average": 4.5,
            "quality_score_median": 4,
            "quality_score_standard_deviation": 1,
            "sid": "FSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "start_date": "2014-01-01"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls \
            .feedback_summaries.create(
                datetime(2008, 1, 2, 0, 0),
                datetime(2008, 1, 2, 0, 0),
                include_subaccounts=True,
                status_callback="https://example.com",
                status_callback_method="GET"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/FeedbackSummary.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "EndDate": "2008-01-02",
                "IncludeSubaccounts": "true",
                "StartDate": "2008-01-02",
                "StatusCallback": "https://example.com",
                "StatusCallbackMethod": "GET"
            },
            query_params={},
        )

    def test_create_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "call_count": 10200,
            "call_feedback_count": 729,
            "end_date": "2014-01-31",
            "issues": [
                {
                    "count": 45,
                    "description": "imperfect-audio",
                    "percentage_of_total_calls": "0.04%"
                }
            ],
            "quality_score_average": 4.5,
            "quality_score_median": 4,
            "quality_score_standard_deviation": 1,
            "sid": "FSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "start_date": "2014-01-01"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls \
            .feedback_summaries.create(
                datetime(2008, 1, 2, 0, 0),
                datetime(2008, 1, 2, 0, 0),
                include_subaccounts=True,
                status_callback="https://example.com",
                status_callback_method="GET"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.call_count)
        self.assertEqual(10200, instance.call_count)
        self.assertIsNotNone(instance.call_feedback_count)
        self.assertEqual(729, instance.call_feedback_count)
        self.assertIsNotNone(instance.end_date)
        self.assertEqual(parse_iso_date("2014-01-31"), instance.end_date)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"FSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.start_date)
        self.assertEqual(parse_iso_date("2014-01-01"), instance.start_date)

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "call_count": 10200,
            "call_feedback_count": 729,
            "end_date": "2014-01-31",
            "issues": [
                {
                    "count": 45,
                    "description": "imperfect-audio",
                    "percentage_of_total_calls": "0.04%"
                }
            ],
            "quality_score_average": 4.5,
            "quality_score_median": 4,
            "quality_score_standard_deviation": 1,
            "sid": "FSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "start_date": "2014-01-01"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls \
            .feedback_summaries.get("FSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/FeedbackSummary/FSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "call_count": 10200,
            "call_feedback_count": 729,
            "end_date": "2014-01-31",
            "issues": [
                {
                    "count": 45,
                    "description": "imperfect-audio",
                    "percentage_of_total_calls": "0.04%"
                }
            ],
            "quality_score_average": 4.5,
            "quality_score_median": 4,
            "quality_score_standard_deviation": 1,
            "sid": "FSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "start_date": "2014-01-01"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls \
            .feedback_summaries.get("FSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.call_count)
        self.assertEqual(10200, instance.call_count)
        self.assertIsNotNone(instance.call_feedback_count)
        self.assertEqual(729, instance.call_feedback_count)
        self.assertIsNotNone(instance.end_date)
        self.assertEqual(parse_iso_date("2014-01-31"), instance.end_date)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"FSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.start_date)
        self.assertEqual(parse_iso_date("2014-01-01"), instance.start_date)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls \
            .feedback_summaries.delete("FSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/FeedbackSummary/FSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_delete_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls \
            .feedback_summaries.delete("FSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())
