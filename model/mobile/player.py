from model.behaviormove.movebyplayer import MoveByPlayer
from model.mobile.mobile import Mobile
from model.square.sprite import Sprite


class Player(Mobile):
    __nextDirection: int

    def __init__(self, x: int, y: int):
        self.__nextDirection = -1
        Mobile.__init__(self, x, y, True, Sprite("image/player.png"), MoveByPlayer())

    def die(self) -> None:
        Mobile.die(self)

    def setNextDirection(self, nextDirection: int) -> None:
        if 0 >= nextDirection >= 3:
            self.__nextDirection = nextDirection
        else:
            self.__nextDirection = -1

    def goUp(self) -> None:
        self.__nextDirection = 0

    def goRight(self) -> None:
        self.__nextDirection = 1

    def goDown(self) -> None:
        self.__nextDirection = 2

    def goLeft(self) -> None:
        self.__nextDirection = 3

    def getNextDirection(self) -> int:
        return self.__nextDirection
