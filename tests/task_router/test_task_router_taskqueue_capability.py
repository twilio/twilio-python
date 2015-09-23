import time
import unittest

from twilio import jwt
from twilio.task_router import TaskRouterTaskQueueCapability


class TaskRouterTaskQueueCapabilityTest(unittest.TestCase):

    def setUp(self):
        self.account_sid = "AC123"
        self.auth_token = "foobar"
        self.workspace_sid = "WS456"
        self.taskqueue_sid = "WQ789"
        self.capability = TaskRouterTaskQueueCapability(self.account_sid, self.auth_token, self.workspace_sid, self.taskqueue_sid)

    def test_generate_token(self):

        token = self.capability.generate_token()
        self.assertNotEqual(None, token)

        decoded = jwt.decode(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        self.assertEqual(decoded["iss"], self.account_sid)
        self.assertEqual(decoded["account_sid"], self.account_sid)
        self.assertEqual(decoded["workspace_sid"], self.workspace_sid)
        self.assertEqual(decoded["taskqueue_sid"], self.taskqueue_sid)
        self.assertEqual(decoded["channel"], self.taskqueue_sid)
        self.assertEqual(decoded["version"], "v1")
        self.assertEqual(decoded["friendly_name"], self.taskqueue_sid)

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

        # websocket GET
        get_policy = policies[0]
        self.assertEqual("https://event-bridge.twilio.com/v1/wschannels/AC123/WQ789", get_policy['url'])
        self.assertEqual("GET", get_policy['method'])
        self.assertTrue(get_policy['allow'])
        self.assertEqual({}, get_policy['query_filter'])
        self.assertEqual({}, get_policy['post_filter'])

        # websocket POST
        post_policy = policies[1]
        self.assertEqual("https://event-bridge.twilio.com/v1/wschannels/AC123/WQ789", post_policy['url'])
        self.assertEqual("POST", post_policy['method'])
        self.assertTrue(post_policy['allow'])
        self.assertEqual({}, post_policy['query_filter'])
        self.assertEqual({}, post_policy['post_filter'])

        # fetch GET
        fetch_policy = policies[2]
        self.assertEqual("https://taskrouter.twilio.com/v1/Workspaces/WS456/TaskQueues/WQ789", fetch_policy['url'])
        self.assertEqual("GET", fetch_policy['method'])
        self.assertTrue(fetch_policy['allow'])
        self.assertEqual({}, fetch_policy['query_filter'])
        self.assertEqual({}, fetch_policy['post_filter'])

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

        self.assertEqual(policy['url'], "https://taskrouter.twilio.com/v1/Workspaces/WS456/TaskQueues/WQ789/**")
        self.assertEqual(policy['method'], "GET")
        self.assertTrue(policy['allow'])
        self.assertEqual({}, policy['query_filter'])
        self.assertEqual({}, policy['post_filter'])

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

        self.assertEqual(policy['url'], "https://taskrouter.twilio.com/v1/Workspaces/WS456/TaskQueues/WQ789/**")
        self.assertEqual(policy['method'], "POST")
        self.assertTrue(policy['allow'])
        self.assertEqual({}, policy['query_filter'])
        self.assertEqual({}, policy['post_filter'])

if __name__ == "__main__":
    unittest.main()
