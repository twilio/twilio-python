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
from twilio.rest.taskrouter.client import TaskrouterClient
from twilio.rest.http import Response
from twilio.rest.resources.util import parse_iso_date


class ReservationIntegrationTest(unittest.TestCase):

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations?PageSize=50&Page=0",
                "key": "reservations",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations"
            },
            "reservations": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "2014-05-14T10:50:02Z",
                    "date_updated": "2014-05-15T16:03:42Z",
                    "links": {
                        "task": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "worker": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    "reservation_status": "reserved",
                    "sid": "WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "task_sid": "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations/WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "worker_name": "Doug",
                    "worker_sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ]
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.get("WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .reservations.list()
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("2014-05-14T10:50:02Z"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("2014-05-15T16:03:42Z"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].reservation_status)
        self.assertEqual(u"reserved", instances[0].reservation_status)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].task_sid)
        self.assertEqual(u"WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].task_sid)
        self.assertIsNotNone(instances[0].worker_name)
        self.assertEqual(u"Doug", instances[0].worker_name)
        self.assertIsNotNone(instances[0].worker_sid)
        self.assertEqual(u"WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].worker_sid)
        self.assertIsNotNone(instances[0].workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].workspace_sid)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations?PageSize=50&Page=0",
                "key": "reservations",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations"
            },
            "reservations": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "2014-05-14T10:50:02Z",
                    "date_updated": "2014-05-15T16:03:42Z",
                    "links": {
                        "task": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "worker": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    "reservation_status": "reserved",
                    "sid": "WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "task_sid": "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations/WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "worker_name": "Doug",
                    "worker_sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ]
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.get("WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .reservations.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations?PageSize=50&Page=0",
                "key": "reservations",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations"
            },
            "reservations": []
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.get("WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .reservations.list()
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations?PageSize=50&Page=0",
                "key": "reservations",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations"
            },
            "reservations": []
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.get("WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .reservations.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2014-05-14T10:50:02Z",
            "date_updated": "2014-05-15T16:03:42Z",
            "links": {
                "task": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "worker": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
            "reservation_status": "reserved",
            "sid": "WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "task_sid": "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations/WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "worker_name": "Doug",
            "worker_sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.get("WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .reservations.get("WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations/WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2014-05-14T10:50:02Z",
            "date_updated": "2014-05-15T16:03:42Z",
            "links": {
                "task": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "worker": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
            "reservation_status": "reserved",
            "sid": "WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "task_sid": "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations/WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "worker_name": "Doug",
            "worker_sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.get("WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .reservations.get("WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2014-05-14T10:50:02Z"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2014-05-15T16:03:42Z"), instance.date_updated)
        self.assertIsNotNone(instance.reservation_status)
        self.assertEqual(u"reserved", instance.reservation_status)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.task_sid)
        self.assertEqual(u"WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.task_sid)
        self.assertIsNotNone(instance.worker_name)
        self.assertEqual(u"Doug", instance.worker_name)
        self.assertIsNotNone(instance.worker_sid)
        self.assertEqual(u"WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.worker_sid)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2014-05-14T10:50:02Z",
            "date_updated": "2014-05-15T16:03:42Z",
            "links": {
                "task": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "worker": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
            "reservation_status": "reserved",
            "sid": "WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "task_sid": "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations/WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "worker_name": "Doug",
            "worker_sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.get("WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .reservations.update(
                "WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "reservation_status",
                worker_activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations/WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "ReservationStatus": "reservation_status",
                "WorkerActivitySid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2014-05-14T10:50:02Z",
            "date_updated": "2014-05-15T16:03:42Z",
            "links": {
                "task": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "worker": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
            "reservation_status": "reserved",
            "sid": "WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "task_sid": "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Reservations/WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "worker_name": "Doug",
            "worker_sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.get("WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .reservations.update(
                "WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "reservation_status",
                worker_activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2014-05-14T10:50:02Z"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2014-05-15T16:03:42Z"), instance.date_updated)
        self.assertIsNotNone(instance.reservation_status)
        self.assertEqual(u"reserved", instance.reservation_status)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.task_sid)
        self.assertEqual(u"WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.task_sid)
        self.assertIsNotNone(instance.worker_name)
        self.assertEqual(u"Doug", instance.worker_name)
        self.assertIsNotNone(instance.worker_sid)
        self.assertEqual(u"WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.worker_sid)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)
