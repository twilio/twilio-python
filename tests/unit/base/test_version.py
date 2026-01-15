import aiounittest
from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.page import Page
from twilio.http.response import Response


class TestPage(Page):
    def get_instance(self, payload):
        return payload


class StreamTestCase(IntegrationTestCase):
    def setUp(self):
        super(StreamTestCase, self).setUp()

        self.holodeck.mock(
            Response(
                200,
                """
            {
                "next_page_uri": "/2010-04-01/Accounts/AC123/Messages.json?Page=1",
                "messages": [{"body": "payload0"}, {"body": "payload1"}]
            }
            """,
            ),
            Request(
                url="https://api.twilio.com/2010-04-01/Accounts/AC123/Messages.json"
            ),
        )

        self.holodeck.mock(
            Response(
                200,
                """
            {
                "next_page_uri": "/2010-04-01/Accounts/AC123/Messages.json?Page=2",
                "messages": [{"body": "payload2"}, {"body": "payload3"}]
            }
            """,
            ),
            Request(
                url="https://api.twilio.com/2010-04-01/Accounts/AC123/Messages.json?Page=1"
            ),
        )

        self.holodeck.mock(
            Response(
                200,
                """
            {
                "next_page_uri": null,
                "messages": [{"body": "payload4"}]
            }
            """,
            ),
            Request(
                url="https://api.twilio.com/2010-04-01/Accounts/AC123/Messages.json?Page=2"
            ),
        )

        self.version = self.client.api.v2010
        self.response = self.version.page(
            method="GET", uri="/Accounts/AC123/Messages.json"
        )
        self.page = TestPage(self.version, self.response, {})

    def test_stream(self):
        messages = list(self.version.stream(self.page))

        self.assertEqual(len(messages), 5)

    def test_stream_limit(self):
        messages = list(self.version.stream(self.page, limit=3))

        self.assertEqual(len(messages), 3)

    def test_stream_page_limit(self):
        messages = list(self.version.stream(self.page, page_limit=1))

        self.assertEqual(len(messages), 2)


