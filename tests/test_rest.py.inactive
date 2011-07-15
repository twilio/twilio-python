import json
import os
import unittest

from datetime import datetime
from datetime import date
from mock import patch
from mock import Mock
from twilio import TwilioException
from twilio import TwilioRestException
from twilio.rest import TwilioRestClient as TwilioClient
from twilio.rest.resources import *

ACCOUNT_SID = "AC111111111"
AUTH_TOKEN  = "AUTH_TOKEN"
BASE_URI    = "https://api.twilio.com/2010-04-01/"
ACCOUNT_URI = "{0}Accounts/{1}/".format(BASE_URI, ACCOUNT_SID)

DEFAULT_HEADERS = {
    'User-Agent': 'twilio-python/3.0.0',
    }

FORM_CONTENT_TYPE = {
    'Content-type': 'application/x-www-form-urlencoded',
    'User-Agent': 'twilio-python/3.0.0',
    }

def create_mock_request(status=200, content="{}"):
    request = Mock()
    resp = Mock()
    resp.status = status
    resp.reason = "CREATED"
    request.return_value = resp, content
    return request

class GeneralResourceTest(unittest.TestCase):

    def setUp(self):
        self.c = TwilioClient(account=ACCOUNT_SID, token=AUTH_TOKEN)

    def mock_request(self, status=200, content="{}"):
        request = Mock()
        resp = Mock()
        resp.status = status
        resp.reason = "CREATED"
        request.return_value = resp, content
        self.c.client.request = request
        return request

class ListResourceTest(GeneralResourceTest):

    def check_list_uri(self, resource, e_uri, **kwargs):
        body = '{"%s":[]}' % resource.key
        request = self.mock_request(content=body)
        resource.list(**kwargs)
        request.assert_called_with(e_uri, method="GET",
                                   headers=DEFAULT_HEADERS)

    def check_delete_uri(self, resource, sid, e_uri):
        request = self.mock_request()
        resource.delete(sid)
        request.assert_called_with(e_uri, method="DELETE",
                                   headers=DEFAULT_HEADERS)

    def check_update_uri(self, resource, sid, e_uri, body, **kwargs):
        request = self.mock_request(content='{"sid":"hey"}')
        resource.update(sid, **kwargs)
        request.assert_called_with(e_uri, method="POST", body=body,
                                   headers=FORM_CONTENT_TYPE)

    def check_paging(self, resource, response, uri):
        request = self.mock_request(content=response)
        resource.list(page=2)
        request.assert_called_with(uri, method="GET",
                                   headers=DEFAULT_HEADERS)

class InstanceResourceTest(GeneralResourceTest):

    def check_update_uri(self, resource, e_uri, body, **kwargs):
        request = self.mock_request(content='{"sid":"hey"}')
        resource.update(**kwargs)
        request.assert_called_with(e_uri, method="POST", body=body,
                                   headers=FORM_CONTENT_TYPE)

    def check_delete_uri(self, resource, e_uri):
        request = self.mock_request(content='{"sid":"hey"}')
        resource.delete()
        request.assert_called_with(e_uri, method="DELETE",
                                   headers=DEFAULT_HEADERS)

class ClientTest(unittest.TestCase):

    def setUp(self):
        self.c = TwilioClient(account=ACCOUNT_SID, token=AUTH_TOKEN)

    def test_creation(self):
        c = TwilioClient(account=ACCOUNT_SID, token=AUTH_TOKEN)
        self.assertEquals(c.account_sid, ACCOUNT_SID)
        self.assertEquals(c.auth_token, AUTH_TOKEN)

    def test_creation_env_variables(self):
        creds = {
            "TWILIO_ACCOUNT_SID": ACCOUNT_SID,
            "TWILIO_AUTH_TOKEN": AUTH_TOKEN,
            }

        with patch.dict(os.environ, creds):
            c = TwilioClient()

        self.assertEquals(c.account_sid, ACCOUNT_SID)
        self.assertEquals(c.auth_token, AUTH_TOKEN)

    def test_credential_adding(self):
        client = Mock()
        client.add_credentials = Mock()
        c = TwilioClient(account=ACCOUNT_SID, token=AUTH_TOKEN, client=client)

        client.add_credentials.assert_called_with(ACCOUNT_SID, AUTH_TOKEN)

    def test_creation_fails(self):
        with self.assertRaises(TwilioException) as cm:
            with patch.dict(os.environ, {}, clear=True):
                c = TwilioClient()

    def test_notificaitons_uri(self):
        uri = "{0}Notifications".format(ACCOUNT_URI)
        self.assertEquals(self.c.notifications.uri, uri)


