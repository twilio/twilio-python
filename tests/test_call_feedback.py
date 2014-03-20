import unittest

from nose.tools import assert_equal
from mock import Mock, patch, ANY
from tools import create_mock_json
from twilio.rest.resources import Call

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
            timeout=ANY,
        )
