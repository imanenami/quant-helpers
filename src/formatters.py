import abc
import datetime
from typing import Any

import numpy as np

from . import logger


class Formatter(abc.ABC):
    """Abstract Base Class which defines the interface for any formatter object"""
    def __init__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def format(self, field_name: str, field_value: str) -> Any:
        pass


class DefaultFormatter(Formatter):
    """Default Formatter class which treats every field other than `time_field` as `float`"""

    def __init__(
        self, time_field: str = "time", time_format: str = "%d.%m.%Y %H:%M:%S.000"
    ):
        self.time_field = time_field
        self.time_format = time_format

    def format(self, field_name: str, field_value: str) -> datetime.datetime | float:
        if field_name == self.time_field:
            return self.format_time(field_value)
        return self.format_any(field_value)

    def format_time(self, field_value: str) -> datetime.datetime:
        return datetime.datetime.strptime(field_value, self.time_format)

    def format_any(self, field_value: str) -> float:
        return self.to_float(field_value)

    @staticmethod
    def to_float(val: str) -> float:
        try:
            return float(val)
        except Exception:
            logger.warning(f"WARN: Unable to convert {val} to Float")
            return np.nan
