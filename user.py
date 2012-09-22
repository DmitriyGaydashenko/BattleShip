# -*- coding: utf-8 -*-
#Здесь определён класс User - класс для представления пользователя, будь он клиент или сервер
__author__="Serg"
__date__ ="$22.09.2012 23:50:26$"
from userGameField import userGameField
from enemyGameField import enemyGameField

class User:
    playerName = "";#имя/ник игрока
    __isServer = False;
    __isLoose = False;
    network = 0 #TODO:network wrapper
    gameField = userGameField()
    enemyField = enemyGameField()
    
    def __init__(self,playerName="unnamedPlayer",serverMode=False):
        self.playerName = playerName
        self.isServer = serverMode
        return;
    def onShot(self,enemyShot):
        shotResult = this.gameField.processShot(enemyShot);
        #shotResult отвечает константой CELLTYPE_* из gameFields - это новое состояние клетки
        return;
    def makeShot(self):

        return;
    def assignNetworkWrapper(self,network):
        self.network = network
    @property
    def isServer(self):
        return self.__isServer;
    @property
    def isLoose(self):
        return self.__isLoose;
