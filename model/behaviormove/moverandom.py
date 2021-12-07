from model.behaviormove.behaviormove import BehaviorMove
import random


class MoveRandom(BehaviorMove):
    def getTarget(self) -> [int]:
        newX = self._mobile.getX()
        newY = self._mobile.getY()
        temp = random.randint(0, 3)
        if temp == 0:
            newY -= 1
        elif temp == 1:
            newX += 1
        elif temp == 2:
            newY += 1
        else:
            newX -= 1
        return newX, newY
