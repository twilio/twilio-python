import unittest
from unittest.mock import Mock
from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.base.token_pagination import TokenPagination
from twilio.http.response import Response


class TestTokenPaginationPage(TokenPagination):
    """Test implementation of TokenPagination"""

    def get_instance(self, payload):
        return payload


class TokenPaginationPropertyTest(unittest.TestCase):
    """Test TokenPagination property accessors"""

    def setUp(self):
        self.version = Mock()
        self.version.domain = Mock()

        # Mock response with token pagination format
        self.payload = {
            "meta": {
                "key": "items",
                "pageSize": 50,
                "nextToken": "next_abc123",
                "previousToken": "prev_xyz789",
            },
            "items": [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}],
        }

        self.response = Mock()
        self.response.text = """
        {
            "meta": {
                "key": "items",
                "pageSize": 50,
                "nextToken": "next_abc123",
                "previousToken": "prev_xyz789"
            },
            "items": [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
        }
        """
        self.response.status_code = 200

        self.solution = {
            "account_sid": "ACxxxx",
            "api_uri": "/Accounts/ACxxxx/Resources.json",
        }
        self.page = TestTokenPaginationPage(
            self.version,
            self.response,
            "/Accounts/ACxxxx/Resources.json",
            self.solution,
        )

    def test_key_property(self):
        """Test that key property returns the correct value"""
        self.assertEqual(self.page.key, "items")

    def test_page_size_property(self):
        """Test that page_size property returns the correct value"""
        self.assertEqual(self.page.page_size, 50)

    def test_next_token_property(self):
        """Test that next_token property returns the correct value"""
        self.assertEqual(self.page.next_token, "next_abc123")

    def test_previous_token_property(self):
        """Test that previous_token property returns the correct value"""
        self.assertEqual(self.page.previous_token, "prev_xyz789")

    def test_properties_without_meta(self):
        """Test that properties return None when meta is missing"""
        response = Mock()
        response.text = '{"items": []}'
        response.status_code = 200

        page = TestTokenPaginationPage(
            self.version, response, "/Accounts/ACxxxx/Resources.json", self.solution
        )

        self.assertIsNone(page.key)
        self.assertIsNone(page.page_size)
        self.assertIsNone(page.next_token)
        self.assertIsNone(page.previous_token)

    def test_properties_with_partial_meta(self):
        """Test that properties return None when specific keys are missing"""
        response = Mock()
        response.text = '{"meta": {"key": "items"}, "items": []}'
        response.status_code = 200

        page = TestTokenPaginationPage(
            self.version, response, "/Accounts/ACxxxx/Resources.json", self.solution
        )

        self.assertEqual(page.key, "items")
        self.assertIsNone(page.page_size)
        self.assertIsNone(page.next_token)
        self.assertIsNone(page.previous_token)


class TokenPaginationNavigationTest(IntegrationTestCase):
    """Test TokenPagination next_page and previous_page methods"""

    def setUp(self):
        super(TokenPaginationNavigationTest, self).setUp()

        # Mock first page response
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "meta": {
                    "key": "items",
                    "pageSize": 2,
                    "nextToken": "token_page2",
                    "previousToken": null
                },
                "items": [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
            }
            """,
            ),
            Request(
                url="https://api.twilio.com/2010-04-01/Accounts/ACaaaa/Resources.json"
            ),
        )

        # Mock second page response (next page)
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "meta": {
                    "key": "items",
                    "pageSize": 2,
                    "nextToken": "token_page3",
                    "previousToken": "token_prev1"
                },
                "items": [{"id": 3, "name": "Item 3"}, {"id": 4, "name": "Item 4"}]
            }
            """,
            ),
            Request(
                url="https://api.twilio.com/2010-04-01/Accounts/ACaaaa/Resources.json?pageToken=token_page2"
            ),
        )

        # Mock third page response (has no next)
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "meta": {
                    "key": "items",
                    "pageSize": 2,
                    "nextToken": null,
                    "previousToken": "token_prev2"
                },
                "items": [{"id": 5, "name": "Item 5"}]
            }
            """,
            ),
            Request(
                url="https://api.twilio.com/2010-04-01/Accounts/ACaaaa/Resources.json?pageToken=token_page3"
            ),
        )

        # Mock previous page response (going back to page 1)
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "meta": {
                    "key": "items",
                    "pageSize": 2,
                    "nextToken": "token_page2",
                    "previousToken": null
                },
                "items": [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
            }
            """,
            ),
            Request(
                url="https://api.twilio.com/2010-04-01/Accounts/ACaaaa/Resources.json?pageToken=token_prev1"
            ),
        )

        # Mock going back from page 3 to page 2
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "meta": {
                    "key": "items",
                    "pageSize": 2,
                    "nextToken": "token_page3",
                    "previousToken": "token_prev1"
                },
                "items": [{"id": 3, "name": "Item 3"}, {"id": 4, "name": "Item 4"}]
            }
            """,
            ),
            Request(
                url="https://api.twilio.com/2010-04-01/Accounts/ACaaaa/Resources.json?pageToken=token_prev2"
            ),
        )

        self.version = self.client.api.v2010
        self.response = self.version.page(
            method="GET", uri="/Accounts/ACaaaa/Resources.json"
        )

        self.solution = {
            "account_sid": "ACaaaa",
            "api_uri": "/2010-04-01/Accounts/ACaaaa/Resources.json",
        }

        self.page = TestTokenPaginationPage(
            self.version,
            self.response,
            "/2010-04-01/Accounts/ACaaaa/Resources.json",
            self.solution,
        )

    def test_next_page(self):
        """Test that next_page() navigates to the next page using token"""
        self.assertIsNotNone(self.page.next_token)
        self.assertEqual(self.page.next_token, "token_page2")

        next_page = self.page.next_page()

        self.assertIsNotNone(next_page)
        self.assertIsInstance(next_page, TestTokenPaginationPage)
        # Verify we got the next page's data
        self.assertEqual(next_page.next_token, "token_page3")
        self.assertEqual(next_page.previous_token, "token_prev1")

    def test_next_page_none_when_no_token(self):
        """Test that next_page() returns None when there's no next token"""
        # Navigate to the last page
        next_page = self.page.next_page()
        last_page = next_page.next_page()

        # Last page should have no next token
        self.assertIsNone(last_page.next_token)

        # next_page() should return None
        result = last_page.next_page()
        self.assertIsNone(result)

    def test_previous_page(self):
        """Test that previous_page() navigates to the previous page using token"""
        # Navigate to second page first
        next_page = self.page.next_page()
        self.assertIsNotNone(next_page.previous_token)
        self.assertEqual(next_page.previous_token, "token_prev1")

        # Go back to previous page
        prev_page = next_page.previous_page()

        self.assertIsNotNone(prev_page)
        self.assertIsInstance(prev_page, TestTokenPaginationPage)
        # Verify we got the first page's data
        self.assertIsNone(prev_page.previous_token)
        self.assertEqual(prev_page.next_token, "token_page2")

    def test_previous_page_none_when_no_token(self):
        """Test that previous_page() returns None when there's no previous token"""
        # First page should have no previous token
        self.assertIsNone(self.page.previous_token)

        # previous_page() should return None
        result = self.page.previous_page()
        self.assertIsNone(result)

    def test_navigation_chain(self):
        """Test navigating through multiple pages forward and backward"""
        # Page 1 -> Page 2
        page2 = self.page.next_page()
        self.assertEqual(page2.previous_token, "token_prev1")

        # Page 2 -> Page 3
        page3 = page2.next_page()
        self.assertIsNone(page3.next_token)
        self.assertEqual(page3.previous_token, "token_prev2")

        # Page 3 -> Page 2 (backward)
        back_to_page2 = page3.previous_page()
        self.assertIsNotNone(back_to_page2)


