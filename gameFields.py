__author__="Serg"
__date__ ="$22.09.2012 21:40:55$"

#базовый класс для полей игры (поле игрока и копия поля противника, к-я заполняется по ходу игры)

class gameField:
    self.__sizeX = 10;
    self.__sizeY = 10;
    self.__field = [[0]*self.__sizeX]*self.__sizeY; #создаётся поле заполненное нулями __sizeX на __sizeY
    #константы для всевозможных значений в клетках
    CELLTYPE_NONE = 0;
    CELLTYPE_ALIVESHIP = 1;
    CELLTYPE_SHOOTED_CELL = 2;
    CELLTYPE_SHOOTED_SHIP = 3;

    def __init__(self):
        #конструктор поля проходится по всему массиву клеток и заполняет их CELLTYPE_NONE
        for cell in self.__field.flat:
            cell = CELLTYPE_NONE;
        return self;
    
    def getValueByCoords(self,x=0,y=0):
        return self.__field[x][y]

    def setValueByCoords(self,x=0,y=0,value=0):
        self.__field[x][y] = value;
        return self.__field[x][y];