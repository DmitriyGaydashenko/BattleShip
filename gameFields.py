# -*- coding: utf-8 -*-
__author__="Serg"
__date__ ="$22.09.2012 21:40:55$"
import sys
#базовый класс для полей игры (поле игрока и копия поля противника, к-я заполняется по ходу игры)

class gameField:
    _sizeX = 10;
    _sizeY = 10;
    _field = [[0]*_sizeX]*_sizeY; #создаётся поле заполненное нулями __sizeX на __sizeY
    #константы для всевозможных значений в клетках
    CELLTYPE_NONE = 0;
    CELLTYPE_ALIVESHIP = 1;
    CELLTYPE_SHOOTED_CELL = 2;
    CELLTYPE_SHOOTED_SHIP = 3;

    def __init__(self):
        #конструктор поля проходится по всему массиву клеток и заполняет их CELLTYPE_NONE
            for x in range(self._sizeX):
                for y in range(self._sizeY):
                    self._field[x][y] = self.CELLTYPE_NONE;
    
    def getValueByCoords(self,x=0,y=0):
        return self._field[int(x)][int(y)]

    def setValueByCoords(self,x=0,y=0,value=0):
        self._field[int(x)][int(y)] = int(value);
        return self._field[int(x)][int(y)];
    
    def getByCoords(self,x,y):#псевдоним
        return self.getValueByCoords(x,y)

#getSize по параметру sign(0/1) возвращает x или y измерение поля
    def getSize(self,sign=0):
        if sign==0:
            return self._sizeX
        else:
            return self._sizeY

    def friendlyPrint(self):
        s=""
        for y in range(self._sizeY):
            print s
            s = ""
            for x in range(self._sizeX):
                s+= " {0} ".format(self._field[x][y])


