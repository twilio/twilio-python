from twilio.rest.resources.imports import httplib2
from twilio.rest.resources.imports import socks
from twilio.rest.resources.imports import PROXY_TYPE_HTTP
from twilio.rest.resources.imports import PROXY_TYPE_HTTP_NO_TUNNEL
from twilio.rest.resources.imports import PROXY_TYPE_SOCKS4
from twilio.rest.resources.imports import PROXY_TYPE_SOCKS5


class Connection(object):
    _proxy_info = None

    @classmethod
    def proxy_info(cls):
        return cls._proxy_info

    @classmethod
    def set_proxy_info(cls, proxy_host, proxy_port,
                       proxy_type=PROXY_TYPE_HTTP, proxy_rdns=None,
                       proxy_user=None, proxy_pass=None):
        cls._proxy_info = httplib2.ProxyInfo(
            proxy_type,
            proxy_host,
            proxy_port,
            proxy_rdns=proxy_rdns,
            proxy_user=proxy_user,
            proxy_pass=proxy_pass,
        )


_hush_pyflakes = [
    socks,
    PROXY_TYPE_HTTP_NO_TUNNEL,
    PROXY_TYPE_SOCKS4,
    PROXY_TYPE_SOCKS5
]
