import unittest

from mock import patch

from twilio.rest.resources import Tokens


DEFAULT = {
    'Ttl': None,
}


class TokensTest(unittest.TestCase):

    def setUp(self):
        self.resource = Tokens('foo', ('sid', 'token'))
        self.params = DEFAULT.copy()

    def test_create(self):
        with patch.object(self.resource, 'create_instance') as mock:
            self.resource.create(
                ttl=111,
            )
            mock.assert_called_with(
                {
                    'ttl': 111,
                }
            )
