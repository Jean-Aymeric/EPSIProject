from abc import ABC, abstractmethod
from contract.imodel import IModel
from contract.iview import IView
from contract.action import Action


class IController(ABC):
    @abstractmethod
    def start(self) -> None:
        ...

    @abstractmethod
    def setModel(self, model: IModel) -> None:
        ...

    @abstractmethod
    def setView(self, view: IView) -> None:
        ...

    @abstractmethod
    def viewIsClosed(self) -> None:
        ...

    @abstractmethod
    def performAction(self, action: Action) -> None:
        ...