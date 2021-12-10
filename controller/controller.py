from contract.icontroller import IController
from contract.imodel import IModel
from contract.iview import IView
from contract.action import Action
from time import sleep


class Controller(IController):
    __model: IModel
    __view: IView
    __running: bool

    def __init__(self):
        self.__running = True

    def setModel(self, model: IModel):
        self.__model = model

    def setView(self, view: IView):
        self.__view = view
        self.__view.setController(self)

    def start(self):
        for i in range(10):
            self.__model.addStar()
        self.__model.addPlayer()
        while self.__running:
            self.__view.show()
            for mobile in self.__model.getMobiles():
                mobile.move()
            sleep(0.05)

    def viewIsClosed(self) -> None:
        self.__running = False

    def performAction(self, action: Action):
        if action == Action.UP:
            self.__model.getPlayer().goUp()
        elif action == Action.RIGHT:
            self.__model.getPlayer().goRight()
        elif action == Action.DOWN:
            self.__model.getPlayer().goDown()
        elif action == Action.LEFT:
            self.__model.getPlayer().goLeft()
