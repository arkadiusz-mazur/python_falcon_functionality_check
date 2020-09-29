from abc import abstractmethod
from typing import Any, Optional


class Command:
    def __init__(self, **kwargs: Any) -> None:
        for field in kwargs:
            setattr(self, field, kwargs[field])

    @abstractmethod
    def handle(self) -> Optional[Any]:
        pass
