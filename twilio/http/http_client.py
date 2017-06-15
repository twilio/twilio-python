from requests import Request, Session

from twilio.http import HttpClient, get_cert_file
from twilio.http.response import Response


class TwilioHttpClient(HttpClient):
    """
    General purpose HTTP Client for interacting with the Twilio API
    """
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
        session = Session()
        session.verify = get_cert_file()

        request = Request(method.upper(), url, params=params, data=data, headers=headers, auth=auth)

        prepped_request = session.prepare_request(request)
        response = session.send(
            prepped_request,
            allow_redirects=allow_redirects,
            timeout=timeout,
        )

        return Response(int(response.status_code), response.content)
