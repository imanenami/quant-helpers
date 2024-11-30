import abc
import datetime

import numpy as np


class Recorder(abc.ABC):
    """Abstract Base Class which defines the interface for any stats recorder object"""

    REPORT_STATS = ["abstract_stat"]

    def __init__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def record(self, *args):
        pass

    def __str__(self) -> str:
        return ", ".join(
            [f"{stat.title()}={getattr(self, stat)}" for stat in self.REPORT_STATS]
        )


class SummaryRecorder(Recorder):
    """Stats recorder which provides basic summary stats such as mean, max, min, count, etc."""

    REPORT_STATS = ["sum", "count", "mean", "min", "max", "elapsed"]

    def __init__(self):
        self.min = 0
        self.max = 0
        self.sum = 0
        self.count = 0
        self.start_time = datetime.datetime.now()
        self.last_record = datetime.datetime.now()

    def record(self, x):
        if not np.isfinite(x):
            return

        self.sum += x
        self.count += 1
        if x > self.max:
            self.max = x
        elif x < self.min:
            self.min = x
        self.last_record = datetime.datetime.now()

    @property
    def mean(self) -> float:
        return self.sum / self.count

    @property
    def elapsed(self) -> str:
        return f"{(self.last_record - self.start_time).seconds}s"
