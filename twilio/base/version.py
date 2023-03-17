import json

from twilio.base import values
from twilio.base.domain import Domain
from twilio.base.exceptions import TwilioRestException


class Version(object):
    """
    Represents an API version.
    """

    def __init__(self, domain: Domain, version: str):
        self.domain = domain
        self.version = version

    def absolute_url(self, uri):
        """
        Turns a relative uri into an absolute url.
        """
        return self.domain.absolute_url(self.relative_uri(uri))

    def relative_uri(self, uri):
        """
        Turns a relative uri into a versioned relative uri.
        """
        return "{}/{}".format(self.version.strip("/"), uri.strip("/"))

    def request(
        self,
        method,
        uri,
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
        url = self.relative_uri(uri)
        return self.domain.request(
            method,
            url,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
        )

    async def request_async(
        self,
        method,
        uri,
        params=None,
        data=None,
        headers=None,
        auth=None,
        timeout=None,
        allow_redirects=False,
    ):
        """
        Make an asynchronous HTTP request
        """
        url = self.relative_uri(uri)
        return await self.domain.request_async(
            method,
            url,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
        )

    @classmethod
    def exception(cls, method, uri, response, message):
        """
        Wraps an exceptional response in a `TwilioRestException`.
        """
        # noinspection PyBroadException
        try:
            error_payload = json.loads(response.text)
            if "message" in error_payload:
                message = "{}: {}".format(message, error_payload["message"])
            details = error_payload.get("details")
            code = error_payload.get("code", response.status_code)
            return TwilioRestException(
                response.status_code, uri, message, code, method, details
            )
        except Exception:
            return TwilioRestException(
                response.status_code, uri, message, response.status_code, method
            )

    def _parse_fetch(self, method, uri, response):
        """
        Parses fetch response JSON
        """
        # Note that 3XX response codes are allowed for fetches.
        if response.status_code < 200 or response.status_code >= 400:
            raise self.exception(method, uri, response, "Unable to fetch record")

        return json.loads(response.text)

    def fetch(
        self,
        method,
        uri,
        params=None,
        data=None,
        headers=None,
        auth=None,
        timeout=None,
        allow_redirects=False,
    ):
        """
        Fetch a resource instance.
        """
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

        return self._parse_fetch(method, uri, response)

    async def fetch_async(
        self,
        method,
        uri,
        params=None,
        data=None,
        headers=None,
        auth=None,
        timeout=None,
        allow_redirects=False,
    ):
        """
        Asynchronously fetch a resource instance.
        """
        response = await self.request_async(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
        )

        return self._parse_fetch(method, uri, response)

    def _parse_update(self, method, uri, response):
        """
        Parses update response JSON
        """
        if response.status_code < 200 or response.status_code >= 300:
            raise self.exception(method, uri, response, "Unable to update record")

        return json.loads(response.text)

    def update(
        self,
        method,
        uri,
        params=None,
        data=None,
        headers=None,
        auth=None,
        timeout=None,
        allow_redirects=False,
    ):
        """
        Update a resource instance.
        """
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

        return self._parse_update(method, uri, response)

    async def update_async(
        self,
        method,
        uri,
        params=None,
        data=None,
        headers=None,
        auth=None,
        timeout=None,
        allow_redirects=False,
    ):
        """
        Asynchronously update a resource instance.
        """
        response = await self.request_async(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
        )

        return self._parse_update(method, uri, response)

    def _parse_delete(self, method, uri, response):
        """
        Parses delete response JSON
        """
        if response.status_code < 200 or response.status_code >= 300:
            raise self.exception(method, uri, response, "Unable to delete record")

        return response.status_code == 204

    def delete(
        self,
        method,
        uri,
        params=None,
        data=None,
        headers=None,
        auth=None,
        timeout=None,
        allow_redirects=False,
    ):
        """
        Delete a resource.
        """
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

        return self._parse_delete(method, uri, response)

    async def delete_async(
        self,
        method,
        uri,
        params=None,
        data=None,
        headers=None,
        auth=None,
        timeout=None,
        allow_redirects=False,
    ):
        """
        Asynchronously delete a resource.
        """
        response = await self.request_async(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
        )

        return self._parse_delete(method, uri, response)

    def read_limits(self, limit=None, page_size=None):
        """
        Takes a limit on the max number of records to read and a max page_size
        and calculates the max number of pages to read.

        :param int limit: Max number of records to read.
        :param int page_size: Max page size.
        :return dict: A dictionary of paging limits.
        """
        if limit is not None and page_size is None:
            page_size = limit

        return {
            "limit": limit or values.unset,
            "page_size": page_size or values.unset,
        }

    def page(
        self,
        method,
        uri,
        params=None,
        data=None,
        headers=None,
        auth=None,
        timeout=None,
        allow_redirects=False,
    ):
        """
        Makes an HTTP request.
        """
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

    async def page_async(
        self,
        method,
        uri,
        params=None,
        data=None,
        headers=None,
        auth=None,
        timeout=None,
        allow_redirects=False,
    ):
        """
        Makes an asynchronous HTTP request.
        """
        return await self.request_async(
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
        """
        Generates records one a time from a page, stopping at prescribed limits.

        :param Page page: The page to stream.
        :param int limit: The max number of records to read.
        :param int page_limit: The max number of pages to read.
        """
        current_record = 1
        current_page = 1

        while page is not None:
            for record in page:
                yield record
                current_record += 1
                if limit and limit is not values.unset and limit < current_record:
                    return

            current_page += 1
            if (
                page_limit
                and page_limit is not values.unset
                and page_limit < current_page
            ):
                return

            page = page.next_page()

    async def stream_async(self, page, limit=None, page_limit=None):
        """
        Generates records one a time from a page, stopping at prescribed limits.

        :param Page page: The page to stream.
        :param int limit: The max number of records to read.
        :param int page_limit: The max number of pages to read.
        """
        current_record = 1
        current_page = 1

        while page is not None:
            for record in page:
                yield record
                current_record += 1
                if limit and limit is not values.unset and limit < current_record:
                    return

            current_page += 1
            if (
                page_limit
                and page_limit is not values.unset
                and page_limit < current_page
            ):
                return

            page = await page.next_page_async()

    def _parse_create(self, method, uri, response):
        """
        Parse create response JSON
        """
        if response.status_code < 200 or response.status_code >= 300:
            raise self.exception(method, uri, response, "Unable to create record")

        return json.loads(response.text)

    def create(
        self,
        method,
        uri,
        params=None,
        data=None,
        headers=None,
        auth=None,
        timeout=None,
        allow_redirects=False,
    ):
        """
        Create a resource instance.
        """
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

        return self._parse_create(method, uri, response)

    async def create_async(
        self,
        method,
        uri,
        params=None,
        data=None,
        headers=None,
        auth=None,
        timeout=None,
        allow_redirects=False,
    ):
        """
        Asynchronously create a resource instance.
        """
        response = await self.request_async(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
        )

        return self._parse_create(method, uri, response)
