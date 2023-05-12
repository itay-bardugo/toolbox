from abc import ABCMeta, abstractmethod
from typing import Any, Type


class Entrypoint(metaclass=ABCMeta):
    def __init__(self, **kwargs):
        self.pipeline = self.get_pipeline_klass()(**kwargs)

    @abstractmethod
    def get_pipeline_klass(self) -> Type[Any]:
        ...

    @abstractmethod
    def enter(self):
        ...
