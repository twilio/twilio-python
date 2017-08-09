from requests import Request, Session, hooks

from twilio.http import HttpClient, get_cert_file
from twilio.http.response import Response
import logging
import json
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

_logger = logging.getLogger('twilio.http_client')


class TwilioHttpClient(HttpClient):
    """
    General purpose HTTP Client for interacting with the Twilio API
    """
    def __init__(self, connection_pool=True, request_hooks=None):
        if connection_pool:
            self.session = Session()
            self.session.verify = get_cert_file()
        else:
            self.session = None

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
        session = self.session
        if session is None:
            session = Session()
            session.verify = get_cert_file()

        kwargs = dict(
            method=method.upper(),
            url=url,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            hooks=self.request_hooks
        )

        if params:
            _logger.info('{method} Request: {url}?{query}'.format(query=urlencode(params), **kwargs))
            _logger.info('PARAMS: {params}'.format(**kwargs))
        else:
            _logger.info('{method} Request: {url}'.format(**kwargs))
        if data:
            _logger.info('PAYLOAD: {data}'.format(**kwargs))

        request = Request(**kwargs)

        prepped_request = session.prepare_request(request)
        response = session.send(
            prepped_request,
            allow_redirects=allow_redirects,
            timeout=timeout,
        )

        if response.json():
            # strip JSON of possible prettyprint
            text = json.dumps(response.json())
        else:
            text = response.text

        _logger.info(u'{method} Response: {status} {text}'.format(method=method, status=response.status_code, text=text))

        return Response(int(response.status_code), response.text)
