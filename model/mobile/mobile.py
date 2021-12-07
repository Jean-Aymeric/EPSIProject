from abc import ABC

from model.behaviormove.behaviormove import BehaviorMove
from model.square.square import Square
from model.square.sprite import Sprite
from contract.imobile import IMobile
from contract.imodel import IModel


class Mobile(Square, IMobile, ABC):
    __x: int
    __y: int
    __model: IModel
    __behaviorMove: BehaviorMove
    __alive: bool

    def __init__(self, x: int, y: int, traversable: bool, sprite: Sprite, behaviorMove: BehaviorMove):
        self.__x = x
        self.__y = y
        self.__alive = True
        self.__behaviorMove = behaviorMove
        self.__behaviorMove.setMobile(self)
        Square.__init__(self, traversable, sprite)

    def getX(self) -> int:
        return self.__x

    def getY(self) -> int:
        return self.__y

    def setX(self, x: int):
        self.__x = x

    def setY(self, y: int):
        self.__y = y

    def setModel(self, model: IModel):
        self.__model = model

    def getModel(self):
        return self.__model

    def move(self):
        if self.__alive:
            self.__behaviorMove.move()

    def die(self):
        self.__alive = False
