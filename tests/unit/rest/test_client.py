import unittest

from twilio.rest import (
    Client
)


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
        request_header = self.client.http_client._test_only_last_request.headers['User-Agent']
        self.assertRegex(request_header, r'^twilio-python\/[0-9.]+(-rc\.[0-9]+)?\s\(\w+\s\w+\)\sPython\/[^\s]+$')

    def test_set_user_agent_extensions(self):
        expected_user_agent_extensions = ['twilio-run/2.0.0-test', 'flex-plugin/3.4.0']
        self.client.user_agent_extensions = expected_user_agent_extensions
        self.client.request('GET', 'https://api.twilio.com/')
        user_agent_headers = self.client.http_client._test_only_last_request.headers['User-Agent']
        user_agent_extensions = user_agent_headers.split(" ")[-len(expected_user_agent_extensions):]
        self.assertEqual(user_agent_extensions, expected_user_agent_extensions)
