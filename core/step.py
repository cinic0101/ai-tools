from abc import ABC, abstractmethod
from typing import Self
from enum import Enum

from core.versioning import Versioning


class StepType(Enum):
    STRING = 0


class StepProcess(ABC):
    _result: any

    @abstractmethod
    def _pre_process(self):
        pass

    @abstractmethod
    def _process(self):
        pass

    @abstractmethod
    def _post_process(self):
        pass

    def process(self) -> Self:
        self._pre_process()
        self._process()
        self._post_process()

        return self

    def result(self) -> any:
        return self._result


class Step(ABC, StepProcess, Versioning):

    @staticmethod
    @abstractmethod
    def input_type() -> StepType:
        pass

    @staticmethod
    @abstractmethod
    def output_type() -> StepType:
        pass
