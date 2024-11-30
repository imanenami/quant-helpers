import datetime
import dataclasses
from collections import namedtuple
from typing import Deque

from .trackers import Recorder


@dataclasses.dataclass(init=True, repr=True)
class MarketDataPoint:
    """Base data class for any market price model"""

    time: datetime.datetime
    symbol: str


@dataclasses.dataclass(init=True, repr=True)
class OhlcDataPoint(MarketDataPoint):
    """Model for OHLC data"""

    O: float  # noqa: E741
    H: float  # noqa: E741
    L: float  # noqa: E741
    C: float  # noqa: E741


@dataclasses.dataclass(init=True, repr=True)
class AnalyticsStream:
    """Base data class for any market data analytics model"""

    time: datetime.datetime
    symbol: str
    index: float
    stats: Recorder


@dataclasses.dataclass(init=True, repr=True)
class MarketModel(AnalyticsStream):
    """Basic Market Model Data"""

    volatility: float

    @property
    def payload(self):
        return {
            f"{self.symbol}_index": self.index,
            f"{self.symbol}_volatility": self.volatility,
        }


@dataclasses.dataclass(init=True, repr=True)
class StreamData:
    time: datetime.datetime
    payload: dict[str, float]


# Basic data types
TimeRange = namedtuple("TimeRange", "start end")
DataStream = Deque
