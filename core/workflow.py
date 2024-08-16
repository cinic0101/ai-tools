from abc import ABC
from typing import Self

from core.step import Step


class Workflow(ABC):
    _index: int
    _steps: list[Step]

    def __init__(self):
        self._index = 0
        self._steps = []

    def __iter__(self):
        for step in self._steps:
            yield step

    def add(self, *steps: Step) -> Self:
        for step in steps:
            self._steps.append(step)

        return self

    def run(self):
        for step in self._steps:
            step.process()