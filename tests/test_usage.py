from mock import patch, Mock
from nose.tools import raises

from tests.tools import create_mock_json
from twilio.rest.resources import Usage
from twilio.rest.resources.usage import UsageTriggers, UsageTrigger

BASE_URI = "https://api.twilio.com/2010-04-01/Accounts/AC123"
ACCOUNT_SID = "AC123"
AUTH = (ACCOUNT_SID, "token")

usage = Usage(BASE_URI, AUTH)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_triggers_create(request):
    resp = create_mock_json("tests/resources/usage_triggers_instance.json")
    resp.status_code = 201
    request.return_value = resp

    usage.triggers.create(
        friendly_name="foo",
        usage_category="sms",
        trigger_by="count",
        recurring="price",
        trigger_value="10.00",
        callback_url="http://www.example.com",
        callback_method="POST"
    )

    uri = "%s/Usage/Triggers" % BASE_URI
    request.assert_called_with("POST", uri, data={
        "FriendlyName": "foo",
        "UsageCategory": "sms",
        "TriggerBy": "count",
        "Recurring": "price",
        "TriggerValue": "10.00",
        "CallbackUrl": "http://www.example.com",
        "CallbackMethod": "POST"
    }, auth=AUTH, use_json_extension=True)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_triggers_paging(request):
    resp = create_mock_json("tests/resources/usage_triggers_list.json")
    request.return_value = resp

    uri = "%s/Usage/Triggers" % BASE_URI
    usage.triggers.list(
        recurring="daily",
        usage_category="sms",
        trigger_by="count")

    request.assert_called_with("GET", uri, params={
        "Recurring": "daily",
        "UsageCategory": "sms",
        "TriggerBy": "count"
    }, auth=AUTH, use_json_extension=True)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_records_paging(request):
    resp = create_mock_json("tests/resources/usage_records_list.json")
    request.return_value = resp

    uri = "%s/Usage/Records" % BASE_URI
    usage.records.list(
        start_date="2012-10-12",
        end_date="2012-10-13",
        category="sms")

    request.assert_called_with("GET", uri, params={
        "StartDate": "2012-10-12",
        "EndDate": "2012-10-13",
        "Category": "sms"
    }, auth=AUTH, use_json_extension=True)


@patch("twilio.rest.resources.base.Resource.request")
def test_delete_trigger(req):
    resp = Mock()
    resp.content = ""
    resp.status_code = 204
    req.return_value = resp, {}

    triggers = UsageTriggers("https://api.twilio.com", None)
    trigger = UsageTrigger(triggers, "UT123")
    trigger.delete()
    uri = "https://api.twilio.com/Usage/Triggers/UT123"
    req.assert_called_with("DELETE", uri)


@raises(AttributeError)
def test_records_create():
    usage.records.all.create


@raises(AttributeError)
def test_records_delete():
    usage.records.all.delete


@raises(AttributeError)
def test_records_get():
    usage.records.all.get('abc')
