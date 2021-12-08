from random import randint

from model.square.blacksquare import BlackSquare
from model.square.greensquare import GreenSquare
from model.square.redsquare import RedSquare
from model.square.square import Square
from model.square.obstacle import Obstacle
from model.square.freesquare import FreeSquare
from contract.iboard import IBoard


class Board(IBoard):
    __width: int
    __height: int
    __squares = [[Square]]
    __obstacles: [Obstacle]
    __freeSquares: [FreeSquare]

    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__squares = [[None] * width for _ in range(height)]
        self.__obstacles = [RedSquare(), GreenSquare()]
        self.__freeSquares = [BlackSquare()]
        self.__fillBoard()

    def __fillBoard(self):
        for i in range(0, self.__width):
            for j in range(0, self.__height):
                if ((i + j) % 3 == 0) and (i % 3 == 0):
                    self.__squares[j][i] = self.__obstacles[randint(0,1)]
                else:
                    self.__squares[j][i] = self.__freeSquares[0]

    def getSquares(self) -> [[Square]]:
        return self.__squares

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height
