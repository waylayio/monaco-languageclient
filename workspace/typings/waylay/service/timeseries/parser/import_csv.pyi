"""
This type stub file was generated by pyright.
"""

import collections.abc
from enum import Enum
from typing import Iterable, Iterator, Optional, Tuple, Union
from contextlib import contextmanager
from .model import CSVReader, CSVReaderAndResource, Measurement, SeriesInput, SeriesSettings

"""Conversion from CSV to elt export format."""
LOG = ...
TIMESERIES_SUFFIXES = ...
DEFAULT_SPOOL_MAX_SIZE = ...
_SPOOLED_TS_LEN = ...
_SPOOLED_TS_FORMAT = ...
class MeasurementsStoreType(Enum):
    """Enum for measurements store types."""
    MEMORY = ...
    SPOOLED = ...


class CsvImportSeriesProvider(collections.abc.Mapping):
    """A series provider that uses cached buffers to process import csv files."""
    def __init__(self, settings: SeriesSettings, measurements_store: Union[str, MeasurementsStoreType] = ...) -> None:
        """Create an import series provider."""
        ...
    
    def __enter__(self): # -> Self:
        """Enter a runtime context."""
        ...
    
    def __exit__(self, exc, value, tb): # -> None:
        """Leave a runtime context, cleaning up all buffers."""
        ...
    
    def close(self): # -> None:
        """Close all buffers."""
        ...
    
    def __iter__(self): # -> Iterator[Tuple[str, str]]:
        """Iterate over the (resource, metric) keys of this provider."""
        ...
    
    def __len__(self): # -> int:
        """Get the number of requested (resource,metric) combinations."""
        ...
    
    def __getitem__(self, resource_metric: Tuple[str, str]) -> Iterable[Measurement]:
        """Create an measurement iterable for a given resource, metric."""
        class _MeasurementIterable:
            ...
        
        
    
    def add_csv_data(self, csv_data: CSVReader, default_resource_id: Optional[str]) -> int:
        """Add a csv data to the measurement buffer."""
        ...
    
    def flip(self): # -> None:
        """Switch from writing to reading mode."""
        ...
    


def prepare_settings_csv(*input_data: SeriesInput, settings: SeriesSettings) -> SeriesSettings:
    """Validate and update the input settings by extracting metadata from a csv header."""
    ...

@contextmanager
def create_import_series_provider(*series_input: SeriesInput, settings: SeriesSettings, progress: bool = ..., measurements_store: MeasurementsStoreType = ...) -> Iterator[CsvImportSeriesProvider]:
    """Create a SeriesProvider from the given csv input and settings.

    This reads the csv input into buffers, ready to export to an etl file.
    Returns a context manager, that closes all temporary buffers on leaving the context.
    """
    ...

def open_csv(*series_inputs: SeriesInput, **csv_format_args) -> Iterator[CSVReaderAndResource]:
    """Open the CSV file specified by this input."""
    ...

