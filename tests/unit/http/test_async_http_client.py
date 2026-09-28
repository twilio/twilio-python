import warnings

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

    async def test_request_called_with_basic_auth_header_without_deprecation(self):
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "error",
                message="BasicAuth is deprecated.*",
                category=DeprecationWarning,
            )
            await self.client.request(
                "doesnt matter",
                "doesnt matter",
                auth=("account_sid", "auth_token"),
            )

        self.session_mock.request.assert_called()
        request_args = self.session_mock.request.call_args.kwargs
        self.assertNotIn("auth", request_args)
        self.assertEqual(
            request_args["headers"]["Authorization"],
            "Basic YWNjb3VudF9zaWQ6YXV0aF90b2tlbg==",
        )

    async def test_request_does_not_mutate_headers_when_adding_basic_auth(self):
        headers = {"X-Test": "value"}

        await self.client.request(
            "doesnt matter",
            "doesnt matter",
            headers=headers,
            auth=("account_sid", "auth_token"),
        )

        request_headers = self.session_mock.request.call_args.kwargs["headers"]
        self.assertEqual(headers, {"X-Test": "value"})
        self.assertIsNot(request_headers, headers)
        self.assertEqual(request_headers["X-Test"], "value")
        self.assertEqual(
            request_headers["Authorization"],
            "Basic YWNjb3VudF9zaWQ6YXV0aF90b2tlbg==",
        )

    async def test_request_preserves_latin1_basic_auth_encoding(self):
        await self.client.request(
            "doesnt matter", "doesnt matter", auth=("café", "päss")
        )

        request_headers = self.session_mock.request.call_args.kwargs["headers"]
        self.assertEqual(request_headers["Authorization"], "Basic Y2Fm6Tpw5HNz")

    async def test_request_accepts_empty_basic_auth_credentials(self):
        await self.client.request("doesnt matter", "doesnt matter", auth=("", ""))

        request_headers = self.session_mock.request.call_args.kwargs["headers"]
        self.assertEqual(request_headers["Authorization"], "Basic Og==")

    async def test_request_rejects_colon_in_basic_auth_username(self):
        with self.assertRaises(ValueError):
            await self.client.request(
                "doesnt matter", "doesnt matter", auth=("account:sid", "auth_token")
            )

        self.session_mock.request.assert_not_called()

    async def test_request_accepts_colon_in_basic_auth_password(self):
        await self.client.request(
            "doesnt matter", "doesnt matter", auth=("account_sid", "auth:token")
        )

        request_headers = self.session_mock.request.call_args.kwargs["headers"]
        self.assertEqual(
            request_headers["Authorization"],
            "Basic YWNjb3VudF9zaWQ6YXV0aDp0b2tlbg==",
        )

    async def test_request_rejects_auth_with_authorization_header(self):
        with self.assertRaisesRegex(
            ValueError,
            "Cannot combine AUTHORIZATION header with AUTH argument",
        ):
            await self.client.request(
                "doesnt matter",
                "doesnt matter",
                headers={"authorization": "Bearer token"},
                auth=("account_sid", "auth_token"),
            )

        self.session_mock.request.assert_not_called()

    async def test_request_checks_auth_header_conflict_before_encoding(self):
        with self.assertRaisesRegex(
            ValueError,
            "Cannot combine AUTHORIZATION header with AUTH argument",
        ):
            await self.client.request(
                "doesnt matter",
                "doesnt matter",
                headers={"Authorization": "Bearer token"},
                auth=("雪", "密"),
            )

        self.session_mock.request.assert_not_called()

    async def test_request_preserves_authorization_header_without_auth(self):
        headers = {"authorization": "Bearer token"}

        await self.client.request("doesnt matter", "doesnt matter", headers=headers)

        request_args = self.session_mock.request.call_args.kwargs
        self.assertNotIn("auth", request_args)
        self.assertEqual(request_args["headers"], headers)

    async def test_request_preserves_basic_auth_none_validation(self):
        with self.assertRaisesRegex(ValueError, "None is not allowed as login value"):
            await self.client.request(
                "doesnt matter", "doesnt matter", auth=(None, "auth_token")
            )
        with self.assertRaisesRegex(
            ValueError, "None is not allowed as password value"
        ):
            await self.client.request(
                "doesnt matter", "doesnt matter", auth=("account_sid", None)
            )

        self.session_mock.request.assert_not_called()

    async def test_request_rejects_non_latin1_basic_auth_credentials(self):
        with self.assertRaises(UnicodeEncodeError):
            await self.client.request(
                "doesnt matter", "doesnt matter", auth=("雪", "密")
            )

        self.session_mock.request.assert_not_called()

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
