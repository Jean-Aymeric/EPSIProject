from random import randint

from contract.imodel import IModel
from contract.iplayer import IPlayer
from model.board import Board
from model.mobile.mobile import Mobile, IMobile
from model.mobile.player import Player
from model.mobile.star import Star


class Model(IModel):
    __board: Board
    __mobiles: [Mobile]
    __player: IPlayer

    def __init__(self):
        self.__board = Board(20, 20)
        self.__mobiles = []

    def getBoard(self):
        return self.__board

    def __addMobile(self, mobile: Mobile) -> None:
        self.__mobiles.append(mobile)
        mobile.setModel(self)

    def addStar(self) -> None:
        self.__addMobile(Star(randint(1, self.getBoard().getWidth() - 1), randint(1, self.getBoard().getHeight() - 1)))

    def addPlayer(self) -> None:
        self.__player = Player(1, 1)
        self.__addMobile(self.__player)

    def getMobiles(self) -> [IMobile]:
        return self.__mobiles

    def getPlayer(self) -> IPlayer:
        return self.__player
