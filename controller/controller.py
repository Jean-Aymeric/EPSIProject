from contract.icontroller import IController
from contract.imodel import IModel
from contract.iview import IView
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
        for i in range(100):
            self.__model.addStar()
        while self.__running:
            self.__view.show()
            for mobile in self.__model.getMobiles():
                mobile.move()
            sleep(0.10)

    def viewIsClosed(self) -> None:
        self.__running = False
