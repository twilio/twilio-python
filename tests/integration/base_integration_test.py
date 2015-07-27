import unittest
from mock import Mock
from tests.integration import config
from tests.integration.api_responses import RESPONSE_HANDLERS, TwilioRequest
from twilio.rest.client import TwilioRestClient
from twilio.rest.resources import base
from twilio.rest.resources.base import Response


class BaseIntegrationTest(unittest.TestCase):

    def setUp(self, response_handlers=RESPONSE_HANDLERS):
        self.response_handlers = response_handlers
        self.client = TwilioRestClient(config.account_sid,
                                       config.auth_token,
                                       config.base_uri)

        if 'https' not in config.base_uri:
            self._make_request = base.make_request
            base.make_request = Mock(side_effect=self._generate_response)

    def tearDown(self):
        if 'https' not in config.base_uri:
            base.make_request = self._make_request

    def _generate_response(self, *args, **kwargs):
        request = TwilioRequest(*args, **kwargs)

        for handler in self.response_handlers:
            if handler.can_respond_to(request):
                return handler.response

        return Response(Mock(status=404), request.url, request.url)
