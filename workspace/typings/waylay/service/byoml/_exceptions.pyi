"""
This type stub file was generated by pyright.
"""

from ...exceptions import RequestError, RestError, RestResponseError, RestResponseParseError

"""Exceptions specific to the Byoml Service."""
class ByomlActionError(RestResponseError):
    """Error that represents the json messages of a byoml response."""
    @property
    def message(self):
        """Get the main user error returned by a byoml error response."""
        ...
    


class ByomlActionParseError(RestResponseParseError, ByomlActionError):
    """Indicates that a byoml response could not be parsed."""
    ...


class ByomlValidationError(RequestError):
    """Exception class for BYOML validation errors."""
    ...


class ModelNotReadyError(RestError):
    """Indicates that a byoml action should be retried."""
    ...


