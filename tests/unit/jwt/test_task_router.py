import unittest
import warnings

import time

from twilio import jwt
from twilio.jwt.task_router import (
    TaskRouterCapability,
    TaskRouterTaskQueueCapability,
    TaskRouterWorkerCapability,
    TaskRouterWorkspaceCapability,
)


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
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456/Workers/WK789", policies[2]),
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
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456/Activities", policies[3]),
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
