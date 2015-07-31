import logging
import unittest
from mock import Mock
from tests.integration.api_responses import TwilioRequest
from twilio.rest.resources import base
from twilio.rest.resources.base import Response


class BaseIntegrationTest(unittest.TestCase):

    def setUp(self, base_uri=None, response_handlers=[]):
        self.response_handlers = response_handlers
        self.base_uri = base_uri

        if 'https' not in base_uri:
            self._make_request = base.make_request
            base.make_request = Mock(side_effect=self._generate_response)

    def tearDown(self):
        if 'https' not in self.base_uri:
            base.make_request = self._make_request

    def _generate_response(self, *args, **kwargs):
        request = TwilioRequest(*args, **kwargs)
        nearest_matches = []

        for handler in self.response_handlers:
            if handler.can_respond_to(request):
                return handler.response

            if handler.url == request.url:
                nearest_matches.append(handler)

        logging.error('Could not match the following request:')
        logging.error(request)

        if nearest_matches:
            logging.error('These are the nearest matching handlers:')
            logging.error(nearest_matches)

        return Response(Mock(status=404), request.url, request.url)
