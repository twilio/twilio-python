from enum import Enum
from typing import Any, Dict, Tuple, Union
from urllib.parse import urlencode


class Match(Enum):
    """
    Special enumeration used to represent a wildcard match.

    The value ANY ("*") is used to indicate that any value
    for a given attribute should be considered a match.
    """
    ANY = "*"


class Request(object):
    """
    Represents an HTTP request definition.

    This class is mainly used to describe or compare HTTP requests
    based on attributes such as method, URL, parameters, headers,
    authentication, and request body data.
    """

    def __init__(
        self,
        method: Union[str, Match] = Match.ANY,
        url: Union[str, Match] = Match.ANY,
        auth: Union[Tuple[str, str], Match] = Match.ANY,
        params: Union[Dict[str, str], Match] = Match.ANY,
        data: Union[Dict[str, str], Match] = Match.ANY,
        headers: Union[Dict[str, str], Match] = Match.ANY,
        **kwargs: Any
    ):
        # HTTP method (GET, POST, etc.) or Match.ANY as a wildcard
        self.method = method

        # Normalize the HTTP method to uppercase if provided
        if method and method is not Match.ANY:
            self.method = method.upper()

        # Request URL or wildcard
        self.url = url

        # Authentication tuple (username, password) or wildcard
        self.auth = auth

        # Query parameters sent with the request
        self.params = params

        # Request body data
        self.data = data

        # HTTP headers included in the request
        self.headers = headers

    @classmethod
    def attribute_equal(cls, lhs, rhs) -> bool:
        """
        Compares two request attributes, supporting wildcard matching.

        If either side is Match.ANY, the attributes are considered equal.
        """
        if lhs == Match.ANY or rhs == Match.ANY:
            # ANY matches everything
            return True

        # Normalize falsy values to None before comparison
        lhs = lhs or None
        rhs = rhs or None

        return lhs == rhs

    def __eq__(self, other) -> bool:
        """
        Compares two Request objects for equality.

        Each attribute is compared individually using attribute_equal
        to allow wildcard matching.
        """
        if not isinstance(other, Request):
            return False

        return (
            self.attribute_equal(self.method, other.method)
            and self.attribute_equal(self.url, other.url)
            and self.attribute_equal(self.auth, other.auth)
            and self.attribute_equal(self.params, other.params)
            and self.attribute_equal(self.data, other.data)
            and self.attribute_equal(self.headers, other.headers)
        )

    def __str__(self) -> str:
        """
        Returns a human-readable representation of the request.

        The format resembles a curl-like representation including
        parameters, headers, and request body.
        """
        params = ""
        if self.params and self.params != Match.ANY:
            # Encode query parameters for URL usage
            params = "?{}".format(urlencode(self.params, doseq=True))

        data = ""
        if self.data and self.data != Match.ANY:
            # If the request is GET, mimic curl's -G option
            if self.method == "GET":
                data = "\n -G"
            
            # Format request body parameters
            data += "\n{}".format(
                "\n".join(' -d "{}={}"'.format(k, v) for k, v in self.data.items())
            )

        headers = ""
        if self.headers and self.headers != Match.ANY:
            # Format headers, excluding authorization for security reasons
            headers = "\n{}".format(
                "\n".join(
                    ' -H "{}: {}"'.format(k, v)
                    for k, v in self.headers.items()
                    if k.lower() != "authorization"
                )
            )

        return "{method} {url}{params}{data}{headers}".format(
            method=self.method,
            url=self.url,
            params=params,
            data=data,
            headers=headers,
        )

    def __repr__(self) -> str:
        """
        Returns the string representation of the Request object.

        Used mainly for debugging or logging.
        """
        return str(self)