class VersionTestCase(IntegrationTestCase):
    def test_fetch_redirect(self):
        self.holodeck.mock(
            Response(307, '{"redirect_to": "some_place"}'),
            Request(url="https://messaging.twilio.com/v1/Deactivations"),
        )
        response = self.client.messaging.v1.fetch(method="GET", uri="/Deactivations")

        self.assertIsNotNone(response)

    def test_delete_success(self):
        self.holodeck.mock(
            Response(201, ""),
            Request(
                method="DELETE",
                url="https://api.twilio.com/2010-04-01/Accounts/AC123/Messages/MM123.json",
            ),
        )
        result = self.client.api.v2010.delete(
            method="DELETE", uri="/Accounts/AC123/Messages/MM123.json"
        )

        self.assertTrue(result)

    def test_delete_not_found(self):
        self.holodeck.mock(
            Response(404, '{"message": "Resource not found"}'),
            Request(
                method="DELETE",
                url="https://api.twilio.com/2010-04-01/Accounts/AC123/Messages/MM456.json",
            ),
        )

        with self.assertRaises(Exception) as context:
            self.client.api.v2010.delete(
                method="DELETE", uri="/Accounts/AC123/Messages/MM456.json"
            )

        self.assertIn("Unable to delete record", str(context.exception))

    def test_fetch_with_response_info(self):
        self.holodeck.mock(
            Response(
                200,
                '{"sid": "AC123", "name": "Test Account"}',
                {"X-Custom-Header": "test-value"},
            ),
            Request(url="https://api.twilio.com/2010-04-01/Accounts/AC123.json"),
        )
        payload, status_code, headers = self.client.api.v2010.fetch_with_response_info(
            method="GET", uri="/Accounts/AC123.json"
        )

        self.assertEqual(payload["sid"], "AC123")
        self.assertEqual(payload["name"], "Test Account")
        self.assertEqual(status_code, 200)
        self.assertIn("X-Custom-Header", headers)
        self.assertEqual(headers["X-Custom-Header"], "test-value")

    def test_update_with_response_info(self):
        self.holodeck.mock(
            Response(
                200,
                '{"sid": "AC123", "name": "Updated Account"}',
                {"X-Update-Header": "updated"},
            ),
            Request(
                method="POST",
                url="https://api.twilio.com/2010-04-01/Accounts/AC123.json",
            ),
        )
        payload, status_code, headers = self.client.api.v2010.update_with_response_info(
            method="POST", uri="/Accounts/AC123.json", data={"name": "Updated Account"}
        )

        self.assertEqual(payload["sid"], "AC123")
        self.assertEqual(payload["name"], "Updated Account")
        self.assertEqual(status_code, 200)
        self.assertIn("X-Update-Header", headers)

    def test_delete_with_response_info(self):
        self.holodeck.mock(
            Response(204, "", {"X-Delete-Header": "deleted"}),
            Request(
                method="DELETE",
                url="https://api.twilio.com/2010-04-01/Accounts/AC123/Messages/MM123.json",
            ),
        )
        success, status_code, headers = self.client.api.v2010.delete_with_response_info(
            method="DELETE", uri="/Accounts/AC123/Messages/MM123.json"
        )

        self.assertTrue(success)
        self.assertEqual(status_code, 204)
        self.assertIn("X-Delete-Header", headers)

    def test_create_with_response_info(self):
        self.holodeck.mock(
            Response(
                201,
                '{"sid": "MM123", "body": "Hello World"}',
                {"X-Create-Header": "created"},
            ),
            Request(
                method="POST",
                url="https://api.twilio.com/2010-04-01/Accounts/AC123/Messages.json",
            ),
        )
        payload, status_code, headers = self.client.api.v2010.create_with_response_info(
            method="POST",
            uri="/Accounts/AC123/Messages.json",
            data={"body": "Hello World"},
        )

        self.assertEqual(payload["sid"], "MM123")
        self.assertEqual(payload["body"], "Hello World")
        self.assertEqual(status_code, 201)
        self.assertIn("X-Create-Header", headers)

    def test_page_with_response_info(self):
        self.holodeck.mock(
            Response(
                200,
                '{"messages": [], "next_page_uri": null}',
                {"X-Page-Header": "page"},
            ),
            Request(
                url="https://api.twilio.com/2010-04-01/Accounts/AC123/Messages.json"
            ),
        )
        response, status_code, headers = self.client.api.v2010.page_with_response_info(
            method="GET", uri="/Accounts/AC123/Messages.json"
        )

        self.assertIsNotNone(response)
        self.assertEqual(status_code, 200)
        self.assertIn("X-Page-Header", headers)

    def test_fetch_with_response_info_error(self):
        self.holodeck.mock(
            Response(404, '{"message": "Resource not found"}'),
            Request(url="https://api.twilio.com/2010-04-01/Accounts/AC456.json"),
        )

        with self.assertRaises(Exception) as context:
            self.client.api.v2010.fetch_with_response_info(
                method="GET", uri="/Accounts/AC456.json"
            )

        self.assertIn("Unable to fetch record", str(context.exception))

    def test_update_with_response_info_error(self):
        self.holodeck.mock(
            Response(400, '{"message": "Invalid request"}'),
            Request(
                method="POST",
                url="https://api.twilio.com/2010-04-01/Accounts/AC123.json",
            ),
        )

        with self.assertRaises(Exception) as context:
            self.client.api.v2010.update_with_response_info(
                method="POST", uri="/Accounts/AC123.json", data={"invalid": "data"}
            )

        self.assertIn("Unable to update record", str(context.exception))

    def test_delete_with_response_info_error(self):
        self.holodeck.mock(
            Response(404, '{"message": "Resource not found"}'),
            Request(
                method="DELETE",
                url="https://api.twilio.com/2010-04-01/Accounts/AC123/Messages/MM456.json",
            ),
        )

        with self.assertRaises(Exception) as context:
            self.client.api.v2010.delete_with_response_info(
                method="DELETE", uri="/Accounts/AC123/Messages/MM456.json"
            )

        self.assertIn("Unable to delete record", str(context.exception))

    def test_create_with_response_info_error(self):
        self.holodeck.mock(
            Response(400, '{"message": "Invalid request"}'),
            Request(
                method="POST",
                url="https://api.twilio.com/2010-04-01/Accounts/AC123/Messages.json",
            ),
        )

        with self.assertRaises(Exception) as context:
            self.client.api.v2010.create_with_response_info(
                method="POST",
                uri="/Accounts/AC123/Messages.json",
                data={"invalid": "data"},
            )

        self.assertIn("Unable to create record", str(context.exception))

    def test_fetch_with_response_info_empty_headers(self):
        self.holodeck.mock(
            Response(200, '{"sid": "AC123", "name": "Test Account"}', None),
            Request(url="https://api.twilio.com/2010-04-01/Accounts/AC123.json"),
        )
        payload, status_code, headers = self.client.api.v2010.fetch_with_response_info(
            method="GET", uri="/Accounts/AC123.json"
        )

        self.assertEqual(payload["sid"], "AC123")
        self.assertEqual(status_code, 200)
        self.assertIsInstance(headers, dict)
        self.assertEqual(len(headers), 0)

    def test_fetch_with_response_info_multiple_headers(self):
        self.holodeck.mock(
            Response(
                200,
                '{"sid": "AC123"}',
                {
                    "X-Custom-Header-1": "value1",
                    "X-Custom-Header-2": "value2",
                    "Content-Type": "application/json",
                },
            ),
            Request(url="https://api.twilio.com/2010-04-01/Accounts/AC123.json"),
        )
        payload, status_code, headers = self.client.api.v2010.fetch_with_response_info(
            method="GET", uri="/Accounts/AC123.json"
        )

        self.assertEqual(status_code, 200)
        self.assertIn("X-Custom-Header-1", headers)
        self.assertIn("X-Custom-Header-2", headers)
        self.assertIn("Content-Type", headers)
        self.assertEqual(headers["X-Custom-Header-1"], "value1")
        self.assertEqual(headers["X-Custom-Header-2"], "value2")

    def test_fetch_with_response_info_returns_tuple(self):
        self.holodeck.mock(
            Response(200, '{"sid": "AC123"}', {"X-Test": "test"}),
            Request(url="https://api.twilio.com/2010-04-01/Accounts/AC123.json"),
        )
        result = self.client.api.v2010.fetch_with_response_info(
            method="GET", uri="/Accounts/AC123.json"
        )

        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)
        payload, status_code, headers = result
        self.assertIsInstance(payload, dict)
        self.assertIsInstance(status_code, int)
        self.assertIsInstance(headers, dict)


