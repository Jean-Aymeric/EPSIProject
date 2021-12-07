from abc import ABC
from model.square.sprite import Sprite
from model.square.square import Square


class FreeSquare(Square, ABC):
    def __init__(self,  image : str):
        Square.__init__(self, True, Sprite(image))

