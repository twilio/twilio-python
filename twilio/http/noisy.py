from twilio.http import HttpClient


class NoisyClient(HttpClient):
    def __init__(self, client):
        super(NoisyClient, self).__init__()
        self._client = client

    def request(self,
                method,
                url,
                params=None,
                data=None,
                headers=None,
                auth=None,
                timeout=None,
                allow_redirects=False):
        print("""

        """)
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
