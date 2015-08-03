from uuid import uuid4
from tests.integration import config
from tests.integration.api_responses import (
    NextGenGETRequestHandler as GRH,
)
from tests.integration.base_integration_test import BaseIntegrationTest
from tests.integration.test_rest_client_list import RESPONSE_HANDLERS
from twilio.rest import TwilioTaskRouterClient

WORKFLOW_CONFIG = """
{
   "task_routing":{
      "filters":[
         {
            "friendly_name":"Test",
            "expression":"1==1",
            "targets":[
               {
                  "queue": "{queue_sid}"
               }
            ]
         }
      ],
   }
}
"""


class TwilioTaskRouterClientTest(BaseIntegrationTest):
    def setUp(self, base_uri=config.taskrouter_uri,
              response_handlers=RESPONSE_HANDLERS):
        super(TwilioTaskRouterClientTest, self).setUp(
            base_uri=base_uri, response_handlers=response_handlers
        )
        self.client = TwilioTaskRouterClient(config.taskrouter_account_sid,
                                             config.auth_token,
                                             base_uri)
        self._create_workspace()
        self.workspace_sid = 'WS24f2a02bf848485e77ed7ab1ca1b39a8'

    def _create_workspace(self, name=None):
        name = name or str(uuid4())
        self.workspace = self.client.workspaces.create(name)

    def _create_activity(self, name=None, available=True):
        name = name or str(uuid4())
        self.activity = self.client.activities(self.workspace.sid).create(name, available)

    def _create_task(self):
        self.task = self.client.tasks(self.workspace.sid).create({}, self.worflow.sid)

    def _create_workflow(self):
        self.task = self.client.workflows(self.workspace_sid).create('friendly', )

    def _create_task_queue(self, name=None, assignment_activity_sid=None,
                           reservation_activity_sid=None):
        name = name or str(uuid4())
        assignment_activity_sid = (assignment_activity_sid or self.activity.sid)
        reservation_activity_sid = (reservation_activity_sid or self.reservation_activity.sid)

        self.task_queue = self.client.task_queues(self.workspace.sid).create(name,
                                                                             reservation_activity_sid,
                                                                             assignment_activity_sid)

    def _create_reservation_activity(self):
        self.reservation_activity = self._create_activity(available=False)

    def test_workspace(self):
        self.response_handlers = [
            GRH('v1/Workspaces', 'task_router/workspaces_list.json'),
            GRH('v1/Workspaces/{}'.format(self.workspace_sid),
                'task_router/workspaces_instance.json', params=None)
        ]

        self.client.workspaces.list()
        self.client.workspaces.get(self.workspace.sid)

    def test_activities(self):
        self.response_handlers = [
            GRH('/Workspaces/{}/Activities'.format(self.workspace_sid), 'task_router/activities_list.json'),
            GRH('/Workspaces/{}/Activities/{}'
                .format(self.workspace_sid,
                        'WA87d8cadc3ca0b4837acb94061dada3c0'),
                'task_router/activities_instance.json', params=None
                )
        ]
        self._create_activity()

        self.client.activities(self.workspace.sid).list()
        self.client.activities(self.workspace.sid).get(self.activity.sid)

    def test_events(self):
        self.response_handlers = [
            GRH('/Workspaces/{}/Events'.format(self.workspace_sid), 'task_router/events_list.json'),
            GRH('/Workspaces/{}/Events/{}'
                .format(self.workspace.sid,
                        'EVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/events_instance.json', params=None
                )
        ]

        events = self.client.events(self.workspace.sid).list()
        if len(events) > 0:
            self.client.events(self.workspace.sid).get(events[0].sid)

    def test_tasks(self):
        self.response_handlers = [
            GRH('/Workspaces/{}/Tasks'.format(self.workspace_sid), 'task_router/tasks_list.json'),
            GRH('/Workspaces/{}/Tasks/{}'
                .format('WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                        'WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/tasks_instance.json', params=None
                )
        ]

        self.client.tasks(self.workspace_sid).list()
        self.client.tasks(self.workspace_sid).get('WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

    def test_task_queues(self):
        self.response_handlers = [
            GRH('/Workspaces/{}/TaskQueues'.format(self.workspace_sid), 'task_router/task_queues_list.json'),
            GRH('/Workspaces/{}/TaskQueues/{}'
                .format(self.workspace_sid,
                        'WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/task_queues_instance.json', params=None
                )
        ]
        self._create_activity()
        self._create_reservation_activity()
        self._create_task_queue()

        self.client.task_queues(self.workspace_sid).list()
        self.client.task_queues(self.workspace_sid).get(self.task_queue.sid)

    def test_reservations(self):
        self.response_handlers = [
            GRH('/Workspaces/{}/Tasks/{}/Reservations'
                .format(self.workspace_sid,
                        'WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/reservations_list.json'
                ),
            GRH('/Workspaces/{}/Tasks/{}/Reservations/{}'
                .format('WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                        'WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                        'WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/reservations_instance.json', params=None
                )
        ]

        self.client.reservations(self.workspace_sid, 'WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').list()
        self.client.reservations(self.workspace_sid, 'WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'). \
            get('WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

    def test_workers(self):
        self.response_handlers = [
            GRH('/Workspaces/{}/Workers'.format(self.workspace_sid), 'task_router/workers_list.json'),
            GRH('/Workspaces/{}/Workers/{}'
                .format(self.workspace_sid,
                        'WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/workers_instance.json', params=None
                )
        ]

        self.client.workers(self.workspace_sid).list()
        self.client.workers(self.workspace_sid).get('WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

    def test_workflows(self):
        self.response_handlers = [
            GRH('/Workspaces/{}/Workflows'.format(self.workspace_sid), 'task_router/workflows_list.json'),
            GRH('/Workspaces/{}/Workflows/{}'
                .format(self.workspace_sid,
                        'WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/workflows_instance.json', params=None
                )
        ]

        self.client.workflows(self.workspace_sid).list()
        self.client.workflows(self.workspace_sid).get('WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
