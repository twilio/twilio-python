import unittest

import time

from twilio.jwt.taskrouter.capabilities import (
    WorkerCapabilityToken,
    TaskQueueCapabilityToken,
    WorkspaceCapabilityToken,
)


class TaskQueueCapabilityTokenTest(unittest.TestCase):

    def setUp(self):
        self.account_sid = "AC123"
        self.auth_token = "foobar"
        self.workspace_sid = "WS456"
        self.taskqueue_sid = "WQ789"
        self.capability = TaskQueueCapabilityToken(self.account_sid, self.auth_token,
                                                   self.workspace_sid, self.taskqueue_sid)

    def test_generate_token(self):
        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = TaskQueueCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        self.assertEqual(decoded.payload["iss"], self.account_sid)
        self.assertEqual(decoded.payload["account_sid"], self.account_sid)
        self.assertEqual(decoded.payload["workspace_sid"], self.workspace_sid)
        self.assertEqual(decoded.payload["taskqueue_sid"], self.taskqueue_sid)
        self.assertEqual(decoded.payload["channel"], self.taskqueue_sid)
        self.assertEqual(decoded.payload["version"], "v1")
        self.assertEqual(decoded.payload["friendly_name"], self.taskqueue_sid)

    def test_generate_token_with_default_ttl(self):
        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = TaskQueueCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        self.assertAlmostEqual(int(time.time()) + 3600, decoded.valid_until, delta=5)

    def test_generate_token_with_custom_ttl(self):
        ttl = 10000

        token = self.capability.to_jwt(ttl=ttl)
        self.assertNotEqual(None, token)

        decoded = TaskQueueCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        self.assertAlmostEqual(int(time.time()) + 10000, decoded.valid_until, delta=5)

    def test_default(self):
        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = TaskQueueCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        policies = decoded.payload['policies']
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

        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = TaskQueueCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        policies = decoded.payload['policies']
        self.assertEqual(len(policies), 4)

        # confirm the additional policy generated with allow_fetch_subresources()
        policy = policies[3]

        self.assertEqual(policy['url'], "https://taskrouter.twilio.com/v1/Workspaces/WS456/TaskQueues/WQ789/**")
        self.assertEqual(policy['method'], "GET")
        self.assertTrue(policy['allow'])
        self.assertEqual({}, policy['query_filter'])
        self.assertEqual({}, policy['post_filter'])

    def test_allow_updates_subresources(self):
        self.capability.allow_update_subresources()

        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = TaskQueueCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        policies = decoded.payload['policies']
        self.assertEqual(len(policies), 4)

        # confirm the additional policy generated with allow_updates_subresources()
        policy = policies[3]

        self.assertEqual(policy['url'], "https://taskrouter.twilio.com/v1/Workspaces/WS456/TaskQueues/WQ789/**")
        self.assertEqual(policy['method'], "POST")
        self.assertTrue(policy['allow'])
        self.assertEqual({}, policy['query_filter'])
        self.assertEqual({}, policy['post_filter'])

    def test_pass_policy_in_constructor(self):
        self.capability = TaskQueueCapabilityToken(self.account_sid, self.auth_token,
                                                   self.workspace_sid, self.taskqueue_sid,
                                                   allow_update_subresources=True)

        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = TaskQueueCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        policies = decoded.payload['policies']
        self.assertEqual(len(policies), 4)

        # confirm the additional policy generated with allow_updates_subresources()
        policy = policies[3]

        self.assertEqual(policy['url'], "https://taskrouter.twilio.com/v1/Workspaces/WS456/TaskQueues/WQ789/**")
        self.assertEqual(policy['method'], "POST")
        self.assertTrue(policy['allow'])
        self.assertEqual({}, policy['query_filter'])
        self.assertEqual({}, policy['post_filter'])


