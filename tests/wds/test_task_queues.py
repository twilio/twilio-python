import unittest

from mock import patch, Mock

from tests.tools import create_mock_json
from twilio.rest.resources.wds.task_queues import TaskQueues, TaskQueue


AUTH = ("AC123", "token")
BASE_URI = "https://wds.twilio.com/v1/Accounts/AC123/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
TASK_QUEUE_SID = "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


class TaskQueueTest(unittest.TestCase):
    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_create(self, request):
        resp = create_mock_json('tests/resources/wds/task_queues_instance.json')
        resp.status_code = 201
        request.return_value = resp

        task_queues = TaskQueues(BASE_URI, AUTH)
        task_queues.create("Test TaskQueue", "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        exp_params = {
            'FriendlyName': "Test TaskQueue",
            'AssignmentActivitySid': "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            'ReservationActivitySid': 'WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        }

        request.assert_called_with("POST", "{}/TaskQueues".format(BASE_URI), data=exp_params, auth=AUTH)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_delete_instance(self, request):
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        request.return_value = resp

        uri = "{}/TaskQueues/{}".format(BASE_URI, TASK_QUEUE_SID)
        list_resource = TaskQueues(BASE_URI, AUTH)
        task_queue = TaskQueue(list_resource, TASK_QUEUE_SID)
        task_queue.delete()
        request.assert_called_with("DELETE", uri, auth=AUTH)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_delete_list(self, request):
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        request.return_value = resp

        uri = "{}/TaskQueues/{}".format(BASE_URI, TASK_QUEUE_SID)
        list_resource = TaskQueues(BASE_URI, AUTH)
        list_resource.delete(TASK_QUEUE_SID)
        request.assert_called_with("DELETE", uri, auth=AUTH)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get(self, request):
        resp = create_mock_json('tests/resources/wds/task_queues_instance.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{}/TaskQueues/{}".format(BASE_URI, TASK_QUEUE_SID)
        list_resource = TaskQueues(BASE_URI, AUTH)
        list_resource.get(TASK_QUEUE_SID)
        request.assert_called_with("GET", uri, auth=AUTH)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_list(self, request):
        resp = create_mock_json('tests/resources/wds/task_queues_list.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{}/TaskQueues".format(BASE_URI)
        list_resource = TaskQueues(BASE_URI, AUTH)
        list_resource.list()
        request.assert_called_with("GET", uri, params={}, auth=AUTH)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_update_instance(self, request):
        resp = create_mock_json('tests/resources/wds/task_queues_instance.json')
        resp.status_code = 201
        request.return_value = resp

        uri = "{}/TaskQueues/{}".format(BASE_URI, TASK_QUEUE_SID)
        list_resource = TaskQueues(BASE_URI, AUTH)
        task_queue = TaskQueue(list_resource, TASK_QUEUE_SID)
        task_queue.update(friendly_name='Test TaskQueue', assignment_activity_sid='WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                          reservation_activity_sid='WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        exp_params = {
            'FriendlyName': "Test TaskQueue",
            'AssignmentActivitySid': "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            'ReservationActivitySid': 'WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        }

        request.assert_called_with("POST", uri, data=exp_params, auth=AUTH)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_update_list(self, request):
        resp = create_mock_json('tests/resources/wds/task_queues_instance.json')
        resp.status_code = 201
        request.return_value = resp

        uri = "{}/TaskQueues/{}".format(BASE_URI, TASK_QUEUE_SID)
        list_resource = TaskQueues(BASE_URI, AUTH)
        list_resource.update(TASK_QUEUE_SID, friendly_name='Test TaskQueue',
                             assignment_activity_sid='WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                             reservation_activity_sid='WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        exp_params = {
            'FriendlyName': "Test TaskQueue",
            'AssignmentActivitySid': "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            'ReservationActivitySid': 'WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        }

        request.assert_called_with("POST", uri, data=exp_params, auth=AUTH)
