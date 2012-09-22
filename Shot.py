from Data import Data
class Shot(Data):
    __x = 0
    __y = 0
    def __init__(self, x, y):
        self._className = self.__class__.__name__
        self.__x = x
        self.__y = y 
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def toString(self):
        return [self._className, self.__x, self.__y]
s = Shot(-1, 2)
print (s.toString())