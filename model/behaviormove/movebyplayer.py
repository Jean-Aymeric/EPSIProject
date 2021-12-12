from model.behaviormove.behaviormove import BehaviorMove


class MoveByPlayer(BehaviorMove):
    def getTarget(self) -> [int]:
        newX = self._mobile.getX()
        newY = self._mobile.getY()
        temp = self._mobile.getNextDirection()
        if temp == 0:
            newY -= 1
        elif temp == 1:
            newX += 1
        elif temp == 2:
            newY += 1
        elif temp == 3:
            newX -= 1
        self._mobile.setNextDirection(-1)
        return newX, newY
