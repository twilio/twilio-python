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


class WorkflowIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "assignment_callback_url": "http://example.com",
            "configuration": "task-routing:\\n  - filter: \\n      - 1 == 1\\n    target:\\n      - queue: WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\\n        set-priority: 0\\n",
            "date_created": "2014-05-14T10:50:02Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "document_content_type": "application/json",
            "fallback_assignment_callback_url": null,
            "friendly_name": "Default Fifo Workflow",
            "sid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "task_reservation_timeout": 120,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workflows.get("WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
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
            "assignment_callback_url": "http://example.com",
            "configuration": "task-routing:\\n  - filter: \\n      - 1 == 1\\n    target:\\n      - queue: WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\\n        set-priority: 0\\n",
            "date_created": "2014-05-14T10:50:02Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "document_content_type": "application/json",
            "fallback_assignment_callback_url": null,
            "friendly_name": "Default Fifo Workflow",
            "sid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "task_reservation_timeout": 120,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workflows.get("WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.assignment_callback_url)
        self.assertEqual(u"http://example.com", instance.assignment_callback_url)
        self.assertIsNotNone(instance.configuration)
        self.assertEqual(u"task-routing:\n  - filter: \n      - 1 == 1\n    target:\n      - queue: WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n        set-priority: 0\n", instance.configuration)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2014-05-14T10:50:02Z"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2014-05-14T23:26:06Z"), instance.date_updated)
        self.assertIsNotNone(instance.document_content_type)
        self.assertEqual(u"application/json", instance.document_content_type)
        self.assertIsNone(instance.fallback_assignment_callback_url)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"Default Fifo Workflow", instance.friendly_name)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.task_reservation_timeout)
        self.assertEqual(120, instance.task_reservation_timeout)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "assignment_callback_url": "http://example.com",
            "configuration": "task-routing:\\n  - filter: \\n      - 1 == 1\\n    target:\\n      - queue: WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\\n        set-priority: 0\\n",
            "date_created": "2014-05-14T10:50:02Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "document_content_type": "application/json",
            "fallback_assignment_callback_url": null,
            "friendly_name": "Default Fifo Workflow",
            "sid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "task_reservation_timeout": 120,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workflows.update(
                "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                friendly_name="friendly_name",
                assignment_callback_url="/example",
                fallback_assignment_callback_url="/example",
                configuration="configuration",
                task_reservation_timeout=1
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "AssignmentCallbackUrl": "/example",
                "Configuration": "configuration",
                "FallbackAssignmentCallbackUrl": "/example",
                "FriendlyName": "friendly_name",
                "TaskReservationTimeout": 1
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "assignment_callback_url": "http://example.com",
            "configuration": "task-routing:\\n  - filter: \\n      - 1 == 1\\n    target:\\n      - queue: WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\\n        set-priority: 0\\n",
            "date_created": "2014-05-14T10:50:02Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "document_content_type": "application/json",
            "fallback_assignment_callback_url": null,
            "friendly_name": "Default Fifo Workflow",
            "sid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "task_reservation_timeout": 120,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workflows.update(
                "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                friendly_name="friendly_name",
                assignment_callback_url="/example",
                fallback_assignment_callback_url="/example",
                configuration="configuration",
                task_reservation_timeout=1
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.assignment_callback_url)
        self.assertEqual(u"http://example.com", instance.assignment_callback_url)
        self.assertIsNotNone(instance.configuration)
        self.assertEqual(u"task-routing:\n  - filter: \n      - 1 == 1\n    target:\n      - queue: WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n        set-priority: 0\n", instance.configuration)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2014-05-14T10:50:02Z"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2014-05-14T23:26:06Z"), instance.date_updated)
        self.assertIsNotNone(instance.document_content_type)
        self.assertEqual(u"application/json", instance.document_content_type)
        self.assertIsNone(instance.fallback_assignment_callback_url)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"Default Fifo Workflow", instance.friendly_name)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.task_reservation_timeout)
        self.assertEqual(120, instance.task_reservation_timeout)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workflows.delete("WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_delete_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workflows.delete("WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows?PageSize=50&Page=0",
                "key": "workflows",
                "last_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows?PageSize=50&Page=0",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows?PageSize=50&Page=0"
            },
            "workflows": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "assignment_callback_url": "http://example.com",
                    "configuration": "task-routing:\\n  - filter: \\n      - 1 == 1\\n    target:\\n      - queue: WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\\n        set-priority: 0\\n",
                    "date_created": "2014-05-14T10:50:02Z",
                    "date_updated": "2014-05-15T16:47:51Z",
                    "document_content_type": "application/json",
                    "fallback_assignment_callback_url": null,
                    "friendly_name": "Default Fifo Workflow",
                    "sid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "task_reservation_timeout": 120,
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ]
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workflows.list(friendly_name="friendly_name")
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].assignment_callback_url)
        self.assertEqual(u"http://example.com", instances[0].assignment_callback_url)
        self.assertIsNotNone(instances[0].configuration)
        self.assertEqual(u"task-routing:\n  - filter: \n      - 1 == 1\n    target:\n      - queue: WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n        set-priority: 0\n", instances[0].configuration)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("2014-05-14T10:50:02Z"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("2014-05-15T16:47:51Z"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].document_content_type)
        self.assertEqual(u"application/json", instances[0].document_content_type)
        self.assertIsNone(instances[0].fallback_assignment_callback_url)
        self.assertIsNotNone(instances[0].friendly_name)
        self.assertEqual(u"Default Fifo Workflow", instances[0].friendly_name)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].task_reservation_timeout)
        self.assertEqual(120, instances[0].task_reservation_timeout)
        self.assertIsNotNone(instances[0].workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].workspace_sid)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows?PageSize=50&Page=0",
                "key": "workflows",
                "last_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows?PageSize=50&Page=0",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows?PageSize=50&Page=0"
            },
            "workflows": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "assignment_callback_url": "http://example.com",
                    "configuration": "task-routing:\\n  - filter: \\n      - 1 == 1\\n    target:\\n      - queue: WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\\n        set-priority: 0\\n",
                    "date_created": "2014-05-14T10:50:02Z",
                    "date_updated": "2014-05-15T16:47:51Z",
                    "document_content_type": "application/json",
                    "fallback_assignment_callback_url": null,
                    "friendly_name": "Default Fifo Workflow",
                    "sid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "task_reservation_timeout": 120,
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ]
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workflows.list(friendly_name="friendly_name")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "FriendlyName": "friendly_name"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows?PageSize=50&Page=0",
                "key": "workflows",
                "last_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows?PageSize=50&Page=0",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows?PageSize=50&Page=0"
            },
            "workflows": []
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workflows.list(friendly_name="friendly_name")
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows?PageSize=50&Page=0",
                "key": "workflows",
                "last_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows?PageSize=50&Page=0",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows?PageSize=50&Page=0"
            },
            "workflows": []
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workflows.list(friendly_name="friendly_name")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "FriendlyName": "friendly_name"
            },
        )

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "assignment_callback_url": "http://example.com",
            "configuration": "task-routing:\\n  - filter: \\n      - 1 == 1\\n    target:\\n      - queue: WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\\n        set-priority: 0\\n",
            "date_created": "2014-05-14T10:50:02Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "document_content_type": "application/json",
            "fallback_assignment_callback_url": null,
            "friendly_name": "Default Fifo Workflow",
            "sid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "task_reservation_timeout": 120,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workflows.create(
                "friendly_name",
                "configuration",
                "/example",
                fallback_assignment_callback_url="/example",
                task_reservation_timeout=1
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "AssignmentCallbackUrl": "/example",
                "Configuration": "configuration",
                "FallbackAssignmentCallbackUrl": "/example",
                "FriendlyName": "friendly_name",
                "TaskReservationTimeout": 1
            },
            query_params={},
        )

    def test_create_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "assignment_callback_url": "http://example.com",
            "configuration": "task-routing:\\n  - filter: \\n      - 1 == 1\\n    target:\\n      - queue: WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\\n        set-priority: 0\\n",
            "date_created": "2014-05-14T10:50:02Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "document_content_type": "application/json",
            "fallback_assignment_callback_url": null,
            "friendly_name": "Default Fifo Workflow",
            "sid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "task_reservation_timeout": 120,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workflows.create(
                "friendly_name",
                "configuration",
                "/example",
                fallback_assignment_callback_url="/example",
                task_reservation_timeout=1
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.assignment_callback_url)
        self.assertEqual(u"http://example.com", instance.assignment_callback_url)
        self.assertIsNotNone(instance.configuration)
        self.assertEqual(u"task-routing:\n  - filter: \n      - 1 == 1\n    target:\n      - queue: WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n        set-priority: 0\n", instance.configuration)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2014-05-14T10:50:02Z"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2014-05-14T23:26:06Z"), instance.date_updated)
        self.assertIsNotNone(instance.document_content_type)
        self.assertEqual(u"application/json", instance.document_content_type)
        self.assertIsNone(instance.fallback_assignment_callback_url)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"Default Fifo Workflow", instance.friendly_name)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.task_reservation_timeout)
        self.assertEqual(120, instance.task_reservation_timeout)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)
