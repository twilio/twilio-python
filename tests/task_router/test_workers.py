import unittest

from mock import patch, Mock

from tests.tools import create_mock_json
from twilio.rest.resources.task_router.workers import Workers, Worker


AUTH = ("AC123", "token")
BASE_URI = "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
WORKER_SID = "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
TIMEOUT = 30


class WorkerTest(unittest.TestCase):
    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_create(self, request):
        resp = create_mock_json('tests/resources/task_router/workers_instance.json')
        resp.status_code = 201
        request.return_value = resp

        workers = Workers(BASE_URI, AUTH, TIMEOUT)
        workers.create("Test Worker")
        exp_params = {
            'FriendlyName': "Test Worker"
        }

        request.assert_called_with("POST", "{0}/Workers".format(BASE_URI), data=exp_params, auth=AUTH,
                                   timeout=TIMEOUT, use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_delete_instance(self, request):
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        request.return_value = resp

        uri = "{0}/Workers/{1}".format(BASE_URI, WORKER_SID)
        list_resource = Workers(BASE_URI, AUTH, TIMEOUT)
        worker = Worker(list_resource, WORKER_SID)
        worker.delete()
        request.assert_called_with("DELETE", uri, auth=AUTH,
                                   timeout=TIMEOUT, use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_delete_list(self, request):
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        request.return_value = resp

        uri = "{0}/Workers/{1}".format(BASE_URI, WORKER_SID)
        list_resource = Workers(BASE_URI, AUTH, TIMEOUT)
        list_resource.delete(WORKER_SID)
        request.assert_called_with("DELETE", uri, auth=AUTH, timeout=TIMEOUT,
                                   use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get(self, request):
        resp = create_mock_json('tests/resources/task_router/workers_instance.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{0}/Workers/{1}".format(BASE_URI, WORKER_SID)
        list_resource = Workers(BASE_URI, AUTH, TIMEOUT)
        list_resource.get(WORKER_SID)
        request.assert_called_with("GET", uri, auth=AUTH,
                                   timeout=TIMEOUT, use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_list(self, request):
        resp = create_mock_json('tests/resources/task_router/workers_list.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{0}/Workers".format(BASE_URI)
        list_resource = Workers(BASE_URI, AUTH, TIMEOUT)
        list_resource.list()
        request.assert_called_with("GET", uri, params={}, auth=AUTH,
                                   timeout=TIMEOUT, use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_update_instance(self, request):
        resp = create_mock_json('tests/resources/task_router/workers_instance.json')
        resp.status_code = 201
        request.return_value = resp

        uri = "{0}/Workers/{1}".format(BASE_URI, WORKER_SID)
        list_resource = Workers(BASE_URI, AUTH, TIMEOUT)
        worker = Worker(list_resource, WORKER_SID)
        worker.update(friendly_name='Test Worker')
        exp_params = {
            'FriendlyName': "Test Worker"
        }

        request.assert_called_with("POST", uri, data=exp_params, auth=AUTH,
                                   timeout=TIMEOUT, use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_update_list(self, request):
        resp = create_mock_json('tests/resources/task_router/workers_instance.json')
        resp.status_code = 201
        request.return_value = resp

        uri = "{0}/Workers/{1}".format(BASE_URI, WORKER_SID)
        list_resource = Workers(BASE_URI, AUTH, TIMEOUT)
        list_resource.update(WORKER_SID, friendly_name='Test Worker')
        exp_params = {
            'FriendlyName': "Test Worker"
        }

        request.assert_called_with("POST", uri, data=exp_params, auth=AUTH,
                                   timeout=TIMEOUT, use_json_extension=False)
