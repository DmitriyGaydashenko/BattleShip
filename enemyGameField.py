# -*- coding: utf-8 -*-
__author__="Serg"
__date__ ="$22.09.2012 22:27:47$"
from gameFields import gameField

class enemyGameField(gameField):
    def __init__(self):
            for x in range(len(self._field)):
                for y in range(len(self._field[x])):
                    self._field[x][y] = self.CELLTYPE_NONE;