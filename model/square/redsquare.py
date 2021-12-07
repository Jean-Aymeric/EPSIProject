from model.square.obstacle import Obstacle


class RedSquare(Obstacle):
    def __init__(self):
        Obstacle.__init__(self, "image/redsquare.png")
