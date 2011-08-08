import unittest
from mock import Mock
from twilio import TwilioException
from twilio.rest.resources import Application
from twilio.rest.resources import Applications


class AvailablePhoneNumberTest(unittest.TestCase):

    def setUp(self):
        self.parent = Mock()
        self.resource = Applications("http://api.twilio.com", ("user", "pass"))

    def test_update(self):
        request = Mock()
        request.return_value = (Mock(), {"sid": "123"})
        self.resource.request = request

        self.resource.update("123", voice_url="hey")

        uri = "http://api.twilio.com/Applications/123"
        request.assert_called_with("POST", uri, data={"VoiceUrl":"hey"})

    def test_create(self):
        request = Mock()
        request.return_value = (request, {"sid": "123"})
        request.status_code = 201

        self.resource.request = request

        self.resource.create(friendly_name="hey")

        uri = "http://api.twilio.com/Applications"
        request.assert_called_with("POST", uri, data={"FriendlyName":"hey"})
