import httplib2
from six import integer_types, string_types, iteritems
from six import binary_type

from twilio.compat import urlencode, urlparse
from twilio.http import get_cert_file, HttpClient
from twilio.http.response import Response


class Httplib2Client(HttpClient):

    def __init__(self, proxy_info=httplib2.proxy_info_from_environment):
        self.proxy_info = proxy_info

    def request(self,
                method,
                url,
                params=None,
                data=None,
                headers=None,
                auth=None,
                timeout=None,
                allow_redirects=False):
        """Sends an HTTP request

        :param str method: The HTTP method to use
        :param str url: The URL to request
        :param dict params: Query parameters to append to the URL
        :param dict data: Parameters to go in the body of the HTTP request
        :param dict headers: HTTP Headers to send with the request
        :param tuple auth: Basic Auth arguments
        :param float timeout: Socket/Read timeout for the request
        :param boolean allow_redirects: Whether or not to allow redirects

        :return: An http response
        :rtype: A :class:`Response <twilio.rest.http.response.Response>` object

        See the requests documentation for explanation of all these parameters
        """
        http = httplib2.Http(
            timeout=timeout,
            ca_certs=get_cert_file(),
            proxy_info=self.proxy_info,
        )
        http.follow_redirects = allow_redirects

        if auth is not None:
            http.add_credentials(auth[0], auth[1])

        if data is not None:
            udata = {}
            for k, v in iteritems(data):
                key = k.encode('utf-8')
                if isinstance(v, (list, tuple, set)):
                    udata[key] = [self.encode_atom(x) for x in v]
                elif isinstance(v, (integer_types, binary_type, string_types)):
                    udata[key] = self.encode_atom(v)
                else:
                    raise ValueError('data should be an integer, '
                                     'binary, or string, or sequence ')
            data = urlencode(udata, doseq=True)

        if params is not None:
            enc_params = urlencode(params, doseq=True)
            if urlparse(url).query:
                url = '%s&%s' % (url, enc_params)
            else:
                url = '%s?%s' % (url, enc_params)

        resp, content = http.request(url, method, headers=headers, body=data)

        return Response(int(resp.status), content.decode('utf-8'))

    @classmethod
    def encode_atom(cls, atom):
        if isinstance(atom, (integer_types, binary_type)):
            return atom
        elif isinstance(atom, string_types):
            return atom.encode('utf-8')
        else:
            raise ValueError('list elements should be an integer, binary, or string')
