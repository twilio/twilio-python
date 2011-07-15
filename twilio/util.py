import base64
import hmac
from hashlib import sha1

class RequestValidator(object):

    def __init__(self, token):
        self.token = token

    def compute_signature(self, uri, params):
        """Compute the signature for a given request

        :param uri: full URI that Twilio requested on your server
        :param params: post vars that Twilio sent with the request
        :param auth: tuple with (account_sid, token)

        Returns the computed signature
        """
        s = uri
        if len(params) > 0:
            for k, v in sorted(params.items()):
                s += k + v

        # compute signature and compare signatures
        computed = base64.encodestring(hmac.new(self.token, s, sha1).digest())
        return computed.strip()

    def validate(self, uri, params, signature):
        """Validate a request from Twilio

        :param uri: full URI that Twilio requested on your server
        :param params: post vars that Twilio sent with the request
        :param signature: expexcted signature in HTTP X-Twilio-Signature header
        :param auth: tuple with (account_sid, token)

        returns true if the request passes validation, false if not
        """
        return self.compute_signature(uri, params) == signature
