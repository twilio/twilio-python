import unittest

import time
from nose.tools import assert_true, assert_equal

from twilio.jwt import Jwt
from twilio.jwt.client import ClientCapabilityToken, ScopeURI


class ClientCapabilityTokenTest(unittest.TestCase):

    def assertIn(self, foo, bar, msg=None):
        """backport for 2.6"""
        return assert_true(foo in bar, msg=(msg or "%s not found in %s" % (foo, bar)))

    def now(self):
        return int(time.time())

    def test_no_permissions(self):
        token = ClientCapabilityToken("AC123", "XXXXX")
        assert_equal(len(token._generate_payload()), 1)
        assert_equal(token._generate_payload()["scope"], '')

    def test_inbound_permissions(self):
        token = ClientCapabilityToken("AC123", "XXXXX")
        token.allow_client_incoming("andy")

        eurl = "scope:client:incoming?clientName=andy"
        assert_equal(len(token._generate_payload()), 1)
        assert_equal(token._generate_payload()['scope'], eurl)

    def test_outbound_permissions(self):
        token = ClientCapabilityToken("AC123", "XXXXX")
        token.allow_client_outgoing("AP123")

        eurl = "scope:client:outgoing?appSid=AP123"

        assert_equal(len(token._generate_payload()), 1)
        self.assertIn(eurl, token._generate_payload()['scope'])

    def test_outbound_permissions_params(self):
        token = ClientCapabilityToken("AC123", "XXXXX")
        token.allow_client_outgoing("AP123", foobar=3)

        eurl = "scope:client:outgoing?appParams=foobar%3D3&appSid=AP123"
        assert_equal(token.payload["scope"], eurl)

    def test_events(self):
        token = ClientCapabilityToken("AC123", "XXXXX")
        token.allow_event_stream()

        event_uri = "scope:stream:subscribe?path=%2F2010-04-01%2FEvents"
        assert_equal(token.payload["scope"], event_uri)

    def test_events_with_filters(self):
        token = ClientCapabilityToken("AC123", "XXXXX")
        token.allow_event_stream(foobar="hey")

        event_uri = "scope:stream:subscribe?params=foobar%3Dhey&path=%2F2010-04-01%2FEvents"
        assert_equal(token.payload["scope"], event_uri)

    def test_decode(self):
        token = ClientCapabilityToken("AC123", "XXXXX")
        token.allow_client_outgoing("AP123", foobar=3)
        token.allow_client_incoming("andy")
        token.allow_event_stream()

        outgoing_uri = "scope:client:outgoing?appParams=foobar%3D3&appSid=AP123&clientName=andy"
        incoming_uri = "scope:client:incoming?clientName=andy"
        event_uri = "scope:stream:subscribe?path=%2F2010-04-01%2FEvents"

        result = Jwt.from_jwt(token.to_jwt(), "XXXXX")
        scope = result.payload["scope"].split(" ")

        self.assertIn(outgoing_uri, scope)
        self.assertIn(incoming_uri, scope)
        self.assertIn(event_uri, scope)

    def test_encode_full_payload(self):
        token = ClientCapabilityToken("AC123", "XXXXX")
        token.allow_event_stream(foobar="hey")
        token.allow_client_incoming("andy")

        event_uri = "scope:stream:subscribe?params=foobar%3Dhey&path=%2F2010-04-01%2FEvents"
        incoming_uri = "scope:client:incoming?clientName=andy"

        self.assertIn(event_uri, token.payload["scope"])
        self.assertIn(incoming_uri, token.payload["scope"])
        self.assertEqual(token.payload['iss'], 'AC123')
        self.assertGreaterEqual(token.payload['exp'], self.now())

    def test_pass_scopes_in_constructor(self):
        token = ClientCapabilityToken('AC123', 'XXXXX', allow_client_outgoing={
            'application_sid': 'AP123',
            'param1': 'val1'
        })
        outgoing_uri = "scope:client:outgoing?appParams=param1%3Dval1&appSid=AP123"
        result = Jwt.from_jwt(token.to_jwt(), "XXXXX")
        self.assertEqual(outgoing_uri, result.payload["scope"])


class ScopeURITest(unittest.TestCase):

    def test_to_payload_no_params(self):
        scope_uri = ScopeURI('service', 'godmode')
        self.assertEqual('scope:service:godmode', scope_uri.to_payload())

    def test_to_payload_with_params(self):
        scope_uri = ScopeURI('service', 'godmode', {'key': 'val'})
        self.assertEqual('scope:service:godmode?key=val', scope_uri.to_payload())

    def test_to_payload_with_params_encoded(self):
        scope_uri = ScopeURI('service', 'godmode', {'key with space': 'val'})
        self.assertEqual('scope:service:godmode?key+with+space=val', scope_uri.to_payload())
