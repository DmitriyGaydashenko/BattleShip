# -*- coding: utf-8 -*-
__author__="Serg"
__date__ ="$22.09.2012 22:08:34$"
from gameFields import gameField
from Shot import Shot
import sys
import random


class userGameField(gameField):
    def randomInit(self):
        #TODO: сделать создание поля пользователем. Временное решение: генерим рандомное поле
            for x in range(self._sizeX):
                for y in range(self._sizeY):
                    self.setValueByCoords(x,y,random.choice([self.CELLTYPE_NONE,self.CELLTYPE_ALIVESHIP]));
    def processShot(self,enemyShot):
        x = enemyShot.getX();
        y = enemyShot.getY();
        if self.getByCoords(x, y) == self.CELLTYPE_NONE:
            self.setValueByCoords(x, y, self.CELLTYPE_SHOOTED_CELL)
        elif self.getByCoords(x, y) ==  self.ALIVESHIP:
            self.setValueByCoords(x, y, self.CELLTYPE_SHOOTED_SHIP)
        else:
            self.setValueByCoords(x,y, self.CELLTYPE_SHOOTED_CELL)
            #ошибки замалчиваются
        return self.getByCoords(x, y);
    def checkAlive(self):
        for x in range(self._sizeX):
                for y in range(self._sizeY):
                    if(self.getByCoords(x,y)==self.CELLTYPE_ALIVESHIP):
                        return True;
        return False;
        