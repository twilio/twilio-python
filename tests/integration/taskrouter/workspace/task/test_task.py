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


class TaskIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "age": 25200,
            "assignment_status": "pending",
            "attributes": "{\\"body\\": \\"hello\\"}",
            "date_created": "2014-05-14T10:50:02Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "priority": 0,
            "sid": "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "task_queue_sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "timeout": 60,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workflow_sid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.get("WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
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
            "age": 25200,
            "assignment_status": "pending",
            "attributes": "{\\"body\\": \\"hello\\"}",
            "date_created": "2014-05-14T10:50:02Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "priority": 0,
            "sid": "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "task_queue_sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "timeout": 60,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workflow_sid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.get("WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.age)
        self.assertEqual(25200, instance.age)
        self.assertIsNotNone(instance.assignment_status)
        self.assertEqual(u"pending", instance.assignment_status)
        self.assertIsNotNone(instance.attributes)
        self.assertEqual(u"{\"body\": \"hello\"}", instance.attributes)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2014-05-14T10:50:02Z"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2014-05-14T23:26:06Z"), instance.date_updated)
        self.assertIsNotNone(instance.priority)
        self.assertEqual(0, instance.priority)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.task_queue_sid)
        self.assertEqual(u"WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.task_queue_sid)
        self.assertIsNotNone(instance.timeout)
        self.assertEqual(60, instance.timeout)
        self.assertIsNotNone(instance.workflow_sid)
        self.assertEqual(u"WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workflow_sid)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "age": 25200,
            "assignment_status": "pending",
            "attributes": "{\\"body\\": \\"hello\\"}",
            "date_created": "2014-05-14T10:50:02Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "priority": 0,
            "sid": "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "task_queue_sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "timeout": 60,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workflow_sid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.update(
                "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                attributes="attributes",
                assignment_status="pending",
                reason="reason",
                priority=1
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "AssignmentStatus": "pending",
                "Attributes": "attributes",
                "Priority": 1,
                "Reason": "reason"
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "age": 25200,
            "assignment_status": "pending",
            "attributes": "{\\"body\\": \\"hello\\"}",
            "date_created": "2014-05-14T10:50:02Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "priority": 0,
            "sid": "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "task_queue_sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "timeout": 60,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workflow_sid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.update(
                "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                attributes="attributes",
                assignment_status="pending",
                reason="reason",
                priority=1
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.age)
        self.assertEqual(25200, instance.age)
        self.assertIsNotNone(instance.assignment_status)
        self.assertEqual(u"pending", instance.assignment_status)
        self.assertIsNotNone(instance.attributes)
        self.assertEqual(u"{\"body\": \"hello\"}", instance.attributes)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2014-05-14T10:50:02Z"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2014-05-14T23:26:06Z"), instance.date_updated)
        self.assertIsNotNone(instance.priority)
        self.assertEqual(0, instance.priority)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.task_queue_sid)
        self.assertEqual(u"WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.task_queue_sid)
        self.assertIsNotNone(instance.timeout)
        self.assertEqual(60, instance.timeout)
        self.assertIsNotNone(instance.workflow_sid)
        self.assertEqual(u"WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workflow_sid)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.delete("WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
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
            .tasks.delete("WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks?PageSize=50&Page=0",
                "key": "tasks",
                "last_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks?PageSize=50&Page=0",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks?PageSize=50&Page=0"
            },
            "tasks": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "age": 25200,
                    "assignment_status": "pending",
                    "attributes": "{\\"body\\": \\"hello\\"}",
                    "date_created": "2014-05-14T14:26:54Z",
                    "date_updated": "2014-05-15T16:03:42Z",
                    "priority": 0,
                    "sid": "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "task_queue_sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "timeout": 60,
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workflow_sid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ]
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.list(
                priority=1,
                assignment_status="pending",
                workflow_sid="WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                workflow_name="workflow_name",
                task_queue_sid="WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                task_queue_name="task_queue_name"
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].age)
        self.assertEqual(25200, instances[0].age)
        self.assertIsNotNone(instances[0].assignment_status)
        self.assertEqual(u"pending", instances[0].assignment_status)
        self.assertIsNotNone(instances[0].attributes)
        self.assertEqual(u"{\"body\": \"hello\"}", instances[0].attributes)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("2014-05-14T14:26:54Z"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("2014-05-15T16:03:42Z"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].priority)
        self.assertEqual(0, instances[0].priority)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].task_queue_sid)
        self.assertEqual(u"WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].task_queue_sid)
        self.assertIsNotNone(instances[0].timeout)
        self.assertEqual(60, instances[0].timeout)
        self.assertIsNotNone(instances[0].workflow_sid)
        self.assertEqual(u"WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].workflow_sid)
        self.assertIsNotNone(instances[0].workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].workspace_sid)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks?PageSize=50&Page=0",
                "key": "tasks",
                "last_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks?PageSize=50&Page=0",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks?PageSize=50&Page=0"
            },
            "tasks": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "age": 25200,
                    "assignment_status": "pending",
                    "attributes": "{\\"body\\": \\"hello\\"}",
                    "date_created": "2014-05-14T14:26:54Z",
                    "date_updated": "2014-05-15T16:03:42Z",
                    "priority": 0,
                    "sid": "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "task_queue_sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "timeout": 60,
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workflow_sid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ]
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.list(
                priority=1,
                assignment_status="pending",
                workflow_sid="WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                workflow_name="workflow_name",
                task_queue_sid="WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                task_queue_name="task_queue_name"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "AssignmentStatus": "pending",
                "Priority": 1,
                "TaskQueueName": "task_queue_name",
                "TaskQueueSid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "WorkflowName": "workflow_name",
                "WorkflowSid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks?PageSize=50&Page=0",
                "key": "tasks",
                "last_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks?PageSize=50&Page=0",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks?PageSize=50&Page=0"
            },
            "tasks": []
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.list(
                priority=1,
                assignment_status="pending",
                workflow_sid="WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                workflow_name="workflow_name",
                task_queue_sid="WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                task_queue_name="task_queue_name"
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks?PageSize=50&Page=0",
                "key": "tasks",
                "last_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks?PageSize=50&Page=0",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks?PageSize=50&Page=0"
            },
            "tasks": []
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.list(
                priority=1,
                assignment_status="pending",
                workflow_sid="WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                workflow_name="workflow_name",
                task_queue_sid="WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                task_queue_name="task_queue_name"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "AssignmentStatus": "pending",
                "Priority": 1,
                "TaskQueueName": "task_queue_name",
                "TaskQueueSid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "WorkflowName": "workflow_name",
                "WorkflowSid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
        )

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "age": 25200,
            "assignment_status": "pending",
            "attributes": "{\\"body\\": \\"hello\\"}",
            "date_created": "2014-05-14T10:50:02Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "priority": 0,
            "sid": "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "task_queue_sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "timeout": 60,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workflow_sid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.create(
                "attributes",
                "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                timeout=1,
                priority=1
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "Attributes": "attributes",
                "Priority": 1,
                "Timeout": 1,
                "WorkflowSid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
            query_params={},
        )

    def test_create_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "age": 25200,
            "assignment_status": "pending",
            "attributes": "{\\"body\\": \\"hello\\"}",
            "date_created": "2014-05-14T10:50:02Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "priority": 0,
            "sid": "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "task_queue_sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "timeout": 60,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workflow_sid": "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tasks.create(
                "attributes",
                "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                timeout=1,
                priority=1
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.age)
        self.assertEqual(25200, instance.age)
        self.assertIsNotNone(instance.assignment_status)
        self.assertEqual(u"pending", instance.assignment_status)
        self.assertIsNotNone(instance.attributes)
        self.assertEqual(u"{\"body\": \"hello\"}", instance.attributes)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2014-05-14T10:50:02Z"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2014-05-14T23:26:06Z"), instance.date_updated)
        self.assertIsNotNone(instance.priority)
        self.assertEqual(0, instance.priority)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.task_queue_sid)
        self.assertEqual(u"WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.task_queue_sid)
        self.assertIsNotNone(instance.timeout)
        self.assertEqual(60, instance.timeout)
        self.assertIsNotNone(instance.workflow_sid)
        self.assertEqual(u"WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workflow_sid)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)
