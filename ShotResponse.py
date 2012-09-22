from Data import Data
class ShotResponse(Data):
    __shotState = 0
    def __init__(self, shotState):
        self._className = self.__class__.__name__
        self.__shotState = shotState
    def toString(self):
        return [self._className, self.__shotState]
    def getShotState(self):
        return self.__shotState