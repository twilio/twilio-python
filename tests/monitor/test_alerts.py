import unittest

from mock import patch

from tests.tools import create_mock_json
from twilio.rest.resources.monitor.alerts import Alerts


AUTH = ("AC123", "token")
BASE_URI = "https://monitor.twilio.com/v1"
EVENT_SID = "NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


class AlertTest(unittest.TestCase):
    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get(self, request):
        resp = create_mock_json('tests/resources/monitor/alerts_instance.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{0}/Alerts/{1}".format(BASE_URI, EVENT_SID)
        list_resource = Alerts(BASE_URI, AUTH)
        list_resource.get(EVENT_SID)
        request.assert_called_with("GET", uri, auth=AUTH, use_json_extension=False)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_list(self, request):
        resp = create_mock_json('tests/resources/monitor/alerts_list.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{0}/Alerts".format(BASE_URI)
        list_resource = Alerts(BASE_URI, AUTH)
        list_resource.list()
        request.assert_called_with("GET", uri, params={}, auth=AUTH, use_json_extension=False)
