import json
import unittest
from uuid import uuid1
from twilio.ext.holodeck import holodeck
from twilio.rest import TwilioTaskRouterClient


class TwilioTaskRouterClientTest(unittest.TestCase):
    def setUp(self):
        self.client = TwilioTaskRouterClient('AC' + 'a' * 32, 'AUTHTOKEN')
        holodeck.activate()

        self.workspace = self.client.workspaces.create('friendly_name').execute()

    def tearDown(self):
        holodeck.deactivate()

    def test_workspace(self):
        self.client.workspaces.list().execute()
        self.client.workspaces.get(self.workspace.sid).execute()
        self.workspace.update().execute()

    def test_events(self):
        events = self.client.events(self.workspace.sid).list().execute()
        if len(events) > 0:
            self.client.events(self.workspace.sid).get(events[0].sid).execute()

    def test_tasks(self):
        base_uri = '/Workspaces/{}'.format(self.workspace.sid)

        reservation_activity = self.workspace.activities.create('friendly_name', False).execute()
        reservation_activity.update(friendly_name='friendly_name').execute()

        assignment_activity = self.workspace.activities.create('friendly_name', False).execute()
        assignment_activity.update(friendly_name='friendly_name').execute()

        queue = self.workspace.task_queues.create('friendly_name', reservation_activity.sid,
                                                  assignment_activity.sid).execute()
        queue.update().execute()

        workflow_config = {
            "task_routing": {
                "filters": [
                    {
                        "friendly_name": "Test",
                        "expression": "1==1",
                        "targets": [
                            {
                                "queue": queue.sid
                            }
                        ]
                    }
                ],
            }
        }

        workflow = self.workspace.workflows.create(workflow_name, json.dumps(workflow_config),
                                                   'http://www.example.com').execute()
        workflow.update(friendly_name=workflow_name + 'a').execute()

        task = self.workspace.tasks.create("{}", workflow.sid).execute()
        task.update(reason='reason').execute()
        self.workspace.tasks.list().execute()
        self.workspace.tasks.get(task.sid).execute()

        task.delete().execute()
        workflow.delete().execute()
        queue.delete().execute()
        assignment_activity.delete().execute()
        reservation_activity.delete().execute()

    def test_worker(self):
        base_uri = '/Workspaces/{}'.format(self.workspace.sid)

        worker = self.workspace.workers.create('friendly_name').execute()
        self.workspace.workers.get(worker.sid).execute()
        self.workspace.workers.list().execute()
        worker.update(friendly_name=worker_name + 'a').execute()
        worker.delete().execute()
