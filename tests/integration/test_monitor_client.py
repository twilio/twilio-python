from tests.integration import config
from tests.integration.api_responses import (
    NextGenGETRequestHandler as GRH,
)
from tests.integration.base_integration_test import BaseIntegrationTest
from tests.integration.test_rest_client_list import RESPONSE_HANDLERS
from twilio.rest.monitor import TwilioMonitorClient


class TwilioMonitorClientTest(BaseIntegrationTest):

    def setUp(self, base_uri=config.monitor_uri,
              response_handlers=RESPONSE_HANDLERS):
        super(TwilioMonitorClientTest, self).setUp(
            base_uri=base_uri, response_handlers=response_handlers)

        self.client = TwilioMonitorClient(config.account_sid,
                                          config.auth_token,
                                          base_uri)

    def test_alert_list(self):
        self.response_handlers = [
            GRH('/Alerts', 'monitor/alerts_list.json'),
            GRH('/Alerts/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'monitor/alerts_instance.json', params=None)
        ]

        self.client.alerts.list()
        self.client.alerts.get('NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

    def test_event_list(self):
        self.response_handlers = [
            GRH('/Events', 'monitor/events_list.json'),
            GRH('/Events/AEbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'monitor/events_instance.json', params=None),
        ]

        self.client.events.list()
        self.client.events.get('AEbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