class AsyncVersionTestCase(aiounittest.AsyncTestCase):
    def setUp(self):
        from tests.holodeck import AsyncHolodeck
        from twilio.rest import Client

        self.holodeck = AsyncHolodeck()
        self.client = Client(
            "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", http_client=self.holodeck
        )

    async def test_fetch_with_response_info_async(self):
        """Test fetch_with_response_info_async method"""
        self.holodeck.mock(
            Response(
                200,
                '{"sid": "AC123", "name": "Test Account"}',
                {"X-Custom-Header": "test-value"},
            ),
            Request(url="https://api.twilio.com/2010-04-01/Accounts/AC123.json"),
        )
        payload, status_code, headers = (
            await self.client.api.v2010.fetch_with_response_info_async(
                method="GET", uri="/Accounts/AC123.json"
            )
        )

        self.assertEqual(payload["sid"], "AC123")
        self.assertEqual(payload["name"], "Test Account")
        self.assertEqual(status_code, 200)
        self.assertIn("X-Custom-Header", headers)
        self.assertEqual(headers["X-Custom-Header"], "test-value")

    async def test_update_with_response_info_async(self):
        """Test update_with_response_info_async method"""
        self.holodeck.mock(
            Response(
                200,
                '{"sid": "AC123", "name": "Updated Account"}',
                {"X-Update-Header": "updated"},
            ),
            Request(
                method="POST",
                url="https://api.twilio.com/2010-04-01/Accounts/AC123.json",
            ),
        )
        payload, status_code, headers = (
            await self.client.api.v2010.update_with_response_info_async(
                method="POST",
                uri="/Accounts/AC123.json",
                data={"name": "Updated Account"},
            )
        )

        self.assertEqual(payload["sid"], "AC123")
        self.assertEqual(payload["name"], "Updated Account")
        self.assertEqual(status_code, 200)
        self.assertIn("X-Update-Header", headers)

    async def test_delete_with_response_info_async(self):
        """Test delete_with_response_info_async method"""
        self.holodeck.mock(
            Response(204, "", {"X-Delete-Header": "deleted"}),
            Request(
                method="DELETE",
                url="https://api.twilio.com/2010-04-01/Accounts/AC123/Messages/MM123.json",
            ),
        )
        success, status_code, headers = (
            await self.client.api.v2010.delete_with_response_info_async(
                method="DELETE", uri="/Accounts/AC123/Messages/MM123.json"
            )
        )

        self.assertTrue(success)
        self.assertEqual(status_code, 204)
        self.assertIn("X-Delete-Header", headers)

    async def test_create_with_response_info_async(self):
        """Test create_with_response_info_async method"""
        self.holodeck.mock(
            Response(
                201,
                '{"sid": "MM123", "body": "Hello World"}',
                {"X-Create-Header": "created"},
            ),
            Request(
                method="POST",
                url="https://api.twilio.com/2010-04-01/Accounts/AC123/Messages.json",
            ),
        )
        payload, status_code, headers = (
            await self.client.api.v2010.create_with_response_info_async(
                method="POST",
                uri="/Accounts/AC123/Messages.json",
                data={"body": "Hello World"},
            )
        )

        self.assertEqual(payload["sid"], "MM123")
        self.assertEqual(payload["body"], "Hello World")
        self.assertEqual(status_code, 201)
        self.assertIn("X-Create-Header", headers)

    async def test_page_with_response_info_async(self):
        """Test page_with_response_info_async method"""
        self.holodeck.mock(
            Response(
                200,
                '{"messages": [], "next_page_uri": null}',
                {"X-Page-Header": "page"},
            ),
            Request(
                url="https://api.twilio.com/2010-04-01/Accounts/AC123/Messages.json"
            ),
        )
        response, status_code, headers = (
            await self.client.api.v2010.page_with_response_info_async(
                method="GET", uri="/Accounts/AC123/Messages.json"
            )
        )

        self.assertIsNotNone(response)
        self.assertEqual(status_code, 200)
        self.assertIn("X-Page-Header", headers)

    async def test_fetch_with_response_info_async_error(self):
        """Test fetch_with_response_info_async method with error"""
        self.holodeck.mock(
            Response(404, '{"message": "Resource not found"}'),
            Request(url="https://api.twilio.com/2010-04-01/Accounts/AC456.json"),
        )

        with self.assertRaises(Exception) as context:
            await self.client.api.v2010.fetch_with_response_info_async(
                method="GET", uri="/Accounts/AC456.json"
            )

        self.assertIn("Unable to fetch record", str(context.exception))

    async def test_update_with_response_info_async_error(self):
        """Test update_with_response_info_async method with error"""
        self.holodeck.mock(
            Response(400, '{"message": "Invalid request"}'),
            Request(
                method="POST",
                url="https://api.twilio.com/2010-04-01/Accounts/AC123.json",
            ),
        )

        with self.assertRaises(Exception) as context:
            await self.client.api.v2010.update_with_response_info_async(
                method="POST", uri="/Accounts/AC123.json", data={"invalid": "data"}
            )

        self.assertIn("Unable to update record", str(context.exception))

    async def test_delete_with_response_info_async_error(self):
        """Test delete_with_response_info_async method with error"""
        self.holodeck.mock(
            Response(404, '{"message": "Resource not found"}'),
            Request(
                method="DELETE",
                url="https://api.twilio.com/2010-04-01/Accounts/AC123/Messages/MM456.json",
            ),
        )

        with self.assertRaises(Exception) as context:
            await self.client.api.v2010.delete_with_response_info_async(
                method="DELETE", uri="/Accounts/AC123/Messages/MM456.json"
            )

        self.assertIn("Unable to delete record", str(context.exception))

    async def test_create_with_response_info_async_error(self):
        """Test create_with_response_info_async method with error"""
        self.holodeck.mock(
            Response(400, '{"message": "Invalid request"}'),
            Request(
                method="POST",
                url="https://api.twilio.com/2010-04-01/Accounts/AC123/Messages.json",
            ),
        )

        with self.assertRaises(Exception) as context:
            await self.client.api.v2010.create_with_response_info_async(
                method="POST",
                uri="/Accounts/AC123/Messages.json",
                data={"invalid": "data"},
            )

        self.assertIn("Unable to create record", str(context.exception))

    async def test_fetch_with_response_info_async_empty_headers(self):
        """Test fetch_with_response_info_async with None headers"""
        self.holodeck.mock(
            Response(200, '{"sid": "AC123", "name": "Test Account"}', None),
            Request(url="https://api.twilio.com/2010-04-01/Accounts/AC123.json"),
        )
        payload, status_code, headers = (
            await self.client.api.v2010.fetch_with_response_info_async(
                method="GET", uri="/Accounts/AC123.json"
            )
        )

        self.assertEqual(payload["sid"], "AC123")
        self.assertEqual(status_code, 200)
        self.assertIsInstance(headers, dict)
        self.assertEqual(len(headers), 0)

    async def test_fetch_with_response_info_async_multiple_headers(self):
        """Test fetch_with_response_info_async with multiple headers"""
        self.holodeck.mock(
            Response(
                200,
                '{"sid": "AC123"}',
                {
                    "X-Custom-Header-1": "value1",
                    "X-Custom-Header-2": "value2",
                    "Content-Type": "application/json",
                },
            ),
            Request(url="https://api.twilio.com/2010-04-01/Accounts/AC123.json"),
        )
        payload, status_code, headers = (
            await self.client.api.v2010.fetch_with_response_info_async(
                method="GET", uri="/Accounts/AC123.json"
            )
        )

        self.assertEqual(status_code, 200)
        self.assertIn("X-Custom-Header-1", headers)
        self.assertIn("X-Custom-Header-2", headers)
        self.assertIn("Content-Type", headers)
        self.assertEqual(headers["X-Custom-Header-1"], "value1")
        self.assertEqual(headers["X-Custom-Header-2"], "value2")

    async def test_fetch_with_response_info_async_returns_tuple(self):
        """Test that fetch_with_response_info_async returns proper tuple structure"""
        self.holodeck.mock(
            Response(200, '{"sid": "AC123"}', {"X-Test": "test"}),
            Request(url="https://api.twilio.com/2010-04-01/Accounts/AC123.json"),
        )
        result = await self.client.api.v2010.fetch_with_response_info_async(
            method="GET", uri="/Accounts/AC123.json"
        )

        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)
        payload, status_code, headers = result
        self.assertIsInstance(payload, dict)
        self.assertIsInstance(status_code, int)
        self.assertIsInstance(headers, dict)
