import unittest

from mock import patch, Mock

from twilio.rest import (
    Client,
    TwilioClient,
    TwilioRestClient,
    TwilioIpMessagingClient,
    TwilioLookupsClient,
    TwilioMonitorClient,
    TwilioPricingClient,
    TwilioTaskRouterClient,
    TwilioTrunkingClient,
)
from twilio.base.obsolete import ObsoleteException
from twilio.http.http_client import TwilioHttpClient
from twilio.http.response import Response


class TestDummyClients(unittest.TestCase):
    def test_obsolete_exception_twilioclient(self):
        self.assertRaises(ObsoleteException, TwilioClient,
                          "Expected raised ObsoleteException")

    def test_obsolete_exception_twiliorestclient(self):
        self.assertRaises(ObsoleteException, TwilioRestClient,
                          "Expected raised ObsoleteException")

    def test_obsolete_exception_twilioipmessagingclient(self):
        self.assertRaises(ObsoleteException, TwilioIpMessagingClient,
                          "Expected raised ObsoleteException")

    def test_obsolete_exception_twiliolookupsclient(self):
        self.assertRaises(ObsoleteException, TwilioLookupsClient,
                          "Expected raised ObsoleteException")

    def test_obsolete_exception_twiliomonitorclient(self):
        self.assertRaises(ObsoleteException, TwilioMonitorClient,
                          "Expected raised ObsoleteException")

    def test_obsolete_exception_twiliopricingclient(self):
        self.assertRaises(ObsoleteException, TwilioPricingClient,
                          "Expected raised ObsoleteException")

    def test_obsolete_exception_twiliotaskrouterclient(self):
        self.assertRaises(ObsoleteException, TwilioTaskRouterClient,
                          "Expected raised ObsoleteException")

    def test_obsolete_exception_twiliotrunkingclient(self):
        self.assertRaises(ObsoleteException, TwilioTrunkingClient,
                          "Expected raised ObsoleteException")


class TestRegionEdgeClients(unittest.TestCase):
    def setUp(self):
        self.http_client_patcher = patch('twilio.rest.TwilioHttpClient')

        self.http_client_mock = Mock(wraps=TwilioHttpClient())
        self.request_mock = Mock()

        self.http_client_mock.request.return_value = Response(500, '')
        self.http_client_mock.request.side_effect = self.validate_url
        self.request_mock.headers = {}

        self.http_client_constructor_mock = self.http_client_patcher.start()
        self.http_client_constructor_mock.return_value = self.http_client_mock

        self.client = Client('username', 'password')

    def tearDown(self):
        self.http_client_patcher.stop()

    def validate_url(self, method, url, **kwargs):
        if url == self.request_mock.url:
            return Response(200, 'test response')

        return Response(
            500,
            'Incorrect url: expected {expected}, got {returned}'.format(
                expected=self.request_mock.url,
                returned=url)
        )

    def validate_success_response(self, response):
        self.assertEqual(200, response.status_code)
        self.assertEqual('test response', response.content)

    def test_set_client_edge_default_region(self):
        self.request_mock.url = 'https://api.edge.us1.twilio.com'

        self.client.edge = 'edge'
        response = self.client.request('GET', 'https://api.twilio.com')

        self.validate_success_response(response)

    def test_set_client_region(self):
        self.request_mock.url = 'https://api.region.twilio.com'

        self.client.region = 'region'
        response = self.client.request('GET', 'https://api.twilio.com')

        self.validate_success_response(response)

    def test_set_uri_region(self):
        self.request_mock.url = 'https://api.region.twilio.com'

        response = self.client.request('GET', 'https://api.region.twilio.com')

        self.validate_success_response(response)

    def test_set_client_edge_region(self):
        self.request_mock.url = 'https://api.edge.region.twilio.com'

        self.client.edge = 'edge'
        self.client.region = 'region'
        response = self.client.request('GET', 'https://api.twilio.com')

        self.validate_success_response(response)

    def test_set_client_edge_uri_region(self):
        self.request_mock.url = 'https://api.edge.region.twilio.com'

        self.client.edge = 'edge'
        response = self.client.request('GET', 'https://api.region.twilio.com')

        self.validate_success_response(response)

    def test_set_client_region_uri_edge_region(self):
        self.request_mock.url = 'https://api.edge.region.twilio.com'

        self.client.region = 'region'
        response = self.client.request('GET', 'https://api.edge.uriRegion.twilio.com')

        self.validate_success_response(response)

    def test_set_client_edge_uri_edge_region(self):
        self.request_mock.url = 'https://api.edge.region.twilio.com'

        self.client.edge = 'edge'
        response = self.client.request('GET', 'https://api.uriEdge.region.twilio.com')

        self.validate_success_response(response)

    def test_set_uri_edge_region(self):
        self.request_mock.url = 'https://api.edge.region.twilio.com'

        response = self.client.request('GET', 'https://api.edge.region.twilio.com')

        self.validate_success_response(response)

