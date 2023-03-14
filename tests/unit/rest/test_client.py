import unittest
import aiounittest

from mock import AsyncMock, Mock
from twilio.http.response import Response
from twilio.rest import Client


class TestRegionEdgeClients(unittest.TestCase):
    def setUp(self):
        self.client = Client("username", "password")

    def test_set_client_edge_default_region(self):
        self.client.edge = "edge"
        self.assertEqual(
            self.client.get_hostname("https://api.twilio.com"),
            "https://api.edge.us1.twilio.com",
        )

    def test_set_client_region(self):
        self.client.region = "region"
        self.assertEqual(
            self.client.get_hostname("https://api.twilio.com"),
            "https://api.region.twilio.com",
        )

    def test_set_uri_region(self):
        self.assertEqual(
            self.client.get_hostname("https://api.region.twilio.com"),
            "https://api.region.twilio.com",
        )

    def test_set_client_edge_region(self):
        self.client.edge = "edge"
        self.client.region = "region"
        self.assertEqual(
            self.client.get_hostname("https://api.twilio.com"),
            "https://api.edge.region.twilio.com",
        )

    def test_set_client_edge_uri_region(self):
        self.client.edge = "edge"
        self.assertEqual(
            self.client.get_hostname("https://api.region.twilio.com"),
            "https://api.edge.region.twilio.com",
        )

    def test_set_client_region_uri_edge_region(self):
        self.client.region = "region"
        self.assertEqual(
            self.client.get_hostname("https://api.edge.uriRegion.twilio.com"),
            "https://api.edge.region.twilio.com",
        )

    def test_set_client_edge_uri_edge_region(self):
        self.client.edge = "edge"
        self.assertEqual(
            self.client.get_hostname("https://api.uriEdge.region.twilio.com"),
            "https://api.edge.region.twilio.com",
        )

    def test_set_uri_edge_region(self):
        self.assertEqual(
            self.client.get_hostname("https://api.edge.region.twilio.com"),
            "https://api.edge.region.twilio.com",
        )

    def test_periods_in_query(self):
        self.client.region = "region"
        self.client.edge = "edge"
        self.assertEqual(
            self.client.get_hostname(
                "https://api.twilio.com/path/to/something.json?foo=12.34"
            ),
            "https://api.edge.region.twilio.com/path/to/something.json?foo=12.34",
        )


class TestUserAgentClients(unittest.TestCase):
    def setUp(self):
        self.client = Client("username", "password")

    def tearDown(self):
        self.client.http_client.session.close()

    def test_set_default_user_agent(self):
        self.client.request("GET", "https://api.twilio.com/")
        request_header = self.client.http_client._test_only_last_request.headers[
            "User-Agent"
        ]
        self.assertRegex(
            request_header,
            r"^twilio-python\/[0-9.]+(-rc\.[0-9]+)?\s\(\w+\s\w+\)\sPython\/[^\s]+$",
        )

    def test_set_user_agent_extensions(self):
        expected_user_agent_extensions = ["twilio-run/2.0.0-test", "flex-plugin/3.4.0"]
        self.client.user_agent_extensions = expected_user_agent_extensions
        self.client.request("GET", "https://api.twilio.com/")
        user_agent_headers = self.client.http_client._test_only_last_request.headers[
            "User-Agent"
        ]
        user_agent_extensions = user_agent_headers.split(" ")[
            -len(expected_user_agent_extensions) :
        ]
        self.assertEqual(user_agent_extensions, expected_user_agent_extensions)


class TestClientAsyncRequest(aiounittest.AsyncTestCase):
    def setUp(self):
        self.mock_async_http_client = AsyncMock()
        self.mock_async_http_client.request.return_value = Response(200, "test")
        self.mock_async_http_client.is_async = True
        self.client = Client(
            "username", "password", http_client=self.mock_async_http_client
        )

    async def test_raise_error_if_client_not_marked_async(self):
        mock_http_client = Mock()
        mock_http_client.request.return_value = Response(200, "doesnt matter")
        mock_http_client.is_async = None

        client = Client("username", "password", http_client=mock_http_client)
        with self.assertRaises(RuntimeError):
            await client.request_async("doesnt matter", "doesnt matter")

    async def test_raise_error_if_client_is_not_async(self):
        mock_http_client = Mock()
        mock_http_client.request.return_value = Response(200, "doesnt matter")
        mock_http_client.is_async = False

        client = Client("username", "password", http_client=mock_http_client)
        with self.assertRaises(RuntimeError):
            await client.request_async("doesnt matter", "doesnt matter")

    async def test_request_async_called_with_method_and_url(self):
        await self.client.request_async("GET", "http://mock.twilio.com")
        self.assertEqual(self.mock_async_http_client.request.call_args.args[0], "GET")
        self.assertEqual(
            self.mock_async_http_client.request.call_args.args[1],
            "http://mock.twilio.com",
        )
