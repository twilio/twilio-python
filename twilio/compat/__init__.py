
# Those are not supported by the six library and needs to be done manually
from six import binary_type

try:
    # python 3
    from urllib.parse import urlencode, urlparse, urljoin
except ImportError:
    # python 2 backward compatibility
    #noinspection PyUnresolvedReferences
    from urllib import urlencode
    #noinspection PyUnresolvedReferences
    from urlparse import urlparse, urljoin
