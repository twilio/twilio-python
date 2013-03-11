from __future__ import with_statement
import six
if six.PY3:
    import unittest
else:
    import unittest2 as unittest

from mock import Mock, patch
from twilio.rest.resources import AuthorizedConnectApps
from twilio.rest.resources import AuthorizedConnectApp


class AuthorizedConnectAppTest(unittest.TestCase):

    def setUp(self):
        self.parent = Mock()
        self.uri = "/base"
        self.auth = ("AC123", "token")
        self.resource = AuthorizedConnectApps(self.uri, self.auth)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_get(self, mock):
        mock.return_value = Mock()
        mock.return_value.content = '{"connect_app_sid": "SID"}'

        self.resource.get("SID")
        mock.assert_called_with("GET", "/base/AuthorizedConnectApps/SID",
                                auth=self.auth)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list(self, mock):
        mock.return_value = Mock()
        mock.return_value.content = '{"authorized_connect_apps": []}'

        self.resource.list()
        mock.assert_called_with("GET", "/base/AuthorizedConnectApps",
                                params={}, auth=self.auth)

    def test_load(self):
        instance = AuthorizedConnectApp(Mock(), "sid")
        instance.load({
            "connect_app_sid": "SID",
            "account_sid": "AC8dfe2f2358cf421cb6134cf6f217c6a3",
            "permissions": ["get-all"],
            "connect_app_friendly_name": "foo",
            "connect_app_description": "bat",
            "connect_app_company_name": "bar",
            "connect_app_homepage_url": "http://www.google.com",
            "uri": "/2010-04-01/Accounts/",
        })

        self.assertEquals(instance.permissions, ["get-all"])
        self.assertEquals(instance.sid, "SID")
        self.assertEquals(instance.friendly_name, "foo")
        self.assertEquals(instance.description, "bat")
        self.assertEquals(instance.homepage_url, "http://www.google.com")
        self.assertEquals(instance.company_name, "bar")

    def test_delete(self):
        with self.assertRaises(AttributeError):
            self.resource.delete()

    def test_create(self):
        with self.assertRaises(AttributeError):
            self.resource.create()

    def test_update(self):
        with self.assertRaises(AttributeError):
            self.resource.update()
