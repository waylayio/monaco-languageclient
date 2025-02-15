"""
This type stub file was generated by pyright.
"""

from waylay.service._base import WaylayAction

"""Resource action method decorators specific for the 'byoml' service."""
DEFAULT_BYOML_MODEL_TIMEOUT = ...
TEMPORARY_FAILURES = ...
TEMPORARY_FAILURE_EXCEPTIONS = ...
WAIT_EXPONENTIAL = ...
DEFAULT_RETRY_ATTEMPTS = ...
DEFAULT_RETRY_MAX_DELAY = ...
def before_sleep_logger(action: WaylayAction, logger=..., level=...): # -> Callable[..., None]:
    """Create a before-sleep log function for tenacity.Retrying."""
    ...

def byoml_exception_decorator(action_method): # -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]:
    """Create a decorator that parses json error responses."""
    ...

def byoml_raise_not_ready_get(action_method): # -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]:
    """Create a decorator that retries after certain exceptions."""
    ...

def byoml_retry_upload_after_deletion_decorator(action_method): # -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any | None]:
    """
    Create a decorator that retries uploading a model.

    Occurs after a model with the same name has been deleted.
    """
    ...

def byoml_retry_decorator(action_method): # -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any | None]:
    """Create a decorator that retries after certain exceptions."""
    ...

def is_retry_failure(exc): # -> bool:
    """Check if exception is a custom error or temporary error."""
    ...

def is_temporary_failure_exception(exc): # -> bool:
    """Check if a given exception is a custom temporary failure exception."""
    ...

def is_temporary_failure(exc): # -> bool:
    """Check if given exception is temporary."""
    ...

def is_409_error(exc): # -> Literal[False]:
    """Check if given exception is a 409 error."""
    ...

