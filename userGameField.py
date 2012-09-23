# -*- coding: utf-8 -*-
__author__="Serg"
__date__ ="$22.09.2012 22:08:34$"
from gameFields import gameField
from Shot import Shot
import sys
import random


class userGameField(gameField):
    def __init__(self):
        #TODO: сделать создание поля пользователем. Временное решение: генерим рандомное поле
            for x in range(len(self._field)):
                for y in range(len(self._field[x])):
                    self._field[x][y] = random.choice([self.CELLTYPE_NONE,self.CELLTYPE_ALIVESHIP]);
    def processShot(self,enemyShot):
        x = enemyShot.getX();
        y = enemyShot.getY();
        if self._field[x][y] == self.CELLTYPE_NONE:
            self._field[x][y] = CELLTYPE_SHOOTED_CELL
        elif self._field[x][y] ==  self.ALIVESHIP:
            self._field[x][y] = CELLTYPE_SHOOTED_SHIP
        else:
            self._field[x][y] = CELLTYPE_SHOOTED_CELL
            #ошибки замалчиваются
        return self._field[x][y];
    def checkAlive(self):
        for x in range(len(self._field)):
                for y in range(len(self._field[x])):
                    if(self._field[x][y]==self.CELLTYPE_ALIVESHIP):
                        return True;
        return False;
        