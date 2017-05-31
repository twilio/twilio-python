import unittest
import warnings

from twilio import jwt
from twilio.task_router import TaskRouterCapability


class TaskRouterCapabilityTest(unittest.TestCase):

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

    def test_workspace_default(self):
        account_sid = "AC123"
        auth_token = "foobar"
        workspace_sid = "WS456"
        channel_id = "WS456"
        capability = TaskRouterCapability(account_sid, auth_token, workspace_sid, channel_id)

        capability.generate_token()

        token = capability.generate_token()
        self.assertNotEqual(None, token)

        decoded = jwt.decode(token, auth_token)
        self.assertNotEqual(None, decoded)

        self.check_decoded(decoded, account_sid, workspace_sid, channel_id)

        policies = decoded['policies']
        self.assertEqual(len(policies), 3)

        for method, url, policy in [
            ('GET', "https://event-bridge.twilio.com/v1/wschannels/AC123/WS456", policies[0]),
            ('POST', "https://event-bridge.twilio.com/v1/wschannels/AC123/WS456", policies[1]),
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456", policies[2]),
        ]:
            yield self.check_policy, method, url, policy

    def test_worker_default(self):
        account_sid = "AC123"
        auth_token = "foobar"
        workspace_sid = "WS456"
        worker_sid = "WK789"
        capability = TaskRouterCapability(account_sid, auth_token, workspace_sid, worker_sid)

        capability.generate_token()

        token = capability.generate_token()
        self.assertNotEqual(None, token)

        decoded = jwt.decode(token, auth_token)
        self.assertNotEqual(None, decoded)

        self.check_decoded(decoded, account_sid, workspace_sid, worker_sid, worker_sid)

        policies = decoded['policies']
        self.assertEqual(len(policies), 6)

        for method, url, policy in [
            ('GET', "https://event-bridge.twilio.com/v1/wschannels/AC123/WK789", policies[0]),
            ('POST', "https://event-bridge.twilio.com/v1/wschannels/AC123/WK789", policies[1]),
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456/Workers/WK789", policies[2])
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456/Activities", policies[3]),
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456/Tasks/**", policies[4]),
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456/Workers/WK789/Reservations/**", policies[5])
        ]:
            yield self.check_policy, method, url, policy

    def test_task_queue_default(self):
        account_sid = "AC123"
        auth_token = "foobar"
        workspace_sid = "WS456"
        taskqueue_sid = "WQ789"
        capability = TaskRouterCapability(account_sid, auth_token, workspace_sid, taskqueue_sid)

        capability.generate_token()

        token = capability.generate_token()
        self.assertNotEqual(None, token)

        decoded = jwt.decode(token, auth_token)
        self.assertNotEqual(None, decoded)

        self.check_decoded(decoded, account_sid, workspace_sid, taskqueue_sid, taskqueue_sid)

        policies = decoded['policies']
        self.assertEqual(len(policies), 3)

        for method, url, policy in [
            ('GET', "https://event-bridge.twilio.com/v1/wschannels/AC123/WQ789", policies[0]),
            ('POST', "https://event-bridge.twilio.com/v1/wschannels/AC123/WQ789", policies[1])
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456/TaskQueues/WQ789", policies[2])
        ]:
            yield self.check_policy, method, url, policy

    def test_deprecated_worker(self):
        account_sid = "AC123"
        auth_token = "foobar"
        workspace_sid = "WS456"
        worker_sid = "WK789"
        capability = TaskRouterCapability(account_sid, auth_token, workspace_sid, worker_sid)

        capability.generate_token()

        token = capability.generate_token()
        self.assertNotEqual(None, token)

        decoded = jwt.decode(token, auth_token)
        self.assertNotEqual(None, decoded)

        self.check_decoded(decoded, account_sid, workspace_sid, worker_sid, worker_sid)

        policies = decoded['policies']
        self.assertEqual(len(policies), 6)

        # should expect 6 policies
        for method, url, policy in [
            ('GET', "https://event-bridge.twilio.com/v1/wschannels/AC123/WK789", policies[0]),
            ('POST', "https://event-bridge.twilio.com/v1/wschannels/AC123/WK789", policies[1]),
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456/Activities", policies[2]),
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456/Tasks/**", policies[3]),
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456/Workers/WK789/Reservations/**", policies[4]),
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456/Workers/WK789", policies[5])
        ]:
            yield self.check_policy, method, url, policy

        # check deprecated warnings
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            capability.allow_worker_fetch_attributes()
            assert len(w) == 1
            assert issubclass(w[-1].category, DeprecationWarning)
            assert "deprecated" in str(w[-1].message)

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            capability.allow_worker_activity_updates()
            assert len(w) == 1
            assert issubclass(w[-1].category, DeprecationWarning)
            assert "deprecated" in str(w[-1].message)

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            capability.allow_task_reservation_updates()
            assert len(w) == 1
            assert issubclass(w[-1].category, DeprecationWarning)
            assert "deprecated" in str(w[-1].message)

if __name__ == "__main__":
    unittest.main()
