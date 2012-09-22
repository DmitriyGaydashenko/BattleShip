class Data :
    _className = ""
    def __init__(self):
        self._className = self.__class__.__name__
    def getClassName(self):
        return self._className
    def toString(self) :
        return self.getClassName()
        #return self.__class__.__name__
    def selfSend(self):
        return 0