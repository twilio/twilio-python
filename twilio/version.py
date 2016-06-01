import json
from math import ceil
from twilio import values
from twilio.exceptions import TwilioException


class Version(object):
    MAX_PAGE_SIZE = 1000

    def __init__(self, domain):
        """
        :param Domain domain:
        :return:
        """
        self.domain = domain
        self.version = None

    def absolute_url(self, uri):
        return self.domain.absolute_url(self.relative_uri(uri))

    def relative_uri(self, uri):
        return '{}/{}'.format(self.version.strip('/'), uri.strip('/'))

    def request(self, method, uri, params=None, data=None, headers=None,
                auth=None, timeout=None, allow_redirects=False):
        url = self.relative_uri(uri)
        return self.domain.request(
            method,
            url,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects
        )

    def fetch(self, method, uri, params=None, data=None, headers=None, auth=None, timeout=None,
              allow_redirects=False):
        response = self.request(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
        )

        if response.status_code < 200 or response.status_code >= 300:
            raise TwilioException('Unable to fetch record')

        return json.loads(response.content)

    def update(self, method, uri, params=None, data=None, headers=None, auth=None, timeout=None,
               allow_redirects=False):
        response = self.request(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
        )

        if response.status_code < 200 or response.status_code >= 300:
            raise TwilioException('Unable to update record')

        return json.loads(response.content)

    def delete(self, method, uri, params=None, data=None, headers=None, auth=None, timeout=None,
               allow_redirects=False):
        response = self.request(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
        )

        if response.status_code < 200 or response.status_code >= 300:
            raise TwilioException('Unable to delete record')

        return response.status_code == 204

    def read_limits(self, limit=None, page_size=None):
        page_limit = values.unset

        if limit is not None:

            if page_size is None:
                # If there is no user-specified page_size, pick the most network efficient size
                page_size = min(limit, self.MAX_PAGE_SIZE)

            page_limit = int(ceil(limit / float(page_size)))

        return {
            'limit': limit or values.unset,
            'page_size': page_size or values.unset,
            'page_limit': page_limit,
        }

    def page(self, method, uri, params=None, data=None, headers=None, auth=None, timeout=None,
             allow_redirects=False):
        return self.request(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
        )

    def stream(self, page, limit=None, page_limit=None):
        current_record = 1
        current_page = 1

        while page is not None:
            for record in page:
                yield record
                current_record += 1
                if limit and limit is not values.unset and limit < current_record:
                    return

            if page_limit and page_limit is not values.unset and page_limit < current_page:
                return

            page = page.next_page()
            current_page += 1

    def create(self, method, uri, params=None, data=None, headers=None, auth=None, timeout=None,
               allow_redirects=False):
        response = self.request(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
        )

        if response.status_code < 200 or response.status_code >= 300:
            raise TwilioException('[{}] Unable to create record\n{}'.format(response.status_code,
                                                                            response.content))

        return json.loads(response.content)

