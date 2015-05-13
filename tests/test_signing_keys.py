import unittest
from nose.tools import assert_raises
from twilio.rest.resources.signing_keys import SigningKeys


class SigningKeysTest(unittest.TestCase):

    def test_list(self):
        """
        Tests the Error part
        """
        keys = SigningKeys(self, [], {})
        assert_raises(AttributeError, keys.list)
