import logging
from typing import Dict, Optional, Tuple

from aiohttp import ClientSession
from aiohttp_retry import ExponentialRetry, RetryClient

from twilio.http import AsyncHttpClient
from twilio.http.request import Request as TwilioRequest
from twilio.http.response import Response

try:
    from aiohttp import encode_basic_auth as _aiohttp_encode_basic_auth
except ImportError:
    from aiohttp import BasicAuth

    def _aiohttp_encode_basic_auth(
        login: str, password: str = "", encoding: str = "utf-8"
    ) -> str:
        """Encode Basic Auth credentials on aiohttp versions before 3.14."""
        return BasicAuth(login=login, password=password, encoding=encoding).encode()


_logger = logging.getLogger("twilio.async_http_client")


def _validate_basic_auth(login: str, password: str) -> None:
    """Validate Basic Auth credentials using aiohttp's legacy rules."""
    if login is None:
        raise ValueError("None is not allowed as login value")
    if password is None:
        raise ValueError("None is not allowed as password value")
    if ":" in login:
        raise ValueError('A ":" is not allowed in login (RFC 1945#section-11.1)')


class AsyncTwilioHttpClient(AsyncHttpClient):
    """
    General purpose asynchronous HTTP Client for interacting with the Twilio API
    """

    def __init__(
        self,
        pool_connections: bool = True,
        trace_configs=None,
        timeout: Optional[float] = None,
        logger: logging.Logger = _logger,
        proxy_url: Optional[str] = None,
        max_retries: Optional[int] = None,
    ):
        """
        Constructor for the AsyncTwilioHttpClient

        :param pool_connections: Creates a client session for making requests from.
        :param trace_configs: Configuration used to trace request lifecycle events. See aiohttp library TraceConfig
                              documentation for more info.
        :param timeout: Timeout for the requests (seconds)
        :param logger
        :param proxy_url: Proxy URL
        :param max_retries: Maximum number of retries each request should attempt
        """
        super().__init__(logger, True, timeout)
        self.proxy_url = proxy_url
        self.trace_configs = trace_configs
        self.session = (
            ClientSession(trace_configs=self.trace_configs)
            if pool_connections
            else None
        )
        if max_retries is not None:
            retry_options = ExponentialRetry(attempts=max_retries)
            self.session = RetryClient(
                client_session=self.session, retry_options=retry_options
            )

    async def request(
        self,
        method: str,
        url: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Response:
        """
        Make an asynchronous HTTP Request with parameters provided.

        :param method: The HTTP method to use
        :param url: The URL to request
        :param params: Query parameters to append to the URL
        :param data: Parameters to go in the body of the HTTP request
        :param headers: HTTP Headers to send with the request
        :param auth: Basic Auth arguments (username, password entries)
        :param timeout: Socket/Read timeout for the request. Overrides the timeout if set on the client.
        :param allow_redirects: Whether or not to allow redirects
        See the requests documentation for explanation of all these parameters

        :return: An http response
        """
        if timeout is not None and timeout <= 0:
            raise ValueError(timeout)

        request_headers = headers
        if auth is not None:
            _validate_basic_auth(auth[0], auth[1])
            if headers is not None and any(
                name.lower() == "authorization" for name in headers
            ):
                raise ValueError(
                    "Cannot combine AUTHORIZATION header "
                    "with AUTH argument or credentials encoded in URL"
                )
            authorization = _aiohttp_encode_basic_auth(
                auth[0], auth[1], encoding="latin1"
            )
            request_headers = headers.copy() if headers is not None else {}
            request_headers["Authorization"] = authorization

        kwargs = {
            "method": method.upper(),
            "url": url,
            "params": params,
            "data": data,
            "headers": request_headers,
            "timeout": timeout,
            "allow_redirects": allow_redirects,
        }

        self.log_request(kwargs)
        self._test_only_last_response = None

        temp = False
        session = None
        if self.session:
            session = self.session
        else:
            session = ClientSession()
            temp = True
        self._test_only_last_request = TwilioRequest(auth=None, **kwargs)
        response = await session.request(**kwargs)
        self.log_response(response.status, response)
        self._test_only_last_response = Response(
            response.status, await response.text(), response.headers
        )
        if temp:
            await session.close()
        return self._test_only_last_response

    async def close(self):
        """
        Closes the HTTP client session
        """
        if self.session:
            await self.session.close()

    async def __aenter__(self):
        """
        Async context manager setup
        """
        return self

    async def __aexit__(self, *excinfo):
        """
        Async context manager exit
        """
        if self.session:
            await self.session.close()
