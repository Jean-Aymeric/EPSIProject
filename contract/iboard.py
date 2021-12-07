from abc import ABC, abstractmethod

from contract.isquare import ISquare


class IBoard(ABC):
    @abstractmethod
    def getSquares(self) -> [ISquare]:
        ...

    @abstractmethod
    def getWidth(self) -> int:
        ...

    @abstractmethod
    def getHeight(self) -> int:
        ...
