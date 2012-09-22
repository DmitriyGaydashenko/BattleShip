# -*- coding: utf-8 -*-
__author__="Serg"
__date__ ="$22.09.2012 21:17:33$"
import sys
import gameFields
import userGameField
import enemyGameField
from user import *
from GameProtocol import *
import StringIO

io = StringIO.StringIO()
if __name__ == "__main__":
    print 'Welcome to BattleShip by DarthVader and Livich\n','='*25
    name = raw_input("Enter your nickname: ")
    __isServer = raw_input("Do you want to be a server (s) or client (c)?: ")
    if __isServer == "s":
        __isServer = True
    else:
        __isServer = False
    userObj = User(name,__isServer)
    networkWrapper = GameProtocol(userObj)
    userObj.assignNetworkWrapper(networkWrapper)#теперь пользователь подключён к сети


