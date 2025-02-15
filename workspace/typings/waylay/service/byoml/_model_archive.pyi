"""
This type stub file was generated by pyright.
"""

import os
from contextlib import contextmanager
from typing import Any, BinaryIO, Callable, Dict, Iterator, Optional, Tuple, Union
from pathlib import Path

PathLike = Union[str, os.PathLike]
PytorchModel = Any
TensorflowModel = Any
XgboostModel = Any
SklearnModel = Any
ByomlModel = Union[PytorchModel, TensorflowModel, XgboostModel, SklearnModel]
ModelSerializer = Callable[[PathLike, ByomlModel], PathLike]
def assert_dir_exists(dir_name: PathLike): # -> None:
    """Raise error if the input directory does not exist."""
    ...

SUPPORTED_FRAMEWORKS: Dict[str, ModelSerializer] = ...
class ModelArchiveBuilder:
    """A context to build model archives."""
    work_dir_path: Path
    def __init__(self, work_dir: Optional[PathLike]) -> None:
        """Create a model archive build context."""
        ...
    
    def __enter__(self): # -> Self:
        """Enter the model archive build context."""
        ...
    
    def __exit__(self, typ, value, traceback): # -> None:
        """Exit the model archive build context."""
        ...
    
    def serialize_model(self, trained_model: ByomlModel, framework: str) -> PathLike:
        """Serialize a model to a given path."""
        ...
    


class ModelZipArchiveBuilder(ModelArchiveBuilder):
    """A context to build a zip model archives (legacy byoml api)."""
    @contextmanager
    def save_model_in_dir(self, trained_model: Union[PathLike, ByomlModel], framework: str): # -> Generator[BytesIO, Any, None]:
        """Create the model zip file in a temporary buffer."""
        ...
    


class ModelPlugArchiveBuilder(ModelArchiveBuilder):
    """A context to build a model plug archive (openfaas)."""
    model_spec_path: Path
    model_path: Path
    requirements_path: Path
    lib_path: Path
    def add_model_spec(self, model_spec: Dict): # -> None:
        """Add a model specification."""
        ...
    
    def add_model(self, trained_model: Union[PathLike, ByomlModel], framework: str): # -> None:
        """Add a serialized model file."""
        ...
    
    def add_requirements(self, requirements_file: Optional[PathLike], requirements: Optional[str]): # -> None:
        """Add requirements file."""
        ...
    
    def add_lib(self, lib: Optional[PathLike]): # -> None:
        """Add a lib folder."""
        ...
    
    @contextmanager
    def create_plug_tar_archive(self) -> Iterator[Tuple[BinaryIO, int]]:
        """Create a tar archive buffer."""
        ...
    


