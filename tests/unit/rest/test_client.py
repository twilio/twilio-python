import unittest
from twilio.rest import (
    TwilioClient,
    TwilioRestClient,
    TwilioIpMessagingClient,
    TwilioLookupsClient,
    TwilioMonitorClient,
    TwilioPricingClient,
    TwilioTaskRouterClient,
    TwilioTrunkingClient,
)
from twilio.base.obsolete import ObsoleteException


class TestDummyClients(unittest.TestCase):
    def test_obsolete_exception_twilioclient(self):
        self.assertRaises(ObsoleteException, TwilioClient,
                          "Expected raised ObsoleteException")

    def test_obsolete_exception_twiliorestclient(self):
        self.assertRaises(ObsoleteException, TwilioRestClient,
                          "Expected raised ObsoleteException")

    def test_obsolete_exception_twilioipmessagingclient(self):
        self.assertRaises(ObsoleteException, TwilioIpMessagingClient,
                          "Expected raised ObsoleteException")

    def test_obsolete_exception_twiliolookupsclient(self):
        self.assertRaises(ObsoleteException, TwilioLookupsClient,
                          "Expected raised ObsoleteException")

    def test_obsolete_exception_twiliomonitorclient(self):
        self.assertRaises(ObsoleteException, TwilioMonitorClient,
                          "Expected raised ObsoleteException")

    def test_obsolete_exception_twiliopricingclient(self):
        self.assertRaises(ObsoleteException, TwilioPricingClient,
                          "Expected raised ObsoleteException")

    def test_obsolete_exception_twiliotaskrouterclient(self):
        self.assertRaises(ObsoleteException, TwilioTaskRouterClient,
                          "Expected raised ObsoleteException")

    def test_obsolete_exception_twiliotrunkingclient(self):
        self.assertRaises(ObsoleteException, TwilioTrunkingClient,
                          "Expected raised ObsoleteException")
