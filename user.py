# -*- coding: utf-8 -*-
#Здесь определён класс User - класс для представления пользователя, будь он клиент или сервер
__author__="Serg"
__date__ ="$22.09.2012 23:50:26$"
from userGameField import userGameField
from enemyGameField import enemyGameField
from GameProtocol import netPackage

class User:
    playerName = "";#имя/ник игрока
    __isServer = False;
    __isLoose = False;
    network = 0 #TODO:network wrapper
    gameField = userGameField()
    gameField.randomInit()
    enemyField = enemyGameField()
    
    def __init__(self,playerName="unnamedPlayer",serverMode=False):
        self.playerName = playerName
        self.isServer = serverMode
        return;
    def onLoose(self):
        self.__isLoose = True;
    
    def onShot(self,enemyShot):
        shotResult = self.gameField.processShot(enemyShot);
        #shotResult отвечает константой CELLTYPE_* из gameFields - это новое состояние клетки
        print "Enemy shot("+enemyShot.getX()+","+enemyShot.getY()+") result: "+{
        self.gameField.CELLTYPE_SHOOTED_CELL: "empty cell",
        self.gameField.CELLTYPE_SHOOTED_SHIP: "ship shooted"
        }.get(shotResult);
        if self.gameField.checkAlive() == False:
            self.onLoose();
        
    def makeShot(self):
        x=-1
        y=-1
        print "Your field: \n"
        self.gameField.friendlyPrint();
        print "\n Enemy field: \n"
        self.enemyField.friendlyPrint();
        while x==-1 or y==-1 or self.enemyField.getByCoords(int(x),int(y))!=0: #проверка, чтобы туда действительно можно было стрелять
            if x>self.enemyField.getSize(0) or y>self.enemyField.getSize(1):
                continue
            if(self.enemyField.getByCoords(x,y)==2):
                print "There we's already shooted. Retry...\n"
            if(self.enemyField.getByCoords(x,y)==3):
                print "There we's already shooted and there was a ship. Retry...\n"
            x = raw_input("X = ")
            y = raw_input("Y = ")
        self.network.send(netPackage(netPackage.NPTYPE_SHOT).jsonize({"x":x,"y":y}));#всё сразу же пошло в сеть
        shotResponse = self.network.recive()
        self.enemyField.setValueByCoords(x,y, shotResponse.getShotState());
        return;
    def assignNetworkWrapper(self,network):
        self.network = network
    @property
    def isServer(self):
        return self.__isServer;
    @property
    def isLoose(self):
        return self.__isLoose;
