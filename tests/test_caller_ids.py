import sys
import json

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from mock import patch, Mock

from twilio.rest.resources import CallerId, CallerIds


account_sid = 'foo'
base_uri = u'/2010-04-01'
account_uri = u'%s/Accounts/%s' % (base_uri, account_sid)
caller_ids_uri = u'%s/OutgoingCallerIds' % account_uri
caller_id_sid = u'PN5de64aaa67d210f4294c0fc682eddd46'
caller_id_uri = u'%s/OutgoingCallerIds/%s' % (account_uri, caller_id_sid)
ajson = lambda uri: "%s.json" % uri

caller_ids_json = {
    u'end': 0,
    u'first_page_uri': "%s%s" % (ajson(caller_ids_uri), '?Page=0&PageSize=50'),
    u'last_page_uri': "%s%s" % (ajson(caller_ids_uri), '?Page=0&PageSize=50'),
    u'next_page_uri': None,
    u'num_pages': 1,
    u'outgoing_caller_ids': [
        {u'account_sid': account_sid,
         u'date_created': u'Mon, 27 Aug 2012 23:29:03 +0000',
         u'date_updated': u'Mon, 27 Aug 2012 23:29:03 +0000',
         u'friendly_name': u'(706) 555-4901',
         u'phone_number': u'+17065554901',
         u'sid': caller_id_sid,
         u'uri': ajson(caller_id_uri)}
    ],
    u'page': 0,
    u'page_size': 50,
    u'previous_page_uri': None,
    u'start': 0,
    u'total': 1,
    u'uri': ajson(caller_ids_uri)
}

caller_id_json = {
    u'account_sid': account_sid,
    u'date_created': u'Mon, 27 Aug 2012 23:29:03 +0000',
    u'date_updated': u'Mon, 27 Aug 2012 23:29:03 +0000',
    u'friendly_name': u'(706) 555-4901',
    u'phone_number': u'+17065554901',
    u'sid': caller_id_sid,
    u'uri': ajson(caller_id_uri)
}

validate_json = {
    u'account_sid': account_sid,
    u'call_sid': u'CA4543263561f0cf8f7636a59a8874cc48',
    u'friendly_name': None,
    u'phone_number': u'+14045551111',
    u'validation_code': u'209780'
}

update_json = {
    u'account_sid': u'ACe422163cdbde8c46ed55603c812af1b3',
    u'date_created': u'Mon, 27 Aug 2012 23:29:03 +0000',
    u'date_updated': u'Sun, 14 Oct 2012 06:27:01 +0000',
    u'friendly_name': u'my num',
    u'phone_number': u'+17065554901',
    u'sid': caller_id_sid,
    u'uri': ajson(caller_id_uri),
}


class CallerIdsTests(unittest.TestCase):

    def setUp(self):
        self.auth = (account_sid, "token")
        self.resource = CallerIds(account_uri, self.auth)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list(self, mtr):
        mtr.return_value = Mock()
        mtr.return_value.content = json.dumps(caller_ids_json)
        ret = self.resource.list()
        mtr.assert_called_with("GET", caller_ids_uri,
            params={}, auth=self.auth)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_validate(self, mtr):
        mtr.return_value = Mock()
        mtr.return_value.content = json.dumps(validate_json)
        num = u'+14045551111'
        ret = self.resource.validate(num)
        mtr.assert_called_with("POST", caller_ids_uri,
            data={"PhoneNumber": num}, auth=self.auth)
        self.assertEqual(validate_json, ret)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_update(self, mtr):
        mtr.return_value = Mock()
        mtr.return_value.content = json.dumps(update_json)
        self.resource.update(caller_id_sid, friendly_name="My Num")
        mtr.assert_called_with("POST", caller_id_uri,
            data={"FriendlyName": "My Num"}, auth=self.auth)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_delete(self, mtr):
        mtr.return_value = Mock()
        self.resource.delete(caller_id_sid)
        mtr.assert_called_with("DELETE", caller_id_uri, auth=self.auth)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_caller_id_delete(self, mtr):
        # CallerId.delete calls
        # InstanceResource.delete_instance
        # calls instance.parent.delete(instance.name) -- name is the sid
        # calls ListResource.delete_instance(parent, sid)
        # a somewhat circuitous route to calling the delete above
        mtr.return_value = Mock()
        cid = CallerId(self.resource, caller_id_sid)
        cid.delete()
        mtr.assert_called_with("DELETE", caller_id_uri, auth=self.auth)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_caller_id_update(self, mtr):
        mtr.return_value = Mock()
        mtr.return_value.content = json.dumps(update_json)
        cid = CallerId(self.resource, caller_id_sid)
        cid.update(friendly_name="My Num")
        mtr.assert_called_with("POST", caller_id_uri,
            data={"FriendlyName": "My Num"}, auth=self.auth)

