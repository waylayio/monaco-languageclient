"""
This type stub file was generated by pyright.
"""

from waylay.service import WaylayResource

"""REST definitions for the 'series' entity of the 'data' service."""
DEFAULT_DECORATORS = ...
RESOURCE_ARG = ...
class EventsResource(WaylayResource):
    """REST Resource for the 'events' ingestion of the 'data' service."""
    link_roots = ...
    actions = ...
    def get_action_full_url(self, action_name, *parts):
        """Override the regular url computation when not using api gateway."""
        ...
    


