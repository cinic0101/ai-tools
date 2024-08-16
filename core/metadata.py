from abc import ABC


class Metadata(ABC):
    _meta: dict = None

    def __init__(self):
        self._meta = {}

    def _set_meta(self, key: str, value: any):
        self._meta[key] = value

    def meta(self):
        return self._meta
