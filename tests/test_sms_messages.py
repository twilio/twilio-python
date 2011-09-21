import unittest
from datetime import date
from mock import patch, Mock
from twilio.rest.resources import SmsMessages


class SmsTest(unittest.TestCase):

    def setUp(self):
        self.resource = SmsMessages("foo", ("sid", "token"))

    def test_list_after(self):
        self.resource.get_instances = Mock()
        self.resource.list(after=date(2011, 1, 1))
        self.resource.get_instances.assert_called_with(params={
            "DateSent>": "2011-01-01"})

    def test_list_before(self):
        self.resource.get_instances = Mock()
        self.resource.list(before=date(2011, 1, 1))
        self.resource.get_instances.assert_called_with(params={
            "DateSent<": "2011-01-01"})



