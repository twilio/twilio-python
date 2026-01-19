"""
ApiResponse class for wrapping API responses with metadata
"""

from typing import Dict, Generic, TypeVar

T = TypeVar("T")


class ApiResponse(Generic[T]):
    """
    Wrapper for API responses that includes HTTP metadata.

    This class is returned by *_with_http_info methods and provides access to:
    - The response data (resource instance, list, or boolean)
    - HTTP status code
    - Response headers

    Attributes:
        data: The response data (instance, list, or boolean for delete operations)
        status_code: HTTP status code from the response
        headers: Dictionary of response headers

    Example:
        >>> response = client.accounts.create_with_http_info(friendly_name="Test")
        >>> print(response.status_code)  # 201
        >>> print(response.headers['Content-Type'])  # application/json
        >>> account = response.data
        >>> print(account.sid)
    """

    def __init__(self, data: T, status_code: int, headers: Dict[str, str]):
        """
        Initialize an ApiResponse

        Args:
            data: The response payload (instance, list, or boolean)
            status_code: HTTP status code (e.g., 200, 201, 204)
            headers: Dictionary of response headers
        """
        self.data = data
        self.status_code = status_code
        self.headers = headers

    def __repr__(self) -> str:
        """String representation of the ApiResponse"""
        return f"ApiResponse(status_code={self.status_code}, data={type(self.data).__name__})"

    def __str__(self) -> str:
        """Human-readable string representation"""
        return f"<ApiResponse [{self.status_code}] with {type(self.data).__name__}>"
