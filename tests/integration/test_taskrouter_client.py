import json
from uuid import uuid1
from tests.integration import config
from tests.integration.api_responses import (
    NextGenGETRequestHandler as GRH,
    NextGenPOSTRequestHandler as PRH,
    NextGenDELETERequestHandler as DRH,
)
from tests.integration.base_integration_test import BaseIntegrationTest
from twilio.rest import TwilioTaskRouterClient


class TwilioTaskRouterClientTest(BaseIntegrationTest):
    def setUp(self, base_uri=config.taskrouter_uri, response_handlers=[]):
        super(TwilioTaskRouterClientTest, self).setUp(base_uri=base_uri,
                                                      response_handlers=response_handlers)
        self.client = TwilioTaskRouterClient(config.post_account_sid,
                                             config.auth_token,
                                             base_uri)

        self.workspace_name = str(uuid1())

        self.response_handlers = [
            PRH('/Workspaces', 'task_router/workspaces_instance.json', {
                'FriendlyName': self.workspace_name
            })
        ]

        self.workspace = self.client.workspaces.create(self.workspace_name).execute()

    def tearDown(self):
        self.response_handlers = [
            DRH('/Workspaces/{}'.format(self.workspace.sid))
        ]
        self.workspace.delete().execute()

    def test_workspace(self):
        self.response_handlers = [
            GRH('/Workspaces', 'task_router/workspaces_list.json',
                auth=(config.post_account_sid, config.auth_token)),
            GRH('/Workspaces/{}'.format(self.workspace.sid),
                'task_router/workspaces_instance.json', params=None,
                auth=(config.post_account_sid, config.auth_token)),

            PRH('/Workspaces/{}'.format(self.workspace.sid),
                'task_router/workspaces_instance.json', {
                    "FriendlyName": "Test Workspacea"
                })
        ]

        self.client.workspaces.list().execute()
        self.client.workspaces.get(self.workspace.sid).execute()
        self.workspace.update(friendly_name=self.workspace.friendly_name + 'a')\
            .execute()

    def test_events(self):
        self.response_handlers = [
            GRH('/Workspaces/{}/Events'.format(self.workspace.sid),
                'task_router/events_list.json',
                auth=(config.post_account_sid, config.auth_token)),
            GRH('/Workspaces/{}/Events/{}'
                .format(self.workspace.sid, 'EVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/events_instance.json', params=None,
                auth=(config.post_account_sid, config.auth_token)),
        ]

        events = self.client.events(self.workspace.sid).list().execute()
        if len(events) > 0:
            self.client.events(self.workspace.sid).get(events[0].sid).execute()

    def test_tasks(self):
        base_uri = '/Workspaces/{}'.format(self.workspace.sid)
        reservation_activity_name = str(uuid1())
        assignment_activity_name = str(uuid1())
        queue_name = str(uuid1())
        workflow_name = str(uuid1())

        self.response_handlers = [
            PRH('{}/Activities'.format(base_uri), 'task_router/activities_instance.json', {
                'FriendlyName': reservation_activity_name,
                'Available': 'false'
            }),
            PRH('{}/Activities/{}'.format(base_uri, 'WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/activities_instance.json', {
                    'FriendlyName': reservation_activity_name + 'a',
                }),
            PRH('{}/Activities'.format(base_uri), 'task_router/activities_instance.json', {
                'FriendlyName': assignment_activity_name,
                'Available': 'false'
            }),
            PRH('{}/Activities/{}'.format(base_uri, 'WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/activities_instance.json', {
                    'FriendlyName': assignment_activity_name + 'a',
                }),
            PRH('{}/TaskQueues'.format(base_uri), 'task_router/task_queues_instance.json', {
                "FriendlyName": queue_name,
                "ReservationActivitySid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "AssignmentActivitySid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }),
            PRH('{}/TaskQueues/{}'.format(base_uri, 'WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/task_queues_instance.json', {
                    "FriendlyName": queue_name + 'a'
                }),
        ]

        reservation_activity = self.workspace.activities.create(reservation_activity_name,
                                                                False).execute()
        reservation_activity.update(friendly_name=reservation_activity_name + 'a').execute()

        assignment_activity = self.workspace.activities.create(assignment_activity_name,
                                                               False).execute()
        assignment_activity.update(friendly_name=assignment_activity_name + 'a').execute()

        queue = self.workspace.task_queues.create(queue_name, reservation_activity.sid,
                                                  assignment_activity.sid).execute()
        queue.update(friendly_name=queue_name + 'a').execute()

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

        self.response_handlers.extend([
            PRH('{}/Workflows'.format(base_uri), 'task_router/workflows_instance.json', {
                "FriendlyName": workflow_name,
                "Configuration": json.dumps(workflow_config),
                "AssignmentCallbackUrl": "http://www.example.com"
            }),
            PRH('{}/Workflows/{}'.format(base_uri, 'WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/workflows_instance.json', {
                    "FriendlyName": workflow_name + 'a',
                }),
        ])

        workflow = self.workspace.workflows.create(workflow_name, json.dumps(workflow_config),
                                                   'http://www.example.com').execute()
        workflow.update(friendly_name=workflow_name + 'a').execute()

        self.response_handlers.extend([
            PRH('{}/Tasks'.format(base_uri), 'task_router/tasks_instance.json', {
                "Attributes": "{}",
                "WorkflowSid": workflow.sid
            }),
            PRH('{}/Tasks/{}'.format(base_uri, 'WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/tasks_instance.json', {
                    "Reason": 'reason'
                }),
            GRH('{}/Tasks'.format(base_uri), 'task_router/tasks_list.json',
                auth=(config.post_account_sid, config.auth_token)),
            GRH('{}/Tasks/{}'.format(base_uri, 'WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/tasks_instance.json',
                params=None,
                auth=(config.post_account_sid, config.auth_token)),
        ])
        task = self.workspace.tasks.create("{}", workflow.sid).execute()
        task.update(reason='reason').execute()
        self.workspace.tasks.list().execute()
        self.workspace.tasks.get(task.sid).execute()

        self.response_handlers.extend([
            DRH('{}/Tasks/{}'.format(base_uri, 'WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')),
            DRH('{}/Workflows/{}'.format(base_uri, 'WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')),
            DRH('{}/TaskQueues/{}'.format(base_uri, 'WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')),
            DRH('{}/Activities/{}'.format(base_uri, 'WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
        ])

        task.delete().execute()
        workflow.delete().execute()
        queue.delete().execute()
        assignment_activity.delete().execute()
        reservation_activity.delete().execute()

    def test_worker(self):
        base_uri = '/Workspaces/{}'.format(self.workspace.sid)
        worker_name = str(uuid1())

        self.response_handlers = [
            PRH('{}/Workers'.format(base_uri), 'task_router/workers_instance.json', {
                "FriendlyName": worker_name
            }),
            PRH('{}/Workers/{}'.format(base_uri, 'WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/workers_instance.json', {
                    "FriendlyName": worker_name + 'a'
                }),
            GRH('{}/Workers/{}'.format(base_uri, 'WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/workers_instance.json', params=None,
                auth=(config.post_account_sid, config.auth_token)),
            GRH('{}/Workers'.format(base_uri), 'task_router/workers_list.json',
                auth=(config.post_account_sid, config.auth_token)),
            DRH('{}/Workers/{}'.format(base_uri, 'WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
        ]

        worker = self.workspace.workers.create(worker_name).execute()
        self.workspace.workers.get(worker.sid).execute()
        self.workspace.workers.list().execute()
        worker.update(friendly_name=worker_name + 'a').execute()
        worker.delete().execute()
