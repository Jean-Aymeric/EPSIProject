from contract.isprite import ISprite


class Sprite(ISprite):
    __imageName: str

    def __init__(self, imageName: str) -> None:
        self.__imageName = imageName

    def getImageName(self) -> str:
        return self.__imageName
