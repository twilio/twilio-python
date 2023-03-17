import os
import platform
from typing import Dict, Optional, Tuple
from urllib.parse import urlparse, urlunparse

from twilio import __version__
from twilio.base.exceptions import TwilioException
from twilio.http import HttpClient
from twilio.http.http_client import TwilioHttpClient
from twilio.http.response import Response


class ClientBase(object):
    """A client for accessing the Twilio API."""

    def __init__(
        self,
        username=None,
        password=None,
        account_sid=None,
        region=None,
        http_client=None,
        environment=None,
        edge=None,
        user_agent_extensions=None,
    ):
        """
        Initializes the Twilio Client

        :param str username: Username to authenticate with
        :param str password: Password to authenticate with
        :param str account_sid: Account SID, defaults to Username
        :param str region: Twilio Region to make requests to, defaults to 'us1' if an edge is provided
        :param HttpClient http_client: HttpClient, defaults to TwilioHttpClient
        :param dict environment: Environment to look for auth details, defaults to os.environ
        :param str edge: Twilio Edge to make requests to, defaults to None
        :param list[str] user_agent_extensions: Additions to the user agent string
        """
        environment = environment or os.environ

        self.username = username or environment.get("TWILIO_ACCOUNT_SID")
        """ :type : str """
        self.password = password or environment.get("TWILIO_AUTH_TOKEN")
        """ :type : str """
        self.edge = edge or environment.get("TWILIO_EDGE")
        """ :type : str """
        self.region = region or environment.get("TWILIO_REGION")
        """ :type : str """
        self.user_agent_extensions = user_agent_extensions or []
        """ :type : list[str] """

        if not self.username or not self.password:
            raise TwilioException("Credentials are required to create a TwilioClient")

        self.account_sid = account_sid or self.username
        """ :type : str """
        self.auth = (self.username, self.password)
        """ :type : tuple(str, str) """
        self.http_client: HttpClient = http_client or TwilioHttpClient()
        """ :type : HttpClient """

    def request(
        self,
        method,
        uri,
        params=None,
        data=None,
        headers=None,
        auth=None,
        timeout=None,
        allow_redirects=False,
    ) -> Response:
        """
        Makes a request to the Twilio API using the configured http client
        Authentication information is automatically added if none is provided

        :param str method: HTTP Method
        :param str uri: Fully qualified url
        :param dict[str, str] params: Query string parameters
        :param dict[str, str] data: POST body data
        :param dict[str, str] headers: HTTP Headers
        :param tuple(str, str) auth: Authentication
        :param int timeout: Timeout in seconds
        :param bool allow_redirects: Should the client follow redirects

        :returns: Response from the Twilio API
        """
        auth = self.get_auth(auth)
        headers = self.get_headers(method, headers)
        uri = self.get_hostname(uri)

        return self.http_client.request(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
        )

    async def request_async(
        self,
        method,
        uri,
        params=None,
        data=None,
        headers=None,
        auth=None,
        timeout=None,
        allow_redirects=False,
    ) -> Response:
        """
        Asynchronously makes a request to the Twilio API  using the configured http client
        The configured http client must be an asynchronous http client
        Authentication information is automatically added if none is provided

        :param str method: HTTP Method
        :param str uri: Fully qualified url
        :param dict[str, str] params: Query string parameters
        :param dict[str, str] data: POST body data
        :param dict[str, str] headers: HTTP Headers
        :param tuple(str, str) auth: Authentication
        :param int timeout: Timeout in seconds
        :param bool allow_redirects: Should the client follow redirects

        :returns: Response from the Twilio API
        """
        if not self.http_client.is_async:
            raise RuntimeError(
                "http_client must be asynchronous to support async API requests"
            )

        auth = self.get_auth(auth)
        headers = self.get_headers(method, headers)
        uri = self.get_hostname(uri)

        return await self.http_client.request(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
        )

    def get_auth(self, auth: Optional[Tuple[str, str]]) -> Tuple[str, str]:
        """
        Get the request authentication object
        :param auth: Authentication (username, password)
        :returns: The authentication object
        """
        return auth or self.auth

    def get_headers(
        self, method: str, headers: Optional[Dict[str, str]]
    ) -> Dict[str, str]:
        """
        Get the request headers including user-agent, extensions, encoding, content-type, MIME type
        :param method: HTTP method
        :param headers: HTTP headers
        :returns: HTTP headers
        """
        headers = headers or {}

        # Set User-Agent
        pkg_version = __version__
        os_name = platform.system()
        os_arch = platform.machine()
        python_version = platform.python_version()
        headers["User-Agent"] = "twilio-python/{} ({} {}) Python/{}".format(
            pkg_version,
            os_name,
            os_arch,
            python_version,
        )
        # Extensions
        for extension in self.user_agent_extensions:
            headers["User-Agent"] += " {}".format(extension)
        headers["X-Twilio-Client"] = "python-{}".format(__version__)

        # Types, encodings, etc.
        headers["Accept-Charset"] = "utf-8"
        if method == "POST" and "Content-Type" not in headers:
            headers["Content-Type"] = "application/x-www-form-urlencoded"
        if "Accept" not in headers:
            headers["Accept"] = "application/json"

        return headers

    def get_hostname(self, uri: str) -> str:
        """
        Determines the proper hostname given edge and region preferences
        via client configuration or uri.

        :param uri: Fully qualified url

        :returns: The final uri used to make the request
        """
        if not self.edge and not self.region:
            return uri

        parsed_url = urlparse(uri)
        pieces = parsed_url.netloc.split(".")
        prefix = pieces[0]
        suffix = ".".join(pieces[-2:])
        region = None
        edge = None
        if len(pieces) == 4:
            # product.region.twilio.com
            region = pieces[1]
        elif len(pieces) == 5:
            # product.edge.region.twilio.com
            edge = pieces[1]
            region = pieces[2]

        edge = self.edge or edge
        region = self.region or region or (edge and "us1")

        parsed_url = parsed_url._replace(
            netloc=".".join([part for part in [prefix, edge, region, suffix] if part])
        )
        return str(urlunparse(parsed_url))

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio {}>".format(self.account_sid)
