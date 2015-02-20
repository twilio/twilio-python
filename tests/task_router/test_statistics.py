from mock import patch
from tests.tools import create_mock_json

from twilio.rest.resources.task_router.workers import Workers, Worker
from twilio.rest.resources.task_router.task_queues import TaskQueues, TaskQueue
from twilio.rest.resources.task_router.workflows import Workflows, Workflow

AUTH = ("AC123", "token")
BASE_URI = "https://taskrouter.twilio.com/v1/Accounts/AC123/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
WORKER_SID = "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
TIMEOUT = 30


@patch("twilio.rest.resources.base.make_twilio_request")
def test_fetch_worker_statistics(request):
    resp = create_mock_json('tests/resources/task_router/workers_statistics_instance.json')
    resp.status_code = 200
    request.return_value = resp

    workers = Workers(BASE_URI, AUTH, TIMEOUT)
    worker = Worker(workers, 'WK123')
    worker.load_subresources()
    worker.statistics.get()
    request.assert_called_with(
        'GET',
        '{0}/Workers/WK123/Statistics'.format(BASE_URI),
        params={},
        auth=AUTH,
        timeout=TIMEOUT,
        use_json_extension=False,
    )


@patch("twilio.rest.resources.base.make_twilio_request")
def test_fetch_workers_statistics(request):
    resp = create_mock_json('tests/resources/task_router/workers_statistics_instance.json')
    resp.status_code = 200
    request.return_value = resp

    workers = Workers(BASE_URI, AUTH, TIMEOUT)
    workers.statistics.get()
    request.assert_called_with('GET',
                               '{0}/Workers/Statistics'.format(BASE_URI),
                               params={}, auth=AUTH, timeout=TIMEOUT,
                               use_json_extension=False)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_fetch_task_queue_statistics(request):
    resp = create_mock_json('tests/resources/task_router/task_queues_instance.json')
    resp.status_code = 200
    request.return_value = resp

    tqs = TaskQueues(BASE_URI, AUTH, 30)
    tq = TaskQueue(tqs, 'TQ123')
    tq.load_subresources()
    tq.statistics.get()
    request.assert_called_with('GET',
                               '{0}/TaskQueues/TQ123/Statistics'.format(BASE_URI),
                               params={}, auth=AUTH, timeout=30,
                               use_json_extension=False)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_fetch_task_queues_statistics(request):
    resp = create_mock_json('tests/resources/task_router/task_queues_instance.json')
    resp.status_code = 200
    request.return_value = resp

    tqs = TaskQueues(BASE_URI, AUTH, 30)
    tqs.statistics.get()
    request.assert_called_with('GET',
                               '{0}/TaskQueues/Statistics'.format(BASE_URI),
                               params={}, auth=AUTH, use_json_extension=False)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_fetch_task_workflow_statistics(request):
    resp = create_mock_json('tests/resources/task_router/workflows_instance.json')
    resp.status_code = 200
    request.return_value = resp

    workflows = Workflows(BASE_URI, AUTH)
    workflow = Workflow(workflows, 'WF123')
    workflow.load_subresources()
    workflow.statistics.get()
    request.assert_called_with('GET',
                               '{0}/Workflows/WF123/Statistics'.format(BASE_URI),
                               params={}, auth=AUTH, use_json_extension=False)
