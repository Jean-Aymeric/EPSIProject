from abc import ABC, abstractmethod

from contract.iboard import IBoard
from contract.imobile import IMobile
from contract.isquare import ISquare
from contract.isprite import ISprite


class IModel(ABC):
    @abstractmethod
    def getBoard(self) -> IBoard:
        ...

    @abstractmethod
    def addStar(self) -> None:
        ...

    @abstractmethod
    def getMobiles(self) -> [IMobile]:
        ...
