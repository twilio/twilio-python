import unittest
import datetime
from twilio.rest import serialize


class Iso8601DateTestCase(unittest.TestCase):

    def test_datetime(self):
        value = datetime.datetime(2015, 01, 02, 12, 0, 0, 0)
        actual = serialize.iso8601_date(value)
        self.assertEqual('2015-01-02', actual)

    def test_datetime_without_time(self):
        value = datetime.datetime(2015, 01, 02)
        actual = serialize.iso8601_date(value)
        self.assertEqual('2015-01-02', actual)

    def test_date(self):
        value = datetime.date(2015, 01, 02)
        actual = serialize.iso8601_date(value)
        self.assertEqual('2015-01-02', actual)

    def test_str(self):
        actual = serialize.iso8601_date('2015-01-02')
        self.assertEqual('2015-01-02', actual)

