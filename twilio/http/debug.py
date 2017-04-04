from twilio.http import HttpClient
from twilio.http.request import Request


class DebugClient(HttpClient):
    """
    A `DebugClient` can be used to print out requests before sending them out.
    """
    def __init__(self, client):
        super(DebugClient, self).__init__()
        self._client = client

    def request(self, method, url, params=None, data=None, headers=None, auth=None,
                timeout=None,
                allow_redirects=False):
        """
        Make an HTTP request.
        """
        req = Request(method=method, url=url, auth=auth, params=params, data=data, headers=headers)
        print(req)
        return self._client.request(
            method,
            url,
            params,
            data,
            headers,
            auth,
            timeout,
            allow_redirects
        )
