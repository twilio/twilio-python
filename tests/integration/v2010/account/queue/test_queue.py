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


class QueueIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "average_wait_time": 0,
            "current_size": 0,
            "date_created": "Tue, 04 Aug 2015 18:39:09 +0000",
            "date_updated": "Tue, 04 Aug 2015 18:39:09 +0000",
            "friendly_name": "0.361280134646222",
            "max_size": 100,
            "sid": "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.get("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "average_wait_time": 0,
            "current_size": 0,
            "date_created": "Tue, 04 Aug 2015 18:39:09 +0000",
            "date_updated": "Tue, 04 Aug 2015 18:39:09 +0000",
            "friendly_name": "0.361280134646222",
            "max_size": 100,
            "sid": "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.get("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.average_wait_time)
        self.assertEqual(0, instance.average_wait_time)
        self.assertIsNotNone(instance.current_size)
        self.assertEqual(0, instance.current_size)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Tue, 04 Aug 2015 18:39:09 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Tue, 04 Aug 2015 18:39:09 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"0.361280134646222", instance.friendly_name)
        self.assertIsNotNone(instance.max_size)
        self.assertEqual(100, instance.max_size)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "average_wait_time": 0,
            "current_size": 0,
            "date_created": "Tue, 04 Aug 2015 18:39:09 +0000",
            "date_updated": "Tue, 04 Aug 2015 18:39:09 +0000",
            "friendly_name": "0.361280134646222",
            "max_size": 100,
            "sid": "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.update(
                "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                friendly_name="friendly_name",
                max_size=1
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "FriendlyName": "friendly_name",
                "MaxSize": 1
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "average_wait_time": 0,
            "current_size": 0,
            "date_created": "Tue, 04 Aug 2015 18:39:09 +0000",
            "date_updated": "Tue, 04 Aug 2015 18:39:09 +0000",
            "friendly_name": "0.361280134646222",
            "max_size": 100,
            "sid": "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.update(
                "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                friendly_name="friendly_name",
                max_size=1
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.average_wait_time)
        self.assertEqual(0, instance.average_wait_time)
        self.assertIsNotNone(instance.current_size)
        self.assertEqual(0, instance.current_size)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Tue, 04 Aug 2015 18:39:09 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Tue, 04 Aug 2015 18:39:09 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"0.361280134646222", instance.friendly_name)
        self.assertIsNotNone(instance.max_size)
        self.assertEqual(100, instance.max_size)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.delete("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            .queues.delete("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json?PageSize=1&Page=12857",
            "next_page_uri": null,
            "num_pages": 12858,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "queues": [
                {
                    "average_wait_time": 0,
                    "current_size": 0,
                    "date_created": "Tue, 04 Aug 2015 18:39:09 +0000",
                    "date_updated": "Tue, 04 Aug 2015 18:39:09 +0000",
                    "friendly_name": "0.361280134646222",
                    "max_size": 100,
                    "sid": "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "start": 0,
            "total": 12858,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.list()
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].average_wait_time)
        self.assertEqual(0, instances[0].average_wait_time)
        self.assertIsNotNone(instances[0].current_size)
        self.assertEqual(0, instances[0].current_size)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("Tue, 04 Aug 2015 18:39:09 +0000"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("Tue, 04 Aug 2015 18:39:09 +0000"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].friendly_name)
        self.assertEqual(u"0.361280134646222", instances[0].friendly_name)
        self.assertIsNotNone(instances[0].max_size)
        self.assertEqual(100, instances[0].max_size)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json?PageSize=1&Page=12857",
            "next_page_uri": null,
            "num_pages": 12858,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "queues": [
                {
                    "average_wait_time": 0,
                    "current_size": 0,
                    "date_created": "Tue, 04 Aug 2015 18:39:09 +0000",
                    "date_updated": "Tue, 04 Aug 2015 18:39:09 +0000",
                    "friendly_name": "0.361280134646222",
                    "max_size": 100,
                    "sid": "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "start": 0,
            "total": 12858,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json?PageSize=1&Page=12857",
            "next_page_uri": null,
            "num_pages": 12858,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "queues": [],
            "start": 0,
            "total": 12858,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.list()
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json?PageSize=1&Page=12857",
            "next_page_uri": null,
            "num_pages": 12858,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "queues": [],
            "start": 0,
            "total": 12858,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "average_wait_time": 0,
            "current_size": 0,
            "date_created": "Tue, 04 Aug 2015 18:39:09 +0000",
            "date_updated": "Tue, 04 Aug 2015 18:39:09 +0000",
            "friendly_name": "0.361280134646222",
            "max_size": 100,
            "sid": "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.create(
                friendly_name="friendly_name",
                max_size=1
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "FriendlyName": "friendly_name",
                "MaxSize": 1
            },
            query_params={},
        )

    def test_create_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "average_wait_time": 0,
            "current_size": 0,
            "date_created": "Tue, 04 Aug 2015 18:39:09 +0000",
            "date_updated": "Tue, 04 Aug 2015 18:39:09 +0000",
            "friendly_name": "0.361280134646222",
            "max_size": 100,
            "sid": "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.create(
                friendly_name="friendly_name",
                max_size=1
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.average_wait_time)
        self.assertEqual(0, instance.average_wait_time)
        self.assertIsNotNone(instance.current_size)
        self.assertEqual(0, instance.current_size)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Tue, 04 Aug 2015 18:39:09 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Tue, 04 Aug 2015 18:39:09 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"0.361280134646222", instance.friendly_name)
        self.assertIsNotNone(instance.max_size)
        self.assertEqual(100, instance.max_size)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
