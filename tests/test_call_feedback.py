import unittest

from nose.tools import assert_equal
from mock import Mock, patch, ANY
from tests.tools import create_mock_json
from twilio.rest.resources import Call, Calls

AUTH = ('foo', 'bar')


class CallFeedbackTest(unittest.TestCase):

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get_call_feedback(self, request):
        resp = create_mock_json('tests/resources/call_feedback.json')
        request.return_value = resp

        mock = Mock()
        mock.uri = '/base'
        call = Call(mock, 'CA123')
        call.load_subresources()
        feedback = call.feedback.get()
        assert_equal(5, feedback.quality_score, 5)
        assert_equal(['imperfect-audio', 'post-dial-delay'], feedback.issues)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_create_call_feedback(self, request):
        resp = create_mock_json('tests/resources/call_feedback.json')
        resp.status_code = 201
        request.return_value = resp

        mock = Mock()
        mock.uri = '/base'
        mock.auth = AUTH
        call = Call(mock, 'CA123')
        call.load_subresources()
        feedback = call.feedback.create(
            quality_score=5,
            issues=['imperfect-audio', 'post-dial-delay'],
        )

        exp_data = {
            'QualityScore': 5,
            'Issues': ['imperfect-audio', 'post-dial-delay'],
        }
        assert_equal(5, feedback.quality_score, 5)
        assert_equal(['imperfect-audio', 'post-dial-delay'], feedback.issues)
        request.assert_called_with(
            "POST", "/base/CA123/Feedback",
            data=exp_data, auth=AUTH,
            timeout=ANY, use_json_extension=True,
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_create_call_feedback_one_request(self, request):
        resp = create_mock_json('tests/resources/call_feedback.json')
        resp.status_code = 201
        request.return_value = resp

        base_uri = 'https://api.twilio.com/2010-04-01/Accounts/AC123'
        account_sid = 'AC123'
        auth = (account_sid, "token")

        calls = Calls(base_uri, auth)
        uri = "%s/Calls/CA123/Feedback" % base_uri
        feedback = calls.feedback(
            'CA123',
            quality_score=5,
            issue=['imperfect-audio', 'post-dial-delay']
        )

        exp_data = {
            'QualityScore': 5,
            'Issue': ['imperfect-audio', 'post-dial-delay'],
        }

        assert_equal(['imperfect-audio', 'post-dial-delay'], feedback.issues)
        request.assert_called_with(
            "POST", uri,
            data=exp_data, auth=auth,
            use_json_extension=True,
        )


class CallFeedbackSummaryTest(unittest.TestCase):

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get_call_feedback_summary(self, request):
        resp = create_mock_json('tests/resources/call_feedback_summary.json')
        request.return_value = resp

        base_uri = 'https://api.twilio.com/2010-04-01/Accounts/AC123'
        account_sid = 'AC123'
        auth = (account_sid, "token")

        calls = Calls(base_uri, auth)
        uri = "%s/Calls/Summary" % base_uri
        feedback = calls.summary.get()
        assert_equal(10200, feedback.call_count)
        assert_equal(729, feedback.call_feedback_count)

        request.assert_called_with('GET', uri, params={}, auth=auth,
                                   use_json_extension=True)
