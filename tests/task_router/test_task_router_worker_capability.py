import sys

import time
import unittest
import warnings

from twilio import jwt
from twilio.task_router.capability import TaskRouterWorkerCapability

class TaskRouterWorkerCapabilityTest(unittest.TestCase):

  def setUp(self):
    self.account_sid = "AC123"
    self.auth_token = "foobar"
    self.workspace_sid = "WS456"
    self.worker_sid = "WK789"
    self.capability = TaskRouterWorkerCapability(self.account_sid, self.auth_token, self.workspace_sid, self.worker_sid)

  def test_generate_token(self):

    token = self.capability.generate_token()
    self.assertIsNotNone(token)

    decoded = jwt.decode(token, self.auth_token)
    self.assertIsNotNone(decoded)

    self.assertEqual(decoded["iss"], self.account_sid)
    self.assertEqual(decoded["account_sid"], self.account_sid)
    self.assertEqual(decoded["workspace_sid"], self.workspace_sid)
    self.assertEqual(decoded["worker_sid"], self.worker_sid)
    self.assertEqual(decoded["channel"], self.worker_sid)
    self.assertEqual(decoded["version"], "v1")
    self.assertEqual(decoded["friendly_name"], self.worker_sid)

  def test_generate_token_with_default_ttl(self): 
    token = self.capability.generate_token()
    self.assertIsNotNone(token)

    decoded = jwt.decode(token, self.auth_token)
    self.assertIsNotNone(decoded)

    self.assertEqual(int(time.time()) + 3600, decoded["exp"])

  def test_generate_token_with_custom_ttl(self): 
    ttl = 10000

    token = self.capability.generate_token(ttl)
    self.assertIsNotNone(token)

    decoded = jwt.decode(token, self.auth_token)
    self.assertIsNotNone(decoded)

    self.assertEqual(int(time.time()) + 10000, decoded["exp"])    

  def test_defaults(self): 
    token = self.capability.generate_token()
    self.assertIsNotNone(token)

    decoded = jwt.decode(token, self.auth_token)
    self.assertIsNotNone(decoded)

    websocket_url = 'https://event-bridge.twilio.com/v1/wschannels/%s/%s' % (self.account_sid, self.worker_sid)

    # expect 5 policies 
    policies = decoded['policies']
    self.assertEqual(len(policies), 5)

    # policy 0 - GET websocket 
    get_policy = policies[0]
    self.assertIsNotNone(get_policy)
    self.assertEqual(get_policy['url'], websocket_url)
    self.assertEqual(get_policy['method'], 'GET')
    self.assertTrue(get_policy['allowed'])
    self.assertEqual(get_policy['query_filter'], {})
    self.assertEqual(get_policy['post_filter'], {})

    # policy 1 - POST
    post_policy = policies[1]
    self.assertIsNotNone(post_policy)
    self.assertEqual(post_policy['url'], websocket_url)
    self.assertEqual(post_policy['method'], 'POST')
    self.assertTrue(post_policy['allowed'])
    self.assertEqual(post_policy['query_filter'], {})
    self.assertEqual(post_policy['post_filter'], {})

    # policy 2 - Worker fetch 
    worker_fetch_policy = policies[2]
    self.assertIsNotNone(worker_fetch_policy)
    self.assertEqual(worker_fetch_policy['url'], 'https://taskrouter.twilio.com/v1/Workspaces/WS456/Workers/WK789')
    self.assertEqual(worker_fetch_policy['method'], 'GET')
    self.assertTrue(worker_fetch_policy['allowed'])
    self.assertEqual(worker_fetch_policy['query_filter'], {})
    self.assertEqual(worker_fetch_policy['post_filter'], {})

    # policy 3 - Reservation fetch
    reservation_fetch_policy = policies[3]
    self.assertIsNotNone(reservation_fetch_policy)
    self.assertEqual(reservation_fetch_policy['url'], 'https://taskrouter.twilio.com/v1/Workspaces/WS456/Tasks/**')
    self.assertEqual(reservation_fetch_policy['method'], 'GET')
    self.assertTrue(reservation_fetch_policy['allowed'])
    self.assertEqual(reservation_fetch_policy['query_filter'], {})
    self.assertEqual(reservation_fetch_policy['post_filter'], {})

    # policy 4 - Activity fetch 
    activity_fetch_policy = policies[4]
    self.assertIsNotNone(activity_fetch_policy)
    self.assertEqual(activity_fetch_policy['url'], 'https://taskrouter.twilio.com/v1/Workspaces/WS456/Activities')
    self.assertEqual(activity_fetch_policy['method'], 'GET')
    self.assertTrue(activity_fetch_policy['allowed'])
    self.assertEqual(activity_fetch_policy['query_filter'], {})
    self.assertEqual(activity_fetch_policy['post_filter'], {})

  def test_allow_activity_updates(self): 

    # allow activity updates to the worker 
    self.capability.allow_activity_updates()

    token = self.capability.generate_token()
    self.assertIsNotNone(token)

    decoded = jwt.decode(token, self.auth_token)
    self.assertIsNotNone(decoded)

    policies = decoded['policies']
    self.assertEqual(len(policies), 6)
    policy = policies[5]

    url = "https://taskrouter.twilio.com/v1/Workspaces/%s/Workers/%s" % (self.workspace_sid, self.worker_sid)

    self.assertEqual(url, policy["url"])
    self.assertEqual("POST", policy["method"])
    self.assertTrue(policy["allowed"])
    self.assertIsNotNone(policy['post_filter'])
    self.assertEqual({}, policy['query_filter'])
    self.assertTrue(policy['post_filter']['ActivitySid'])

  def test_allow_reservation_updates(self): 
    # allow reservation updates
    self.capability.allow_reservation_updates()

    token = self.capability.generate_token()
    self.assertIsNotNone(token)

    decoded = jwt.decode(token, self.auth_token)
    self.assertIsNotNone(decoded)

    policies = decoded['policies']
    self.assertEqual(len(policies), 6)

    policy = policies[5]

    url = "https://taskrouter.twilio.com/v1/Workspaces/%s/Tasks/**" % self.workspace_sid

    self.assertEqual(url, policy["url"])
    self.assertEqual("POST", policy["method"])
    self.assertTrue(policy["allowed"])
    self.assertIsNotNone(policy["post_filter"])
    self.assertEqual({}, policy["query_filter"])
    self.assertTrue(policy["post_filter"]["ReservationStatus"])

if __name__ == "__main__":
  unittest.main()
