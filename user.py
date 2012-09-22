#Здесь определён класс User - класс для представления пользователя, будь он клиент или сервер
__author__="Serg"
__date__ ="$22.09.2012 23:50:26$"
from userGameField import userGameField
from enemyGameField import enemyGameField

class user:
    playerName = "";#имя/ник игрока
    __isServer = false;
    network = null#TODO:network wrapper
    gameField = userGameField()
    enemyField = enemyGameField()
    
    def __init__(self,playerName="unnamedPlayer",serverMode=false,netWrapper=null):
        self.playerName = playerName
        self.isServer = serverMode
        self.network = netWrapper
        return;
    def onShot(self,enemyShot):
        shotResult = this.gameField.processShot(this.gameField,enemyShot);
        #shotResult отвечает константой CELLTYPE_* из gameFields - это новое состояние клетки
        return;
    def makeShot(self):

        return;
