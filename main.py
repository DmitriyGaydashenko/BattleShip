# -*- coding: utf-8 -*-
__author__="Serg"
__date__ ="$22.09.2012 21:17:33$"
import sys
import gameFields
import userGameField
import enemyGameField
import user
import StringIO


if __name__ == "__main__":
    io = StringIO.StringIO()
    io.write("Welcome to BattleShip by DarthVader and Livich\nEnter your nickname: ")
    name = io.getvalue()
    io.write("Do you want to be a server (s) or client (c)?: ")
    isServer = io.getvalue()
    if isServer == "s":
        isServer = True
    else:
        isEerver = False
    
    user = user(name,isServer,null) #TODO: подключить сюда сетевой враппер


