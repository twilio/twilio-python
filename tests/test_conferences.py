from datetime import date
import unittest

from mock import Mock
from twilio.rest.resources import Conferences

DEFAULT = {
    'DateUpdated<': None,
    'DateUpdated>': None,
    'DateUpdated': None,
    'DateCreated<': None,
    'DateCreated>': None,
    'DateCreated': None,
}


class ConferenceTest(unittest.TestCase):

    def setUp(self):
        self.resource = Conferences("foo", ("sid", "token"))
        self.params = DEFAULT.copy()

    def test_list(self):
        self.resource.get_instances = Mock()
        self.resource.list()
        self.resource.get_instances.assert_called_with(self.params)

    def test_list_after(self):
        self.resource.get_instances = Mock()
        self.resource.list(created_after=date(2011, 1, 1))
        self.params["DateCreated>"] = "2011-01-01"
        self.resource.get_instances.assert_called_with(self.params)

    def test_list_on(self):
        self.resource.get_instances = Mock()
        self.resource.list(created=date(2011, 1, 1))
        self.params["DateCreated"] = "2011-01-01"
        self.resource.get_instances.assert_called_with(self.params)

    def test_list_before(self):
        self.resource.get_instances = Mock()
        self.resource.list(created_before=date(2011, 1, 1))
        self.params["DateCreated<"] = "2011-01-01"
        self.resource.get_instances.assert_called_with(self.params)
