from twilio.rest.resources.imports import httplib2
from twilio.rest.resources.imports import socks


class Connection(object):
    _proxy_info = None

    @classmethod
    def proxy_info(cls):
        return cls._proxy_info

    @classmethod
    def set_proxy_info(cls, proxy_url, proxy_port):
        cls._proxy_info = httplib2.ProxyInfo(
            socks.PROXY_TYPE_HTTP,
            proxy_url,
            proxy_port,
        )
