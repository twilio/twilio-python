import json
import unittest
from unittest.mock import Mock

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.api_v1_version import ApiV1Version
from twilio.base.exceptions import TwilioRestException, TwilioServiceException
from twilio.base.page import Page
from twilio.base.version import Version
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


class ExceptionTestCase(unittest.TestCase):
    """Test cases for ApiV1Version.exception() method"""

    def test_exception_rfc9457_compliant(self):
        """Test that RFC-9457 compliant errors create TwilioServiceException"""
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

        error_payload = json.loads(response.text)
        exception = ApiV1Version.exception(
            method="POST", uri="/test", response=response, error_payload=error_payload
        )

        self.assertIsInstance(exception, TwilioServiceException)
        self.assertEqual(exception.type, "https://www.twilio.com/docs/api/errors/20001")
        self.assertEqual(exception.title, "Invalid parameter")
        self.assertEqual(exception.status, 400)
        self.assertEqual(exception.code, 20001)
        self.assertEqual(exception.detail, "The 'PhoneNumber' parameter is required.")
        self.assertEqual(
            exception.instance, "/api/v1/accounts/AC123/calls/CA456"
        )
        self.assertEqual(exception.method, "POST")
        self.assertEqual(exception.uri, "/test")

    def test_exception_rfc9457_with_validation_errors(self):
        """Test RFC-9457 error with validation errors array"""
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

        error_payload = json.loads(response.text)
        exception = ApiV1Version.exception(
            method="POST", uri="/test", response=response, error_payload=error_payload
        )

        self.assertIsInstance(exception, TwilioServiceException)
        self.assertEqual(exception.title, "Validation failed")
        self.assertEqual(len(exception.errors), 2)
        self.assertEqual(exception.errors[0]["detail"], "must be a positive integer")
        self.assertEqual(exception.errors[0]["pointer"], "#/age")
        self.assertEqual(
            exception.errors[1]["detail"], "must be 'green', 'red' or 'blue'"
        )
        self.assertEqual(exception.errors[1]["pointer"], "#/profile/color")

    def test_exception_rfc9457_minimal(self):
        """Test RFC-9457 with only required fields"""
        response = Mock(spec=Response)
        response.status_code = 404
        response.text = """{
            "type": "https://www.twilio.com/docs/api/errors/20404",
            "title": "Resource not found",
            "status": 404,
            "code": 20404
        }"""

        error_payload = json.loads(response.text)
        exception = ApiV1Version.exception(
            method="GET", uri="/test", response=response, error_payload=error_payload
        )

        self.assertIsInstance(exception, TwilioServiceException)
        self.assertEqual(exception.title, "Resource not found")
        self.assertIsNone(exception.detail)
        self.assertIsNone(exception.instance)
        self.assertEqual(exception.errors, [])

    def test_exception_with_error_payload_parameter(self):
        """Test passing error_payload directly to exception method"""
        response = Mock(spec=Response)
        response.status_code = 400
        response.text = "This should be ignored"

        error_payload = {
            "type": "https://www.twilio.com/docs/api/errors/20001",
            "title": "Invalid parameter",
            "status": 400,
            "code": 20001,
            "detail": "Pre-parsed error payload"
        }

        exception = ApiV1Version.exception(
            method="POST",
            uri="/test",
            response=response,
            error_payload=error_payload
        )

        self.assertIsInstance(exception, TwilioServiceException)
        self.assertEqual(exception.title, "Invalid parameter")
        self.assertEqual(exception.detail, "Pre-parsed error payload")


class ApiV1VersionParseTestCase(unittest.TestCase):
    """Test cases for ApiV1Version._parse_* methods with RFC-9457 error handling"""

    def test_parse_fetch_with_rfc9457_error(self):
        """Test that _parse_fetch raises TwilioServiceException for RFC-9457 errors"""
        # Create a mock domain
        domain = Mock()
        service_version = ApiV1Version(domain, "v1")

        response = Mock(spec=Response)
        response.status_code = 404
        response.text = """{
            "type": "https://www.twilio.com/docs/api/errors/20404",
            "title": "Resource not found",
            "status": 404,
            "code": 20404,
            "detail": "The requested resource does not exist"
        }"""

        with self.assertRaises(TwilioServiceException) as context:
            service_version._parse_fetch("GET", "/test", response)

        exception = context.exception
        self.assertEqual(exception.title, "Resource not found")
        self.assertEqual(exception.detail, "The requested resource does not exist")
        self.assertEqual(exception.status, 404)

    def test_parse_update_with_rfc9457_error(self):
        """Test that _parse_update raises TwilioServiceException for RFC-9457 errors"""
        domain = Mock()
        service_version = ApiV1Version(domain, "v1")

        response = Mock(spec=Response)
        response.status_code = 400
        response.text = """{
            "type": "https://www.twilio.com/docs/api/errors/20001",
            "title": "Invalid parameter",
            "status": 400,
            "code": 20001
        }"""

        with self.assertRaises(TwilioServiceException) as context:
            service_version._parse_update("PUT", "/test", response)

        exception = context.exception
        self.assertEqual(exception.title, "Invalid parameter")

    def test_parse_delete_with_rfc9457_error(self):
        """Test that _parse_delete raises TwilioServiceException for RFC-9457 errors"""
        domain = Mock()
        service_version = ApiV1Version(domain, "v1")

        response = Mock(spec=Response)
        response.status_code = 403
        response.text = """{
            "type": "https://www.twilio.com/docs/api/errors/20403",
            "title": "Forbidden",
            "status": 403,
            "code": 20403,
            "detail": "You do not have permission to delete this resource"
        }"""

        with self.assertRaises(TwilioServiceException) as context:
            service_version._parse_delete("DELETE", "/test", response)

        exception = context.exception
        self.assertEqual(exception.title, "Forbidden")
        self.assertEqual(exception.detail, "You do not have permission to delete this resource")

    def test_parse_create_with_rfc9457_error(self):
        """Test that _parse_create raises TwilioServiceException for RFC-9457 errors"""
        domain = Mock()
        service_version = ApiV1Version(domain, "v1")

        response = Mock(spec=Response)
        response.status_code = 422
        response.text = """{
            "type": "https://www.twilio.com/docs/api/errors/20001",
            "title": "Validation failed",
            "status": 422,
            "code": 20001,
            "errors": [
                {"detail": "must be a valid phone number", "pointer": "#/to"}
            ]
        }"""

        with self.assertRaises(TwilioServiceException) as context:
            service_version._parse_create("POST", "/test", response)

        exception = context.exception
        self.assertEqual(exception.title, "Validation failed")
        self.assertEqual(len(exception.errors), 1)
        self.assertEqual(exception.errors[0]["detail"], "must be a valid phone number")

    def test_parse_fetch_success(self):
        """Test that _parse_fetch returns data on success"""
        domain = Mock()
        service_version = ApiV1Version(domain, "v1")

        response = Mock(spec=Response)
        response.status_code = 200
        response.text = '{"data": "success"}'

        result = service_version._parse_fetch("GET", "/test", response)
        self.assertEqual(result, {"data": "success"})

    def test_parse_delete_success(self):
        """Test that _parse_delete returns True on success"""
        domain = Mock()
        service_version = ApiV1Version(domain, "v1")

        response = Mock(spec=Response)
        response.status_code = 204
        response.text = ""

        result = service_version._parse_delete("DELETE", "/test", response)
        self.assertTrue(result)
