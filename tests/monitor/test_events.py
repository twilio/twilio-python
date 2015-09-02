import unittest

from mock import patch

from tests.tools import create_mock_json
from twilio.rest.http import HttpClient
from twilio.rest.resources.monitor.events import Events


AUTH = ("AC123", "token")
BASE_URI = "https://monitor.twilio.com/v1"
EVENT_SID = "AEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


class EventTest(unittest.TestCase):

    def setUp(self):
        self.client = HttpClient()

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get(self, request):
        resp = create_mock_json('tests/resources/monitor/events_instance.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{0}/Events/{1}".format(BASE_URI, EVENT_SID)
        list_resource = Events(self.client, BASE_URI, AUTH)
        list_resource.get(EVENT_SID).execute()
        request.assert_called_with("GET", uri, auth=AUTH, use_json_extension=False,
                                   client=self.client)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_list(self, request):
        resp = create_mock_json('tests/resources/monitor/events_list.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{0}/Events".format(BASE_URI)
        list_resource = Events(self.client, BASE_URI, AUTH)
        list_resource.list().execute()
        request.assert_called_with("GET", uri, params={}, auth=AUTH, use_json_extension=False,
                                   client=self.client)
