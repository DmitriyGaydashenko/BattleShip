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
    def onLoose(self):
        self.__isLoose = True;
        print "\nYou loose!\n"
    
    def onShot(self,enemyShot):
        shotResult = this.gameField.processShot(enemyShot);
        #shotResult отвечает константой CELLTYPE_* из gameFields - это новое состояние клетки
        print "Enemy shot("+enemyShot.getX()+","+enemyShot.getY()+") result: "+{
        gameField.CELLTYPE_SHOOTED_CELL: "empty cell",
        gameField.CELLTYPE_SHOOTED_SHIP: "ship shooted"
        }.get(shotResult);
        if gameField.checkAlive() == False:
            self.onLoose();
        
    def makeShot(self):
        x=-1
        y=-1
        print "Your field: \n"
        self.gameField.friendlyPrint();
        print "\n Enemy field: \n"
        self.enemyField.friendlyPrint();
        while self.gameField[x][y]<>0 or x==-1 or y==-1: #проверка, чтобы туда действительно можно было стрелять
            if x==-1 or y==-1 or x>self.gameField.getSize(0) or y>self.gameField.getSize(1):
                continue
            if(self.gameField[x][y]==2):
                print "There we's already shooted. Retry...\n"
            if(self.gameField[x][y]==3):
                print "There we's already shooted and there was a ship. Retry...\n"
            x = raw_input("Your shot. X = ")
            y = raw_input("Y = ")
        shot = shot(x,y);
        network.send(shot);#всё сразу же пошло в сеть
        return;
    def assignNetworkWrapper(self,network):
        self.network = network
    @property
    def isServer(self):
        return self.__isServer;
    @property
    def isLoose(self):
        return self.__isLoose;
