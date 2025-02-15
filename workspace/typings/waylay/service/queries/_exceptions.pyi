"""
This type stub file was generated by pyright.
"""

from typing import Any, List, Mapping
from ...exceptions import RestRequestError, RestResponseError, RestResponseParseError

"""Exceptions specific to the Queries Service."""
class QueryActionError(RestResponseError):
    """Error that represents the json messages of a query response."""
    @property
    def messages(self) -> List[Mapping[str, Any]]:
        """Get the list of message objects returned by a query error response."""
        ...
    
    @property
    def message(self):
        """Get the main user error returned by a query error response."""
        ...
    


class QueryActionParseError(RestResponseParseError, QueryActionError):
    """Indicates that a query response could not be parsed."""
    ...


class QueryRequestError(RestRequestError):
    """Indicates issues with the request arguments."""
    ...


