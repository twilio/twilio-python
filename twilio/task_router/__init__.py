import time

from .. import jwt


TASK_ROUTER_BASE_URL = 'https://taskrouter.twilio.com'
TASK_ROUTER_BASE_WS_URL = 'https://event-bridge.twilio.com/v1/wschannels'

REQUIRED = {'required': True}
OPTIONAL = {'required': False}


class TaskRouterCapability(object):
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
    def __init__(self, account_sid, auth_token, workspace_sid, worker_sid,
                 base_url=TASK_ROUTER_BASE_URL,
                 version='v1',
                 base_ws_url=TASK_ROUTER_BASE_WS_URL):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.workspace_sid = workspace_sid
        self.worker_sid = worker_sid
        self.version = version
        self.base_url = '%s/%s' % (base_url, self.version)
        self.base_ws_url = base_ws_url
        self.policies = []

        self._allow_worker_websocket_urls()
        self._allow_activity_list_fetch()

    @property
    def workspace_url(self):
        return '%s/Workspaces/%s' % (self.base_url, self.workspace_sid)

    @property
    def worker_url(self):
        return '%s/Workers/%s' % (self.workspace_url, self.worker_sid)

    def _allow_worker_websocket_urls(self):
        worker_event_url = '%s/%s/%s' % (
            self.base_ws_url,
            self.account_sid,
            self.worker_sid,
        )
        self.policies.append(make_policy(
            worker_event_url,
            'GET',
        ))
        self.policies.append(make_policy(
            worker_event_url,
            'POST',
        ))

    def _allow_activity_list_fetch(self):
        self.policies.append(make_policy(
            '%s/Activities' % self.workspace_url,
            'GET',
        ))

    def allow_worker_activity_updates(self):
        self.policies.append(make_policy(
            self.worker_url,
            'POST',
            post_filter={'ActivitySid': REQUIRED},
        ))

    def allow_worker_fetch_attributes(self):
        self.policies.append(make_policy(
            self.worker_url,
            'GET',
        ))

    def allow_task_reservation_updates(self):
        tasks_url = '%s/Tasks/**' % self.workspace_url
        self.policies.append(make_policy(
            tasks_url,
            'POST',
            post_filter={'ReservationStatus': REQUIRED},
        ))

    def generate_token(self, ttl=3600, attributes=None):
        """
        Generate a token string based on the credentials and permissions
        previously configured on this object.

        :param int ttl: Expiration time in seconds of the token. Defaults to
            3600 seconds (1 hour).
        :param dict attributes: Extra attributes to pass into the token.
        """

        return self._generate_token(
            ttl,
            {
                'account_sid': self.account_sid,
                'channel': self.worker_sid,
                'worker_sid': self.worker_sid,
                'workspace_sid': self.workspace_sid,
            }
        )

    def _generate_token(self, ttl, attributes=None):
        payload = {
            'version': self.version,
            'friendly_name': self.worker_sid,
            'policies': self.policies,
            'iss': self.account_sid,
            'exp': int(time.time()) + ttl,
        }

        if attributes is not None:
            payload.update(attributes)

        return jwt.encode(payload, self.auth_token, 'HS256')


def make_policy(url, method, query_filter=None, post_filter=None,
                allowed=True):
    """
    Create a policy dictionary for the given resource and method.

    :param str url: the resource URL to grant or deny access to
    :param str method: the HTTP method to allow or deny
    :param dict query_filter: specific GET parameter names to require or allow
    :param dict post_filter: POST parameter names to require or allow
    :param allowed bool: whether this request is allowed
    """

    return {
        'url': url,
        'method': method,
        'allow': allowed,
        'query_filter': query_filter or {},
        'post_filter': post_filter or {},
    }
