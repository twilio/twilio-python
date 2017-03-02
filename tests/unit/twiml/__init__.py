import unittest

from six import text_type


class TwilioTest(unittest.TestCase):
    def strip(self, xml):
        return text_type(xml)
