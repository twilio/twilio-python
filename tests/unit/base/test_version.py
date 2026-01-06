import unittest
from unittest.mock import Mock

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.version import Version
from twilio.base.exceptions import (
    TwilioRestException,
    TwilioServiceException,
    TwilioException,
)
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


class VersionExceptionTestCase(unittest.TestCase):
    """Test cases for base Version.exception() method with RFC-9457 auto-detection"""

    def test_exception_rfc9457_auto_detection(self):
        """Test that base Version auto-detects RFC-9457 errors and creates TwilioServiceException"""
        response = Mock(spec=Response)
        response.status_code = 400
        response.text = """{
            "type": "https://www.twilio.com/docs/api/errors/20001",
            "title": "Invalid parameter",
            "status": 400,
            "code": 20001,
            "detail": "The 'PhoneNumber' parameter is required.",
            "instance": "/api/v1/accounts/AC123/calls/CA456"
        }"""

        exception = Version.exception(
            method="POST", uri="/test", response=response, message="Test error"
        )

        self.assertIsInstance(exception, TwilioServiceException)
        self.assertEqual(exception.type, "https://www.twilio.com/docs/api/errors/20001")
        self.assertEqual(exception.title, "Invalid parameter")
        self.assertEqual(exception.status, 400)
        self.assertEqual(exception.code, 20001)
        self.assertEqual(exception.detail, "The 'PhoneNumber' parameter is required.")
        self.assertEqual(exception.instance, "/api/v1/accounts/AC123/calls/CA456")
        self.assertEqual(exception.method, "POST")
        self.assertEqual(exception.uri, "/test")

    def test_exception_legacy_format_fallback(self):
        """Test that base Version falls back to TwilioRestException for legacy errors"""
        response = Mock(spec=Response)
        response.status_code = 400
        response.text = """{
            "message": "Invalid phone number",
            "code": 21211
        }"""

        exception = Version.exception(
            method="POST", uri="/test", response=response, message="Test error"
        )

        self.assertIsInstance(exception, TwilioRestException)
        self.assertEqual(exception.status, 400)
        self.assertEqual(exception.code, 21211)
        self.assertIn("Invalid phone number", exception.msg)

    def test_exception_rfc9457_with_validation_errors_base_version(self):
        """Test base Version handles RFC-9457 with validation errors array"""
        response = Mock(spec=Response)
        response.status_code = 422
        response.text = """{
            "type": "https://www.twilio.com/docs/api/errors/20001",
            "title": "Validation failed",
            "status": 422,
            "code": 20001,
            "detail": "Request validation failed",
            "errors": [
                {"detail": "must be a positive integer", "pointer": "#/age"},
                {"detail": "must be 'green', 'red' or 'blue'", "pointer": "#/profile/color"}
            ]
        }"""

        exception = Version.exception(
            method="POST", uri="/test", response=response, message="Validation error"
        )

        self.assertIsInstance(exception, TwilioServiceException)
        self.assertEqual(exception.title, "Validation failed")
        self.assertEqual(len(exception.errors), 2)
        self.assertEqual(exception.errors[0]["detail"], "must be a positive integer")
        self.assertEqual(exception.errors[0]["pointer"], "#/age")

    def test_exception_malformed_json_fallback(self):
        """Test that base Version handles malformed JSON gracefully"""
        response = Mock(spec=Response)
        response.status_code = 500
        response.text = "This is not JSON"

        exception = Version.exception(
            method="GET", uri="/test", response=response, message="Server error"
        )

        self.assertIsInstance(exception, TwilioRestException)
        self.assertEqual(exception.status, 500)


