from model.square.obstacle import Obstacle


class GreenSquare(Obstacle):
    def __init__(self):
        Obstacle.__init__(self, "image/greensquare.png")
