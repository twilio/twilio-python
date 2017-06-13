import unittest

from nose.tools import raises
from six import text_type

from twilio.twiml import format_language, TwiMLException, TwiML


class TwilioTest(unittest.TestCase):
    def strip(self, xml):
        return text_type(xml)

    @raises(TwiMLException)
    def test_append_fail(self):
        t = TwiML()
        t.append('foobar')

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
