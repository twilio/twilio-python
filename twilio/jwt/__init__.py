""" JSON Web Token implementation

Minimum implementation based on this spec:
http://self-issued.info/docs/draft-jones-json-web-token-01.html
"""
import base64
import hashlib
import hmac
from six import text_type, binary_type, b

# default text to binary representation conversion
def binary(txt):
    return txt.encode('utf-8')
try:
    import json
except ImportError:
    import simplejson as json


__all__ = ['encode', 'decode', 'DecodeError']

class DecodeError(Exception): pass

signing_methods = {
    'HS256': lambda msg, key: hmac.new(key, msg, hashlib.sha256).digest(),
    'HS384': lambda msg, key: hmac.new(key, msg, hashlib.sha384).digest(),
    'HS512': lambda msg, key: hmac.new(key, msg, hashlib.sha512).digest(),
}

def base64url_decode(input):
    input += b('=') * (4 - (len(input) % 4))
    return base64.urlsafe_b64decode(input)

def base64url_encode(input):
    return base64.urlsafe_b64encode(input).decode('utf-8').replace('=', '')

def header(jwt):
    header_segment = jwt.split('.', 1)[0]
    try:
        return json.loads(base64url_decode(header_segment))
    except (ValueError, TypeError):
        raise DecodeError("Invalid header encoding")

def encode(payload, key, algorithm='HS256'):
    segments = []
    header = {"typ": "JWT", "alg": algorithm}
    header_as_binary = binary(json.dumps(header))
    segments.append(base64url_encode(header_as_binary))
    payload_as_binary = binary(json.dumps(payload))
    segments.append(base64url_encode(payload_as_binary))
    signing_input = '.'.join(segments)
    try:
        ascii_key = text_type(key).encode('utf8')
        signature = signing_methods[algorithm](binary(signing_input), ascii_key)
    except KeyError:
        raise NotImplementedError("Algorithm not supported")
    segments.append(base64url_encode(signature))
    return '.'.join(segments)

def decode(jwt, key='', verify=True):
    try:
        signing_input, crypto_segment = jwt.rsplit('.', 1)
        header_segment, payload_segment = signing_input.split('.', 1)
    except ValueError:
        raise DecodeError("Not enough segments")
    try:
        header = json.loads(base64url_decode(binary(header_segment)).decode('utf-8'))
        payload = json.loads(base64url_decode(binary(payload_segment)).decode('utf-8'))
        signature = base64url_decode(binary(crypto_segment))
    except (ValueError, TypeError):
        raise DecodeError("Invalid segment encoding")
    if verify:
        try:
            ascii_key = key
            if not signature == signing_methods[header['alg']](binary(signing_input), binary(ascii_key)):
                raise DecodeError("Signature verification failed")
        except KeyError:
            raise DecodeError("Algorithm not supported")
    return payload
