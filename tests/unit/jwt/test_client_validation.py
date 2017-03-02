import unittest
import time

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PublicFormat,
    PrivateFormat,
    NoEncryption
)

from twilio.http.validation_client import ValidationPayload
from twilio.jwt import Jwt
from twilio.jwt.validation import ClientValidationJwt


class ClientValidationJwtTest(unittest.TestCase):
    def test_generate_payload_basic(self):
        vp = ValidationPayload(
            method='GET',
            path='https://api.twilio.com/',
            query_string='q1=v1',
            signed_headers=['headerb', 'headera'],
            all_headers={'head': 'toe', 'headera': 'vala', 'headerb': 'valb'},
            body='me=letop&you=leworst'
        )

        expected_payload = '\n'.join([
            'GET',
            'https://api.twilio.com/',
            'q1=v1',
            'headera:vala',
            'headerb:valb',
            '',
            'headera;headerb',
            '{}'.format(ClientValidationJwt._hash('me=letop&you=leworst'))
        ])
        expected_payload = ClientValidationJwt._hash(expected_payload)

        jwt = ClientValidationJwt('AC123', 'SK123', 'CR123', 'secret', vp)

        actual_payload = jwt._generate_payload()
        self.assertEqual('headera;headerb', actual_payload['hrh'])
        self.assertEqual(expected_payload, actual_payload['rqh'])

    def test_generate_payload_complex(self):
        vp = ValidationPayload(
            method='GET',
            path='https://api.twilio.com/',
            query_string='q1=v1&q2=v2&a=b',
            signed_headers=['headerb', 'headera'],
            all_headers={'head': 'toe', 'Headerb': 'valb', 'yeezy': 'weezy'},
            body='me=letop&you=leworst'
        )

        expected_payload = '\n'.join([
            'GET',
            'https://api.twilio.com/',
            'a=b&q1=v1&q2=v2',
            'headerb:valb',
            '',
            'headera;headerb',
            '{}'.format(ClientValidationJwt._hash('me=letop&you=leworst'))
        ])
        expected_payload = ClientValidationJwt._hash(expected_payload)

        jwt = ClientValidationJwt('AC123', 'SK123', 'CR123', 'secret', vp)

        actual_payload = jwt._generate_payload()
        self.assertEqual('headera;headerb', actual_payload['hrh'])
        self.assertEqual(expected_payload, actual_payload['rqh'])

    def test_generate_payload_no_query_string(self):
        vp = ValidationPayload(
            method='GET',
            path='https://api.twilio.com/',
            query_string='',
            signed_headers=['headerb', 'headera'],
            all_headers={'head': 'toe', 'Headerb': 'valb', 'yeezy': 'weezy'},
            body='me=letop&you=leworst'
        )

        expected_payload = '\n'.join([
            'GET',
            'https://api.twilio.com/',
            '',
            'headerb:valb',
            '',
            'headera;headerb',
            '{}'.format(ClientValidationJwt._hash('me=letop&you=leworst'))
        ])
        expected_payload = ClientValidationJwt._hash(expected_payload)

        jwt = ClientValidationJwt('AC123', 'SK123', 'CR123', 'secret', vp)

        actual_payload = jwt._generate_payload()
        self.assertEqual('headera;headerb', actual_payload['hrh'])
        self.assertEqual(expected_payload, actual_payload['rqh'])

    def test_generate_payload_no_req_body(self):
        vp = ValidationPayload(
            method='GET',
            path='https://api.twilio.com/',
            query_string='q1=v1',
            signed_headers=['headerb', 'headera'],
            all_headers={'head': 'toe', 'headera': 'vala', 'headerb': 'valb'},
            body=''
        )

        expected_payload = '\n'.join([
            'GET',
            'https://api.twilio.com/',
            'q1=v1',
            'headera:vala',
            'headerb:valb',
            '',
            'headera;headerb',
            ''
        ])
        expected_payload = ClientValidationJwt._hash(expected_payload)

        jwt = ClientValidationJwt('AC123', 'SK123', 'CR123', 'secret', vp)

        actual_payload = jwt._generate_payload()
        self.assertEqual('headera;headerb', actual_payload['hrh'])
        self.assertEqual(expected_payload, actual_payload['rqh'])

    def test_generate_payload_header_keys_lowercased(self):
        vp = ValidationPayload(
            method='GET',
            path='https://api.twilio.com/',
            query_string='q1=v1',
            signed_headers=['headerb', 'headera'],
            all_headers={'head': 'toe', 'Headera': 'vala', 'Headerb': 'valb'},
            body='me=letop&you=leworst'
        )

        expected_payload = '\n'.join([
            'GET',
            'https://api.twilio.com/',
            'q1=v1',
            'headera:vala',
            'headerb:valb',
            '',
            'headera;headerb',
            '{}'.format(ClientValidationJwt._hash('me=letop&you=leworst'))
        ])
        expected_payload = ClientValidationJwt._hash(expected_payload)

        jwt = ClientValidationJwt('AC123', 'SK123', 'CR123', 'secret', vp)

        actual_payload = jwt._generate_payload()
        self.assertEqual('headera;headerb', actual_payload['hrh'])
        self.assertEqual(expected_payload, actual_payload['rqh'])

    def test_generate_payload_no_headers(self):
        vp = ValidationPayload(
            method='GET',
            path='https://api.twilio.com/',
            query_string='q1=v1',
            signed_headers=['headerb', 'headera'],
            all_headers={},
            body='me=letop&you=leworst'
        )

        expected_payload = '\n'.join([
            'GET',
            'https://api.twilio.com/',
            'q1=v1',
            '',
            'headera;headerb',
            '{}'.format(ClientValidationJwt._hash('me=letop&you=leworst'))
        ])
        expected_payload = ClientValidationJwt._hash(expected_payload)

        jwt = ClientValidationJwt('AC123', 'SK123', 'CR123', 'secret', vp)

        actual_payload = jwt._generate_payload()
        self.assertEqual('headera;headerb', actual_payload['hrh'])
        self.assertEqual(expected_payload, actual_payload['rqh'])

    def test_generate_payload_schema_correct_1(self):
        """Test against a known good rqh payload hash"""
        vp = ValidationPayload(
            method='GET',
            path='/Messages',
            query_string='PageSize=5&Limit=10',
            signed_headers=['authorization', 'host'],
            all_headers={'authorization': 'foobar', 'host': 'api.twilio.com'},
            body='foobar'
        )

        expected_hash = '4dc9b67bed579647914587b0e22a1c65c1641d8674797cd82de65e766cce5f80'

        jwt = ClientValidationJwt('AC123', 'SK123', 'CR123', 'secret', vp)

        actual_payload = jwt._generate_payload()
        self.assertEqual('authorization;host', actual_payload['hrh'])
        self.assertEqual(expected_hash, actual_payload['rqh'])

    def test_generate_payload_schema_correct_2(self):
        """Test against a known good rqh payload hash"""
        vp = ValidationPayload(
            method='POST',
            path='/Messages',
            query_string='',
            signed_headers=['authorization', 'host'],
            all_headers={'authorization': 'foobar', 'host': 'api.twilio.com'},
            body='testbody'
        )

        expected_hash = 'bd792c967c20d546c738b94068f5f72758a10d26c12979677501e1eefe58c65a'

        jwt = ClientValidationJwt('AC123', 'SK123', 'CR123', 'secret', vp)

        actual_payload = jwt._generate_payload()
        self.assertEqual('authorization;host', actual_payload['hrh'])
        self.assertEqual(expected_hash, actual_payload['rqh'])

    def test_jwt_payload(self):
        vp = ValidationPayload(
            method='GET',
            path='/Messages',
            query_string='PageSize=5&Limit=10',
            signed_headers=['authorization', 'host'],
            all_headers={'authorization': 'foobar', 'host': 'api.twilio.com'},
            body='foobar'
        )
        expected_hash = '4dc9b67bed579647914587b0e22a1c65c1641d8674797cd82de65e766cce5f80'

        jwt = ClientValidationJwt('AC123', 'SK123', 'CR123', 'secret', vp)

        self.assertDictContainsSubset({
            'hrh': 'authorization;host',
            'rqh': expected_hash,
            'iss': 'SK123',
            'sub': 'AC123',
        }, jwt.payload)
        self.assertGreaterEqual(jwt.payload['exp'], time.time(), 'JWT exp is before now')
        self.assertLessEqual(jwt.payload['exp'], time.time() + 301, 'JWT exp is after now + 5mins')
        self.assertDictEqual({
            'alg': 'RS256',
            'typ': 'JWT',
            'cty': 'twilio-pkrv;v=1',
            'kid': 'CR123'
        }, jwt.headers)

    def test_jwt_signing(self):
        vp = ValidationPayload(
            method='GET',
            path='/Messages',
            query_string='PageSize=5&Limit=10',
            signed_headers=['authorization', 'host'],
            all_headers={'authorization': 'foobar', 'host': 'api.twilio.com'},
            body='foobar'
        )
        expected_hash = '4dc9b67bed579647914587b0e22a1c65c1641d8674797cd82de65e766cce5f80'

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key().public_bytes(Encoding.PEM, PublicFormat.PKCS1)
        private_key = private_key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption())

        jwt = ClientValidationJwt('AC123', 'SK123', 'CR123', private_key, vp)
        decoded = Jwt.from_jwt(jwt.to_jwt(), public_key)

        self.assertDictContainsSubset({
            'hrh': 'authorization;host',
            'rqh': expected_hash,
            'iss': 'SK123',
            'sub': 'AC123',
        }, decoded.payload)
        self.assertGreaterEqual(decoded.payload['exp'], time.time(), 'JWT exp is before now')
        self.assertLessEqual(decoded.payload['exp'], time.time() + 501, 'JWT exp is after now + 5m')
        self.assertDictEqual({
            'alg': 'RS256',
            'typ': 'JWT',
            'cty': 'twilio-pkrv;v=1',
            'kid': 'CR123'
        }, decoded.headers)


