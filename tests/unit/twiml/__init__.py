import unittest

from nose.tools import raises

from twilio.twiml import (
    format_language,
    lower_camel,
    TwiMLException,
    TwiML
)


class TwilioTest(unittest.TestCase):
    def strip(self, xml):
        return str(xml)

    @raises(TwiMLException)
    def test_append_fail(self):
        t = TwiML()
        t.append(12345)

    def test_format_language_none(self):
        language = None
        self.assertEqual(language, format_language(language))

    def test_format_language_valid(self):
        language = 'en-US'
        self.assertEqual(language, format_language(language))

    def test_format_language_coerced(self):
        language = 'EN_us'
        self.assertEqual('en-US', format_language(language))

    @raises(TwiMLException)
    def test_format_language_fail(self):
        format_language('this is invalid')

    def test_lower_camel_empty_string(self):
        self.assertEqual('', lower_camel(''))

    def test_lower_camel_none(self):
        self.assertEqual(None, lower_camel(None))

    def test_lower_camel_single_word(self):
        self.assertEqual('foo', lower_camel('foo'))

    def test_lower_camel_double_word(self):
        self.assertEqual('fooBar', lower_camel('foo_bar'))

    def test_lower_camel_multi_word(self):
        self.assertEqual('fooBarBaz', lower_camel('foo_bar_baz'))

    def test_lower_camel_multi_word_mixed_case(self):
        self.assertEqual('fooBarBaz', lower_camel('foO_Bar_baz'))

    def test_lower_camel_camel_cased(self):
        self.assertEqual('fooBar', lower_camel('fooBar'))
