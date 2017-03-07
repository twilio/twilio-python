import unittest

from nose.tools import raises
from six import text_type

from twilio.twiml import TwiMLException, TwiML


class TwilioTest(unittest.TestCase):
    def strip(self, xml):
        return text_type(xml)

    @raises(TwiMLException)
    def test_append_fail(self):
        t = TwiML()
        t.append('foobar')
