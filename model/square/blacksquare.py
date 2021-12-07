from model.square.freesquare import FreeSquare


class BlackSquare(FreeSquare):
    def __init__(self):
        FreeSquare.__init__(self, "image/blacksquare.png")
