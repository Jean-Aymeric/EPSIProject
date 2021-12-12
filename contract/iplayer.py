from abc import ABC, abstractmethod

from contract.imobile import IMobile


class IPlayer(IMobile, ABC):
    @abstractmethod
    def setNextDirection(self, nextDirection: int) -> None:
        ...

    @abstractmethod
    def goUp(self) -> None:
        ...

    @abstractmethod
    def goRight(self) -> None:
        ...

    @abstractmethod
    def goLeft(self) -> None:
        ...

    @abstractmethod
    def goDown(self) -> None:
        ...
