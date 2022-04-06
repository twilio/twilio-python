import logging

from requests import Request, Session, hooks
from requests.adapters import HTTPAdapter
from urllib.parse import urlencode
from twilio.http import HttpClient
from twilio.http.request import Request as TwilioRequest
from twilio.http.response import Response

_logger = logging.getLogger('twilio.http_client')


class TwilioHttpClient(HttpClient):
    """
    General purpose HTTP Client for interacting with the Twilio API
    """

    def __init__(self, pool_connections=True, request_hooks=None, timeout=None, logger=_logger, proxy=None,
                 max_retries=None):
        """
        Constructor for the TwilioHttpClient

        :param bool pool_connections
        :param request_hooks
        :param int timeout: Timeout for the requests.
                            Timeout should never be zero (0) or less.
        :param logger
        :param dict proxy: Http proxy for the requests session
        :param int max_retries: Maximum number of retries each request should attempt
        """
        self.session = Session() if pool_connections else None
        if self.session and max_retries is not None:
            self.session.mount('https://', HTTPAdapter(max_retries=max_retries))
        self.last_request = None
        self.last_response = None
        self.logger = logger
        self.request_hooks = request_hooks or hooks.default_hooks()

        if timeout is not None and timeout <= 0:
            raise ValueError(timeout)
        self.timeout = timeout
        self.proxy = proxy

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
        if timeout is not None and timeout <= 0:
            raise ValueError(timeout)

        kwargs = {
            'method': method.upper(),
            'url': url,
            'params': params,
            'data': data,
            'headers': headers,
            'auth': auth,
            'hooks': self.request_hooks
        }

        self._log_request(kwargs)

        self.last_response = None
        session = self.session or Session()
        if self.proxy:
            session.proxies = self.proxy
        request = Request(**kwargs)
        self.last_request = TwilioRequest(**kwargs)

        prepped_request = session.prepare_request(request)
        response = session.send(
            prepped_request,
            allow_redirects=allow_redirects,
            timeout=timeout if timeout is not None else self.timeout,
        )

        self._log_response(response)

        self.last_response = Response(int(response.status_code), response.text, response.headers)

        return self.last_response

    def _log_request(self, kwargs):
        self.logger.info('-- BEGIN Twilio API Request --')

        if kwargs['params']:
            self.logger.info('{} Request: {}?{}'.format(kwargs['method'], kwargs['url'], urlencode(kwargs['params'])))
            self.logger.info('Query Params: {}'.format(kwargs['params']))
        else:
            self.logger.info('{} Request: {}'.format(kwargs['method'], kwargs['url']))

        if kwargs['headers']:
            self.logger.info('Headers:')
            for key, value in kwargs['headers'].items():
                # Do not log authorization headers
                if 'authorization' not in key.lower():
                    self.logger.info('{} : {}'.format(key, value))

        self.logger.info('-- END Twilio API Request --')

    def _log_response(self, response):
        self.logger.info('Response Status Code: {}'.format(response.status_code))
        self.logger.info('Response Headers: {}'.format(response.headers))
