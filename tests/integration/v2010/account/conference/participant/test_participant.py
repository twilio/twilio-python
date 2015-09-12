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


class ParticipantIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",
            "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",
            "end_conference_on_exit": false,
            "muted": false,
            "start_conference_on_enter": true,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .conferences.get("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.get()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",
            "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",
            "end_conference_on_exit": false,
            "muted": false,
            "start_conference_on_enter": true,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .conferences.get("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.get()
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.call_sid)
        self.assertEqual(u"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.call_sid)
        self.assertIsNotNone(instance.conference_sid)
        self.assertEqual(u"CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.conference_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Fri, 18 Feb 2011 21:07:19 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Fri, 18 Feb 2011 21:07:19 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.end_conference_on_exit)
        self.assertEqual(False, instance.end_conference_on_exit)
        self.assertIsNotNone(instance.muted)
        self.assertEqual(False, instance.muted)
        self.assertIsNotNone(instance.start_conference_on_enter)
        self.assertEqual(True, instance.start_conference_on_enter)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",
            "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",
            "end_conference_on_exit": false,
            "muted": false,
            "start_conference_on_enter": true,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .conferences.get("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.update(True)
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "Muted": "true"
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",
            "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",
            "end_conference_on_exit": false,
            "muted": false,
            "start_conference_on_enter": true,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .conferences.get("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.update(True)
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.call_sid)
        self.assertEqual(u"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.call_sid)
        self.assertIsNotNone(instance.conference_sid)
        self.assertEqual(u"CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.conference_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Fri, 18 Feb 2011 21:07:19 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Fri, 18 Feb 2011 21:07:19 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.end_conference_on_exit)
        self.assertEqual(False, instance.end_conference_on_exit)
        self.assertIsNotNone(instance.muted)
        self.assertEqual(False, instance.muted)
        self.assertIsNotNone(instance.start_conference_on_enter)
        self.assertEqual(True, instance.start_conference_on_enter)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .conferences.get("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.delete()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            .conferences.get("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.delete()
        
        self.assertTrue(query.execute())

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "participants": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",
                    "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",
                    "end_conference_on_exit": false,
                    "muted": false,
                    "start_conference_on_enter": true,
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .conferences.get("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.list(muted=True)
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].call_sid)
        self.assertEqual(u"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].call_sid)
        self.assertIsNotNone(instances[0].conference_sid)
        self.assertEqual(u"CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].conference_sid)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("Fri, 18 Feb 2011 21:07:19 +0000"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("Fri, 18 Feb 2011 21:07:19 +0000"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].end_conference_on_exit)
        self.assertEqual(False, instances[0].end_conference_on_exit)
        self.assertIsNotNone(instances[0].muted)
        self.assertEqual(False, instances[0].muted)
        self.assertIsNotNone(instances[0].start_conference_on_enter)
        self.assertEqual(True, instances[0].start_conference_on_enter)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "participants": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",
                    "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",
                    "end_conference_on_exit": false,
                    "muted": false,
                    "start_conference_on_enter": true,
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .conferences.get("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.list(muted=True)
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "Muted": "true"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "participants": [],
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .conferences.get("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.list(muted=True)
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "participants": [],
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .conferences.get("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .participants.list(muted=True)
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "Muted": "true"
            },
        )
