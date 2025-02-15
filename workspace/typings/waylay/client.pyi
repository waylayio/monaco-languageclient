"""
This type stub file was generated by pyright.
"""

import sys
from typing import Iterable, List, Mapping, Optional, Type, TypeVar
from .service import ByomlService, DataService, ETLService, QueriesService, ResourcesService, StorageService, TimeSeriesService, UtilService, WaylayService, WaylayServiceContext
from .service.analytics import AnalyticsServiceLegacy
from .config import TenantSettings, WaylayConfig
from .auth import WaylayCredentials

"""REST client for the Waylay Platform."""
if sys.version_info < (3, 10):
    ...
else:
    ...
S = TypeVar('S', bound=WaylayService)
logger = ...
class WaylayClient:
    """REST client for the Waylay Platform."""
    analytics: AnalyticsServiceLegacy = ...
    byoml: ByomlService
    config: WaylayConfig
    timeseries: TimeSeriesService
    resources: ResourcesService
    storage: StorageService
    util: UtilService
    etl: ETLService
    data: DataService
    queries: QueriesService
    @classmethod
    def from_profile(cls, profile: str = ..., *, interactive=..., gateway_url=...): # -> Self:
        """Create a WaylayClient named profile.

        Uses credentials from environment variables or a locally stored configuration.
        """
        ...
    
    @classmethod
    def from_client_credentials(cls, api_key: str, api_secret: str, *, gateway_url=..., accounts_url=..., settings: TenantSettings = ...): # -> Self:
        """Create a WaylayClient using the given client credentials."""
        ...
    
    @classmethod
    def from_token(cls, token_string: str, *, gateway_url=..., accounts_url=..., settings: TenantSettings = ...): # -> Self:
        """Create a WaylayClient using a waylay token."""
        ...
    
    @classmethod
    def from_credentials(cls, credentials: WaylayCredentials, settings: TenantSettings = ...): # -> Self:
        """Create a WaylayClient using the given client credentials."""
        ...
    
    def __init__(self, config: WaylayConfig) -> None:
        """Create a WaylayConfig instance."""
        ...
    
    @property
    def services(self) -> List[WaylayService]:
        """Get the services that are available through this client."""
        ...
    
    @property
    def service_context(self) -> WaylayServiceContext:
        """Get the WaylayServiceContext view on this client."""
        ...
    
    def configure(self, config: WaylayConfig): # -> None:
        """Update this client with the given configuration."""
        ...
    
    def list_root_urls(self) -> Mapping[str, Optional[str]]:
        """List the currently configured root url for each of the registered REST services."""
        ...
    
    def __repr__(self): # -> str:
        """Get a technical string representation of this instance."""
        ...
    
    def load_services(self): # -> None:
        """Load all services that are registered with the `waylay_services` entry point."""
        ...
    
    def register_service(self, *service_class: Type[S]) -> Iterable[S]:
        """Create and initialize one or more service of the given class.

        Replaces any existing with the same service_key.
        """
        ...
    
    def get(self, service_class: Type[S]) -> Optional[S]:
        """Get the service instance for the provided class, if it is registered.

        Implements the `WaylayServiceContext.get` protocol.
        """
        ...
    
    def require(self, service_class: Type[S]) -> S:
        """Get the service instance for the given class or raise a ConfigError.

        Implements the `WaylayServiceContext.require` protocol.
        """
        ...
    
    def list(self) -> List[WaylayService]:
        """List all registered Services.

        Implements the `WaylayServiceContext.list` protocol.
        """
        ...
    


