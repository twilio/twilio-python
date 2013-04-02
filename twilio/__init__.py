__version_info__ = ('3', '4', '5')
__version__ = '.'.join(__version_info__)


class TwilioException(Exception):
    pass


class TwilioRestException(TwilioException):

    def __init__(self, status, uri, msg="", code=None):
        self.uri = uri
        self.status = status
        self.msg = msg
        self.code = code

    def __str__(self):
        return "HTTP ERROR %s: %s \n %s" % (self.status, self.msg, self.uri)