class TwilioServiceExceptionTestCase(unittest.TestCase):
    """Comprehensive test cases for TwilioServiceException"""

    def test_minimal_required_fields(self):
        """Test TwilioServiceException with only required fields"""
        exc = TwilioServiceException(
            type_uri="https://www.twilio.com/docs/api/errors/20003",
            title="Authentication Failed",
            status=401,
            code=20003,
        )

        self.assertEqual(exc.type, "https://www.twilio.com/docs/api/errors/20003")
        self.assertEqual(exc.title, "Authentication Failed")
        self.assertEqual(exc.status, 401)
        self.assertEqual(exc.code, 20003)
        self.assertIsNone(exc.detail)
        self.assertIsNone(exc.instance)
        self.assertEqual(exc.errors, [])
        self.assertEqual(exc.method, "GET")
        self.assertEqual(exc.uri, "")

    def test_all_fields_populated(self):
        """Test TwilioServiceException with all fields populated"""
        errors = [
            {"detail": "Field is required", "pointer": "#/name"},
            {"detail": "Must be a valid email", "pointer": "#/email"},
        ]

        exc = TwilioServiceException(
            type_uri="https://www.twilio.com/docs/api/errors/20001",
            title="Invalid Request",
            status=400,
            code=20001,
            detail="The request could not be processed",
            instance="/api/v1/accounts/AC123/messages/SM456",
            errors=errors,
            method="POST",
            uri="/api/v1/messages",
        )

        self.assertEqual(exc.type, "https://www.twilio.com/docs/api/errors/20001")
        self.assertEqual(exc.title, "Invalid Request")
        self.assertEqual(exc.status, 400)
        self.assertEqual(exc.code, 20001)
        self.assertEqual(exc.detail, "The request could not be processed")
        self.assertEqual(exc.instance, "/api/v1/accounts/AC123/messages/SM456")
        self.assertEqual(len(exc.errors), 2)
        self.assertEqual(exc.errors[0]["detail"], "Field is required")
        self.assertEqual(exc.errors[0]["pointer"], "#/name")
        self.assertEqual(exc.method, "POST")
        self.assertEqual(exc.uri, "/api/v1/messages")

    def test_partial_optional_fields(self):
        """Test TwilioServiceException with some optional fields"""
        exc = TwilioServiceException(
            type_uri="https://www.twilio.com/docs/api/errors/20002",
            title="Rate Limit Exceeded",
            status=429,
            code=20002,
            detail="Too many requests",
            method="POST",
            uri="/api/v1/calls",
        )

        self.assertEqual(exc.detail, "Too many requests")
        self.assertIsNone(exc.instance)
        self.assertEqual(exc.errors, [])
        self.assertEqual(exc.method, "POST")
        self.assertEqual(exc.uri, "/api/v1/calls")

    def test_empty_errors_array(self):
        """Test TwilioServiceException with explicitly empty errors array"""
        exc = TwilioServiceException(
            type_uri="https://www.twilio.com/docs/api/errors/20001",
            title="Bad Request",
            status=400,
            code=20001,
            errors=[],
        )

        self.assertEqual(exc.errors, [])

    def test_none_errors_becomes_empty_list(self):
        """Test that None errors parameter becomes empty list"""
        exc = TwilioServiceException(
            type_uri="https://www.twilio.com/docs/api/errors/20001",
            title="Bad Request",
            status=400,
            code=20001,
            errors=None,
        )

        self.assertEqual(exc.errors, [])
        self.assertIsInstance(exc.errors, list)

    def test_different_http_methods(self):
        """Test TwilioServiceException with different HTTP methods"""
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

        for method in methods:
            exc = TwilioServiceException(
                type_uri="https://www.twilio.com/docs/api/errors/20001",
                title="Error",
                status=400,
                code=20001,
                method=method,
            )
            self.assertEqual(exc.method, method)

    def test_different_status_codes(self):
        """Test TwilioServiceException with various HTTP status codes"""
        status_codes = [400, 401, 403, 404, 422, 429, 500, 502, 503]

        for status_code in status_codes:
            exc = TwilioServiceException(
                type_uri="https://www.twilio.com/docs/api/errors/20001",
                title="Error",
                status=status_code,
                code=20001,
            )
            self.assertEqual(exc.status, status_code)

    def test_string_representation_non_tty(self):
        """Test __str__ method for non-TTY output (plain text)"""
        exc = TwilioServiceException(
            type_uri="https://www.twilio.com/docs/api/errors/20001",
            title="Invalid Parameter",
            status=400,
            code=20001,
            detail="The PhoneNumber parameter is required",
        )

        # Mock sys.stderr to simulate non-TTY
        import sys

        original_stderr = sys.stderr
        try:
            sys.stderr = Mock()
            sys.stderr.isatty = Mock(return_value=False)

            result = str(exc)

            self.assertIn("HTTP 400 error", result)
            self.assertIn("Invalid Parameter", result)
            self.assertIn("The PhoneNumber parameter is required", result)
        finally:
            sys.stderr = original_stderr

    def test_string_representation_non_tty_with_validation_errors(self):
        """Test __str__ method for non-TTY with validation errors"""
        errors = [
            {"detail": "must be positive", "pointer": "#/age"},
            {"detail": "must be valid email", "pointer": "#/email"},
        ]

        exc = TwilioServiceException(
            type_uri="https://www.twilio.com/docs/api/errors/20001",
            title="Validation Failed",
            status=422,
            code=20001,
            detail="Request validation failed",
            errors=errors,
        )

        import sys

        original_stderr = sys.stderr
        try:
            sys.stderr = Mock()
            sys.stderr.isatty = Mock(return_value=False)

            result = str(exc)

            self.assertIn("HTTP 422 error", result)
            self.assertIn("Validation Failed", result)
            self.assertIn("Request validation failed", result)
            self.assertIn("Validation errors", result)
            self.assertIn("#/age", result)
            self.assertIn("must be positive", result)
        finally:
            sys.stderr = original_stderr

    def test_string_representation_tty(self):
        """Test __str__ method for TTY output (colored)"""
        exc = TwilioServiceException(
            type_uri="https://www.twilio.com/docs/api/errors/20001",
            title="Invalid Parameter",
            status=400,
            code=20001,
            detail="The PhoneNumber parameter is required",
            instance="/api/v1/accounts/AC123/calls/CA456",
            method="POST",
            uri="/api/v1/calls",
        )

        import sys

        original_stderr = sys.stderr
        try:
            sys.stderr = Mock()
            sys.stderr.isatty = Mock(return_value=True)

            result = str(exc)

            # Check for ANSI escape codes (color formatting)
            self.assertIn("\033[", result)
            # Check for content
            self.assertIn("HTTP Error", result)
            self.assertIn("POST /api/v1/calls", result)
            self.assertIn("Invalid Parameter", result)
            self.assertIn("The PhoneNumber parameter is required", result)
            self.assertIn("400", result)
            self.assertIn("20001", result)
            self.assertIn("https://www.twilio.com/docs/api/errors/20001", result)
        finally:
            sys.stderr = original_stderr

    def test_string_representation_tty_with_validation_errors(self):
        """Test __str__ method for TTY with validation errors (colored)"""
        errors = [
            {"detail": "must be positive", "pointer": "#/age"},
            {"detail": "must be valid", "pointer": "#/email"},
        ]

        exc = TwilioServiceException(
            type_uri="https://www.twilio.com/docs/api/errors/20001",
            title="Validation Failed",
            status=422,
            code=20001,
            errors=errors,
            method="POST",
            uri="/api/v1/users",
        )

        import sys

        original_stderr = sys.stderr
        try:
            sys.stderr = Mock()
            sys.stderr.isatty = Mock(return_value=True)

            result = str(exc)

            self.assertIn("Validation Errors", result)
            self.assertIn("#/age", result)
            self.assertIn("must be positive", result)
            self.assertIn("#/email", result)
            self.assertIn("must be valid", result)
        finally:
            sys.stderr = original_stderr

    def test_string_representation_tty_no_uri(self):
        """Test __str__ method when uri is empty"""
        exc = TwilioServiceException(
            type_uri="https://www.twilio.com/docs/api/errors/20001",
            title="Error",
            status=400,
            code=20001,
            method="GET",
            uri="",
        )

        import sys

        original_stderr = sys.stderr
        try:
            sys.stderr = Mock()
            sys.stderr.isatty = Mock(return_value=True)

            result = str(exc)

            self.assertIn("(no URI)", result)
        finally:
            sys.stderr = original_stderr

    def test_validation_errors_with_missing_fields(self):
        """Test validation errors with missing detail or pointer fields"""
        errors = [
            {"detail": "error detail"},  # missing pointer
            {"pointer": "#/field"},  # missing detail
            {},  # both missing
        ]

        exc = TwilioServiceException(
            type_uri="https://www.twilio.com/docs/api/errors/20001",
            title="Validation Failed",
            status=422,
            code=20001,
            errors=errors,
        )

        import sys

        original_stderr = sys.stderr
        try:
            # Test non-TTY output
            sys.stderr = Mock()
            sys.stderr.isatty = Mock(return_value=False)

            result = str(exc)
            # Should handle missing fields gracefully
            self.assertIn("Validation errors", result)
        finally:
            sys.stderr = original_stderr

    def test_multiple_validation_errors(self):
        """Test with multiple validation errors"""
        errors = [
            {"detail": "Field is required", "pointer": "#/firstName"},
            {"detail": "Must be at least 18", "pointer": "#/age"},
            {"detail": "Invalid format", "pointer": "#/phoneNumber"},
            {"detail": "Must be unique", "pointer": "#/email"},
        ]

        exc = TwilioServiceException(
            type_uri="https://www.twilio.com/docs/api/errors/20001",
            title="Validation Failed",
            status=422,
            code=20001,
            errors=errors,
        )

        self.assertEqual(len(exc.errors), 4)
        self.assertEqual(exc.errors[2]["pointer"], "#/phoneNumber")
        self.assertEqual(exc.errors[3]["detail"], "Must be unique")

    def test_exception_as_parent_class(self):
        """Test that TwilioServiceException is a proper exception"""
        exc = TwilioServiceException(
            type_uri="https://www.twilio.com/docs/api/errors/20001",
            title="Error",
            status=400,
            code=20001,
        )

        self.assertIsInstance(exc, Exception)
        self.assertIsInstance(exc, TwilioException)

    def test_exception_can_be_raised_and_caught(self):
        """Test that TwilioServiceException can be raised and caught"""
        with self.assertRaises(TwilioServiceException) as context:
            raise TwilioServiceException(
                type_uri="https://www.twilio.com/docs/api/errors/20001",
                title="Test Error",
                status=400,
                code=20001,
            )

        self.assertEqual(context.exception.title, "Test Error")
        self.assertEqual(context.exception.code, 20001)
