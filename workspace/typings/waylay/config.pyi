"""
This type stub file was generated by pyright.
"""

import httpx
from typing import Any, Mapping, MutableMapping, Optional, Type
from .auth import CredentialsCallback, WaylayCredentials, WaylayToken, WaylayTokenAuth

"""Client configuration."""
log = ...
_http = httpx
TenantSettings = Mapping[str, str]
Settings = MutableMapping[str, str]
DEFAULT_PROFILE = ...
SERVICE_KEY_API = ...
SERVICE_KEY_GATEWAY = ...
SERVICE_KEY_ACCOUNTS = ...
DEFAULT_DOC_URL: str = ...
DEFAULT_APIDOC_URL: str = ...
DOC_URL_KEY: str = ...
APIDOC_URL_KEY: str = ...
class WaylayConfig:
    """Manages the authentication and endpoint configuration for the Waylay Platform."""
    profile: str
    _auth: WaylayTokenAuth
    _local_settings: Settings
    _tenant_settings: Optional[TenantSettings] = ...
    _token_auth_provider: Type[WaylayTokenAuth] = ...
    def __init__(self, credentials: WaylayCredentials = ..., profile: str = ..., settings: TenantSettings = ..., fetch_tenant_settings=..., credentials_callback: Optional[CredentialsCallback] = ...) -> None:
        """Create a WaylayConfig."""
        ...
    
    @property
    def credentials(self): # -> WaylayCredentials:
        """Get current credentials.

        As configured or returned by last callback).
        """
        ...
    
    def get_root_url(self, config_key: str, *, default_root_url: Optional[str] = ..., gateway_root_path: Optional[str] = ..., default_root_path: str = ..., resolve_settings: bool = ...) -> Optional[str]:
        """Get the root url for a waylay service."""
        ...
    
    def set_root_url(self, config_key: str, root_url: Optional[str]): # -> None:
        """Override the root url for the given server.

        Will persist on `save`.
        Setting a `None` value will remove the override.
        """
        ...
    
    @property
    def accounts_url(self) -> Optional[str]:
        """Get the accounts url."""
        ...
    
    @property
    def gateway_url(self): # -> str | None:
        """Get the gateway url."""
        ...
    
    @property
    def doc_url(self) -> str:
        """Get the root url of the documentation site."""
        ...
    
    @property
    def apidoc_url(self) -> str:
        """Get the root url of the api documentation site."""
        ...
    
    @property
    def tenant_settings(self) -> TenantSettings:
        """Get the tenant settings as stored on accounts.

        Will fetch settings when not present and initialised with 'fetch_tenant_settings=True'.
        """
        ...
    
    @property
    def local_settings(self) -> TenantSettings:
        """Get the settings overrides for this configuration.

        These include the endpoint overrides that are stored with the profile.
        """
        ...
    
    def set_local_settings(self, **settings: Optional[str]) -> TenantSettings:
        """Set a local endpoint url override for a service."""
        ...
    
    @property
    def settings(self) -> TenantSettings:
        """Get settings, from tenant configuration and local overrides."""
        ...
    
    def get_settings(self, resolve=...) -> TenantSettings:
        """Get the tenant settings.

        As resolved form the accounts backend, and overridden with local settings.
        If `resolve=True`, fetch and cache tenant settings from the accounts backend.
        """
        ...
    
    def get_valid_token(self) -> WaylayToken:
        """Get the current valid authentication token or fail."""
        ...
    
    @property
    def auth(self) -> _http.Auth:
        """Get the current the http authentication interceptor."""
        ...
    
    @property
    def domain(self) -> Optional[str]:
        """Get the Waylay domain of the current user."""
        ...
    
    @property
    def global_settings_url(self) -> str:
        """Get the REST url that fetches global settings."""
        ...
    
    @classmethod
    def config_file_path(cls, profile: str = ...) -> str:
        """Compute the default OS path used to store this configuration."""
        ...
    
    @classmethod
    def load(cls, profile: str = ..., *, interactive: bool = ..., skip_error: bool = ..., gateway_url: str = ...): # -> Self | None:
        """Load a stored waylay configuration."""
        ...
    
    @classmethod
    def from_dict(cls, config_json: Mapping[str, Any]): # -> Self:
        """Create a WaylayConfig from a dict representation."""
        ...
    
    def to_dict(self, obfuscate=...): # -> dict[str, Any]:
        """Get the (obfuscated) attributes of this WaylayConfig.

        Secret credentials are obfuscated.
        """
        ...
    
    def save(self) -> str:
        """Save the configuration as specified in the profile.

        Returns the save location.
        """
        ...
    
    @classmethod
    def delete(cls, profile: str = ...) -> str:
        """Delete a stored profile.

        Returns the deleted location.
        """
        ...
    
    @classmethod
    def list_profiles(cls): # -> dict[str | Any, str]:
        """List stored config profiles."""
        ...
    
    def __repr__(self): # -> str:
        """Show the implementation class an main attributes."""
        ...
    
    def __str__(self) -> str:
        """Show the main (obfuscated) attributes as a string."""
        ...
    


