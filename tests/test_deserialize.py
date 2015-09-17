import unittest
import datetime
import pytz
from twilio.rest import deserialize


class Iso8601DateTimeTestCase(unittest.TestCase):

    def test_parsable(self):
        actual = deserialize.iso8601_datetime('2015-01-02T03:04:05Z')
        expected = datetime.datetime(2015, 1, 2, 3, 4, 5, 0, pytz.utc)
        self.assertEqual(expected, actual)

    def test_not_parsable(self):
        actual = deserialize.iso8601_datetime('not-a-date')
        self.assertEqual('not-a-date', actual)


