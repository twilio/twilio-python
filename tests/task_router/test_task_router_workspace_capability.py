import time
import unittest

from twilio import jwt
from twilio.task_router import TaskRouterWorkspaceCapability


class TaskRouterWorkspaceCapabilityTest(unittest.TestCase):
    def check_policy(self, method, url, policy):
        self.assertEqual(url, policy['url'])
        self.assertEqual(method, policy['method'])
        self.assertTrue(policy['allow'])
        self.assertEqual({}, policy['query_filter'])
        self.assertEqual({}, policy['post_filter'])

    def check_decoded(self, decoded, account_sid, workspace_sid, channel_id, channel_sid=None):
        self.assertEqual(decoded["iss"], account_sid)
        self.assertEqual(decoded["account_sid"], account_sid)
        self.assertEqual(decoded["workspace_sid"], workspace_sid)
        self.assertEqual(decoded["channel"], channel_id)
        self.assertEqual(decoded["version"], "v1")
        self.assertEqual(decoded["friendly_name"], channel_id)

        if 'worker_sid' in decoded.keys():
            self.assertEqual(decoded['worker_sid'], channel_sid)
        if 'taskqueue_sid' in decoded.keys():
            self.assertEqual(decoded['taskqueue_sid'], channel_sid)

    def setUp(self):
        self.account_sid = "AC123"
        self.auth_token = "foobar"
        self.workspace_sid = "WS456"
        self.capability = TaskRouterWorkspaceCapability(self.account_sid, self.auth_token, self.workspace_sid)

    def test_generate_token(self):

        token = self.capability.generate_token()
        self.assertNotEqual(None, token)

        decoded = jwt.decode(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        self.check_decoded(decoded, self.account_sid, self.workspace_sid, self.workspace_sid)

    def test_generate_token_with_default_ttl(self):
        token = self.capability.generate_token()
        self.assertNotEqual(None, token)

        decoded = jwt.decode(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        self.assertEqual(int(time.time()) + 3600, decoded["exp"])

    def test_generate_token_with_custom_ttl(self):
        ttl = 10000

        token = self.capability.generate_token(ttl)
        self.assertNotEqual(None, token)

        decoded = jwt.decode(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        self.assertEqual(int(time.time()) + 10000, decoded["exp"])

    def test_default(self):
        token = self.capability.generate_token()
        self.assertNotEqual(None, token)

        decoded = jwt.decode(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        policies = decoded['policies']
        self.assertEqual(len(policies), 3)

        for method, url, policy in [
            ('GET', "https://event-bridge.twilio.com/v1/wschannels/AC123/WS456", policies[0]),
            ('POST', "https://event-bridge.twilio.com/v1/wschannels/AC123/WS456", policies[1]),
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456", policies[2])
        ]:
            yield self.check_policy, method, url, policy

    def test_allow_fetch_subresources(self):
        self.capability.allow_fetch_subresources()

        token = self.capability.generate_token()
        self.assertNotEqual(None, token)

        decoded = jwt.decode(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        policies = decoded['policies']
        self.assertEqual(len(policies), 4)

        # confirm the additional policy generated with allow_fetch_subresources()
        policy = policies[3]

        self.check_policy('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456/**", policy)

    def test_allow_updates_subresources(self):
        self.capability.allow_updates_subresources()

        token = self.capability.generate_token()
        self.assertNotEqual(None, token)

        decoded = jwt.decode(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        policies = decoded['policies']
        self.assertEqual(len(policies), 4)

        # confirm the additional policy generated with allow_updates_subresources()
        policy = policies[3]

        self.check_policy('POST', "https://taskrouter.twilio.com/v1/Workspaces/WS456/**", policy)

if __name__ == "__main__":
    unittest.main()
