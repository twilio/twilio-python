from datetime import date
import unittest

from mock import patch
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
        with patch.object(self.resource, 'get_instances') as mock:
            self.resource.list(date_sent=date(2011, 1, 1))
            self.params['DateSent'] = "2011-01-01"
            mock.assert_called_with(self.params)

    def test_list_after(self):
        with patch.object(self.resource, 'get_instances') as mock:
            self.resource.list(after=date(2011, 1, 1))
            self.params['DateSent>'] = "2011-01-01"
            mock.assert_called_with(self.params)

    def test_list_before(self):
        with patch.object(self.resource, 'get_instances') as mock:
            self.resource.list(before=date(2011, 1, 1))
            self.params['DateSent<'] = "2011-01-01"
            mock.assert_called_with(self.params)

    def test_create(self):
        with patch.object(self.resource, 'create_instance') as mock:
            self.resource.create(
                from_='+14155551234',
                to='+14155556789',
                body=u('ahoy hoy'),
            )
            mock.assert_called_with(
                {
                    'from': '+14155551234',
                    'to': '+14155556789',
                    'body': u('ahoy hoy'),
                },
            )

    def test_delete(self):
        with patch.object(self.resource, 'delete_instance') as mock:
            self.resource.delete('MM123')
            mock.assert_called_with('MM123')

    def test_redact(self):
        with patch.object(self.resource, 'update_instance') as mock:
            self.resource.redact('MM123')
            mock.assert_called_with('MM123', {'Body': ''})
