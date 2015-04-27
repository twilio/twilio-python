import time

import jwt


class ScopedAuthenticationToken:
    ACTION_ALL = '*'
    ACTION_DELETE = 'DELETE'
    ACTION_GET = 'GET'
    ACTION_POST = 'POST'
    ACTION_PUT = 'PUT'

    def __init__(self, signing_key_sid, account_sid, token_id=None, ttl=3600, grants=[]):
        self.signing_key_sid = signing_key_sid
        self.account_sid = account_sid
        if token_id:
            self.token_id = token_id
        else:
            self.token_id = '{}-{}'.format(signing_key_sid, time.time())
        self.ttl = ttl
        self.grants = grants

    def add_grant(self, grant):
        self.grants.append(grant)

    def generate_token(self, secret):
        payload = {
            "jti": self.token_id,
            "iss": self.signing_key_sid,
            "sub": self.account_sid,
            "nbf": time.time(),
            "exp": time.time() + self.ttl,
            "grants": []
        }

        for grant in self.grants:
            payload['grants'].append({
                'res': grant.res,
                'act': grant.act
            })

        return jwt.encode(payload, secret, headers={"cty": "twilio-sat;v=1"})


class Grant:
    def __init__(self, resource, action=ScopedAuthenticationToken.ACTION_ALL):
        self.res = resource
        self.act = action
