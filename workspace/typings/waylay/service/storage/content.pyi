"""
This type stub file was generated by pyright.
"""

import os
import httpx
import httpx._types as _http_types
from typing import Any, Dict, Optional, Union
from pathlib import Path
from waylay.service import WaylayRESTService, WaylayResource

"""REST definitions for handling content from the 'storage' service objects."""
__docformat__ = ...
_http = httpx
class ContentTool(WaylayResource):
    """Tool for handling content from of the 'storage' service objects using signed get and put links."""
    service: WaylayRESTService
    actions: Dict[str, Any] = ...
    def put(self, bucket: str, path: str, content_type: Optional[str] = ..., content: Optional[_http_types.RequestContent] = ..., json: Any = ..., from_file: Optional[Union[str, os.PathLike]] = ..., progress: bool = ..., headers: Optional[_http_types.HeaderTypes] = ..., raw: bool = ..., **kwargs) -> Union[_http.Response, str]:
        """Store the content of a storage object.

Content can be specified with (exactly) one of the attributes 'from_file', 'content' or 'json'.

This method gets a signed url (see storage.object.sign_put),
and uploads the object content to the object store.

Arguments:
    bucket          The name of the bucket.
    path            The object path for the uploaded content.
    content_type    [optional] The content type with which this content will be available.
    content         A byte array or byte stream. With streaming data, you will need
                    to provide a 'content-length' header.
    json            A data structure as to be uploaded with JSON encoding.
    from_file       A file path of the file content that needs to be uploaded.
    progress        [optional, bool] If true, the client will show a progress bar.
    headers         [optional] Additional headers to be used for the upload.
    raw             [optional, bool] If True, the HTTP response object is returned,
                    even in case of failures. Otherwise, return the status text or
                    raises errors on failure.
    kwargs          Additional attributes forwarded to the 'sign_get' request.
        """
        ...
    
    def get(self, bucket: str, path: str, to_file: Optional[Union[str, os.PathLike]] = ..., progress: bool = ..., headers: Optional[_http_types.HeaderTypes] = ..., raw: bool = ..., **kwargs) -> Union[_http.Response, Path]:
        """Retrieve the content of a storage object.

This method gets the signed_url (see storage.object.sign_get),
and downloads the object content from the given url to the object store.

Arguments:
    bucket          The name of the bucket.
    path            The object path for the content to be downloaded.
    to_file         A local file path to which the content should be saved.
                    If succesfull, will return a 'Path' object to that file.
    progress        [optional, bool] If true, the client will show a progress bar.
    headers         [optional] Additional headers to be used for the download.
    raw             [optional, bool] If 'True', the HTTP response object is returned,
                    even in case of failures. Otherwise, raises errors on failure.

    kwargs          Additional attributes forwarded to the 'sign_get' request.

Returns:
    If 'to_file' is specified: a 'Path' object representing the download location.
    Otherwise, w response object having having a properties like
        'content', 'text', 'status_code', 'headers'
    and a
        'json()'
    method to extract the data.
        """
        ...
    


