from twilio.base.exceptions import TwilioException


class HttpClient(object):
    """
    An abstract class representing an HTTP client.
    """
    def request(self, method, url, params=None, data=None, headers=None, auth=None,
                timeout=None, allow_redirects=False):
        """
        Make an HTTP request.
        """
        raise TwilioException('HttpClient is an abstract class')


class AsyncHttpClient(object):
    """
    An abstract class representing an asynchronous HTTP client.
    """
    async def request(self, method, url, params=None, data=None, headers=None,
                      auth=None, allow_redirects=False):
        """
        Make an asynchronous HTTP request.
        """
        raise TwilioException('AsyncHttpClient is an abstract class')
