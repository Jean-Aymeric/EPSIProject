from tkinter import Tk, Canvas
from PIL import Image, ImageTk

from contract.icontroller import IController
from contract.imodel import IModel, IMobile, IBoard, ISquare, ISprite
from contract.iview import IView


class View(IView):
    __model: IModel
    __controller: IController
    __zoom: int

    def __init__(self):
        self.__zoom = 10

    def setModel(self, model: IModel):
        self.__model = model
        self.__createWindow()

    def setController(self, controller: IController) -> None:
        self.__controller = controller

    def __onClosing(self):
        self.__controller.viewIsClosed()
        self.__window.destroy()

    def show(self):
        forest: IBoard
        squares: [[ISquare]]
        forest = self.__model.getBoard()
        squares = forest.getSquares()
        images = {}
        for y in range(self.__model.getBoard().getHeight()):
            for x in range(self.__model.getBoard().getWidth()):
                imageName = squares[y][x].getSprite().getImageName()
                if imageName not in images:
                    image = Image.open(imageName).resize((self.__zoom, self.__zoom), Image.ANTIALIAS)
                    images[imageName] = ImageTk.PhotoImage(image)
                self.__canvas.create_image(x * self.__zoom + self.__zoom / 2,
                                           y * self.__zoom + self.__zoom / 2,
                                           image=images[imageName])
        mobile: IMobile
        for mobile in self.__model.getMobiles():
            imageName = mobile.getSprite().getImageName()
            if imageName not in images:
                image = Image.open(imageName).resize((self.__zoom, self.__zoom), Image.ANTIALIAS)
                images[imageName] = ImageTk.PhotoImage(image)
            self.__canvas.create_image(mobile.getX() * self.__zoom + self.__zoom / 2,
                                       mobile.getY() * self.__zoom + self.__zoom / 2,
                                       image=images[imageName])
        self.__window.update()

    def __createWindow(self):
        self.__window = Tk()
        self.__window.title("EPSI Project")
        self.__window.geometry(str(self.__model.getBoard().getWidth() * self.__zoom)
                               + "x" + str(self.__model.getBoard().getHeight() * self.__zoom))
        self.__canvas = Canvas(self.__window)
        self.__canvas.configure(bg="Black")
        self.__canvas.pack(fill="both", expand=True)
        self.__window.protocol("WM_DELETE_WINDOW", self.__onClosing)
        self.__window.deiconify()
        self.__window.update()
