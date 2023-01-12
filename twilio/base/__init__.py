import os
import platform
from twilio import __version__
from twilio.base.exceptions import TwilioException
from twilio.base.obsolete import obsolete_client
from twilio.http.http_client import TwilioHttpClient
from urllib.parse import (
    urlparse,
    urlunparse,
)


class ClientBase(object):
    """ A client for accessing the Twilio API. """

    def __init__(self, username=None, password=None, account_sid=None, region=None,
                 http_client=None, environment=None, edge=None,
                 user_agent_extensions=None):
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

        :returns: Twilio Client
        :rtype: twilio.rest.Client
        """
        environment = environment or os.environ

        self.username = username or environment.get('TWILIO_ACCOUNT_SID')
        """ :type : str """
        self.password = password or environment.get('TWILIO_AUTH_TOKEN')
        """ :type : str """
        self.account_sid = account_sid or self.username
        """ :type : str """
        self.edge = edge or environment.get('TWILIO_EDGE')
        """ :type : str """
        self.region = region or environment.get('TWILIO_REGION')
        """ :type : str """
        self.user_agent_extensions = user_agent_extensions or []
        """ :type : list[str] """

        if not self.username or not self.password:
            raise TwilioException("Credentials are required to create a TwilioClient")

        self.auth = (self.username, self.password)
        """ :type : tuple(str, str) """
        self.http_client = http_client or TwilioHttpClient()
        """ :type : HttpClient """

    def request(self, method, uri, params=None, data=None, headers=None, auth=None,
                timeout=None, allow_redirects=False):
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
        :rtype: twilio.http.response.Response
        """
        auth = auth or self.auth
        headers = headers or {}

        pkg_version = __version__
        os_name = platform.system()
        os_arch = platform.machine()
        python_version = platform.python_version()
        headers['User-Agent'] = 'twilio-python/{} ({} {}) Python/{}'.format(
            pkg_version,
            os_name,
            os_arch,
            python_version,
        )
        for extension in self.user_agent_extensions:
            headers['User-Agent'] += ' {}'.format(extension)
        headers['X-Twilio-Client'] = 'python-{}'.format(__version__)
        headers['Accept-Charset'] = 'utf-8'

        if method == 'POST' and 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/x-www-form-urlencoded'

        if 'Accept' not in headers:
            headers['Accept'] = 'application/json'

        uri = self.get_hostname(uri)

        return self.http_client.request(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects
        )

    def get_hostname(self, uri):
        """
        Determines the proper hostname given edge and region preferences
        via client configuration or uri.

        :param str uri: Fully qualified url

        :returns: The final uri used to make the request
        :rtype: str
        """
        if not self.edge and not self.region:
            return uri

        parsed_url = urlparse(uri)
        pieces = parsed_url.netloc.split('.')
        prefix = pieces[0]
        suffix = '.'.join(pieces[-2:])
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
        region = self.region or region or (edge and 'us1')

        parsed_url = parsed_url._replace(
            netloc='.'.join([part for part in [prefix, edge, region, suffix] if part])
        )
        return urlunparse(parsed_url)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio {}>'.format(self.account_sid)
