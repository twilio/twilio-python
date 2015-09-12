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


class ParticipantIntegrationTest(unittest.TestCase):

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = ConversationsClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0",
                "key": "participants",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0"
            },
            "participants": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "address": "torkel2@ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.endpoint.twilio.com",
                    "conversation_sid": "CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "2015-05-13T23:03:12Z",
                    "duration": 685,
                    "end_time": "2015-05-13T23:14:40Z",
                    "sid": "PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "start_time": "2015-05-13T23:03:15Z",
                    "status": "disconnected",
                    "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ]
        }
        """))
        
        query = client \
            .conversations.get("CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.list()
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].address)
        self.assertEqual(u"torkel2@ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.endpoint.twilio.com", instances[0].address)
        self.assertIsNotNone(instances[0].conversation_sid)
        self.assertEqual(u"CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].conversation_sid)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("2015-05-13T23:03:12Z"), instances[0].date_created)
        self.assertIsNotNone(instances[0].duration)
        self.assertEqual(685, instances[0].duration)
        self.assertIsNotNone(instances[0].end_time)
        self.assertEqual(parse_iso_date("2015-05-13T23:14:40Z"), instances[0].end_time)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].start_time)
        self.assertEqual(parse_iso_date("2015-05-13T23:03:15Z"), instances[0].start_time)
        self.assertIsNotNone(instances[0].status)
        self.assertEqual(u"disconnected", instances[0].status)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = ConversationsClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0",
                "key": "participants",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0"
            },
            "participants": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "address": "torkel2@ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.endpoint.twilio.com",
                    "conversation_sid": "CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "2015-05-13T23:03:12Z",
                    "duration": 685,
                    "end_time": "2015-05-13T23:14:40Z",
                    "sid": "PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "start_time": "2015-05-13T23:03:15Z",
                    "status": "disconnected",
                    "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ]
        }
        """))
        
        query = client \
            .conversations.get("CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = ConversationsClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0",
                "key": "participants",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0"
            },
            "participants": []
        }
        """))
        
        query = client \
            .conversations.get("CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.list()
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = ConversationsClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0",
                "key": "participants",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0"
            },
            "participants": []
        }
        """))
        
        query = client \
            .conversations.get("CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = ConversationsClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "address": "torkel2@ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.endpoint.twilio.com",
            "conversation_sid": "CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2015-05-13T23:03:12Z",
            "duration": 685,
            "end_time": "2015-05-13T23:14:40Z",
            "sid": "PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "start_time": "2015-05-13T23:03:15Z",
            "status": "disconnected",
            "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .conversations.get("CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.create(
                "+123456789",
                "+987654321"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "From": "+987654321",
                "To": "+123456789"
            },
            query_params={},
        )

    def test_create_can_parse_response(self):
        holodeck = Holodeck()
        client = ConversationsClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "address": "torkel2@ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.endpoint.twilio.com",
            "conversation_sid": "CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2015-05-13T23:03:12Z",
            "duration": 685,
            "end_time": "2015-05-13T23:14:40Z",
            "sid": "PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "start_time": "2015-05-13T23:03:15Z",
            "status": "disconnected",
            "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .conversations.get("CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.create(
                "+123456789",
                "+987654321"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.address)
        self.assertEqual(u"torkel2@ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.endpoint.twilio.com", instance.address)
        self.assertIsNotNone(instance.conversation_sid)
        self.assertEqual(u"CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.conversation_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2015-05-13T23:03:12Z"), instance.date_created)
        self.assertIsNotNone(instance.duration)
        self.assertEqual(685, instance.duration)
        self.assertIsNotNone(instance.end_time)
        self.assertEqual(parse_iso_date("2015-05-13T23:14:40Z"), instance.end_time)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.start_time)
        self.assertEqual(parse_iso_date("2015-05-13T23:03:15Z"), instance.start_time)
        self.assertIsNotNone(instance.status)
        self.assertEqual(u"disconnected", instance.status)

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = ConversationsClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "address": "torkel2@ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.endpoint.twilio.com",
            "conversation_sid": "CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2015-05-13T23:03:12Z",
            "duration": 685,
            "end_time": "2015-05-13T23:14:40Z",
            "sid": "PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "start_time": "2015-05-13T23:03:15Z",
            "status": "disconnected",
            "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .conversations.get("CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.get("PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
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
            "address": "torkel2@ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.endpoint.twilio.com",
            "conversation_sid": "CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2015-05-13T23:03:12Z",
            "duration": 685,
            "end_time": "2015-05-13T23:14:40Z",
            "sid": "PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "start_time": "2015-05-13T23:03:15Z",
            "status": "disconnected",
            "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .conversations.get("CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.get("PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.address)
        self.assertEqual(u"torkel2@ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.endpoint.twilio.com", instance.address)
        self.assertIsNotNone(instance.conversation_sid)
        self.assertEqual(u"CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.conversation_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2015-05-13T23:03:12Z"), instance.date_created)
        self.assertIsNotNone(instance.duration)
        self.assertEqual(685, instance.duration)
        self.assertIsNotNone(instance.end_time)
        self.assertEqual(parse_iso_date("2015-05-13T23:14:40Z"), instance.end_time)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.start_time)
        self.assertEqual(parse_iso_date("2015-05-13T23:03:15Z"), instance.start_time)
        self.assertIsNotNone(instance.status)
        self.assertEqual(u"disconnected", instance.status)
