import base64
import hmac
import logging
from hashlib import sha1, sha256

from urllib.parse import urlparse, parse_qs

logger = logging.getLogger(__name__)

SIGNATURE_HEADER = "X-Twilio-Signature"
# Header Twilio adds to webhooks signed with a SharedKey:
# key=<sharedKeyId>,algorithm=<algorithm>
SIGNATURE_SETTINGS_HEADER = "X-Twilio-Webhooks-Signature-Settings"
HMAC_SHA1 = "HMAC_SHA1"
HMAC_SHA256 = "HMAC_SHA256"

_HASH_FUNCTIONS = {HMAC_SHA1: sha1, HMAC_SHA256: sha256}


def compare(string1, string2):
    """Compare two strings while protecting against timing attacks

    :param str string1: the first string
    :param str string2: the second string

    :returns: True if the strings are equal, False if not
    :rtype: :obj:`bool`
    """
    if len(string1) != len(string2):
        return False
    result = True
    for c1, c2 in zip(string1, string2):
        result &= c1 == c2

    return result


def remove_port(uri):
    """Remove the port number from a URI

    :param uri: parsed URI that Twilio requested on your server

    :returns: full URI without a port number
    :rtype: str
    """
    if not uri.port:
        return uri.geturl()

    new_netloc = uri.netloc.split(":")[0]
    new_uri = uri._replace(netloc=new_netloc)

    return new_uri.geturl()


def add_port(uri):
    """Add the port number to a URI

    :param uri: parsed URI that Twilio requested on your server

    :returns: full URI with a port number
    :rtype: str
    """
    if uri.port:
        return uri.geturl()

    port = 443 if uri.scheme == "https" else 80
    new_netloc = uri.netloc + ":" + str(port)
    new_uri = uri._replace(netloc=new_netloc)

    return new_uri.geturl()


def get_signature_algorithm(signature_settings_header):
    """Get the signing algorithm named in the X-Twilio-Webhooks-Signature-Settings header

    A missing or empty header (or one without ``algorithm=``) means the legacy
    Auth Token signature, HMAC_SHA1.

    :param str signature_settings_header: header value, e.g.
        ``key=webhooks_sharedkey_...,algorithm=HMAC_SHA256``

    :returns: the algorithm name
    :rtype: str
    """
    for part in (signature_settings_header or "").split(","):
        name, separator, value = part.partition("=")
        if separator and name.strip() == "algorithm" and value.strip():
            return value.strip()
    return HMAC_SHA1


class RequestValidator(object):
    def __init__(self, token):
        """
        :param str token: the secret the webhook was signed with: the account Auth Token,
            or the SharedKey secret when the request carries X-Twilio-Webhooks-Signature-Settings
        """
        self.token = token.encode("utf-8")

    def compute_signature(self, uri, params, algorithm=None):
        """Compute the signature for a given request

        :param uri: full URI that Twilio requested on your server
        :param params: post vars that Twilio sent with the request
        :param str algorithm: HMAC_SHA1 (default) or HMAC_SHA256

        :returns: The computed signature
        :raises ValueError: if the algorithm is not supported
        """
        hash_function = _HASH_FUNCTIONS.get((algorithm or HMAC_SHA1).upper())
        if hash_function is None:
            raise ValueError("Unsupported webhook signature algorithm: %s" % algorithm)

        s = uri
        if params:
            for param_name in sorted(set(params)):
                values = self.get_values(params, param_name)

                for value in sorted(set(values)):
                    s += param_name + value

        # compute signature and compare signatures
        mac = hmac.new(self.token, s.encode("utf-8"), hash_function)
        computed = base64.b64encode(mac.digest())
        computed = computed.decode("utf-8")

        return computed.strip()

    def get_values(self, param_dict, param_name):
        try:
            # Support MultiDict used by Flask.
            return param_dict.getall(param_name)
        except AttributeError:
            try:
                # Support QueryDict used by Django.
                return param_dict.getlist(param_name)
            except AttributeError:
                # Fallback to a standard dict.
                return [param_dict[param_name]]

    def compute_hash(self, body):
        computed = sha256(body.encode("utf-8")).hexdigest()

        return computed.strip()

    def validate(self, uri, params, signature, algorithm=None):
        """Validate a request from Twilio

        :param uri: full URI that Twilio requested on your server
        :param params: dictionary of POST variables or string of POST body for JSON requests
        :param signature: expected signature in HTTP X-Twilio-Signature header
        :param str algorithm: HMAC_SHA1 (default) or HMAC_SHA256, see
            :func:`get_signature_algorithm`. An unsupported algorithm fails validation
            and logs a warning.

        :returns: True if the request passes validation, False if not
        """
        if (algorithm or HMAC_SHA1).upper() not in _HASH_FUNCTIONS:
            logger.warning(
                "Unsupported webhook signature algorithm '%s'. Supported: %s, %s. "
                "Upgrade twilio if Twilio added a new one.",
                algorithm,
                HMAC_SHA1,
                HMAC_SHA256,
            )
            return False

        if params is None:
            params = {}

        parsed_uri = urlparse(uri)
        uri_with_port = add_port(parsed_uri)
        uri_without_port = remove_port(parsed_uri)

        valid_body_hash = True  # May not receive body hash, so default succeed

        query = parse_qs(parsed_uri.query)
        if "bodySHA256" in query and isinstance(params, str):
            valid_body_hash = compare(self.compute_hash(params), query["bodySHA256"][0])
            params = {}

        #  check signature of uri with and without port,
        #  since sig generation on back end is inconsistent
        valid_signature = compare(
            self.compute_signature(uri_without_port, params, algorithm), signature
        )
        valid_signature_with_port = compare(
            self.compute_signature(uri_with_port, params, algorithm), signature
        )

        return valid_body_hash and (valid_signature or valid_signature_with_port)
