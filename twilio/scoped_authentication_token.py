import time

import jwt

ALL = '*'

# HTTP Actions
HTTP_DELETE = 'DELETE'
HTTP_GET = 'GET'
HTTP_POST = 'POST'
HTTP_PUT = 'PUT'

# Client Actions
CLIENT_LISTEN = 'listen'
CLIENT_INVITE = 'invite'

class ScopedAuthenticationToken(object):
    def __init__(self, signing_key_sid, account_sid, ttl=3600):
        self.signing_key_sid = signing_key_sid
        self.account_sid = account_sid
        self.ttl = ttl
        self.grants = []

    def add_grant(self, resource, actions=ALL):
        if not isinstance(actions, list):
            actions = [actions]

        self.grants.append({
            'res': resource,
            'act': actions,
        })

    def add_endpoint_grant(self, endpoint, actions=None):
        actions = actions or [CLIENT_LISTEN, CLIENT_INVITE]
        resource = 'sip:{}@{}.endpoint.twilio.com'.format(endpoint,
                                                          self.account_sid)
        self.add_grant(resource, actions)

    def encode(self, secret):
        now = int(time.time())
        payload = {
            "jti": '{}-{}'.format(self.signing_key_sid, now),
            "iss": self.signing_key_sid,
            "sub": self.account_sid,
            "nbf": now,
            "exp": now + self.ttl,
            "grants": self.grants
        }

        return jwt.encode(payload, secret, headers={"cty": "twilio-sat;v=1"})
