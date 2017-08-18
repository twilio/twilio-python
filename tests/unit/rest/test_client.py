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


class TestDummyClients(unittest.TestCase):
    def test_deprecation_error_twilioclient(self):
        self.assertRaises(DeprecationWarning, TwilioClient,
                          "Expected raised DeprecationWarning")

    def test_deprecation_error_twiliorestclient(self):
        self.assertRaises(DeprecationWarning, TwilioRestClient,
                          "Expected raised DeprecationWarning")

    def test_deprecation_error_twilioipmessagingclient(self):
        self.assertRaises(DeprecationWarning, TwilioIpMessagingClient,
                          "Expected raised DeprecationWarning")

    def test_deprecation_error_twiliolookupsclient(self):
        self.assertRaises(DeprecationWarning, TwilioLookupsClient,
                          "Expected raised DeprecationWarning")

    def test_deprecation_error_twiliomonitorclient(self):
        self.assertRaises(DeprecationWarning, TwilioMonitorClient,
                          "Expected raised DeprecationWarning")

    def test_deprecation_error_twiliopricingclient(self):
        self.assertRaises(DeprecationWarning, TwilioPricingClient,
                          "Expected raised DeprecationWarning")

    def test_deprecation_error_twiliotaskrouterclient(self):
        self.assertRaises(DeprecationWarning, TwilioTaskRouterClient,
                          "Expected raised DeprecationWarning")

    def test_deprecation_error_twiliotrunkingclient(self):
        self.assertRaises(DeprecationWarning, TwilioTrunkingClient,
                          "Expected raised DeprecationWarning")
