import unittest

from mock import patch, Mock

from tests.tools import create_mock_json
from twilio.rest.resources.task_router.workspaces import Workspaces, Workspace

BASE_URI = "https://taskrouter.twilio.com/v1/Accounts/AC123"
ACCOUNT_SID = "AC123"
AUTH = (ACCOUNT_SID, "token")
WORKSPACE_SID = "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


class WorkspaceTest(unittest.TestCase):
    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_create(self, request):
        resp = create_mock_json('tests/resources/task_router/workspaces_instance.json')
        resp.status_code = 201
        request.return_value = resp

        uri = "{0}/Workspaces".format(BASE_URI)
        list_resource = Workspaces(BASE_URI, AUTH)
        list_resource.create("Test Workspace", event_callback_uri="http://www.example.com", template='FIFO')
        exp_params = {
            'FriendlyName': "Test Workspace",
            'EventCallbackUri': "http://www.example.com",
            'Template': "FIFO"
        }

        request.assert_called_with("POST", uri, data=exp_params, auth=AUTH,
                                   use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_delete_instance(self, request):
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        request.return_value = resp

        uri = "{0}/Workspaces/{1}".format(BASE_URI, WORKSPACE_SID)
        list_resource = Workspaces(BASE_URI, AUTH)
        workspace = Workspace(list_resource, WORKSPACE_SID)
        workspace.delete()
        request.assert_called_with("DELETE", uri, auth=AUTH,
                                   use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_delete_list(self, request):
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        request.return_value = resp

        uri = "{0}/Workspaces/{1}".format(BASE_URI, WORKSPACE_SID)
        list_resource = Workspaces(BASE_URI, AUTH)
        list_resource.delete(WORKSPACE_SID)
        request.assert_called_with("DELETE", uri, auth=AUTH,
                                   use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get(self, request):
        resp = create_mock_json('tests/resources/task_router/workspaces_instance.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{0}/Workspaces/{1}".format(BASE_URI, WORKSPACE_SID)
        list_resource = Workspaces(BASE_URI, AUTH)
        list_resource.get(WORKSPACE_SID)
        request.assert_called_with("GET", uri, auth=AUTH,
                                   use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_list(self, request):
        resp = create_mock_json('tests/resources/task_router/workspaces_list.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{0}/Workspaces".format(BASE_URI)
        list_resource = Workspaces(BASE_URI, AUTH)
        list_resource.list()
        request.assert_called_with("GET", uri, params={}, auth=AUTH,
                                   use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_update_instance(self, request):
        resp = create_mock_json('tests/resources/task_router/workspaces_instance.json')
        resp.status_code = 201
        request.return_value = resp

        uri = "{0}/Workspaces/{1}".format(BASE_URI, WORKSPACE_SID)
        list_resource = Workspaces(BASE_URI, AUTH)
        workspace = Workspace(list_resource, WORKSPACE_SID)
        workspace.update(friendly_name='Test Workspace', event_callback_uri="http://www.example.com", template='FIFO')
        exp_params = {
            'FriendlyName': "Test Workspace",
            'EventCallbackUri': "http://www.example.com",
            'Template': "FIFO"
        }

        request.assert_called_with("POST", uri, data=exp_params, auth=AUTH,
                                   use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_update_list(self, request):
        resp = create_mock_json('tests/resources/task_router/workspaces_instance.json')
        resp.status_code = 201
        request.return_value = resp

        uri = "{0}/Workspaces/{1}".format(BASE_URI, WORKSPACE_SID)
        list_resource = Workspaces(BASE_URI, AUTH)
        list_resource.update(WORKSPACE_SID, friendly_name='Test Workspace', event_callback_uri="http://www.example.com",
                             template='FIFO')
        exp_params = {
            'FriendlyName': "Test Workspace",
            'EventCallbackUri': "http://www.example.com",
            'Template': "FIFO"
        }

        request.assert_called_with("POST", uri, data=exp_params, auth=AUTH,
                                   use_json_extension=False)
