import random
__author__="Serg"
__date__ ="$22.09.2012 22:08:34$"

class userGameField(gameField):
    def __init__(self):
        #TODO: сделать создание поля пользователем. Временное решение: генерим рандомное поле
            for cell in self.__field.flat:
            cell = random.choice([CELLTYPE_NONE,CELLTYPE_ALIVESHIP]);
        return;