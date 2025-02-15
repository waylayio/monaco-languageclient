"""
This type stub file was generated by pyright.
"""

from typing import Dict, Optional
from .._base import WaylayResource

"""REST definitions for the 'runtime' entity of the 'byoml' service."""
FRAMEWORK_ARG = ...
FRAMEWORK_VERSION_ARG = ...
FRAMEWORK_LIST_RETURN = ...
class FrameworkResource(WaylayResource):
    """REST Inspect supported runtimes for a given framework."""
    link_roots = ...
    actions = ...
    def find_runtime(self, framework: str, framework_version: Optional[str]) -> Dict:
        """Get the byoml plug runtime for this framework and version (default version if not specified).

        framework: the name of the framework
        framework_version: (optional) the version for this framework, the default version is defined by
                           the byoml service itself.
        """
        ...
    


