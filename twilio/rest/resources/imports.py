# parse_qs
try:
    from urlparse import parse_qs
except ImportError:
    from cgi import parse_qs

# json
try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        from django.utils import simplejson as json

# httplib2
import httplib2

try:
    # This only exists in python2.x's httplib2, since GAE doesn't do py3.
    from httplib2 import NotSupportedOnThisPlatform
except ImportError:
    # If anything throws None I will be very surprised.
    NotSupportedOnThisPlatform = None

# socks
try:
    from httplib2 import socks
    from httplib2.socks import PROXY_TYPE_HTTP
    from httplib2.socks import PROXY_TYPE_SOCKS4
    from httplib2.socks import PROXY_TYPE_SOCKS5
except ImportError:
    import socks
    from socks import PROXY_TYPE_HTTP
    from socks import PROXY_TYPE_SOCKS4
    from socks import PROXY_TYPE_SOCKS5
