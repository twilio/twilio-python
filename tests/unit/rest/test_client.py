import unittest
import platform

from twilio import __version__
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
        self.client = Client('username', 'password')

    def test_set_client_edge_default_region(self):
        self.client.edge = 'edge'
        self.assertEqual(self.client.get_hostname('https://api.twilio.com'),
                         'https://api.edge.us1.twilio.com')

    def test_set_client_region(self):
        self.client.region = 'region'
        self.assertEqual(self.client.get_hostname('https://api.twilio.com'),
                         'https://api.region.twilio.com')

    def test_set_uri_region(self):
        self.assertEqual(self.client.get_hostname('https://api.region.twilio.com'),
                         'https://api.region.twilio.com')

    def test_set_client_edge_region(self):
        self.client.edge = 'edge'
        self.client.region = 'region'
        self.assertEqual(self.client.get_hostname('https://api.twilio.com'),
                         'https://api.edge.region.twilio.com')

    def test_set_client_edge_uri_region(self):
        self.client.edge = 'edge'
        self.assertEqual(self.client.get_hostname('https://api.region.twilio.com'),
                         'https://api.edge.region.twilio.com')

    def test_set_client_region_uri_edge_region(self):
        self.client.region = 'region'
        self.assertEqual(self.client.get_hostname('https://api.edge.uriRegion.twilio.com'),
                         'https://api.edge.region.twilio.com')

    def test_set_client_edge_uri_edge_region(self):
        self.client.edge = 'edge'
        self.assertEqual(self.client.get_hostname('https://api.uriEdge.region.twilio.com'),
                         'https://api.edge.region.twilio.com')

    def test_set_uri_edge_region(self):
        self.assertEqual(self.client.get_hostname('https://api.edge.region.twilio.com'),
                         'https://api.edge.region.twilio.com')

    def test_periods_in_query(self):
        self.client.region = 'region'
        self.client.edge = 'edge'
        self.assertEqual(self.client.get_hostname('https://api.twilio.com/path/to/something.json?foo=12.34'),
                         'https://api.edge.region.twilio.com/path/to/something.json?foo=12.34')


class TestUserAgentClients(unittest.TestCase):
    def setUp(self):
        self.client = Client('username', 'password')

    def tearDown(self):
        self.client.http_client.session.close()

    def test_set_default_user_agent(self):
        self.client.request('GET', 'https://api.twilio.com/')
        request_header = self.client.http_client.last_request.headers['User-Agent']
        self.assertRegex(request_header, r'^twilio-python\/[0-9.]+(-rc\.[0-9]+)?\s\(\w+\s\w+\)\sPython\/[^\s]+$')

    def test_set_user_agent_extensions(self):
        expected_user_agent_extensions = ['twilio-run/2.0.0-test', 'flex-plugin/3.4.0']
        self.client.user_agent_extensions = expected_user_agent_extensions
        self.client.request('GET', 'https://api.twilio.com/')
        user_agent_headers = self.client.http_client.last_request.headers['User-Agent']
        user_agent_extensions = user_agent_headers.split(" ")[-len(expected_user_agent_extensions):]
        self.assertEqual(user_agent_extensions, expected_user_agent_extensions)
