__version_info__ = ('3', '6', '5')
__version__ = '.'.join(__version_info__)


class TwilioException(Exception):
    pass


class TwilioRestException(TwilioException):
    """ A generic 400 or 500 level exception from the Twilio API

    :param int status: the HTTP status that was returned for the exception
    :param str uri: The URI that caused the exception
    :param str msg: A human-readable message for the error
    :param int|None code: A Twilio-specific error code for the error. This is
         not available for all errors.
    """

    # XXX: Move this to the twilio.rest folder

    def __init__(self, status, uri, msg="", code=None):
        self.uri = uri
        self.status = status
        self.msg = msg
        self.code = code

    def __str__(self):
        return "HTTP ERROR %s: %s \n %s" % (self.status, self.msg, self.uri)
