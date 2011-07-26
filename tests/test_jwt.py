import jwt
import unittest
import urllib
from twilio.util import TwilioCapability

class TokenTest(unittest.TestCase):

    def assertIn(self, foo, bar, msg=None):
        """backport for 2.6"""
        return self.assertTrue(foo in bar, msg=(msg or "%s not found in %s"
            % (foo, bar)))

    def test_no_permissions(self):
        token = TwilioCapability("AC123", "XXXXX")
        payload = token.payload()
        self.assertEquals(len(payload), 1)
        self.assertEquals(payload["scope"], '')

    def test_inbound_permissions(self):
        token = TwilioCapability("AC123", "XXXXX")
        token.allow_client_incoming("andy")
        payload = token.payload()

        eurl = "scope:client:incoming?clientName=andy"
        self.assertEquals(len(payload), 1)
        self.assertEquals(payload['scope'], eurl)

    def test_outbound_permissions(self):
        token = TwilioCapability("AC123", "XXXXX")
        token.allow_client_outgoing("AP123")
        payload = token.payload()

        eurl = "scope:client:outgoing?appSid=AP123"

        self.assertEquals(len(payload), 1)
        self.assertIn(eurl, payload['scope'])

    def test_outbound_permissions_params(self):
        token = TwilioCapability("AC123", "XXXXX")
        token.allow_client_outgoing("AP123", foobar=3)
        payload = token.payload()

        eurl = "scope:client:outgoing?appSid=AP123&appParams=foobar%3D3"
        self.assertEquals(payload["scope"], eurl)

    def test_events(self):
        token = TwilioCapability("AC123", "XXXXX")
        token.allow_event_stream()
        payload = token.payload()

        event_uri = "scope:stream:subscribe?path=%2F2010-04-01%2FEvents"
        self.assertEquals(payload["scope"], event_uri)

    def test_events_with_filters(self):
        token = TwilioCapability("AC123", "XXXXX")
        token.allow_event_stream(foobar="hey")
        payload = token.payload()

        event_uri = "scope:stream:subscribe?path=%2F2010-04-01%2FEvents&params=foobar%3Dhey"
        self.assertEquals(payload["scope"], event_uri)


    def test_decode(self):
        token = TwilioCapability("AC123", "XXXXX")
        token.allow_client_outgoing("AP123", foobar=3)
        token.allow_client_incoming("andy")
        token.allow_event_stream()

        outgoing_uri = "scope:client:outgoing?appSid=AP123&appParams=foobar%3D3&clientName=andy"
        incoming_uri = "scope:client:incoming?clientName=andy"
        event_uri = "scope:stream:subscribe?path=%2F2010-04-01%2FEvents"

        result = jwt.decode(token.generate(), "XXXXX")
        scope = result["scope"].split(" ")

        self.assertIn(outgoing_uri, scope)
        self.assertIn(incoming_uri, scope)
        self.assertIn(event_uri, scope)
