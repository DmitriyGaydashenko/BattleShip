# -*- coding: utf-8 -*-
__author__="Serg"
__date__ ="$22.09.2012 22:27:47$"
from gameFields import gameField

class enemyGameField(gameField):
    def __init__(self):
            for cell in self._field.flat:
                cell = CELLTYPE_NONE;