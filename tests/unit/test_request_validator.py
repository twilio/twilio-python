# -*- coding: utf-8 -*-
import unittest

from django.conf import settings
from django.http import QueryDict
from multidict import MultiDict

from twilio.request_validator import RequestValidator


class ValidationTest(unittest.TestCase):
    def setUp(self):
        if not settings.configured:
            settings.configure()

        token = "12345"
        self.validator = RequestValidator(token)

        self.uri = "https://mycompany.com/myapp.php?foo=1&bar=2"
        self.params = {
            "CallSid": "CA1234567890ABCDE",
            "Digits": "1234",
            "From": "+14158675309",
            "To": "+18005551212",
            "Caller": "+14158675309",
        }
        self.expected = "RSOYDt4T1cUTdK1PDd93/VVr8B8="
        self.body = '{"property": "value", "boolean": true}'
        self.bodyHash = (
            "0a1ff7634d9ab3b95db5c9a2dfe9416e41502b283a80c7cf19632632f96e6620"
        )
        self.uriWithBody = self.uri + "&bodySHA256=" + self.bodyHash
        self.duplicate_expected = "IK+Dwps556ElfBT0I3Rgjkr1wJU="

    def test_compute_signature(self):
        expected = self.expected
        signature = self.validator.compute_signature(self.uri, self.params)
        assert signature == expected

    def test_compute_hash_unicode(self):
        expected = self.bodyHash
        body_hash = self.validator.compute_hash(self.body)

        assert expected == body_hash

    def test_compute_signature_duplicate_multi_dict(self):
        expected = self.duplicate_expected
        params = MultiDict(
            [
                ("Sid", "CA123"),
                ("SidAccount", "AC123"),
                ("Digits", "5678"),  # Ensure keys are sorted.
                ("Digits", "1234"),  # Ensure values are sorted.
                ("Digits", "1234"),  # Ensure duplicates are removed.
            ]
        )
        signature = self.validator.compute_signature(self.uri, params)
        assert signature == expected

    def test_compute_signature_duplicate_query_dict(self):
        expected = self.duplicate_expected
        params = QueryDict(
            "Sid=CA123&SidAccount=AC123&Digits=5678&Digits=1234&Digits=1234",
            encoding="utf-8",
        )
        signature = self.validator.compute_signature(self.uri, params)
        assert signature == expected

    def test_validation(self):
        assert self.validator.validate(self.uri, self.params, self.expected)

    def test_validation_removes_port_on_https(self):
        uri = self.uri.replace(".com", ".com:1234")
        assert self.validator.validate(uri, self.params, self.expected)

    def test_validation_removes_port_on_http(self):
        expected = "Zmvh+3yNM1Phv2jhDCwEM3q5ebU="  # hash of http uri with port 1234
        uri = self.uri.replace(".com", ".com:1234").replace("https", "http")
        assert self.validator.validate(uri, self.params, expected)

    def test_validation_adds_port_on_https(self):
        expected = "kvajT1Ptam85bY51eRf/AJRuM3w="  # hash of uri with port 443
        assert self.validator.validate(self.uri, self.params, expected)

    def test_validation_adds_port_on_http(self):
        uri = self.uri.replace("https", "http")
        expected = "0ZXoZLH/DfblKGATFgpif+LLRf4="  # hash of uri with port 80
        assert self.validator.validate(uri, self.params, expected)

    def test_validation_of_body_succeeds(self):
        uri = self.uriWithBody
        is_valid = self.validator.validate(
            uri, self.body, "a9nBmqA0ju/hNViExpshrM61xv4="
        )
        assert is_valid
