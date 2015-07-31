from tests.integration import config
from tests.integration.api_responses import (
    NextGenGETRequestHandler as GRH,
)
from tests.integration.base_integration_test import BaseIntegrationTest
from tests.integration.test_rest_client_list import RESPONSE_HANDLERS
from twilio.rest import TwilioTaskRouterClient


class TwilioTaskRouterClientTest(BaseIntegrationTest):
    def setUp(self, base_uri=config.taskrouter_uri,
              response_handlers=RESPONSE_HANDLERS):
        super(TwilioTaskRouterClientTest, self).setUp(
            base_uri=base_uri, response_handlers=response_handlers
        )
        self.client = TwilioTaskRouterClient(config.account_sid,
                                             config.auth_token,
                                             base_uri)
        self.workspace_sid = 'WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

    def test_workspace(self):
        self.response_handlers = [
            GRH('/Workspaces', 'task_router/workspaces_list.json'),
            GRH('/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                'task_router/workspaces_instance.json', params=None)
        ]

        self.client.workspaces.list()
        self.client.workspaces.get('WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

    def test_activities(self):
        self.response_handlers = [
            GRH('/Workspaces/{}/Activities'.format(self.workspace_sid), 'task_router/activities_list.json'),
            GRH('/Workspaces/{}/Activities/{}'
                .format(self.workspace_sid,
                        'WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/activities_instance.json', params=None
                )
        ]

        self.client.activities('WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').list()
        self.client.activities(self.workspace_sid).get('WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

    def test_events(self):
        self.response_handlers = [
            GRH('/Workspaces/{}/Events'.format(self.workspace_sid), 'task_router/events_list.json'),
            GRH('/Workspaces/{}/Events/{}'
                .format('WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                        'EVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                'task_router/events_instance.json', params=None
                )
        ]

        self.client.events(self.workspace_sid).list()
        self.client.events(self.workspace_sid).get('EVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

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

        self.client.task_queues(self.workspace_sid).list()
        self.client.task_queues(self.workspace_sid).get('WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

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
        self.client.reservations(self.workspace_sid, 'WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').\
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
