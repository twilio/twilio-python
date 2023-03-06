import aiohttp
import logging

from aiohttp import BasicAuth
from aiohttp_retry import ExponentialRetry, RetryClient
from twilio.http import AsyncHttpClient
from twilio.http.request import Request as TwilioRequest
from twilio.http.response import Response
from urllib.parse import urlencode

_logger = logging.getLogger('twilio.http_client')


class AsyncTwilioHttpClient(AsyncHttpClient):
    """
    General purpose asynchronous HTTP Client for interacting with the Twilio API
    """

    def __init__(self, pool_connections=True, trace_configs=None, timeout=None, logger=_logger, proxy_url=None,
                 max_retries=None):
        """
        Constructor for the AsyncTwilioHttpClient

        :param bool pool_connections: Creates a client session for making requests from.
        :param trace_configs: Configuration used to trace request lifecycle events. See aiohttp library TraceConfig
                              documentation for more info.
        :param float timeout: Timeout for the requests (seconds)
        :param logger
        :param str proxy_url: Proxy URL
        :param int max_retries: Maximum number of retries each request should attempt
        """
        self.is_async = True
        self._test_only_last_request = None
        self._test_only_last_response = None
        self.logger = logger
        self.proxy_url = proxy_url

        if timeout is not None and timeout <= 0:
            raise ValueError(timeout)

        self.timeout = timeout
        self.trace_configs = trace_configs
        self.session = aiohttp.ClientSession(trace_configs=self.trace_configs) if pool_connections else None
        if max_retries is not None:
            retry_options = ExponentialRetry(attempts=max_retries)
            self.session = RetryClient(client_session=self.session, retry_options=retry_options)

    async def request(self, method, url, params=None, data=None, headers=None, auth=None, timeout=None,
                      allow_redirects=False):
        """
        Make an asynchronous HTTP Request with parameters provided.

        :param str method: The HTTP method to use
        :param str url: The URL to request
        :param dict params: Query parameters to append to the URL
        :param dict data: Parameters to go in the body of the HTTP request
        :param dict headers: HTTP Headers to send with the request
        :param tuple(str, str) auth: Basic Auth arguments (username, password entries)
        :param float timeout: Socket/Read timeout for the request. Overrides the timeout if set on the client.
        :param boolean allow_redirects: Whether or not to allow redirects
        See the requests documentation for explanation of all these parameters

        :return: An http response
        :rtype: A :class:`Response <twilio.rest.http.response.Response>` object
        """
        if timeout is not None and timeout <= 0:
            raise ValueError(timeout)

        basic_auth = None
        if auth is not None:
            basic_auth = BasicAuth(login=auth.username, password=auth.password)

        kwargs = {
            'method': method.upper(),
            'url': url,
            'params': params,
            'data': data,
            'headers': headers,
            'auth': basic_auth,
            'timeout': timeout,
            'allow_redirects': allow_redirects
        }

        self._log_request(kwargs)
        self._test_only_last_response = None

        session = self.session if not None else aiohttp

        self._test_only_last_request = TwilioRequest(**kwargs)
        response = await session.request(**kwargs)
        self._log_response(response)
        self._test_only_last_response = Response(response.status, await response.text(), response.headers)
        return self._test_only_last_response

    async def close(self):
        if self.session:
            await self.session.close()

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
        self.logger.info('Response Status Code: {}'.format(response.status))
        self.logger.info('Response Headers: {}'.format(response.headers))

    async def __aenter__(self):
        """
        Async context manager setup
        """
        return self

    async def __aexit__(self, *excinfo):
        """
        Async context manager exit
        """
        await self.session.close()