class ResourceTest(unittest.TestCase):

    def setUp(self):
        mock_http, request, self.resp = Mock(), Mock(), Mock()
        request.return_value = self.resp, ""
        mock_http.request = request
        self.c = TwilioClient(account=ACCOUNT_SID, token=AUTH_TOKEN,
                              client=mock_http)

    def test_not_found(self):
        self.resp.status = 404
        self.resp.description = "NOT FOUND"
        with self.assertRaises(TwilioRestException) as cm:
            self.c.accounts.create(friendly_name="MyNewAccount")

    def test_auth_required(self):
        self.resp.status = 401
        self.resp.description = "AUTH REQUIRED"
        with self.assertRaises(TwilioRestException) as cm:
            self.c.accounts.create(friendly_name="MyNewAccount")

class AccountsTest(ListResourceTest):

    def setUp(self):
        self.mock_http = Mock()
        self.c = TwilioClient(account=ACCOUNT_SID, token=AUTH_TOKEN,
                              client=self.mock_http)

    def test_paging(self):
        with open("tests/resources/accounts_list.json") as f:
            uri = "{0}Accounts.json?Page=2".format(BASE_URI)
            self.check_paging(self.c.accounts, f.read(), uri)

    def test_uri(self):
        uri = "{0}Accounts".format(BASE_URI)
        self.assertEquals(self.c.accounts.uri, uri)

    def test_create_wrong_arg(self):
        with self.assertRaises(TypeError) as cm:
            a = self.c.accounts.create()

    def test_create(self):
        with open("tests/resources/accounts_instance.json") as f:
            content = f.read()

        request = create_mock_request(201, content)
        self.mock_http.request = request

        c = self.c.accounts.create(friendly_name="account_name")

        entries = json.loads(content)
        self.assertEquals(c.sid, entries["sid"])
        self.assertEquals(c.date_created, entries["date_created"])
        self.assertEquals(c.date_updated, entries["date_updated"])
        self.assertEquals(c.status, entries["status"])
        self.assertEquals(c.auth_token, entries["auth_token"])

    def test_get_uri(self):

        account_sid = "AC4bf2dafb92341f7caf8650403e422d23"
        expected_uri = "{0}Accounts/{1}.json".format(BASE_URI,account_sid)

        request = create_mock_request()
        self.mock_http.request = request

        with self.assertRaises(TwilioException) as cm:
            c = self.c.accounts.get(account_sid)

        request.assert_called_with(expected_uri, method="GET",
                                   headers=DEFAULT_HEADERS)

    def test_list_uri(self):

        expected_uri = "{0}Accounts.json".format(BASE_URI)

        request = create_mock_request()
        self.mock_http.request = request

        with self.assertRaises(TwilioException) as cm:
            c = self.c.accounts.list()

        request.assert_called_with(expected_uri, method="GET",
                                   headers=DEFAULT_HEADERS)

    def test_list_uri_filter(self):

        expected_uri = "{0}Accounts.json?FriendlyName=You&Status=active".format(BASE_URI)

        request = create_mock_request()
        self.mock_http.request = request

        with self.assertRaises(TwilioException) as cm:
            c = self.c.accounts.list(friendly_name="You", status="active")

        request.assert_called_with(expected_uri, method="GET",
                                   headers=DEFAULT_HEADERS)

    def test_update_uri(self):
        account_sid = "AC4bf2dafb92341f7caf8650403e422d23"
        expected_uri = "{0}Accounts/{1}.json".format(BASE_URI, account_sid)

        request = create_mock_request()
        self.mock_http.request = request
        with self.assertRaises(TwilioException) as cm:
            c = self.c.accounts.update(account_sid, friendly_name="You")

        body = "FriendlyName=You"
        request.assert_called_with(expected_uri, method="POST", body=body,
                                   headers=FORM_CONTENT_TYPE)

    def test_instance_update_uri(self):
        account_sid = "AC4bf2dafb92341f7caf8650403e422d23"
        base_uri = "{0}Accounts".format(BASE_URI)
        expected_uri = "{0}Accounts/{1}.json".format(BASE_URI, account_sid)

        request = create_mock_request()
        self.mock_http.request = request
        a = Account(self.c.accounts, base_uri, {"sid": account_sid})

        with self.assertRaises(TwilioException) as cm:
            c = a.update(friendly_name="You")

        body = "FriendlyName=You"
        request.assert_called_with(expected_uri, method="POST", body=body,
                                   headers=FORM_CONTENT_TYPE)

        with open("tests/resources/accounts_instance.json") as f:
            content = f.read()

    def test_close_uri(self):
        account_sid = "AC4bf2dafb92341f7caf8650403e422d23"
        expected_uri = "{0}Accounts/{1}.json".format(BASE_URI, account_sid)

        request = create_mock_request()
        self.mock_http.request = request
        with self.assertRaises(TwilioException) as cm:
            c = self.c.accounts.close(account_sid)

        body = "Status=closed"
        request.assert_called_with(expected_uri, method="POST", body=body,
                                   headers=FORM_CONTENT_TYPE)

    def test_request(self):
        request = create_mock_request(status=201)
        self.mock_http.request = request
        self.c.accounts._create_instance = Mock()

        self.c.accounts.create(friendly_name="MyNewAccount")

        uri = "{0}.json".format(self.c.accounts.uri)
        body = "FriendlyName=MyNewAccount"
        request.assert_called_with(uri, method="POST", body=body,
                                   headers=FORM_CONTENT_TYPE)

    def test_instance_creation(self):

        with open("tests/resources/accounts_instance.json") as f:
            content = f.read()

        entries = json.loads(content)

        print self.c.accounts.instance
        a = self.c.accounts._create_instance(entries)

        uri = "{0}Accounts/{1}".format(BASE_URI, entries["sid"])
        self.assertEquals(a.sid, entries["sid"])
        self.assertEquals(a.uri, uri)
        self.assertEquals(a.date_created, entries["date_created"])
        self.assertEquals(a.date_updated, entries["date_updated"])
        self.assertEquals(a.status, entries["status"])
        self.assertEquals(a.auth_token, entries["auth_token"])


