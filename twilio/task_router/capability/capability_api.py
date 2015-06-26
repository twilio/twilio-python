import time

from .. import jwt


class CapabilityAPI(object):
    """
    A token to control permissions for the TaskRouter service.

    :param str account_sid: The account to generate a token for
    :param str auth_token: The auth token for the account. Used to sign the
        token and will not be included in generated output.
    :param str workspace_sid: The workspace to grant capabilities over
    :param str worker_sid: The worker sid to grant capabilities over
    :param str base_url: The base TaskRouter API URL
    :param str base_ws_url: The base TaskRouter event stream URL
    """
    def __init__(self, account_sid, auth_token, version, friendly_name):
        self.account_sid = account_sid
        self.auth_token = auth_token
        
        self.version = version
        self.friendly_name = friendly_name; 
        self.policies = []

    def add_policy(self, url, method, allowed, query_filter = None, post_filter = None):
    	policy = self.make_policy(url, method, allowed, query_filter, post_filter)
    	self.policies.append(policy)

    def allow(self, url, method, query_filter = None, post_filter = None): 
    	self.add_policy(url, method, True, query_filter, post_filter)

    def deny(self, url, method, query_filter = None, post_filter = None):
    	self.add_policy(url, method, False, query_filter, post_filter)

    def generate_token(self, ttl = 3600, attributes = None):
        return self._generate_token(ttl)

    def _generate_token(self, ttl, attributes=None):
        payload = {
            'iss': self.account_sid,
            'exp': int(time.time()) + ttl,
            'version': self.version,
            'friendly_name': self.friendly_name,
            'policies': self.policies,
        }

        if attributes is not None:
            payload.update(attributes)

        return jwt.encode(payload, self.auth_token, 'HS256')

    def make_policy(self, url, method, allowed = True, query_filter = None, post_filter = None): 
        # Create a policy dictionary for the given resource and method.

        # :param str url: the resource URL to grant or deny access to
        # :param str method: the HTTP method to allow or deny
        # :param allowed bool: whether this request is allowed
        # :param dict query_filter: specific GET parameter names to require or allow
        # :param dict post_filter: POST parameter names to require or allow

        return {
            'url': url, 
            'method': method, 
            'allowed': allowed, 
            'query_filter': query_filter or {}, 
            'post_filter': post_filter or {}
        }