from abc import ABC, abstractmethod

from contract.imodel import IModel


class IView(ABC):
    @abstractmethod
    def show(self) -> None:
        ...

    @abstractmethod
    def setModel(self, model: IModel) -> None:
        ...

    @abstractmethod
    def setController(self, controller) -> None:
        ...
