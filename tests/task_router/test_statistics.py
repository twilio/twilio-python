import unittest
from mock import patch
from tests.tools import create_mock_json
from twilio.rest.http import HttpClient
from twilio.rest.resources.task_router import Workspace, Workspaces

from twilio.rest.resources.task_router.workers import Workers, Worker
from twilio.rest.resources.task_router.task_queues import TaskQueues, TaskQueue
from twilio.rest.resources.task_router.workflows import Workflows, Workflow

AUTH = ("AC123", "token")
BASE_URI = "https://taskrouter.twilio.com/v1/Accounts/AC123/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
WORKER_SID = "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
TIMEOUT = 30


class TestStatistics(unittest.TestCase):

    def setUp(self):
        self.client = HttpClient()

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_fetch_worker_statistics(self, request):
        resp = create_mock_json('tests/resources/task_router/workers_statistics_instance.json')
        resp.status_code = 200
        request.return_value = resp

        workers = Workers(self.client, BASE_URI, AUTH, TIMEOUT)
        worker = Worker(workers, 'WK123')
        worker.load_subresources()
        worker.statistics.get().execute()
        request.assert_called_with(
            'GET',
            '{0}/Workers/WK123/Statistics'.format(BASE_URI),
            auth=AUTH,
            timeout=TIMEOUT,
            use_json_extension=False,
            client=self.client
        )

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_fetch_workers_statistics(self, request):
        resp = create_mock_json('tests/resources/task_router/workers_statistics_instance.json')
        resp.status_code = 200
        request.return_value = resp

        workers = Workers(self.client, BASE_URI, AUTH, TIMEOUT)
        workers.statistics.get().execute()
        request.assert_called_with('GET',
                                   '{0}/Workers/Statistics'.format(BASE_URI),
                                   auth=AUTH, timeout=TIMEOUT,
                                   use_json_extension=False,
                                   client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_fetch_task_queue_statistics(self, request):
        resp = create_mock_json('tests/resources/task_router/task_queues_instance.json')
        resp.status_code = 200
        request.return_value = resp

        tqs = TaskQueues(self.client, BASE_URI, AUTH, 30)
        tq = TaskQueue(tqs, 'TQ123')
        tq.load_subresources()
        tq.statistics.get().execute()
        request.assert_called_with('GET',
                                   '{0}/TaskQueues/TQ123/Statistics'.format(BASE_URI),
                                   auth=AUTH, timeout=30,
                                   use_json_extension=False,
                                   client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_fetch_task_workflow_statistics(self, request):
        resp = create_mock_json('tests/resources/task_router/workflows_instance.json')
        resp.status_code = 200
        request.return_value = resp

        workflows = Workflows(self.client, BASE_URI, AUTH)
        workflow = Workflow(workflows, 'WF123')
        workflow.load_subresources()
        workflow.statistics.get().execute()
        request.assert_called_with('GET',
                                   '{0}/Workflows/WF123/Statistics'.format(BASE_URI),
                                   auth=AUTH, use_json_extension=False,
                                   client=self.client)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_fetch_workspace_statistics(self, request):
        resp = create_mock_json('tests/resources/task_router/workspaces_instance.json')
        resp.status_code = 200
        request.return_value = resp

        workspaces = Workspaces(self.client, BASE_URI, AUTH)
        workspace = Workspace(workspaces, 'WS123')
        workspace.load_subresources()
        workspace.statistics.get().execute()
        request.assert_called_witH('GET',
                                   '{}/Workspaces/WS123/Statistics'.format(BASE_URI),
                                   auth=AUTH, use_json_extensions=False,
                                   client=self.client)
