import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
from datetime import date
from mock import patch, Mock
from twilio.rest.resources import Conferences


class ConferenceTest(unittest.TestCase):

    def setUp(self):
        self.resource = Conferences("foo", ("sid", "token"))

    def test_list(self):
        self.resource.get_instances = Mock()
        self.resource.list()
        self.resource.get_instances.assert_called_with(params={})

    def test_list_after(self):
        self.resource.get_instances = Mock()
        self.resource.list(created_after=date(2011, 1, 1))
        self.resource.get_instances.assert_called_with(params={
            "DateCreated>": "2011-01-01"})

    def test_list_on(self):
        self.resource.get_instances = Mock()
        self.resource.list(created=date(2011, 1, 1))
        self.resource.get_instances.assert_called_with(params={
            "DateCreated": "2011-01-01"})

    def test_list_before(self):
        self.resource.get_instances = Mock()
        self.resource.list(created_before=date(2011, 1, 1))
        self.resource.get_instances.assert_called_with(params={
            "DateCreated<": "2011-01-01"})



