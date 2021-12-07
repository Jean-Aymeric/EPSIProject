from abc import ABC, abstractmethod


class ISprite(ABC):
    @abstractmethod
    def getImageName(self) -> str:
        ...
