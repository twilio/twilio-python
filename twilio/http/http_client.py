from requests import Request, Session, hooks

from twilio.http import HttpClient
from twilio.http.response import Response
from twilio.http.request import Request as TwilioRequest
import logging
from twilio.compat import urlencode

_logger = logging.getLogger('twilio.http_client')


class TwilioHttpClient(HttpClient):
    """
    General purpose HTTP Client for interacting with the Twilio API
    """
    def __init__(self, pool_connections=True, request_hooks=None):
        self.session = Session() if pool_connections else None
        self.last_request = None
        self.last_response = None
        self.request_hooks = request_hooks or hooks.default_hooks()

    def request(self, method, url, params=None, data=None, headers=None, auth=None, timeout=None,
                allow_redirects=False):
        """
        Make an HTTP Request with parameters provided.

        :param str method: The HTTP method to use
        :param str url: The URL to request
        :param dict params: Query parameters to append to the URL
        :param dict data: Parameters to go in the body of the HTTP request
        :param dict headers: HTTP Headers to send with the request
        :param tuple auth: Basic Auth arguments
        :param float timeout: Socket/Read timeout for the request
        :param boolean allow_redirects: Whether or not to allow redirects
        See the requests documentation for explanation of all these parameters

        :return: An http response
        :rtype: A :class:`Response <twilio.rest.http.response.Response>` object
        """

        kwargs = {
            'method': method.upper(),
            'url': url,
            'params': params,
            'data': data,
            'headers': headers,
            'auth': auth,
            'hooks': self.request_hooks
        }

        if params:
            _logger.info('{method} Request: {url}?{query}'.format(query=urlencode(params), **kwargs))
            _logger.info('PARAMS: {params}'.format(**kwargs))
        else:
            _logger.info('{method} Request: {url}'.format(**kwargs))
        if data:
            _logger.info('PAYLOAD: {data}'.format(**kwargs))

        self.last_response = None
        session = self.session or Session()
        request = Request(**kwargs)
        self.last_request = TwilioRequest(**kwargs)

        prepped_request = session.prepare_request(request)
        response = session.send(
            prepped_request,
            allow_redirects=allow_redirects,
            timeout=timeout,
        )

        _logger.info('{method} Response: {status} {text}'.format(method=method, status=response.status_code, text=response.text))

        self.last_response = Response(int(response.status_code), response.text)

        return self.last_response
