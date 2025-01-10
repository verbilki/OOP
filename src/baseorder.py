from abc import ABC, abstractmethod


class BaseOrder(ABC):
    """Абстрактный базовый класс для классов Order и Category."""

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self) -> str:
        pass
