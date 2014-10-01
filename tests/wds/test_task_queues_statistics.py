import unittest

from mock import patch

from tests.tools import create_mock_json
from twilio.rest.resources.wds.task_queues_statistics import TaskQueuesStatistics


AUTH = ("AC123", "token")
BASE_URI = "https://wds.twilio.com/v1/Accounts/AC123/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics"
TASK_QUEUE_SID = "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


class TaskQueueStatisticsTest(unittest.TestCase):
    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get(self, request):
        resp = create_mock_json('tests/resources/wds/task_queues_statistics_instance.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{}/TaskQueues/{}".format(BASE_URI, TASK_QUEUE_SID)
        list_resource = TaskQueuesStatistics(BASE_URI, AUTH)
        list_resource.get(TASK_QUEUE_SID)
        request.assert_called_with("GET", uri, auth=AUTH)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_list(self, request):
        resp = create_mock_json('tests/resources/wds/task_queues_statistics_list.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{}/TaskQueues".format(BASE_URI)
        list_resource = TaskQueuesStatistics(BASE_URI, AUTH)
        list_resource.list()
        request.assert_called_with("GET", uri, params={}, auth=AUTH)
