from contract.iview import IView
from contract.imodel import IModel
from contract.icontroller import IController
from controller.controller import Controller
from model.model import Model
from view.view import View

controller: IController
model: IModel
view: IView

controller = Controller()
model = Model()
view = View()
controller.setView(view)
controller.setModel(model)
view.setModel(model)

controller.start()