class AccountTest(unittest.TestCase):

    ct = FORM_CONTENT_TYPE

    def setUp(self):
        self.mock_http = Mock()
        self.c = TwilioClient(account=ACCOUNT_SID, token=AUTH_TOKEN)

        self.account_sid = "AC4bf2dafb92341f7caf8650403e422d23"
        self.base_uri = "{0}Accounts".format(BASE_URI)
        self.expected_uri = "{0}Accounts/{1}.json".format(BASE_URI,
                                                          self.account_sid)
        self.account =  Account(self.c.accounts, {"sid": self.account_sid})


    def _validate(self, func, content_path, status):
        with open(content_path) as f:
            request = create_mock_request(content=f.read())
            self.mock_http.request = request

        func()

        request.assert_called_with(self.expected_uri, method="POST",
                                   body="Status={0}".format(status),
                                   headers=self.ct)

    def test_close(self):
        self._validate(self.account.close, "tests/resources/accounts_instance.json",
                       Account.CLOSED)

    def test_suspend(self):
        self._validate(self.account.suspend, "tests/resources/accounts_instance.json",
                       Account.SUSPENDED)

    def test_activate(self):
        self._validate(self.account.activate, "tests/resources/accounts_instance.json",
                       Account.ACTIVE)


class CallsTest(ListResourceTest):

    def test_paging(self):
        with open("tests/resources/calls_list.json") as f:
            uri = "{}Calls.json?Page=2".format(ACCOUNT_URI)
            self.check_paging(self.c.calls, f.read(), uri)

    def test_uri(self):
        uri = "{0}Calls".format(ACCOUNT_URI)
        self.assertEquals(self.c.calls.uri, uri)

    def test_get_uri(self):
        csid = "CA12312313"
        e_uri = "{0}Accounts/{1}/Calls/{2}.json".format(BASE_URI,
                                                        ACCOUNT_SID, csid)
        request = self.mock_request()
        with self.assertRaises(TwilioException) as cm:
            c = self.c.calls.get(csid)

        request.assert_called_with(e_uri, method="GET",
                                   headers=DEFAULT_HEADERS)

    def test_list_uri(self):
        query = "EndTime%3C=2009-01-31&StartTime%3E=2009-01-01&EndTime=2009-12-12"
        e_uri = "{0}Accounts/{1}/Calls.json?{2}".format(BASE_URI, ACCOUNT_SID,
                                                        query)
        request = self.mock_request()
        with self.assertRaises(TwilioException) as cm:
            c = self.c.calls.list(ended=date(2009,12,12),
                                  started_after="2009-01-01",
                                  ended_before=datetime.datetime(2009,1,31))

        request.assert_called_with(e_uri, method="GET",
                                   headers=DEFAULT_HEADERS)

    def test_create_uri(self):
        e_uri = "{0}Accounts/{1}/Calls.json".format(BASE_URI, ACCOUNT_SID)
        body = urllib.urlencode({
                "From":5551231234,
                "To":5551231234,
                "Url":"http://www.google.com",
                })
        request = self.mock_request()

        with self.assertRaises(TwilioException) as cm:
            c = self.c.calls.create(to=5551231234, from_=5551231234,
                                    url="http://www.google.com")

        request.assert_called_with(e_uri, method="POST", body=body,
                                   headers=FORM_CONTENT_TYPE)

    def test_hangup_uri(self):
        sid = "CA123123123123"
        e_uri = "{0}Accounts/{1}/Calls/{2}.json".format(BASE_URI, ACCOUNT_SID, sid)
        body = urllib.urlencode({"Status": Call.CANCELED})
        request = self.mock_request()

        with self.assertRaises(TwilioException) as cm:
            c = self.c.calls.hangup(sid)

        request.assert_called_with(e_uri, method="POST", body=body,
                                   headers=FORM_CONTENT_TYPE)

    def test_route_uri(self):
        sid = "CA123123123123"
        e_uri = "{0}Accounts/{1}/Calls/{2}.json".format(BASE_URI, ACCOUNT_SID, sid)
        body = urllib.urlencode({"Url": "http://www.google.com", "Method": "POST"})
        request = self.mock_request()

        with self.assertRaises(TwilioException) as cm:
            c = self.c.calls.route(sid, "http://www.google.com")

        request.assert_called_with(e_uri, method="POST", body=body,
                                   headers=FORM_CONTENT_TYPE)
