import httplib2
import os
from six import integer_types, binary_type, string_types, iteritems
from twilio.rest.resources.connection import Connection
from ..compat import urlencode, urlparse


class Response(object):
    """
    A wrapper to describe a generic response object
    """
    def __init__(self, status_code, content):
        self.content = content
        self.cached = False
        self.status_code = status_code
        self.ok = self.status_code < 400


def get_cert_file():
    """ Get the cert file location or bail """
    # XXX - this currently fails test coverage because we don't actually go
    # over the network anywhere. Might be good to have a test that stands up a
    # local server and authenticates against it.
    try:
        # Apparently __file__ is not available in all places so wrapping this
        # in a try/catch
        current_path = os.path.realpath(__file__)
        ca_cert_path = os.path.join(current_path, "..", "..",
                                    "conf", "cacert.pem")
        return os.path.abspath(ca_cert_path)
    except Exception:
        # None means use the default system file
        return None


class HttpClient(object):

    def make_request(self, method, url,
                     params=None, data=None,
                     headers=None,
                     auth=None, timeout=None,
                     allow_redirects=False):
        """Sends an HTTP request

        :param str method: The HTTP method to use
        :param str url: The URL to request
        :param dict params: Query parameters to append to the URL
        :param dict data: Parameters to go in the body of the HTTP request
        :param dict headers: HTTP Headers to send with the request
        :param float timeout: Socket/Read timeout for the request

        :return: An http response
        :rtype: A :class:`Response <models.Response>` object

        See the requests documentation for explanation of all these parameters
        """
        http = httplib2.Http(
            timeout=timeout,
            ca_certs=get_cert_file(),
            proxy_info=Connection.proxy_info(),
        )
        http.follow_redirects = allow_redirects

        if auth is not None:
            http.add_credentials(auth[0], auth[1])

        def encode_atom(atom):
            if isinstance(atom, (integer_types, binary_type)):
                return atom
            elif isinstance(atom, string_types):
                return atom.encode('utf-8')
            else:
                raise ValueError('list elements should be an integer, '
                                 'binary, or string')

        if data is not None:
            udata = {}
            for k, v in iteritems(data):
                key = k.encode('utf-8')
                if isinstance(v, (list, tuple, set)):
                    udata[key] = [encode_atom(x) for x in v]
                elif isinstance(v, (integer_types, binary_type, string_types)):
                    udata[key] = encode_atom(v)
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