class WorkerCapabilityTokenTest(unittest.TestCase):
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
        self.capability = WorkerCapabilityToken(self.account_sid, self.auth_token,
                                                self.workspace_sid, self.worker_sid)

    def test_generate_token(self):
        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = WorkerCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        self.check_decoded(decoded.payload, self.account_sid, self.workspace_sid, self.worker_sid,
                           self.worker_sid)

    def test_generate_token_with_default_ttl(self):
        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = WorkerCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)
        self.assertAlmostEqual(int(time.time()) + 3600, decoded.valid_until, delta=5)

    def test_generate_token_with_custom_ttl(self):
        ttl = 10000

        token = self.capability.to_jwt(ttl=ttl)
        self.assertNotEqual(None, token)

        decoded = WorkerCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)
        self.assertAlmostEqual(int(time.time()) + 10000, decoded.valid_until, delta=5)

    def test_defaults(self):
        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = WorkerCapabilityToken.decode(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        websocket_url = 'https://event-bridge.twilio.com/v1/wschannels/{0}/{1}'.format(
            self.account_sid,
            self.worker_sid
        )

        # expect 6 policies
        policies = decoded.payload['policies']
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
        self.capability.allow_update_activities()

        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = WorkerCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        policies = decoded.payload['policies']
        self.assertEqual(len(policies), 7)
        policy = policies[6]

        url = "https://taskrouter.twilio.com/v1/Workspaces/{0}/Workers/{1}".format(
            self.workspace_sid,
            self.worker_sid
        )

        self.assertEqual(url, policy["url"])
        self.assertEqual("POST", policy["method"])
        self.assertTrue(policy["allow"])
        self.assertNotEqual(None, policy['post_filter'])
        self.assertEqual({}, policy['query_filter'])
        self.assertTrue(policy['post_filter']['ActivitySid'])

    def test_allow_reservation_updates(self):
        # allow reservation updates
        self.capability.allow_update_reservations()

        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = WorkerCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        policies = decoded.payload['policies']
        self.assertEqual(len(policies), 8)

        taskPolicy = policies[6]
        tasksUrl = "https://taskrouter.twilio.com/v1/Workspaces/{0}/Tasks/**".format(self.workspace_sid)
        self.check_policy('POST', tasksUrl, taskPolicy)

        workerReservationsPolicy = policies[7]
        reservationsUrl = "https://taskrouter.twilio.com/v1/Workspaces/{0}/Workers/{1}/Reservations/**".format(self.workspace_sid, self.worker_sid)
        self.check_policy('POST', reservationsUrl, workerReservationsPolicy)

    def test_pass_policies_in_constructor(self):
        # allow reservation updates
        self.capability = WorkerCapabilityToken(self.account_sid, self.auth_token,
                                                self.workspace_sid, self.worker_sid,
                                                allow_update_reservations=True)

        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = WorkerCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        policies = decoded.payload['policies']
        self.assertEqual(len(policies), 8)

        taskPolicy = policies[6]
        tasksUrl = "https://taskrouter.twilio.com/v1/Workspaces/{0}/Tasks/**".format(self.workspace_sid)
        self.check_policy('POST', tasksUrl, taskPolicy)

        workerReservationsPolicy = policies[7]
        reservationsUrl = "https://taskrouter.twilio.com/v1/Workspaces/{0}/Workers/{1}/Reservations/**".format(self.workspace_sid, self.worker_sid)
        self.check_policy('POST', reservationsUrl, workerReservationsPolicy)


class WorkspaceCapabilityTokenTest(unittest.TestCase):
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
        self.capability = WorkspaceCapabilityToken(self.account_sid, self.auth_token,
                                                   self.workspace_sid)

    def test_generate_token(self):
        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = WorkspaceCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        self.check_decoded(decoded.payload, self.account_sid, self.workspace_sid, self.workspace_sid)

    def test_generate_token_with_default_ttl(self):
        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = WorkspaceCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        self.assertAlmostEqual(int(time.time()) + 3600, decoded.valid_until, delta=5)

    def test_generate_token_with_custom_ttl(self):
        ttl = 10000

        token = self.capability.to_jwt(ttl=ttl)
        self.assertNotEqual(None, token)

        decoded = WorkspaceCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        self.assertAlmostEqual(int(time.time()) + 10000, decoded.valid_until, delta=5)

    def test_default(self):
        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = WorkspaceCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        policies = decoded.payload['policies']
        self.assertEqual(len(policies), 3)

        for method, url, policy in [
            ('GET', "https://event-bridge.twilio.com/v1/wschannels/AC123/WS456", policies[0]),
            ('POST', "https://event-bridge.twilio.com/v1/wschannels/AC123/WS456", policies[1]),
            ('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456", policies[2])
        ]:
            yield self.check_policy, method, url, policy

    def test_allow_fetch_subresources(self):
        self.capability.allow_fetch_subresources()

        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = WorkspaceCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        policies = decoded.payload['policies']
        self.assertEqual(len(policies), 4)

        # confirm the additional policy generated with allow_fetch_subresources()
        policy = policies[3]
        self.check_policy('GET', "https://taskrouter.twilio.com/v1/Workspaces/WS456/**", policy)

    def test_allow_updates_subresources(self):
        self.capability.allow_update_subresources()

        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = WorkspaceCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        policies = decoded.payload['policies']
        self.assertEqual(len(policies), 4)

        # confirm the additional policy generated with allow_update_subresources()
        policy = policies[3]
        self.check_policy('POST', "https://taskrouter.twilio.com/v1/Workspaces/WS456/**", policy)

    def test_pass_policy_in_constructor(self):
        self.capability = WorkspaceCapabilityToken(self.account_sid, self.auth_token,
                                                   self.workspace_sid,
                                                   allow_update_subresources=True)

        token = self.capability.to_jwt()
        self.assertNotEqual(None, token)

        decoded = WorkspaceCapabilityToken.from_jwt(token, self.auth_token)
        self.assertNotEqual(None, decoded)

        policies = decoded.payload['policies']
        self.assertEqual(len(policies), 4)

        # confirm the additional policy generated with allow_update_subresources()
        policy = policies[3]
        self.check_policy('POST', "https://taskrouter.twilio.com/v1/Workspaces/WS456/**", policy)


if __name__ == "__main__":
    unittest.main()
