import unittest

from nose.tools import assert_equal
from mock import Mock, patch, ANY
from tests.tools import create_mock_json
from twilio.rest.http import HttpClient
from twilio.rest.resources import Call, Calls

AUTH = ('foo', 'bar')


class CallFeedbackTest(unittest.TestCase):

    def setUp(self):
        self.client = HttpClient()

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get_call_feedback(self, request):
        resp = create_mock_json('tests/resources/call_feedback.json')
        request.return_value = resp

        mock = Mock()
        mock.uri = '/base'
        mock.client = self.client
        call = Call(mock, 'CA123')
        call.load_subresources()
        feedback = call.feedback.get().execute()
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
        mock.client = self.client

        call = Call(mock, 'CA123')
        call.load_subresources()
        feedback = call.feedback.create(
            quality_score=5,
            issues=['imperfect-audio', 'post-dial-delay'],
        ).execute()

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
            client=self.client
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_create_call_feedback_one_request(self, request):
        resp = create_mock_json('tests/resources/call_feedback.json')
        resp.status_code = 201
        request.return_value = resp

        base_uri = 'https://api.twilio.com/2010-04-01/Accounts/AC123'
        account_sid = 'AC123'
        auth = (account_sid, "token")

        calls = Calls(self.client, base_uri, auth)
        uri = "%s/Calls/CA123/Feedback" % base_uri
        feedback = calls.feedback(
            'CA123',
            quality_score=5,
            issue=['imperfect-audio', 'post-dial-delay']
        ).execute()

        exp_data = {
            'QualityScore': 5,
            'Issue': ['imperfect-audio', 'post-dial-delay'],
        }

        assert_equal(['imperfect-audio', 'post-dial-delay'], feedback.issues)
        request.assert_called_with(
            "POST", uri,
            data=exp_data, auth=auth,
            use_json_extension=True,
            client=self.client
        )


class CallFeedbackSummaryTest(unittest.TestCase):

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get_call_feedback_summary(self, request):
        resp = create_mock_json('tests/resources/call_feedback_summary.json')
        request.return_value = resp

        base_uri = 'https://api.twilio.com/2010-04-01/Accounts/AC123'
        account_sid = 'AC123'
        auth = (account_sid, "token")
        client = HttpClient()

        calls = Calls(client, base_uri, auth)
        uri = "%s/Calls/FeedbackSummary/sid" % base_uri
        feedback = calls.summary.get('sid').execute()
        assert_equal(10200, feedback.call_count)
        assert_equal(729, feedback.call_feedback_count)

        request.assert_called_with('GET', uri, auth=auth,
                                   use_json_extension=True,
                                   client=client)
