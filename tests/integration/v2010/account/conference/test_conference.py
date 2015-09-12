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


class ConferenceIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2008-08-01",
            "date_created": "Fri, 18 Feb 2011 19:26:50 +0000",
            "date_updated": "Fri, 18 Feb 2011 19:27:33 +0000",
            "friendly_name": "AHH YEAH",
            "sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "status": "completed",
            "subresource_uris": {
                "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json"
            },
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .conferences.get("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            "api_version": "2008-08-01",
            "date_created": "Fri, 18 Feb 2011 19:26:50 +0000",
            "date_updated": "Fri, 18 Feb 2011 19:27:33 +0000",
            "friendly_name": "AHH YEAH",
            "sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "status": "completed",
            "subresource_uris": {
                "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json"
            },
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .conferences.get("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2008-08-01", instance.api_version)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Fri, 18 Feb 2011 19:26:50 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Fri, 18 Feb 2011 19:27:33 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"AHH YEAH", instance.friendly_name)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.status)
        self.assertEqual(u"completed", instance.status)

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "conferences": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2010-04-01",
                    "date_created": "Mon, 22 Aug 2011 20:58:45 +0000",
                    "date_updated": "Mon, 22 Aug 2011 20:58:46 +0000",
                    "friendly_name": null,
                    "sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "status": "in-progress",
                    "subresource_uris": {
                        "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json"
                    },
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?PageSize=1&Page=2",
            "next_page_uri": null,
            "num_pages": 3,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 3,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?PageSize=1"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .conferences.list(
                date_created=datetime(2008, 1, 2, 0, 0),
                date_created_before=datetime(2008, 1, 1, 0, 0),
                date_created_after=datetime(2008, 1, 3, 0, 0),
                date_updated=datetime(2008, 1, 2, 0, 0),
                date_updated_before=datetime(2008, 1, 1, 0, 0),
                date_updated_after=datetime(2008, 1, 3, 0, 0),
                friendly_name="friendly_name",
                status="init"
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].api_version)
        self.assertEqual(u"2010-04-01", instances[0].api_version)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("Mon, 22 Aug 2011 20:58:45 +0000"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("Mon, 22 Aug 2011 20:58:46 +0000"), instances[0].date_updated)
        self.assertIsNone(instances[0].friendly_name)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].status)
        self.assertEqual(u"in-progress", instances[0].status)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "conferences": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2010-04-01",
                    "date_created": "Mon, 22 Aug 2011 20:58:45 +0000",
                    "date_updated": "Mon, 22 Aug 2011 20:58:46 +0000",
                    "friendly_name": null,
                    "sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "status": "in-progress",
                    "subresource_uris": {
                        "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json"
                    },
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?PageSize=1&Page=2",
            "next_page_uri": null,
            "num_pages": 3,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 3,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?PageSize=1"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .conferences.list(
                date_created=datetime(2008, 1, 2, 0, 0),
                date_created_before=datetime(2008, 1, 1, 0, 0),
                date_created_after=datetime(2008, 1, 3, 0, 0),
                date_updated=datetime(2008, 1, 2, 0, 0),
                date_updated_before=datetime(2008, 1, 1, 0, 0),
                date_updated_after=datetime(2008, 1, 3, 0, 0),
                friendly_name="friendly_name",
                status="init"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "DateCreated": "2008-01-02",
                "DateCreated<": "2008-01-01",
                "DateCreated>": "2008-01-03",
                "DateUpdated": "2008-01-02",
                "DateUpdated<": "2008-01-01",
                "DateUpdated>": "2008-01-03",
                "FriendlyName": "friendly_name",
                "Status": "init"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "conferences": [],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?PageSize=1&Page=2",
            "next_page_uri": null,
            "num_pages": 3,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 3,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?PageSize=1"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .conferences.list(
                date_created=datetime(2008, 1, 2, 0, 0),
                date_created_before=datetime(2008, 1, 1, 0, 0),
                date_created_after=datetime(2008, 1, 3, 0, 0),
                date_updated=datetime(2008, 1, 2, 0, 0),
                date_updated_before=datetime(2008, 1, 1, 0, 0),
                date_updated_after=datetime(2008, 1, 3, 0, 0),
                friendly_name="friendly_name",
                status="init"
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "conferences": [],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?PageSize=1&Page=2",
            "next_page_uri": null,
            "num_pages": 3,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 3,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?PageSize=1"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .conferences.list(
                date_created=datetime(2008, 1, 2, 0, 0),
                date_created_before=datetime(2008, 1, 1, 0, 0),
                date_created_after=datetime(2008, 1, 3, 0, 0),
                date_updated=datetime(2008, 1, 2, 0, 0),
                date_updated_before=datetime(2008, 1, 1, 0, 0),
                date_updated_after=datetime(2008, 1, 3, 0, 0),
                friendly_name="friendly_name",
                status="init"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "DateCreated": "2008-01-02",
                "DateCreated<": "2008-01-01",
                "DateCreated>": "2008-01-03",
                "DateUpdated": "2008-01-02",
                "DateUpdated<": "2008-01-01",
                "DateUpdated>": "2008-01-03",
                "FriendlyName": "friendly_name",
                "Status": "init"
            },
        )
