import aiounittest

from aiohttp import ClientSession
from mock import patch, AsyncMock
from twilio.http.async_http_client import AsyncTwilioHttpClient


class MockResponse(object):
    """
    A mock of the aiohttp.ClientResponse class
    """

    def __init__(self, text, status, method="GET"):
        self._text = text
        self.status = status
        self.headers = {}
        self.method = method

    async def text(self):
        return self._text


class TestAsyncHttpClientRequest(aiounittest.AsyncTestCase):
    def setUp(self):
        self.session_mock = AsyncMock(wraps=ClientSession)
        self.session_mock.request.return_value = MockResponse("test", 200)

        self.session_patcher = patch("twilio.http.async_http_client.ClientSession")
        session_constructor_mock = self.session_patcher.start()
        session_constructor_mock.return_value = self.session_mock

        self.client = AsyncTwilioHttpClient()

    def tearDown(self):
        self.session_patcher.stop()

    async def test_request_called_with_method_and_url(self):
        await self.client.request("GET", "https://mock.twilio.com")

        self.session_mock.request.assert_called()
        request_args = self.session_mock.request.call_args.kwargs
        self.assertIsNotNone(request_args)
        self.assertEqual(request_args["method"], "GET")
        self.assertEqual(request_args["url"], "https://mock.twilio.com")

    async def test_request_called_with_basic_auth(self):
        await self.client.request(
            "doesnt matter", "doesnt matter", auth=("account_sid", "auth_token")
        )

        self.session_mock.request.assert_called()
        auth = self.session_mock.request.call_args.kwargs["auth"]
        self.assertIsNotNone(auth)
        self.assertEqual(auth.login, "account_sid")
        self.assertEqual(auth.password, "auth_token")

    async def test_invalid_request_timeout_raises_exception(self):
        with self.assertRaises(ValueError):
            await self.client.request("doesnt matter", "doesnt matter", timeout=-1)


class TestAsyncHttpClientRetries(aiounittest.AsyncTestCase):
    def setUp(self):
        self.session_mock = AsyncMock(wraps=ClientSession)
        self.session_mock.request.side_effect = [
            MockResponse("Error", 500),
            MockResponse("Error", 500),
            MockResponse("Success", 200),
        ]

        self.session_patcher = patch("twilio.http.async_http_client.ClientSession")
        session_constructor_mock = self.session_patcher.start()
        session_constructor_mock.return_value = self.session_mock

    def tearDown(self):
        self.session_patcher.stop()

    async def test_request_retries_until_success(self):
        client = AsyncTwilioHttpClient(max_retries=99)
        response = await client.request("doesnt matter", "doesnt matter")

        self.assertEqual(self.session_mock.request.call_count, 3)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Success")

    async def test_request_retries_until_max(self):
        client = AsyncTwilioHttpClient(max_retries=2)
        response = await client.request("doesnt matter", "doesnt matter")

        self.assertEqual(self.session_mock.request.call_count, 2)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.text, "Error")


class TestAsyncHttpClientSession(aiounittest.AsyncTestCase):
    def setUp(self):
        self.session_patcher = patch("twilio.http.async_http_client.ClientSession")
        self.session_constructor_mock = self.session_patcher.start()

    def tearDown(self):
        self.session_patcher.stop()

    def _setup_session_response(self, value):
        session_mock = AsyncMock(wraps=ClientSession)
        session_mock.request.return_value = MockResponse(value, 200)
        session_mock.close.return_value = None
        self.session_constructor_mock.return_value = session_mock

    async def test_session_preserved(self):
        self._setup_session_response("response_1")

        client = AsyncTwilioHttpClient()
        response_1 = await client.request("GET", "https://api.twilio.com")

        self._setup_session_response("response_2")
        response_2 = await client.request("GET", "https://api.twilio.com")

        # Used same session, response should be the same
        self.assertEqual(response_1.content, "response_1")
        self.assertEqual(response_2.content, "response_1")

    async def test_session_not_preserved(self):
        self._setup_session_response("response_1")

        client = AsyncTwilioHttpClient(pool_connections=False)
        response_1 = await client.request("GET", "https://api.twilio.com")

        self._setup_session_response("response_2")
        response_2 = await client.request("GET", "https://api.twilio.com")

        # No session used, responses should be different (not cached)
        self.assertEqual(response_1.content, "response_1")
        self.assertEqual(response_2.content, "response_2")
