import json
import logging
from mock import Mock
from tests.holodeck.base import Request
from tests.holodeck.twiliodeck import TwilioDeck
from twilio.rest.resources.imports import httplib2
from twilio.rest.resources import base


class Holodeck(object):

    def __init__(self):
        self._orig_method = base.make_request
        self._request_handlers = []
        self._active = False
        self._twiliodeck = TwilioDeck(self)

    def activate(self):
        if isinstance(self._orig_method, Mock):
            raise Exception('Another instance of Holodeck is already active')
        self._activate = True
        self.enable_twiliodeck()

        base.make_request = Mock()
        base.make_request.side_effect = self._handle_request

    def enable_twiliodeck(self):
        self._twiliodeck.activate()

    def disable_twiliodeck(self):
        self._twiliodeck.deactivate()

    def deactivate(self):
        if not self._active:
            return

        base.make_request = self._orig_method

    def add(self, request_handler):
        self._request_handlers.append(request_handler)

    def remove(self, request_handler):
        self._request_handlers.remove(request_handler)

    def _handle_request(self, method, url, params=None,
                        data=None, headers=None,
                        cookies=None, files=None,
                        auth=None, timeout=None,
                        allow_redirects=False, proxies=None):

        request = Request(url, method, auth, params or data, headers)

        similarity = 0
        closest_handler = None

        # serve using the most recent matching handler
        for handler in reversed(self._request_handlers):
            if handler.can_serve(request):
                return base.Response(httplib2.Response({
                    'status': str(handler.status_code)
                }), handler.content, url)

            else:
                handler_similarity = handler.similarity(request)
                if handler_similarity > similarity:
                    similarity = handler_similarity
                    closest_handler = handler

        logging.debug('Holodeck could not find handler '
                      'for request :\n%s' % request)

        if closest_handler:
            logging.debug('Did you incorrectly configure '
                          'this handler :\n%s' % closest_handler)

        return base.Response(httplib2.Response({
            'status': '404'
        }), 'Not found - did you forget to configure Holodeck?', url)
