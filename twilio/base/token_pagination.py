from typing import Any, Dict, Optional

from twilio.base.exceptions import TwilioException
from twilio.base.page import Page


class TokenPagination(Page):
    """
    Represents a page of records using token-based pagination.

    Token-based pagination uses next_token and previous_token instead of
    page numbers to navigate through results.

    Example expected response format with token metadata:
    {
      "meta": {
        "key": "items",
        "pageSize": 50,
        "nextToken": "abc123",
        "previousToken": "xyz789"
      },
      "items": [
        { "id": 1, "name": "Item 1" },
        { "id": 2, "name": "Item 2" }
      ]
    }
    """

    @property
    def key(self) -> Optional[str]:
        """
        :return str: Returns the key that identifies the collection in the response.
        """
        if "meta" in self._payload and "key" in self._payload["meta"]:
            return self._payload["meta"]["key"]
        return None

    @property
    def page_size(self) -> Optional[int]:
        """
        :return int: Returns the page size or None if doesn't exist.
        """
        if "meta" in self._payload and "pageSize" in self._payload["meta"]:
            return self._payload["meta"]["pageSize"]
        return None

    @property
    def next_token(self) -> Optional[str]:
        """
        :return str: Returns the next_token for pagination or None if doesn't exist.
        """
        if "meta" in self._payload and "nextToken" in self._payload["meta"]:
            return self._payload["meta"]["nextToken"]
        return None

    @property
    def previous_token(self) -> Optional[str]:
        """
        :return str: Returns the previous_token for pagination or None if doesn't exist.
        """
        if "meta" in self._payload and "previousToken" in self._payload["meta"]:
            return self._payload["meta"]["previousToken"]
        return None

    def _get_page(self, token: Optional[str]) -> Optional["TokenPagination"]:
        """
        Internal helper to fetch a page using a given token.

        :param token: The pagination token to use.
        :return: The page or None if no token exists.
        """
        if not token:
            return None

        params = self._solution.copy()
        params["pageToken"] = token

        # Get the URI from solution and build the absolute URL
        uri = self._solution.get("uri")
        if not uri:
            raise TwilioException("URI must be provided for token pagination")

        url = self._version.domain.absolute_url(uri)
        response = self._version.domain.twilio.request("GET", url, params=params)
        cls = type(self)
        return cls(self._version, response, self._solution)

    async def _get_page_async(self, token: Optional[str]) -> Optional["TokenPagination"]:
        """
        Internal async helper to fetch a page using a given token.

        :param token: The pagination token to use.
        :return: The page or None if no token exists.
        """
        if not token:
            return None

        params = self._solution.copy()
        params["pageToken"] = token

        # Get the URI from solution and build the absolute URL
        uri = self._solution.get("uri")
        if not uri:
            raise TwilioException("URI must be provided for token pagination")

        url = self._version.domain.absolute_url(uri)
        response = await self._version.domain.twilio.request_async("GET", url, params=params)
        cls = type(self)
        return cls(self._version, response, self._solution)

    def next_page(self) -> Optional["TokenPagination"]:
        """
        Return the next page using token-based pagination.
        Makes a request to the same URI with pageToken set to nextToken.

        :return: The next page or None if no next token exists.
        """
        return self._get_page(self.next_token)

    async def next_page_async(self) -> Optional["TokenPagination"]:
        """
        Asynchronously return the next page using token-based pagination.
        Makes a request to the same URI with pageToken set to nextToken.

        :return: The next page or None if no next token exists.
        """
        return await self._get_page_async(self.next_token)

    def previous_page(self) -> Optional["TokenPagination"]:
        """
        Return the previous page using token-based pagination.
        Makes a request to the same URI with pageToken set to previousToken.

        :return: The previous page or None if no previous token exists.
        """
        return self._get_page(self.previous_token)

    async def previous_page_async(self) -> Optional["TokenPagination"]:
        """
        Asynchronously return the previous page using token-based pagination.
        Makes a request to the same URI with pageToken set to previousToken.

        :return: The previous page or None if no previous token exists.
        """
        return await self._get_page_async(self.previous_token)

    def __repr__(self) -> str:
        return "<TokenPagination>"
