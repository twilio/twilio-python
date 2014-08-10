from nose.tools import assert_equal, assert_raises
from mock import patch

from twilio.rest.exceptions import TwilioException
from twilio.rest import TwilioRestClient, find_credentials


def test_creds_not_found():
    """ I shouldn't find credentials if they are not there """
    assert_equal(find_credentials({'foo': 'bar'}), (None, None))


def test_find_creds():
    """ I should find the credentials if they are there """
    env = {
        'TWILIO_ACCOUNT_SID': 'AC123',
        'foo': 'bar',
        'TWILIO_AUTH_TOKEN': '456',
    }
    assert_equal(find_credentials(env), ('AC123', '456'))


@patch("twilio.rest.find_credentials")
def test_creds_error(creds):
    creds.return_value = (None, None)
    assert_raises(TwilioException, TwilioRestClient)
