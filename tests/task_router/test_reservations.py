import unittest

from mock import patch

from tests.tools import create_mock_json
from twilio.rest.http import HttpClient
from twilio.rest.resources.task_router.reservations import Reservations, Reservation


AUTH = ("AC123", "token")
BASE_URI = "https://taskrouter.twilio.com/v1/Accounts/AC123/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks/WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
RESERVATION_SID = "WRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


class TaskQueueTest(unittest.TestCase):

    def setUp(self):
        self.client = HttpClient()

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get(self, request):
        resp = create_mock_json('tests/resources/task_router/reservations_instance.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{0}/Reservations/{1}".format(BASE_URI, RESERVATION_SID)
        list_resource = Reservations(self.client, BASE_URI, AUTH)
        list_resource.get(RESERVATION_SID).execute()
        request.assert_called_with("GET", uri, auth=AUTH,
                                   use_json_extension=False,
                                   client=self.client)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_list(self, request):
        resp = create_mock_json('tests/resources/task_router/reservations_list.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{0}/Reservations".format(BASE_URI)
        list_resource = Reservations(self.client, BASE_URI, AUTH)
        list_resource.list().execute()
        request.assert_called_with("GET", uri, params={}, auth=AUTH,
                                   use_json_extension=False,
                                   client=self.client)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_update_instance(self, request):
        resp = create_mock_json('tests/resources/task_router/reservations_instance.json')
        resp.status_code = 201
        request.return_value = resp

        uri = "{0}/Reservations/{1}".format(BASE_URI, RESERVATION_SID)
        list_resource = Reservations(self.client, BASE_URI, AUTH)
        workflow = Reservation(list_resource, RESERVATION_SID)
        workflow.update(worker_activity_sid='WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                        reservation_status='rejected').execute()
        exp_params = {
            'WorkerActivitySid': "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            'ReservationStatus': "rejected"
        }

        request.assert_called_with("POST", uri, data=exp_params, auth=AUTH,
                                   use_json_extension=False,
                                   client=self.client)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_update_list(self, request):
        resp = create_mock_json('tests/resources/task_router/reservations_instance.json')
        resp.status_code = 201
        request.return_value = resp

        uri = "{0}/Reservations/{1}".format(BASE_URI, RESERVATION_SID)
        list_resource = Reservations(self.client, BASE_URI, AUTH)
        list_resource.update(RESERVATION_SID, worker_activity_sid='WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                             reservation_status='rejected').execute()
        exp_params = {
            'WorkerActivitySid': "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            'ReservationStatus': "rejected"
        }

        request.assert_called_with("POST", uri, data=exp_params, auth=AUTH,
                                   use_json_extension=False,
                                   client=self.client)
