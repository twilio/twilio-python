from twilio.base.exceptions import TwilioException
from urllib.parse import urlencode


class HttpClient(object):
    def __init__(self, logger, is_async, timeout=None):
        """
        Constructor for the abstract HTTP client

        :param logger
        :param bool is_async: Whether the client supports async request calls.
        :param float timeout: Timeout for the requests.
                              Timeout should never be zero (0) or less.
        """
        self.logger = logger
        self.is_async = is_async

        if timeout is not None and timeout <= 0:
            raise ValueError(timeout)
        self.timeout = timeout

        self._test_only_last_request = None
        self._test_only_last_response = None

    """
    An abstract class representing an HTTP client.
    """

    def request(
        self,
        method,
        url,
        params=None,
        data=None,
        headers=None,
        auth=None,
        timeout=None,
        allow_redirects=False,
    ):
        """
        Make an HTTP request.
        """
        raise TwilioException("HttpClient is an abstract class")

    def log_request(self, kwargs):
        """
        Logs the HTTP request
        """
        self.logger.info("-- BEGIN Twilio API Request --")

        if kwargs["params"]:
            self.logger.info(
                "{} Request: {}?{}".format(
                    kwargs["method"], kwargs["url"], urlencode(kwargs["params"])
                )
            )
            self.logger.info("Query Params: {}".format(kwargs["params"]))
        else:
            self.logger.info("{} Request: {}".format(kwargs["method"], kwargs["url"]))

        if kwargs["headers"]:
            self.logger.info("Headers:")
            for key, value in kwargs["headers"].items():
                # Do not log authorization headers
                if "authorization" not in key.lower():
                    self.logger.info("{} : {}".format(key, value))

        self.logger.info("-- END Twilio API Request --")

    def log_response(self, status_code, response):
        """
        Logs the HTTP response
        """
        self.logger.info("Response Status Code: {}".format(status_code))
        self.logger.info("Response Headers: {}".format(response.headers))


class AsyncHttpClient(HttpClient):
    """
    An abstract class representing an asynchronous HTTP client.
    """

    async def request(
        self,
        method,
        url,
        params=None,
        data=None,
        headers=None,
        auth=None,
        allow_redirects=False,
    ):
        """
        Make an asynchronous HTTP request.
        """
        raise TwilioException("AsyncHttpClient is an abstract class")
