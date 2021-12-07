from abc import ABC, abstractmethod

from contract.isprite import ISprite


class ISquare(ABC):
    @abstractmethod
    def getSprite(self) -> ISprite:
        ...

    @abstractmethod
    def isTraversable(self) -> bool:
        ...
