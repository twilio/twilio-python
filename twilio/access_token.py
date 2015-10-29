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


class AccessToken(object):
    def __init__(self, signing_key_sid, account_sid, secret, ttl=3600):
        self.signing_key_sid = signing_key_sid
        self.account_sid = account_sid
        self.secret = secret
        self.ttl = ttl
        self.grants = []

    def add_grant(self, resource, actions=ALL):
        if not isinstance(actions, list):
            actions = [actions]

        self.grants.append({
            'res': resource,
            'act': actions,
        })
        return self

    def add_rest_grant(self, uri, actions=ALL):
        resource = 'https://api.twilio.com/2010-04-01/Accounts/{0}/{1}'.format(
            self.account_sid,
            uri.lstrip('/'),
        )
        return self.add_grant(resource, actions)

    def add_endpoint_grant(self, endpoint, actions=None):
        actions = actions or [CLIENT_LISTEN, CLIENT_INVITE]
        resource = 'sip:{0}@{1}.endpoint.twilio.com'.format(
            endpoint,
            self.account_sid
        )
        return self.add_grant(resource, actions)

    def enable_nts(self):
        return self.add_rest_grant('/Tokens.json', HTTP_POST)

    def to_jwt(self):
        now = int(time.time())
        headers = {
            "cty": "twilio-sat;v=1"
        }
        payload = {
            "jti": '{0}-{1}'.format(self.signing_key_sid, now),
            "iss": self.signing_key_sid,
            "sub": self.account_sid,
            "nbf": now,
            "exp": now + self.ttl,
            "grants": self.grants
        }

        return jwt.encode(payload, self.secret, headers=headers)

    def __str__(self):
        return self.to_jwt().decode('utf-8')
