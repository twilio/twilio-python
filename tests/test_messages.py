import six
if six.PY3:
    import unittest
else:
    import unittest2 as unittest

from datetime import date
from mock import Mock
from six import u
from twilio.rest.resources import Messages

DEFAULT = {
    'From': None,
    'DateSent<': None,
    'DateSent>': None,
    'DateSent': None,
}


class MessageTest(unittest.TestCase):

    def setUp(self):
        self.resource = Messages("foo", ("sid", "token"))
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

    def test_create(self):
        self.resource.create_instance = Mock()
        self.resource.create(
            from_='+14155551234',
            to='+14155556789',
            body=u('ahoy hoy'),
        )
        self.resource.create_instance.assert_called_with(
            {
                'from': '+14155551234',
                'to': '+14155556789',
                'body': u('ahoy hoy'),
            },
        )
