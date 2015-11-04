class Domain(object):
    def __init__(self, twilio):
        """
        :param Twilio twilio:
        :return:
        """
        self.twilio = twilio
        self.base_url = None

    def absolute_url(self, uri):
        return '{}/{}'.format(self.base_url.strip('/'), uri.strip('/'))

    def request(self, method, uri, params=None, data=None, headers=None,
                auth=None, timeout=None, allow_redirects=False):
        url = self.absolute_url(uri)
        return self.twilio.request(
            method,
            url,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects
        )

