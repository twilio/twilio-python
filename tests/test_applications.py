import unittest

from mock import Mock, patch

from twilio.rest.resources import Applications, Application


class ApplicationsTest(unittest.TestCase):
    def setUp(self):
        self.parent = Mock()
        self.resource = Applications("http://api.twilio.com", ("user", "pass"))

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

    def test_update(self):
        request = Mock()
        request.return_value = (Mock(), {"sid": "123"})
        self.resource.request = request

        self.resource.update("123", voice_url="hey")

        uri = "http://api.twilio.com/Applications/123"
        request.assert_called_with("POST", uri, data={"VoiceUrl": "hey"})

    def test_create(self):
        request = Mock()
        request.return_value = (request, {"sid": "123"})
        request.status_code = 201

        self.resource.request = request

        self.resource.create(friendly_name="hey")

        uri = "http://api.twilio.com/Applications"
        request.assert_called_with("POST", uri, data={"FriendlyName": "hey"})

    @patch("twilio.rest.resources.base.Resource.request")
    def test_delete(self, req):
        """ Deleting an application should work """
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        req.return_value = resp, {}

        app = Application(self.resource, "AP123")
        app.delete()
        uri = "http://api.twilio.com/Applications/AP123"
        req.assert_called_with("DELETE", uri)
