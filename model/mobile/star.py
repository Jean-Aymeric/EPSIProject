from model.behaviormove.moverandom import MoveRandom
from model.mobile.mobile import Mobile
from model.square.sprite import Sprite


class Star(Mobile):
    def __init__(self, x: int, y: int):
        Mobile.__init__(self, x, y, True, Sprite("image/star.png"), MoveRandom())

    def die(self) -> None:
        Mobile.die(self)
