from datetime import date
import unittest

from mock import Mock

from twilio.rest.resources import SmsMessages

DEFAULT = {
    'From': None,
    'DateSent<': None,
    'DateSent>': None,
    'DateSent': None,
}


class SmsTest(unittest.TestCase):

    def setUp(self):
        self.resource = SmsMessages("foo", ("sid", "token"))
        self.params = DEFAULT.copy()

    def test_list_on(self):
        self.resource.get_instances = Mock()
        self.resource.list(date_sent=date(2011, 1, 1))
        self.params['DateSent'] = "2011-01-01"
        self.resource.get_instances.assert_called_with(self.params)

    def test_list_after(self):
        self.resource.get_instances = Mock()
        self.resource.list(after=date(2011, 1, 1))
        self.params['DateSent>'] = "2011-01-01"
        self.resource.get_instances.assert_called_with(self.params)

    def test_list_before(self):
        self.resource.get_instances = Mock()
        self.resource.list(before=date(2011, 1, 1))
        self.params['DateSent<'] = "2011-01-01"
        self.resource.get_instances.assert_called_with(self.params)
