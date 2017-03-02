import datetime
import unittest
from decimal import Decimal

import pytz

from twilio.base import deserialize


class Iso8601DateTestCase(unittest.TestCase):

    def test_parsable(self):
        actual = deserialize.iso8601_date('2015-01-02')
        expected = datetime.date(2015, 1, 2)
        self.assertEqual(expected, actual)

    def test_not_parsable(self):
        actual = deserialize.iso8601_date('not-a-date')
        self.assertEqual('not-a-date', actual)


class Iso8601DateTimeTestCase(unittest.TestCase):

    def test_parsable(self):
        actual = deserialize.iso8601_datetime('2015-01-02T03:04:05Z')
        expected = datetime.datetime(2015, 1, 2, 3, 4, 5, 0, pytz.utc)
        self.assertEqual(expected, actual)

    def test_not_parsable(self):
        actual = deserialize.iso8601_datetime('not-a-datetime')
        self.assertEqual('not-a-datetime', actual)


class DecimalTestCase(unittest.TestCase):

    def test_none(self):
        self.assertEqual(None, deserialize.decimal(None))

    def test_empty_string(self):
        self.assertEqual('', deserialize.decimal(''))

    def test_zero_string(self):
        self.assertEqual(Decimal('0.0000'), deserialize.decimal('0.0000'))

    def test_negative_string(self):
        self.assertEqual(Decimal('-0.0123'), deserialize.decimal('-0.0123'))

    def test_positive_string(self):
        self.assertEqual(Decimal('0.0123'), deserialize.decimal('0.0123'))

    def test_zero(self):
        self.assertEqual(0, deserialize.decimal(0))

    def test_negative(self):
        self.assertEqual(-0.0123, deserialize.decimal(-0.0123))

    def test_positive(self):
        self.assertEqual(0.0123, deserialize.decimal(0.0123))


class IntegerTestCase(unittest.TestCase):

    def test_none(self):
        self.assertEqual(None, deserialize.integer(None))

    def test_empty_string(self):
        self.assertEqual('', deserialize.integer(''))

    def test_zero_string(self):
        self.assertEqual(0, deserialize.integer('0'))

    def test_negative_string(self):
        self.assertEqual(-1, deserialize.integer('-1'))

    def test_positive_string(self):
        self.assertEqual(1, deserialize.integer('1'))

    def test_zero(self):
        self.assertEqual(0, deserialize.integer(0))

    def test_negative(self):
        self.assertEqual(-1, deserialize.integer(-1))

    def test_positive(self):
        self.assertEqual(1, deserialize.integer(1))




