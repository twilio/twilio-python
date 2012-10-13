from mock import patch
from nose.tools import raises
from tools import create_mock_json
from twilio.rest.resources import UsageRecords

BASE_URI = "https://api.twilio.com/2010-04-01/Accounts/AC123"
ACCOUNT_SID = "AC123"
AUTH = (ACCOUNT_SID, "token")

list_resource = UsageRecords(BASE_URI, AUTH)


@patch("twilio.rest.resources.base.make_twilio_request")
def test_paging(request):
    resp = create_mock_json("tests/resources/usage_records_list.json")
    request.return_value = resp

    uri = "%s/Usage/Records" % BASE_URI
    list_resource.list(
        start_date="2012-10-12",
        end_date="2012-10-13",
        category="sms")

    request.assert_called_with("GET", uri, params={
        "StartDate": "2012-10-12",
        "EndDate": "2012-10-13",
        "Category": "sms"
    }, auth=AUTH)


@raises(AttributeError)
def test_create():
    list_resource.create


@raises(AttributeError)
def test_delete():
    list_resource.delete


@raises(AttributeError)
def test_get():
    list_resource.get('abc')
