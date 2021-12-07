from abc import ABC, abstractmethod

from contract.imobile import IMobile


class BehaviorMove(ABC):
    _mobile: IMobile

    def setMobile(self, mobile) -> None:
        self._mobile = mobile

    def move(self) -> None:
        newX, newY = self.getTarget()
        if self.__isTargetValid(newX, newY):
            self._mobile.setX(newX)
            self._mobile.setY(newY)

    def __isTargetValid(self, x: int, y: int):
        return self._mobile.getModel().getBoard().getSquares()[y][x].isTraversable() \
               and 0 <= x <= self._mobile.getModel().getBoard().getWidth() \
               and 0 <= y <= self._mobile.getModel().getBoard().getHeight()

    @abstractmethod
    def getTarget(self) -> [int]:
        ...