class CallTest(unittest.TestCase):

    def setUp(self):
        self.c = TwilioClient(account=ACCOUNT_SID, token=AUTH_TOKEN)
        self.call_sid = "CA123123"
        self.base_uri = "{0}Accounts/{1}/Calls".format(BASE_URI, ACCOUNT_SID)
        self.call_uri = "{0}/{1}.json".format(self.base_uri, self.call_sid)

        self.call =  Call(self.c.calls, self.base_uri, {"sid": self.call_sid})

    def mock_request(self, status=200, content="{}"):
        request = Mock()
        resp = Mock()
        resp.status = status
        resp.reason = "CREATED"
        request.return_value = resp, content
        self.c.client.request = request
        return request

    def test_subresources(self):
        euri = "{1}/{0}/Notifications".format(self.call_sid, self.base_uri)
        self.assertEquals(euri, self.call.notifications.uri)

    def test_hangup(self):
        request = self.mock_request()

        try:
            self.call.hangup()
        except:
            pass

        request.assert_called_with(self.call_uri, method="POST",
                                   body="Status={0}".format(Call.CANCELED),
                                   headers=FORM_CONTENT_TYPE)

class CallerIdsTest(ListResourceTest):

    def test_paging(self):
        with open("tests/resources/outgoing_caller_ids_list.json") as f:
            uri = "{}OutgoingCallerIds.json?Page=2".format(ACCOUNT_URI)
            self.check_paging(self.c.caller_ids, f.read(), uri)

    def test_validate(self):

        with open("tests/resources/outgoing_caller_ids_validation.json") as f:
            content = f.read()

        e_uri = "{0}Accounts/{1}/OutgoingCallerIds.json".format(BASE_URI, ACCOUNT_SID)
        body = urllib.urlencode({
                "PhoneNumber": 5551231234,
                })
        request = self.mock_request(status=201, content=content)

        c = self.c.caller_ids.validate(5551231234)
        print c

        request.assert_called_with(e_uri, method="POST", body=body,
                                   headers=FORM_CONTENT_TYPE)
        self.assertTrue("validation_code" in c)

    def test_list(self):

        body = urllib.urlencode({
                "PhoneNumber": 5551231234,
                })
        e_uri = "{}OutgoingCallerIds.json?{}".format(ACCOUNT_URI,body)
        request = self.mock_request()

        with self.assertRaises(TwilioException) as cm:
            c = self.c.caller_ids.list(phone_number=5551231234)

        request.assert_called_with(e_uri, method="GET",
                                   headers=DEFAULT_HEADERS)

    def test_list_uri(self):
        uri =  "{}OutgoingCallerIds.json".format(ACCOUNT_URI)
        self.check_list_uri(self.c.caller_ids, uri)

    def test_delete_uri(self):
        sid = "CI123123"
        uri = "{}OutgoingCallerIds/{}.json".format(ACCOUNT_URI, sid)
        self.check_delete_uri(self.c.caller_ids, sid, uri)

    def test_update_uri(self):
        sid = "CI123123"
        uri = "{}OutgoingCallerIds/{}.json".format(ACCOUNT_URI, sid)
        body = urllib.urlencode({"FriendlyName": "MyCallerId"})
        self.check_update_uri(self.c.caller_ids, sid, uri, body,
                              friendly_name="MyCallerId")