class TokenPaginationErrorTest(unittest.TestCase):
    """Test TokenPagination error handling"""

    def test_next_page_without_uri_in_solution(self):
        """Test that next_page() raises error when URI is missing"""
        version = Mock()
        response = Mock()
        response.text = """
        {
            "meta": {
                "key": "items",
                "pageSize": 50,
                "nextToken": "abc123"
            },
            "items": []
        }
        """
        response.status_code = 200

        # Solution without URI
        solution = {"account_sid": "ACxxxx"}

        # Pass empty string as URI to test the error case
        page = TestTokenPaginationPage(version, response, "", solution)

        with self.assertRaises(TwilioException) as context:
            page.next_page()

        self.assertIn("URI must be provided", str(context.exception))


class TokenPaginationStreamTest(IntegrationTestCase):
    """Test streaming with TokenPagination"""

    def setUp(self):
        super(TokenPaginationStreamTest, self).setUp()

        # Mock page 1
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "meta": {
                    "key": "records",
                    "pageSize": 2,
                    "nextToken": "token_2"
                },
                "records": [{"id": 1}, {"id": 2}]
            }
            """,
            ),
            Request(
                url="https://api.twilio.com/2010-04-01/Accounts/ACaaaa/Records.json"
            ),
        )

        # Mock page 2
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "meta": {
                    "key": "records",
                    "pageSize": 2,
                    "nextToken": "token_3",
                    "previousToken": "token_2"
                },
                "records": [{"id": 3}, {"id": 4}]
            }
            """,
            ),
            Request(
                url="https://api.twilio.com/2010-04-01/Accounts/ACaaaa/Records.json?pageToken=token_2"
            ),
        )

        # Mock page 3 (final)
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "meta": {
                    "key": "records",
                    "pageSize": 2,
                    "nextToken": null,
                    "previousToken": "token_3"
                },
                "records": [{"id": 5}]
            }
            """,
            ),
            Request(
                url="https://api.twilio.com/2010-04-01/Accounts/ACaaaa/Records.json?pageToken=token_3"
            ),
        )

        self.version = self.client.api.v2010
        self.response = self.version.page(
            method="GET", uri="/Accounts/ACaaaa/Records.json"
        )

        self.solution = {
            "account_sid": "ACaaaa",
            "api_uri": "/2010-04-01/Accounts/ACaaaa/Records.json",
        }

        self.page = TestTokenPaginationPage(
            self.version,
            self.response,
            "/2010-04-01/Accounts/ACaaaa/Records.json",
            self.solution,
        )

    def test_stream_all_records(self):
        """Test streaming through all pages"""
        records = list(self.version.stream(self.page))

        self.assertEqual(len(records), 5)
        self.assertEqual(records[0]["id"], 1)
        self.assertEqual(records[4]["id"], 5)

    def test_stream_with_limit(self):
        """Test streaming with a limit"""
        records = list(self.version.stream(self.page, limit=3))

        self.assertEqual(len(records), 3)
        self.assertEqual(records[0]["id"], 1)
        self.assertEqual(records[2]["id"], 3)

    def test_stream_with_page_limit(self):
        """Test streaming with page limit"""
        records = list(self.version.stream(self.page, page_limit=1))

        # Only first page (2 records)
        self.assertEqual(len(records), 2)


if __name__ == "__main__":
    unittest.main()
