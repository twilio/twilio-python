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


class CallIntegrationTest(unittest.TestCase):

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
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
            "from": "+141586753091",
            "group_sid": null,
            "parent_call_sid": null,
            "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "price": "-0.03000",
            "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
            "status": "completed",
            "subresource_uris": {
                "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"
            },
            "to": "+141586753093",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.create(
                "+123456789",
                "+987654321",
                url="https://example.com",
                application_sid="APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                method="GET",
                fallback_url="https://example.com",
                fallback_method="GET",
                status_callback="https://example.com",
                status_callback_method="GET",
                send_digits="send_digits",
                if_machine="if_machine",
                timeout=1,
                record=True
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "ApplicationSid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "FallbackMethod": "GET",
                "FallbackUrl": "https://example.com",
                "From": "+987654321",
                "IfMachine": "if_machine",
                "Method": "GET",
                "Record": "true",
                "SendDigits": "send_digits",
                "StatusCallback": "https://example.com",
                "StatusCallbackMethod": "GET",
                "Timeout": 1,
                "To": "+123456789",
                "Url": "https://example.com"
            },
            query_params={},
        )

    def test_create_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
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
            "from": "+141586753091",
            "group_sid": null,
            "parent_call_sid": null,
            "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "price": "-0.03000",
            "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
            "status": "completed",
            "subresource_uris": {
                "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"
            },
            "to": "+141586753093",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.create(
                "+123456789",
                "+987654321",
                url="https://example.com",
                application_sid="APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                method="GET",
                fallback_url="https://example.com",
                fallback_method="GET",
                status_callback="https://example.com",
                status_callback_method="GET",
                send_digits="send_digits",
                if_machine="if_machine",
                timeout=1,
                record=True
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNone(instance.annotation)
        self.assertIsNone(instance.answered_by)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2010-04-01", instance.api_version)
        self.assertIsNone(instance.caller_name)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Tue, 31 Aug 2010 20:36:28 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Tue, 31 Aug 2010 20:36:44 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.direction)
        self.assertEqual(u"inbound", instance.direction)
        self.assertIsNotNone(instance.duration)
        self.assertEqual(u"15", instance.duration)
        self.assertIsNotNone(instance.end_time)
        self.assertEqual(parse_iso_date("Tue, 31 Aug 2010 20:36:44 +0000"), instance.end_time)
        self.assertIsNotNone(instance.forwarded_from)
        self.assertEqual(u"+141586753093", instance.forwarded_from)
        self.assertIsNotNone(instance.from_)
        self.assertEqual(u"+141586753091", instance.from_)
        self.assertIsNone(instance.group_sid)
        self.assertIsNone(instance.parent_call_sid)
        self.assertIsNotNone(instance.phone_number_sid)
        self.assertEqual(u"PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.phone_number_sid)
        self.assertIsNotNone(instance.price)
        self.assertEqual(u"-0.03000", instance.price)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.start_time)
        self.assertEqual(parse_iso_date("Tue, 31 Aug 2010 20:36:29 +0000"), instance.start_time)
        self.assertIsNotNone(instance.status)
        self.assertEqual(u"completed", instance.status)
        self.assertIsNotNone(instance.to)
        self.assertEqual(u"+141586753093", instance.to)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.delete("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            .calls.delete("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
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
            "from": "+141586753091",
            "group_sid": null,
            "parent_call_sid": null,
            "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "price": "-0.03000",
            "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
            "status": "completed",
            "subresource_uris": {
                "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"
            },
            "to": "+141586753093",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.get("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            "from": "+141586753091",
            "group_sid": null,
            "parent_call_sid": null,
            "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "price": "-0.03000",
            "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
            "status": "completed",
            "subresource_uris": {
                "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"
            },
            "to": "+141586753093",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.get("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNone(instance.annotation)
        self.assertIsNone(instance.answered_by)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2010-04-01", instance.api_version)
        self.assertIsNone(instance.caller_name)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Tue, 31 Aug 2010 20:36:28 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Tue, 31 Aug 2010 20:36:44 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.direction)
        self.assertEqual(u"inbound", instance.direction)
        self.assertIsNotNone(instance.duration)
        self.assertEqual(u"15", instance.duration)
        self.assertIsNotNone(instance.end_time)
        self.assertEqual(parse_iso_date("Tue, 31 Aug 2010 20:36:44 +0000"), instance.end_time)
        self.assertIsNotNone(instance.forwarded_from)
        self.assertEqual(u"+141586753093", instance.forwarded_from)
        self.assertIsNotNone(instance.from_)
        self.assertEqual(u"+141586753091", instance.from_)
        self.assertIsNone(instance.group_sid)
        self.assertIsNone(instance.parent_call_sid)
        self.assertIsNotNone(instance.phone_number_sid)
        self.assertEqual(u"PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.phone_number_sid)
        self.assertIsNotNone(instance.price)
        self.assertEqual(u"-0.03000", instance.price)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.start_time)
        self.assertEqual(parse_iso_date("Tue, 31 Aug 2010 20:36:29 +0000"), instance.start_time)
        self.assertIsNotNone(instance.status)
        self.assertEqual(u"completed", instance.status)
        self.assertIsNotNone(instance.to)
        self.assertEqual(u"+141586753093", instance.to)

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
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
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?PageSize=1&Page=9690",
            "next_page_uri": null,
            "num_pages": 9691,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 9691,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.list(
                to="+123456789",
                from_="+987654321",
                parent_call_sid="CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                status="queued",
                start_time=datetime(2008, 1, 2, 0, 0),
                start_time_before=datetime(2008, 1, 1, 0, 0),
                start_time_after=datetime(2008, 1, 3, 0, 0),
                end_time=datetime(2008, 1, 2, 0, 0),
                end_time_before=datetime(2008, 1, 1, 0, 0),
                end_time_after=datetime(2008, 1, 3, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNone(instances[0].annotation)
        self.assertIsNone(instances[0].answered_by)
        self.assertIsNotNone(instances[0].api_version)
        self.assertEqual(u"2010-04-01", instances[0].api_version)
        self.assertIsNotNone(instances[0].caller_name)
        self.assertEqual(u"", instances[0].caller_name)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("Fri, 04 Sep 2015 22:48:30 +0000"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("Fri, 04 Sep 2015 22:48:35 +0000"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].direction)
        self.assertEqual(u"outbound-api", instances[0].direction)
        self.assertIsNotNone(instances[0].duration)
        self.assertEqual(u"0", instances[0].duration)
        self.assertIsNotNone(instances[0].end_time)
        self.assertEqual(parse_iso_date("Fri, 04 Sep 2015 22:48:35 +0000"), instances[0].end_time)
        self.assertIsNone(instances[0].forwarded_from)
        self.assertIsNotNone(instances[0].from_)
        self.assertEqual(u"kevin", instances[0].from_)
        self.assertIsNotNone(instances[0].from_formatted)
        self.assertEqual(u"kevin", instances[0].from_formatted)
        self.assertIsNone(instances[0].group_sid)
        self.assertIsNone(instances[0].parent_call_sid)
        self.assertIsNotNone(instances[0].phone_number_sid)
        self.assertEqual(u"", instances[0].phone_number_sid)
        self.assertIsNone(instances[0].price)
        self.assertIsNotNone(instances[0].price_unit)
        self.assertEqual(u"USD", instances[0].price_unit)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].start_time)
        self.assertEqual(parse_iso_date("Fri, 04 Sep 2015 22:48:31 +0000"), instances[0].start_time)
        self.assertIsNotNone(instances[0].status)
        self.assertEqual(u"failed", instances[0].status)
        self.assertIsNotNone(instances[0].to)
        self.assertEqual(u"sip:kevin@example.com", instances[0].to)
        self.assertIsNotNone(instances[0].to_formatted)
        self.assertEqual(u"sip:kevin@example.com", instances[0].to_formatted)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
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
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?PageSize=1&Page=9690",
            "next_page_uri": null,
            "num_pages": 9691,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 9691,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.list(
                to="+123456789",
                from_="+987654321",
                parent_call_sid="CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                status="queued",
                start_time=datetime(2008, 1, 2, 0, 0),
                start_time_before=datetime(2008, 1, 1, 0, 0),
                start_time_after=datetime(2008, 1, 3, 0, 0),
                end_time=datetime(2008, 1, 2, 0, 0),
                end_time_before=datetime(2008, 1, 1, 0, 0),
                end_time_after=datetime(2008, 1, 3, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "EndTime": "2008-01-02",
                "EndTime<": "2008-01-01",
                "EndTime>": "2008-01-03",
                "From": "+987654321",
                "ParentCallSid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "StartTime": "2008-01-02",
                "StartTime<": "2008-01-01",
                "StartTime>": "2008-01-03",
                "Status": "queued",
                "To": "+123456789"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "calls": [],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?PageSize=1&Page=9690",
            "next_page_uri": null,
            "num_pages": 9691,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 9691,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.list(
                to="+123456789",
                from_="+987654321",
                parent_call_sid="CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                status="queued",
                start_time=datetime(2008, 1, 2, 0, 0),
                start_time_before=datetime(2008, 1, 1, 0, 0),
                start_time_after=datetime(2008, 1, 3, 0, 0),
                end_time=datetime(2008, 1, 2, 0, 0),
                end_time_before=datetime(2008, 1, 1, 0, 0),
                end_time_after=datetime(2008, 1, 3, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "calls": [],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?PageSize=1&Page=9690",
            "next_page_uri": null,
            "num_pages": 9691,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 9691,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.list(
                to="+123456789",
                from_="+987654321",
                parent_call_sid="CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                status="queued",
                start_time=datetime(2008, 1, 2, 0, 0),
                start_time_before=datetime(2008, 1, 1, 0, 0),
                start_time_after=datetime(2008, 1, 3, 0, 0),
                end_time=datetime(2008, 1, 2, 0, 0),
                end_time_before=datetime(2008, 1, 1, 0, 0),
                end_time_after=datetime(2008, 1, 3, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "EndTime": "2008-01-02",
                "EndTime<": "2008-01-01",
                "EndTime>": "2008-01-03",
                "From": "+987654321",
                "ParentCallSid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "StartTime": "2008-01-02",
                "StartTime<": "2008-01-01",
                "StartTime>": "2008-01-03",
                "Status": "queued",
                "To": "+123456789"
            },
        )

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
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
            "from": "+141586753091",
            "group_sid": null,
            "parent_call_sid": null,
            "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "price": "-0.03000",
            "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
            "status": "completed",
            "subresource_uris": {
                "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"
            },
            "to": "+141586753093",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.update(
                "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                url="https://example.com",
                method="GET",
                status="queued",
                fallback_url="https://example.com",
                fallback_method="GET",
                status_callback="https://example.com",
                status_callback_method="GET"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "FallbackMethod": "GET",
                "FallbackUrl": "https://example.com",
                "Method": "GET",
                "Status": "queued",
                "StatusCallback": "https://example.com",
                "StatusCallbackMethod": "GET",
                "Url": "https://example.com"
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
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
            "from": "+141586753091",
            "group_sid": null,
            "parent_call_sid": null,
            "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "price": "-0.03000",
            "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
            "status": "completed",
            "subresource_uris": {
                "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"
            },
            "to": "+141586753093",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.update(
                "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                url="https://example.com",
                method="GET",
                status="queued",
                fallback_url="https://example.com",
                fallback_method="GET",
                status_callback="https://example.com",
                status_callback_method="GET"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNone(instance.annotation)
        self.assertIsNone(instance.answered_by)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2010-04-01", instance.api_version)
        self.assertIsNone(instance.caller_name)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Tue, 31 Aug 2010 20:36:28 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Tue, 31 Aug 2010 20:36:44 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.direction)
        self.assertEqual(u"inbound", instance.direction)
        self.assertIsNotNone(instance.duration)
        self.assertEqual(u"15", instance.duration)
        self.assertIsNotNone(instance.end_time)
        self.assertEqual(parse_iso_date("Tue, 31 Aug 2010 20:36:44 +0000"), instance.end_time)
        self.assertIsNotNone(instance.forwarded_from)
        self.assertEqual(u"+141586753093", instance.forwarded_from)
        self.assertIsNotNone(instance.from_)
        self.assertEqual(u"+141586753091", instance.from_)
        self.assertIsNone(instance.group_sid)
        self.assertIsNone(instance.parent_call_sid)
        self.assertIsNotNone(instance.phone_number_sid)
        self.assertEqual(u"PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.phone_number_sid)
        self.assertIsNotNone(instance.price)
        self.assertEqual(u"-0.03000", instance.price)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.start_time)
        self.assertEqual(parse_iso_date("Tue, 31 Aug 2010 20:36:29 +0000"), instance.start_time)
        self.assertIsNotNone(instance.status)
        self.assertEqual(u"completed", instance.status)
        self.assertIsNotNone(instance.to)
        self.assertEqual(u"+141586753093", instance.to)
