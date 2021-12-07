from abc import ABC

from model.square.sprite import Sprite, ISprite


class Square(ABC):
    __traversable: bool
    __sprite: Sprite

    def __init__(self, traversable: bool, sprite: ISprite):
        self.__traversable = traversable
        self.__sprite = sprite

    def isTraversable(self) -> bool:
        return self.__traversable

    def getSprite(self) -> ISprite:
        return self.__sprite
