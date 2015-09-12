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
from twilio.rest.conversations.client import ConversationsClient
from twilio.rest.http import Response
from twilio.rest.resources.util import parse_iso_date


class ConversationIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = ConversationsClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2015-05-12T21:13:15Z",
            "duration": 60,
            "end_time": "2015-05-12T21:14:15Z",
            "links": {
                "participants": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants"
            },
            "sid": "CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "start_time": "2015-05-12T21:13:15Z",
            "status": "created",
            "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .conversations.get("CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = ConversationsClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2015-05-12T21:13:15Z",
            "duration": 60,
            "end_time": "2015-05-12T21:14:15Z",
            "links": {
                "participants": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants"
            },
            "sid": "CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "start_time": "2015-05-12T21:13:15Z",
            "status": "created",
            "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .conversations.get("CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2015-05-12T21:13:15Z"), instance.date_created)
        self.assertIsNotNone(instance.duration)
        self.assertEqual(60, instance.duration)
        self.assertIsNotNone(instance.end_time)
        self.assertEqual(parse_iso_date("2015-05-12T21:14:15Z"), instance.end_time)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.start_time)
        self.assertEqual(parse_iso_date("2015-05-12T21:13:15Z"), instance.start_time)
        self.assertIsNotNone(instance.status)
        self.assertEqual(u"created", instance.status)