class CallerIdTest(InstanceResourceTest):

    def setUp(self):
        self.c = TwilioClient(account=ACCOUNT_SID, token=AUTH_TOKEN)
        self.sid = "CA123123"
        self.base_uri = "{0}Accounts/{1}/OutgoingCallerIds".format(BASE_URI, ACCOUNT_SID)
        self.uri = "{0}/{1}.json".format(self.base_uri, self.sid)
        self.callerid =  CallerId(self.c.caller_ids, self.base_uri, {"sid": self.sid})

    def test_hangup(self):
        request = self.mock_request(content='{"sid":"asdh"}')
        self.check_update_uri(self.callerid, self.uri,
                              "FriendlyName=MyFriendlyName",
                              friendly_name="MyFriendlyName")

    def test_delete(self):
        request = self.mock_request(content='{"sid":"asdh"}')
        self.check_delete_uri(self.callerid, self.uri)

class NotificationsTest(ListResourceTest):

    def test_list_uri(self):
        uri =  "{}Notifications.json".format(ACCOUNT_URI)
        self.check_list_uri(self.c.notifications, uri)

    def test_list_uri_fiter(self):
        query = urllib.urlencode({"MessageDate<": "2009-10-10",
                                  "MessageDate>": "2010-10-10",
                                  "LogLevel": 1})
        uri =  "{}Notifications.json?{}".format(ACCOUNT_URI, query)
        self.check_list_uri(self.c.notifications, uri, before="2009-10-10",
                            after="2010-10-10", log_level=1)

    def test_delete_uri(self):
        sid = "N123123"
        uri = "{}Notifications/{}.json".format(ACCOUNT_URI, sid)
        self.check_delete_uri(self.c.notifications, sid, uri)

