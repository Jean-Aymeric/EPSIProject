from abc import ABC, abstractmethod

from contract.isquare import ISquare


class IMobile(ISquare, ABC):
    @abstractmethod
    def getX(self) -> int:
        ...

    @abstractmethod
    def getY(self) -> int:
        ...

    @abstractmethod
    def setModel(self, model) -> None:
        ...

    @abstractmethod
    def getModel(self):
        ...

    @abstractmethod
    def setX(self, x: int):
        ...

    @abstractmethod
    def setY(self, y: int):
        ...
