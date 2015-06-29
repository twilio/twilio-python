import sys

import time
import unittest
import warnings

from twilio import jwt
from twilio.task_router.capability import TaskRouterCapability

class TaskRouterCapabilityTest(unittest.TestCase):

    def test_workspace_default(self):
        account_sid = "AC123"
        auth_token = "foobar"
        workspace_sid = "WS456"
        channel_id = "WS456"
        capability = TaskRouterCapability(account_sid, auth_token, workspace_sid, channel_id)

        capability.generate_token()

        token = capability.generate_token()
        self.assertIsNotNone(token)

        decoded = jwt.decode(token, auth_token)
        self.assertIsNotNone(decoded)

        self.assertEqual(decoded["iss"], account_sid)
        self.assertEqual(decoded["account_sid"], account_sid)
        self.assertEqual(decoded["workspace_sid"], workspace_sid)
        self.assertEqual(decoded["channel"], channel_id)
        self.assertEqual(decoded["version"], "v1")
        self.assertEqual(decoded["friendly_name"], channel_id)

        policies = decoded['policies']
        self.assertEqual(len(policies), 3)

        # websocket GET
        get_policy = policies[0]
        self.assertEqual("https://event-bridge.twilio.com/v1/wschannels/AC123/WS456", get_policy['url'])
        self.assertEqual("GET", get_policy['method'])
        self.assertTrue(get_policy['allowed'])
        self.assertEqual({}, get_policy['query_filter'])
        self.assertEqual({}, get_policy['post_filter'])

        # websocket POST
        post_policy = policies[1]
        self.assertEqual("https://event-bridge.twilio.com/v1/wschannels/AC123/WS456", post_policy['url'])
        self.assertEqual("POST", post_policy['method'])
        self.assertTrue(post_policy['allowed'])
        self.assertEqual({}, post_policy['query_filter'])
        self.assertEqual({}, post_policy['post_filter'])

        # fetch GET
        fetch_policy = policies[2]
        self.assertEqual("https://taskrouter.twilio.com/v1/Workspaces/WS456", fetch_policy['url'])
        self.assertEqual("GET", fetch_policy['method'])
        self.assertTrue(fetch_policy['allowed'])
        self.assertEqual({}, fetch_policy['query_filter'])
        self.assertEqual({}, fetch_policy['post_filter'])

    def test_worker_default(self):
        account_sid = "AC123"
        auth_token = "foobar"
        workspace_sid = "WS456"
        worker_sid = "WK789"
        capability = TaskRouterCapability(account_sid, auth_token, workspace_sid, worker_sid)

        capability.generate_token()

        token = capability.generate_token()
        self.assertIsNotNone(token)

        decoded = jwt.decode(token, auth_token)
        self.assertIsNotNone(decoded)

        self.assertEqual(decoded["iss"], account_sid)
        self.assertEqual(decoded["account_sid"], account_sid)
        self.assertEqual(decoded["workspace_sid"], workspace_sid)
        self.assertEqual(decoded["worker_sid"], worker_sid)
        self.assertEqual(decoded["channel"], worker_sid)
        self.assertEqual(decoded["version"], "v1")
        self.assertEqual(decoded["friendly_name"], worker_sid)

        policies = decoded['policies']
        self.assertEqual(len(policies), 5)

        # activity GET
        fetch_activity = policies[0]
        self.assertEqual("https://taskrouter.twilio.com/v1/Workspaces/WS456/Activities", fetch_activity['url'])
        self.assertEqual("GET", fetch_activity['method'])
        self.assertTrue(fetch_activity['allowed'])
        self.assertEqual({}, fetch_activity['query_filter'])
        self.assertEqual({}, fetch_activity['post_filter'])

        # reservation GET
        fetch_reservation = policies[1]
        self.assertEqual("https://taskrouter.twilio.com/v1/Workspaces/WS456/Tasks/**", fetch_reservation['url'])
        self.assertEqual("GET", fetch_reservation['method'])
        self.assertTrue(fetch_reservation['allowed'])
        self.assertEqual({}, fetch_reservation['query_filter'])
        self.assertEqual({}, fetch_reservation['post_filter'])

        # websocket GET
        get_policy = policies[2]
        self.assertEqual("https://event-bridge.twilio.com/v1/wschannels/AC123/WK789", get_policy['url'])
        self.assertEqual("GET", get_policy['method'])
        self.assertTrue(get_policy['allowed'])
        self.assertEqual({}, get_policy['query_filter'])
        self.assertEqual({}, get_policy['post_filter'])

        # websocket POST
        post_policy = policies[3]
        self.assertEqual("https://event-bridge.twilio.com/v1/wschannels/AC123/WK789", post_policy['url'])
        self.assertEqual("POST", post_policy['method'])
        self.assertTrue(post_policy['allowed'])
        self.assertEqual({}, post_policy['query_filter'])
        self.assertEqual({}, post_policy['post_filter'])

        # fetch GET
        fetch_policy = policies[4]
        self.assertEqual("https://taskrouter.twilio.com/v1/Workspaces/WS456/Workers/WK789", fetch_policy['url'])
        self.assertEqual("GET", fetch_policy['method'])
        self.assertTrue(fetch_policy['allowed'])
        self.assertEqual({}, fetch_policy['query_filter'])
        self.assertEqual({}, fetch_policy['post_filter'])

    def test_task_queue_default(self):
        account_sid = "AC123"
        auth_token = "foobar"
        workspace_sid = "WS456"
        taskqueue_sid = "WQ789"
        capability = TaskRouterCapability(account_sid, auth_token, workspace_sid, taskqueue_sid)

        capability.generate_token()

        token = capability.generate_token()
        self.assertIsNotNone(token)

        decoded = jwt.decode(token, auth_token)
        self.assertIsNotNone(decoded)

        self.assertEqual(decoded["iss"], account_sid)
        self.assertEqual(decoded["account_sid"], account_sid)
        self.assertEqual(decoded["workspace_sid"], workspace_sid)
        self.assertEqual(decoded["taskqueue_sid"], taskqueue_sid)
        self.assertEqual(decoded["channel"], taskqueue_sid)
        self.assertEqual(decoded["version"], "v1")
        self.assertEqual(decoded["friendly_name"], taskqueue_sid)

        policies = decoded['policies']
        self.assertEqual(len(policies), 3)

        # websocket GET
        get_policy = policies[0]
        self.assertEqual("https://event-bridge.twilio.com/v1/wschannels/AC123/WQ789", get_policy['url'])
        self.assertEqual("GET", get_policy['method'])
        self.assertTrue(get_policy['allowed'])
        self.assertEqual({}, get_policy['query_filter'])
        self.assertEqual({}, get_policy['post_filter'])

        # websocket POST
        post_policy = policies[1]
        self.assertEqual("https://event-bridge.twilio.com/v1/wschannels/AC123/WQ789", post_policy['url'])
        self.assertEqual("POST", post_policy['method'])
        self.assertTrue(post_policy['allowed'])
        self.assertEqual({}, post_policy['query_filter'])
        self.assertEqual({}, post_policy['post_filter'])

        # fetch GET
        fetch_policy = policies[2]
        self.assertEqual("https://taskrouter.twilio.com/v1/Workspaces/WS456/TaskQueues/WQ789", fetch_policy['url'])
        self.assertEqual("GET", fetch_policy['method'])
        self.assertTrue(fetch_policy['allowed'])
        self.assertEqual({}, fetch_policy['query_filter'])
        self.assertEqual({}, fetch_policy['post_filter'])

    def test_deprecated_worker(self):
        account_sid = "AC123"
        auth_token = "foobar"
        workspace_sid = "WS456"
        worker_sid = "WK789"
        capability = TaskRouterCapability(account_sid, auth_token, workspace_sid, worker_sid)

        capability.generate_token()

        token = capability.generate_token()
        self.assertIsNotNone(token)

        decoded = jwt.decode(token, auth_token)
        self.assertIsNotNone(decoded)

        self.assertEqual(decoded["iss"], account_sid)
        self.assertEqual(decoded["account_sid"], account_sid)
        self.assertEqual(decoded["workspace_sid"], workspace_sid)
        self.assertEqual(decoded["worker_sid"], worker_sid)
        self.assertEqual(decoded["channel"], worker_sid)
        self.assertEqual(decoded["version"], "v1")
        self.assertEqual(decoded["friendly_name"], worker_sid)

        policies = decoded['policies']
        self.assertEqual(len(policies), 5)

        # should expect 5 policies

        # activity GET
        fetch_activity = policies[0]
        self.assertEqual("https://taskrouter.twilio.com/v1/Workspaces/WS456/Activities", fetch_activity['url'])
        self.assertEqual("GET", fetch_activity['method'])
        self.assertTrue(fetch_activity['allowed'])
        self.assertEqual({}, fetch_activity['query_filter'])
        self.assertEqual({}, fetch_activity['post_filter'])

        # reservation GET
        fetch_reservation = policies[1]
        self.assertEqual("https://taskrouter.twilio.com/v1/Workspaces/WS456/Tasks/**", fetch_reservation['url'])
        self.assertEqual("GET", fetch_reservation['method'])
        self.assertTrue(fetch_reservation['allowed'])
        self.assertEqual({}, fetch_reservation['query_filter'])
        self.assertEqual({}, fetch_reservation['post_filter'])

        # websocket GET
        get_policy = policies[2]
        self.assertEqual("https://event-bridge.twilio.com/v1/wschannels/AC123/WK789", get_policy['url'])
        self.assertEqual("GET", get_policy['method'])
        self.assertTrue(get_policy['allowed'])
        self.assertEqual({}, get_policy['query_filter'])
        self.assertEqual({}, get_policy['post_filter'])

        # websocket POST
        post_policy = policies[3]
        self.assertEqual("https://event-bridge.twilio.com/v1/wschannels/AC123/WK789", post_policy['url'])
        self.assertEqual("POST", post_policy['method'])
        self.assertTrue(post_policy['allowed'])
        self.assertEqual({}, post_policy['query_filter'])
        self.assertEqual({}, post_policy['post_filter'])

        # fetch GET
        fetch_policy = policies[4]
        self.assertEqual("https://taskrouter.twilio.com/v1/Workspaces/WS456/Workers/WK789", fetch_policy['url'])
        self.assertEqual("GET", fetch_policy['method'])
        self.assertTrue(fetch_policy['allowed'])
        self.assertEqual({}, fetch_policy['query_filter'])
        self.assertEqual({}, fetch_policy['post_filter'])

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
