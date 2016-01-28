import time
import unittest

from twilio import jwt
from twilio.task_router import TaskRouterWorkerCapability


class TaskRouterWorkerCapabilityTest(unittest.TestCase):
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
        self.worker_sid = "WK789"
        self.capability = TaskRouterWorkerCapability(self.account_sid, self.auth_token, self.workspace_sid, self.worker_sid)

    def test_generate_token(self):

        token = self.capability.generate_token()
        self.assertNotEqual(None, token)

        decoded = jwt.decode(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        self.check_decoded(decoded, self.account_sid, self.workspace_sid, self.worker_sid, self.worker_sid)

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

    def test_defaults(self):
        token = self.capability.generate_token()
        self.assertNotEqual(None, token)

        decoded = jwt.decode(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        websocket_url = 'https://event-bridge.twilio.com/v1/wschannels/{0}/{1}'.format(self.account_sid, self.worker_sid)

        # expect 6 policies
        policies = decoded['policies']
        self.assertEqual(len(policies), 6)

        # should expect 6 policies
        for method, url, policy in [
            ('GET', websocket_url, policies[0]),
            ('POST', websocket_url, policies[1]),
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456/Workers/WK789", policies[2]),
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456/Activities", policies[3])
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456/Tasks/**", policies[4]),
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456/Workers/WK789/Reservations/**", policies[5])
        ]:
            yield self.check_policy, method, url, policy

    def test_allow_activity_updates(self):

        # allow activity updates to the worker
        self.capability.allow_activity_updates()

        token = self.capability.generate_token()
        self.assertNotEqual(None, token)

        decoded = jwt.decode(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        policies = decoded['policies']
        self.assertEqual(len(policies), 7)
        policy = policies[6]

        url = "https://taskrouter.twilio.com/v1/Workspaces/{0}/Workers/{1}".format(self.workspace_sid, self.worker_sid)

        self.assertEqual(url, policy["url"])
        self.assertEqual("POST", policy["method"])
        self.assertTrue(policy["allow"])
        self.assertNotEqual(None, policy['post_filter'])
        self.assertEqual({}, policy['query_filter'])
        self.assertTrue(policy['post_filter']['ActivitySid'])

    def test_allow_reservation_updates(self):
        # allow reservation updates
        self.capability.allow_reservation_updates()

        token = self.capability.generate_token()
        self.assertNotEqual(None, token)

        decoded = jwt.decode(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        policies = decoded['policies']
        self.assertEqual(len(policies), 8)

        taskPolicy = policies[6]
        tasksUrl = "https://taskrouter.twilio.com/v1/Workspaces/{0}/Tasks/**".format(self.workspace_sid)
        self.check_policy('POST', tasksUrl, taskPolicy)

        workerReservationsPolicy = policies[7]
        reservationsUrl = "https://taskrouter.twilio.com/v1/Workspaces/{0}/Workers/{1}/Reservations/**".format(self.workspace_sid, self.worker_sid)
        self.check_policy('POST', reservationsUrl, workerReservationsPolicy)

if __name__ == "__main__":
    unittest.main()