class NotificationTest(InstanceResourceTest):

    def setUp(self):
        self.c = TwilioClient(account=ACCOUNT_SID, token=AUTH_TOKEN)
        self.sid = "NO123123"
        self.base_uri = "{0}Accounts/{1}/Notifications".format(BASE_URI, ACCOUNT_SID)
        self.uri = "{0}/{1}.json".format(self.base_uri, self.sid)
        self.notification =  Notification(self.c.notifications, self.base_uri, {"sid": self.sid})

    def test_delete(self):
        request = self.mock_request(content='{"sid":"asdh"}')
        self.check_delete_uri(self.notification, self.uri)

    def test_paging(self):
        with open("tests/resources/notifications_list.json") as f:
            uri =  "{}.json?Page=2".format(self.base_uri)
            request = self.mock_request(content=f.read())
            self.c.notifications.list(page=2)
            request.assert_called_with(uri, method="GET",
                                       headers=DEFAULT_HEADERS)


class TranscriptionsTest(ListResourceTest):

    def test_list_uri(self):
        uri =  "{}Transcriptions.json".format(ACCOUNT_URI)
        self.check_list_uri(self.c.transcriptions, uri)

    def test_paging(self):
        with open("tests/resources/transcriptions_list.json") as f:
            uri =  "{}Transcriptions.json?Page=2".format(ACCOUNT_URI)
            request = self.mock_request(content=f.read())
            self.c.transcriptions.list(page=2)
            request.assert_called_with(uri, method="GET",
                                       headers=DEFAULT_HEADERS)

class PhoneNumbersTest(ListResourceTest):

    list_response = "tests/resources/incoming_phone_numbers_list.json"
    instancet_response = "tests/resources/incoming_phone_numbers_instance.json"

    def test_paging(self):
        with open(self.list_response) as f:
            uri = "{}IncomingPhoneNumbers.json?Page=2".format(ACCOUNT_URI)
            self.check_paging(self.c.phone_numbers, f.read(), uri)

    def test_list_uri(self):
        uri =  "{}IncomingPhoneNumbers.json".format(ACCOUNT_URI)
        self.check_list_uri(self.c.phone_numbers, uri)

    def test_delete_uri(self):
        sid = "PN123123"
        uri =  "{}IncomingPhoneNumbers/{}.json".format(ACCOUNT_URI, sid)
        self.check_delete_uri(self.c.phone_numbers, sid, uri)

    def test_check_count(self):
        with open("tests/resources/incoming_phone_numbers_list.json") as f:
            content = f.read()
            self.mock_request(content=content)
            self.assertEquals(self.c.phone_numbers.count(), 3)

class ConferencesTest(ListResourceTest):

    list_response = "tests/resources/conferences_list.json"
    instancet_response = "tests/resources/conferences_instance.json"

    def test_paging(self):
        with open(self.list_response) as f:
            uri = "{}Conferences.json?Page=2".format(ACCOUNT_URI)
            self.check_paging(self.c.conferences, f.read(), uri)

    def test_list_uri(self):
        uri =  "{}Conferences.json".format(ACCOUNT_URI)
        self.check_list_uri(self.c.conferences, uri)


class AvailableNumbersTest(ListResourceTest):

    def test_search_local_uri(self):
        uri =  "{}AvailablePhoneNumbers/US/Local.json".format(ACCOUNT_URI)
        body = '{"available_phone_numbers":[]}'
        request = self.mock_request(content=body)
        self.c.phone_numbers.search()
        request.assert_called_with(uri, method="GET",
                                   headers=DEFAULT_HEADERS)

    def test_search_local_uri(self):
        uri =  "{}AvailablePhoneNumbers/US/TollFree.json".format(ACCOUNT_URI)
        body = '{"available_phone_numbers":[]}'
        request = self.mock_request(content=body)
        self.c.phone_numbers.search(type="TOLLFREE")
        request.assert_called_with(uri, method="GET",
                                   headers=DEFAULT_HEADERS)


class RecordingsTest(ListResourceTest):

    list_response = "tests/resources/recordings_list.json"
    instancet_response = "tests/resources/recordings_instance.json"

    def test_paging(self):
        with open(self.list_response) as f:
            uri = "{}Recordings.json?Page=2".format(ACCOUNT_URI)
            self.check_paging(self.c.recordings, f.read(), uri)

    def test_list_uri(self):
        uri =  "{}Recordings.json".format(ACCOUNT_URI)
        self.check_list_uri(self.c.recordings, uri)
