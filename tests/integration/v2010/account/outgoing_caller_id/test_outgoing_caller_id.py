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


class OutgoingCallerIdIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Fri, 21 Aug 2009 00:11:24 +0000",
            "date_updated": "Fri, 21 Aug 2009 00:11:24 +0000",
            "friendly_name": "(415) 867-5309",
            "phone_number": "+141586753096",
            "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .outgoing_caller_ids.get("PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            "date_created": "Fri, 21 Aug 2009 00:11:24 +0000",
            "date_updated": "Fri, 21 Aug 2009 00:11:24 +0000",
            "friendly_name": "(415) 867-5309",
            "phone_number": "+141586753096",
            "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .outgoing_caller_ids.get("PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Fri, 21 Aug 2009 00:11:24 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Fri, 21 Aug 2009 00:11:24 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"(415) 867-5309", instance.friendly_name)
        self.assertIsNotNone(instance.phone_number)
        self.assertEqual(u"+141586753096", instance.phone_number)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Fri, 21 Aug 2009 00:11:24 +0000",
            "date_updated": "Fri, 21 Aug 2009 00:11:24 +0000",
            "friendly_name": "(415) 867-5309",
            "phone_number": "+141586753096",
            "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .outgoing_caller_ids.update(
                "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                friendly_name="friendly_name"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "FriendlyName": "friendly_name"
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Fri, 21 Aug 2009 00:11:24 +0000",
            "date_updated": "Fri, 21 Aug 2009 00:11:24 +0000",
            "friendly_name": "(415) 867-5309",
            "phone_number": "+141586753096",
            "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .outgoing_caller_ids.update(
                "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                friendly_name="friendly_name"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Fri, 21 Aug 2009 00:11:24 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Fri, 21 Aug 2009 00:11:24 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"(415) 867-5309", instance.friendly_name)
        self.assertIsNotNone(instance.phone_number)
        self.assertEqual(u"+141586753096", instance.phone_number)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .outgoing_caller_ids.delete("PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            .outgoing_caller_ids.delete("PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "outgoing_caller_ids": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "Fri, 21 Aug 2009 00:11:24 +0000",
                    "date_updated": "Fri, 21 Aug 2009 00:11:24 +0000",
                    "friendly_name": "(415) 867-5309",
                    "phone_number": "+141586753096",
                    "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .outgoing_caller_ids.list(
                phone_number="+987654321",
                friendly_name="friendly_name"
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("Fri, 21 Aug 2009 00:11:24 +0000"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("Fri, 21 Aug 2009 00:11:24 +0000"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].friendly_name)
        self.assertEqual(u"(415) 867-5309", instances[0].friendly_name)
        self.assertIsNotNone(instances[0].phone_number)
        self.assertEqual(u"+141586753096", instances[0].phone_number)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "outgoing_caller_ids": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "Fri, 21 Aug 2009 00:11:24 +0000",
                    "date_updated": "Fri, 21 Aug 2009 00:11:24 +0000",
                    "friendly_name": "(415) 867-5309",
                    "phone_number": "+141586753096",
                    "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .outgoing_caller_ids.list(
                phone_number="+987654321",
                friendly_name="friendly_name"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "FriendlyName": "friendly_name",
                "PhoneNumber": "+987654321"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "outgoing_caller_ids": [],
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .outgoing_caller_ids.list(
                phone_number="+987654321",
                friendly_name="friendly_name"
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "outgoing_caller_ids": [],
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .outgoing_caller_ids.list(
                phone_number="+987654321",
                friendly_name="friendly_name"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "FriendlyName": "friendly_name",
                "PhoneNumber": "+987654321"
            },
        )

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Fri, 21 Aug 2009 00:11:24 +0000",
            "date_updated": "Fri, 21 Aug 2009 00:11:24 +0000",
            "friendly_name": "(415) 867-5309",
            "phone_number": "+141586753096",
            "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .outgoing_caller_ids.create(
                "+987654321",
                friendly_name="friendly_name",
                call_delay=1,
                extension="extension",
                status_callback="https://example.com",
                status_callback_method="GET"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "CallDelay": 1,
                "Extension": "extension",
                "FriendlyName": "friendly_name",
                "PhoneNumber": "+987654321",
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
            "date_created": "Fri, 21 Aug 2009 00:11:24 +0000",
            "date_updated": "Fri, 21 Aug 2009 00:11:24 +0000",
            "friendly_name": "(415) 867-5309",
            "phone_number": "+141586753096",
            "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .outgoing_caller_ids.create(
                "+987654321",
                friendly_name="friendly_name",
                call_delay=1,
                extension="extension",
                status_callback="https://example.com",
                status_callback_method="GET"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Fri, 21 Aug 2009 00:11:24 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Fri, 21 Aug 2009 00:11:24 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"(415) 867-5309", instance.friendly_name)
        self.assertIsNotNone(instance.phone_number)
        self.assertEqual(u"+141586753096", instance.phone_number)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
