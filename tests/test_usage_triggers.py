from mock import patch
from tools import create_mock_json
from twilio.rest.resources import UsageTriggers

BASE_URI = "https://api.twilio.com/2010-04-01/Accounts/AC123"
ACCOUNT_SID = "AC123"
AUTH = (ACCOUNT_SID, "token")

list_resource = UsageTriggers(BASE_URI, AUTH)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_create_trigger(request):
    resp = create_mock_json("tests/resources/usage_triggers_instance.json")
    resp.status_code = 201
    request.return_value = resp

    list_resource.create(
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
    }, auth=AUTH)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_paging(request):
    resp = create_mock_json("tests/resources/usage_triggers_list.json")
    request.return_value = resp

    uri = "%s/Usage/Triggers" % BASE_URI
    list_resource.list(
        recurring="daily",
        usage_category="sms",
        trigger_by="count")

    request.assert_called_with("GET", uri, params={
        "Recurring": "daily",
        "UsageCategory": "sms",
        "TriggerBy": "count"
    }, auth=AUTH)
