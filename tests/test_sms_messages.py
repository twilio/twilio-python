import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
from datetime import date
from mock import patch, Mock
from twilio.rest.resources import SmsMessages


class SmsTest(unittest.TestCase):

    def setUp(self):
        self.resource = SmsMessages("foo", ("sid", "token"))

    def test_list_on(self):
        self.resource.get_instances = Mock()
        self.resource.list(date_sent=date(2011, 1, 1))
        self.resource.get_instances.assert_called_with(params={
            "DateSent": "2011-01-01"})

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



