import unittest

from mock import patch, Mock

from tests.tools import create_mock_json
from twilio.rest.resources.task_router.workflows import Workflows, Workflow


AUTH = ("AC123", "token")
BASE_URI = "https://taskrouter.twilio.com/v1/Accounts/AC123/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
WORKFLOW_SID = "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


class WorkflowTest(unittest.TestCase):
    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_create(self, request):
        resp = create_mock_json('tests/resources/task_router/workflows_instance.json')
        resp.status_code = 201
        request.return_value = resp

        workflows = Workflows(BASE_URI, AUTH)
        workflows.create("Test Workflow", "configuration", "http://www.example.com")
        exp_params = {
            'FriendlyName': "Test Workflow",
            'Configuration': "configuration",
            'AssignmentCallbackUrl': 'http://www.example.com'
        }

        request.assert_called_with("POST", "{0}/Workflows".format(BASE_URI), data=exp_params, auth=AUTH,
                                   use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_delete_instance(self, request):
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        request.return_value = resp

        uri = "{0}/Workflows/{1}".format(BASE_URI, WORKFLOW_SID)
        list_resource = Workflows(BASE_URI, AUTH)
        workflow = Workflow(list_resource, WORKFLOW_SID)
        workflow.delete()
        request.assert_called_with("DELETE", uri, auth=AUTH,
                                   use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_delete_list(self, request):
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        request.return_value = resp

        uri = "{0}/Workflows/{1}".format(BASE_URI, WORKFLOW_SID)
        list_resource = Workflows(BASE_URI, AUTH)
        list_resource.delete(WORKFLOW_SID)
        request.assert_called_with("DELETE", uri, auth=AUTH,
                                   use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get(self, request):
        resp = create_mock_json('tests/resources/task_router/workflows_instance.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{0}/Workflows/{1}".format(BASE_URI, WORKFLOW_SID)
        list_resource = Workflows(BASE_URI, AUTH)
        list_resource.get(WORKFLOW_SID)
        request.assert_called_with("GET", uri, auth=AUTH,
                                   use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_list(self, request):
        resp = create_mock_json('tests/resources/task_router/workflows_list.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{0}/Workflows".format(BASE_URI)
        list_resource = Workflows(BASE_URI, AUTH)
        list_resource.list()
        request.assert_called_with("GET", uri, params={}, auth=AUTH,
                                   use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_update_instance(self, request):
        resp = create_mock_json('tests/resources/task_router/workflows_instance.json')
        resp.status_code = 201
        request.return_value = resp

        uri = "{0}/Workflows/{1}".format(BASE_URI, WORKFLOW_SID)
        list_resource = Workflows(BASE_URI, AUTH)
        workflow = Workflow(list_resource, WORKFLOW_SID)
        workflow.update(friendly_name='Test Workflow', configuration='configuration',
                        assignment_callback_url='http://www.example.com')
        exp_params = {
            'FriendlyName': "Test Workflow",
            'Configuration': "configuration",
            'AssignmentCallbackUrl': 'http://www.example.com'
        }

        request.assert_called_with("POST", uri, data=exp_params, auth=AUTH,
                                   use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_update_list(self, request):
        resp = create_mock_json('tests/resources/task_router/workflows_instance.json')
        resp.status_code = 201
        request.return_value = resp

        uri = "{0}/Workflows/{1}".format(BASE_URI, WORKFLOW_SID)
        list_resource = Workflows(BASE_URI, AUTH)
        list_resource.update(WORKFLOW_SID, friendly_name='Test Workflow', configuration='configuration',
                             assignment_callback_url='http://www.example.com')
        exp_params = {
            'FriendlyName': "Test Workflow",
            'Configuration': "configuration",
            'AssignmentCallbackUrl': 'http://www.example.com'
        }

        request.assert_called_with("POST", uri, data=exp_params, auth=AUTH,
                                   use_json_extension=False)
