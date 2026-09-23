from typing import Any, Optional


class Response(object):
    """
    Represents a simplified HTTP response.

    This class stores the HTTP status code, response body content,
    and optional HTTP headers returned by a request.
    """
    def __init__(
        self,
        status_code: int,
        text: str,
        headers: Optional[Any] = None,
    ):
        self.content = text
        self.headers = headers
        self.cached = False
        self.status_code = status_code
        self.ok = self.status_code < 400

    @property
    def text(self) -> str:
        """
        Returns the response body as text.

        This property provides a clearer way to access the response
        content stored in `self.content`.
        """
        return self.content

    def __repr__(self) -> str:
        """
        Returns a string representation of the Response object.

        Mainly used for debugging purposes.
        """
        return "HTTP {} {}".format(self.status_code, self.content)
