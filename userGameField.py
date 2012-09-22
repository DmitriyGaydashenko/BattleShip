# -*- coding: utf-8 -*-
__author__="Serg"
__date__ ="$22.09.2012 22:08:34$"
from gameFields import gameField

class userGameField(gameField):
    def __init__(self):
        #TODO: сделать создание поля пользователем. Временное решение: генерим рандомное поле
            for cell in self._field.flat:
                cell = random.choice([CELLTYPE_NONE,CELLTYPE_ALIVESHIP]);
        