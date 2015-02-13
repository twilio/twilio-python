from __future__ import with_statement
import unittest

from mock import Mock, patch
from nose.tools import assert_equal

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
                                auth=self.auth, use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list(self, mock):
        mock.return_value = Mock()
        mock.return_value.content = '{"authorized_connect_apps": []}'

        self.resource.list()
        mock.assert_called_with("GET", "/base/AuthorizedConnectApps",
                                params={}, auth=self.auth,
                                use_json_extension=True)

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

        assert_equal(instance.permissions, ["get-all"])
        assert_equal(instance.sid, "SID")
        assert_equal(instance.friendly_name, "foo")
        assert_equal(instance.description, "bat")
        assert_equal(instance.homepage_url, "http://www.google.com")
        assert_equal(instance.company_name, "bar")

    def test_delete(self):
        self.assertRaises(AttributeError, getattr, self.resource, 'delete')

    def test_create(self):
        self.assertRaises(AttributeError, getattr, self.resource, 'create')

    def test_update(self):
        self.assertRaises(AttributeError, getattr, self.resource, 'update')
