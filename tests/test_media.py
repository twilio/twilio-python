from datetime import date
import unittest

from mock import Mock
from nose.tools import assert_equal
from twilio.rest.http import HttpClient

from twilio.rest.resources import MediaList

DEFAULT = {
    'DateCreated<': None,
    'DateCreated>': None,
    'DateCreated': None,
}


class MediaTest(unittest.TestCase):

    def setUp(self):
        self.client = HttpClient()
        self.resource = MediaList(self.client, "foo", ("sid", "token"))
        self.params = DEFAULT.copy()

    def test_list_on(self):
        self.resource.get_instances = Mock()
        self.resource.list(date_created=date(2011, 1, 1))
        self.params['DateCreated'] = "2011-01-01"
        self.resource.get_instances.assert_called_with(self.params)

    def test_list_after(self):
        self.resource.get_instances = Mock()
        self.resource.list(after=date(2011, 1, 1))
        self.params['DateCreated>'] = "2011-01-01"
        self.resource.get_instances.assert_called_with(self.params)

    def test_list_before(self):
        self.resource.get_instances = Mock()
        self.resource.list(before=date(2011, 1, 1))
        self.params['DateCreated<'] = "2011-01-01"
        self.resource.get_instances.assert_called_with(self.params)
