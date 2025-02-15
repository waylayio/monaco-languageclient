"""
This type stub file was generated by pyright.
"""

import pandas as pd
from .model import SeriesIterator, SeriesSettings

"""Etl import/export file parser module."""
def prepare_settings_dataframe(input_data: pd.DataFrame, settings: SeriesSettings) -> SeriesSettings:
    """Validate and update the input settings by extracting metadata from a input Pandas DataFrame."""
    ...

def iter_timeseries_dataframe(*input_dataframes: pd.DataFrame, settings: SeriesSettings, progress: bool = ...) -> SeriesIterator:
    """Create a SeriesIterator from the given pandas Dataframe and settings."""
    ...

