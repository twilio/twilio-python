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


class StatisticsIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "cumulative": {
                "avg_task_acceptance_time": 0.0,
                "end_time": "2015-08-18T17:03:13Z",
                "reservations_accepted": 0,
                "reservations_canceled": 0,
                "reservations_created": 0,
                "reservations_rejected": 0,
                "reservations_rescinded": 0,
                "reservations_timed_out": 0,
                "start_time": "2015-08-18T16:48:13Z",
                "tasks_canceled": 0,
                "tasks_created": 0,
                "tasks_deleted": 0,
                "tasks_moved": 0,
                "tasks_timed_out_in_workflow": 0
            },
            "realtime": {
                "activity_statistics": [
                    {
                        "friendly_name": "Offline",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 1
                    },
                    {
                        "friendly_name": "Idle",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    },
                    {
                        "friendly_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    },
                    {
                        "friendly_name": "Reserved",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    },
                    {
                        "friendly_name": "Busy",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    },
                    {
                        "friendly_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    }
                ],
                "longest_task_waiting_age": 0,
                "longest_task_waiting_sid": null,
                "tasks_by_status": {
                    "assigned": 0,
                    "pending": 0,
                    "reserved": 0
                },
                "total_tasks": 0,
                "total_workers": 1
            },
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .statistics.get(
                minutes=1,
                start_date=datetime(2008, 1, 2, 0, 0),
                start_date_before=datetime(2008, 1, 1, 0, 0),
                start_date_after=datetime(2008, 1, 3, 0, 0),
                end_date=datetime(2008, 1, 2, 0, 0),
                end_date_before=datetime(2008, 1, 1, 0, 0),
                end_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "EndDate": "2008-01-02",
                "EndDate<": "2008-01-01",
                "EndDate>": "2008-01-03",
                "Minutes": 1,
                "StartDate": "2008-01-02",
                "StartDate<": "2008-01-01",
                "StartDate>": "2008-01-03"
            },
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "cumulative": {
                "avg_task_acceptance_time": 0.0,
                "end_time": "2015-08-18T17:03:13Z",
                "reservations_accepted": 0,
                "reservations_canceled": 0,
                "reservations_created": 0,
                "reservations_rejected": 0,
                "reservations_rescinded": 0,
                "reservations_timed_out": 0,
                "start_time": "2015-08-18T16:48:13Z",
                "tasks_canceled": 0,
                "tasks_created": 0,
                "tasks_deleted": 0,
                "tasks_moved": 0,
                "tasks_timed_out_in_workflow": 0
            },
            "realtime": {
                "activity_statistics": [
                    {
                        "friendly_name": "Offline",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 1
                    },
                    {
                        "friendly_name": "Idle",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    },
                    {
                        "friendly_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    },
                    {
                        "friendly_name": "Reserved",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    },
                    {
                        "friendly_name": "Busy",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    },
                    {
                        "friendly_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    }
                ],
                "longest_task_waiting_age": 0,
                "longest_task_waiting_sid": null,
                "tasks_by_status": {
                    "assigned": 0,
                    "pending": 0,
                    "reserved": 0
                },
                "total_tasks": 0,
                "total_workers": 1
            },
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .statistics.get(
                minutes=1,
                start_date=datetime(2008, 1, 2, 0, 0),
                start_date_before=datetime(2008, 1, 1, 0, 0),
                start_date_after=datetime(2008, 1, 3, 0, 0),
                end_date=datetime(2008, 1, 2, 0, 0),
                end_date_before=datetime(2008, 1, 1, 0, 0),
                end_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)
