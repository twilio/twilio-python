from __future__ import with_statement
import six
if six.PY3:
    import unittest
else:
    import unittest2 as unittest

from mock import Mock, patch
from twilio.rest.resources import ConnectApps


class ConnectAppTest(unittest.TestCase):

    def setUp(self):
        self.parent = Mock()
        self.uri = "/base"
        self.auth = ("AC123", "token")
        self.resource = ConnectApps(self.uri, self.auth)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_get(self, mock):
        mock.return_value = Mock()
        mock.return_value.content = '{"sid": "SID"}'

        self.resource.get("SID")
        mock.assert_called_with("GET", "/base/ConnectApps/SID",
            auth=self.auth)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_with_paging(self, mock):
        mock.return_value = Mock()
        mock.return_value.content = '{"connect_apps": []}'

        self.resource.list(page=1, page_size=50)
        mock.assert_called_with("GET", "/base/ConnectApps",
                params={"Page": 1, "PageSize": 50}, auth=self.auth)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list(self, mock):
        mock.return_value = Mock()
        mock.return_value.content = '{"connect_apps": []}'

        self.resource.list()
        mock.assert_called_with("GET", "/base/ConnectApps",
            params={}, auth=self.auth)

    def test_create(self):
        with self.assertRaises(AttributeError):
            self.resource.create()

    def test_delete(self):
        with self.assertRaises(AttributeError):
            self.resource.delete()

    def test_update(self):
        with self.assertRaises(AttributeError):
            self.resource.update()
