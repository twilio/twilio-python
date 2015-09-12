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


class MediaIntegrationTest(unittest.TestCase):

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .messages.get("SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .media.delete("MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media/MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            .messages.get("SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .media.delete("MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "content_type": "image/jpeg",
            "date_created": "Sun, 16 Aug 2015 15:53:54 +0000",
            "date_updated": "Sun, 16 Aug 2015 15:53:55 +0000",
            "parent_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sid": "MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media/MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .messages.get("SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .media.get("MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media/MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            "content_type": "image/jpeg",
            "date_created": "Sun, 16 Aug 2015 15:53:54 +0000",
            "date_updated": "Sun, 16 Aug 2015 15:53:55 +0000",
            "parent_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sid": "MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media/MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .messages.get("SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .media.get("MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.content_type)
        self.assertEqual(u"image/jpeg", instance.content_type)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Sun, 16 Aug 2015 15:53:54 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Sun, 16 Aug 2015 15:53:55 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.parent_sid)
        self.assertEqual(u"SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.parent_sid)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json?PageSize=50&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json?PageSize=50&Page=0",
            "media_list": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "content_type": "image/jpeg",
                    "date_created": "Sun, 16 Aug 2015 15:53:54 +0000",
                    "date_updated": "Sun, 16 Aug 2015 15:53:55 +0000",
                    "parent_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sid": "MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media/MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json?PageSize=50&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .messages.get("SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .media.list(
                date_created=datetime(2008, 1, 2, 0, 0),
                date_created_before=datetime(2008, 1, 1, 0, 0),
                date_created_after=datetime(2008, 1, 3, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].content_type)
        self.assertEqual(u"image/jpeg", instances[0].content_type)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("Sun, 16 Aug 2015 15:53:54 +0000"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("Sun, 16 Aug 2015 15:53:55 +0000"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].parent_sid)
        self.assertEqual(u"SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].parent_sid)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json?PageSize=50&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json?PageSize=50&Page=0",
            "media_list": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "content_type": "image/jpeg",
                    "date_created": "Sun, 16 Aug 2015 15:53:54 +0000",
                    "date_updated": "Sun, 16 Aug 2015 15:53:55 +0000",
                    "parent_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sid": "MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media/MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json?PageSize=50&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .messages.get("SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .media.list(
                date_created=datetime(2008, 1, 2, 0, 0),
                date_created_before=datetime(2008, 1, 1, 0, 0),
                date_created_after=datetime(2008, 1, 3, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "DateCreated": "2008-01-02",
                "DateCreated<": "2008-01-01",
                "DateCreated>": "2008-01-03"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json?PageSize=50&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json?PageSize=50&Page=0",
            "media_list": [],
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json?PageSize=50&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .messages.get("SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .media.list(
                date_created=datetime(2008, 1, 2, 0, 0),
                date_created_before=datetime(2008, 1, 1, 0, 0),
                date_created_after=datetime(2008, 1, 3, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json?PageSize=50&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json?PageSize=50&Page=0",
            "media_list": [],
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json?PageSize=50&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .messages.get("SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .media.list(
                date_created=datetime(2008, 1, 2, 0, 0),
                date_created_before=datetime(2008, 1, 1, 0, 0),
                date_created_after=datetime(2008, 1, 3, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "DateCreated": "2008-01-02",
                "DateCreated<": "2008-01-01",
                "DateCreated>": "2008-01-03"
            },
        )
