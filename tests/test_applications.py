import json
import unittest

from mock import Mock, patch

from twilio.rest.resources import Applications, Application


class ApplicationsTest(unittest.TestCase):
    def setUp(self):
        self.parent = Mock()
        self.auth = ("user", "pass")
        self.resource = Applications("http://api.twilio.com", self.auth)

    def test_create_application_sms_url_method(self):
        self.resource.create_instance = Mock()
        self.resource.create(sms_method="hey")
        self.resource.create_instance.assert_called_with({"sms_method": "hey"})

    def test_create_application_sms_url(self):
        self.resource.create_instance = Mock()
        self.resource.create(sms_url="hey")
        self.resource.create_instance.assert_called_with({"sms_url": "hey"})

    def test_update_application_sms_url_method(self):
        self.resource.update_instance = Mock()
        self.resource.update("123", sms_method="hey")
        self.resource.update_instance.assert_called_with(
            "123", {"sms_method": "hey"})

    def test_update_application_sms_url(self):
        self.resource.update_instance = Mock()
        self.resource.update("123", sms_url="hey")
        self.resource.update_instance.assert_called_with(
            "123", {"sms_url": "hey"})

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_update(self, mock):
        response = Mock()
        response.status_code = 200
        response.content = json.dumps({"sid": "123"})
        mock.return_value = response

        self.resource.update("123", voice_url="hey").execute()

        uri = "http://api.twilio.com/Applications/123"
        mock.assert_called_with("POST", uri, data={"VoiceUrl": "hey"},
                                auth=self.auth, use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_create(self, mock):
        response = Mock()
        response.status_code = 201
        response.content = json.dumps({"sid": "123"})
        mock.return_value = response

        self.resource.create(friendly_name="hey").execute()

        uri = "http://api.twilio.com/Applications"
        mock.assert_called_with("POST", uri, data={"FriendlyName": "hey"},
                                auth=self.auth, use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_delete(self, mock):
        """ Deleting an application should work """
        response = Mock()
        response.status_code = 204
        response.content = ""
        mock.return_value = response

        app = Application(self.resource, "AP123")
        app.delete().execute()
        uri = "http://api.twilio.com/Applications/AP123"
        mock.assert_called_with("DELETE", uri,
                                auth=self.auth, use_json_extension=True)
