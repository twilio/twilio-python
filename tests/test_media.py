from datetime import date
import unittest

from mock import Mock
from nose.tools import assert_equal

from twilio.rest.resources import MediaList

DEFAULT = {
    'DateCreated<': None,
    'DateCreated>': None,
    'DateCreated': None,
}


class MediaTest(unittest.TestCase):

    def setUp(self):
        self.resource = MediaList("foo", ("sid", "token"))
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

    def test_call(self):
        base_uri = self.resource.base_uri
        message_media = self.resource('MM123')
        assert_equal(message_media.base_uri, "%s/Messages/%s" % (base_uri, 'MM123'))
