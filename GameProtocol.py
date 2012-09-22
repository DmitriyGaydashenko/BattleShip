# -*- coding: UTF-8 -*-
from socket import *
__author__="Dmitriy"
__date__ ="$23.09.2012 01:18:26$"
import Data
import Shot
from user import User
import ShotResponse
import json
class GameProtocol :
    __socket = 0
    def __init__(self, user):
        ip = ""
        # get server IP if player is't server
        if(user.isServer) :
            ip = '127.0.0.1'
        else :
            ip = raw_input("Enter server IP\n")
        #socket configuration
        self.__socket = socket(AF_INET, SOCK_STREAM)
        self.__socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        #set connecting IP and port
        self.__socket.bind((ip, 1234))
    def send(self, data):
        conn = self.__socket.accept()# open connection
        conn.send(json.decoder(data))# decode data and send it
        conn.close() #Important : close connection
    def recive(self):
        conn = self.__socket.accept()# open connection
        data = json.encoder(conn.recv()) # receive data and encode it 
        conn.close()# close connection
        resultingData = 0
        #define received data type
        if (data[0] == "Shot"):
            resultingData = Shot(data[1], data[2])
        elif (data[0] == "ShotResponse") :
            resultingData = ShotResponse(data[1])
        else :
            raise ValueError("Internal error, invalid data type")
        return resultingData