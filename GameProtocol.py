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
        self.__socket = socket(AF_INET, SOCK_STREAM)
        # get server IP if player is't server
        if(user.isServer) :
            self.__socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            print("Please wait, connecting..")
            ip = '127.0.0.1'
            self.__socket.bind((ip, 1234))
            self.__socket.listen(1)
            conn = self.__socket.accept()# open connection
            data = conn.recv()
            if(data[0] == "Connect?"):
                conn.send(json.encoder("OK"))
                print("Connected")
            conn.closed()
        else :
            ip = raw_input("Enter server IP\n")
            print("Please wait, connecting..")
            self.__socket.connect((ip, 1234))
            self.__socket.send(json.encoder("Connect?"))
            data = json.decoder(self.__socket.recv())
            if(data[0] == "OK"):
                print("Connected")
        #socket configuration
        #set connecting IP and port
    def send(self, data):
        conn, addr = self.__socket.accept()# open connection
        conn.send(json.encoder(data))# encode data and send it
        conn.close() #Important : close connection
    def recive(self):
        self.__socket.listen(1)
        conn = self.__socket.accept()# open connection
        data = json.decoder(conn.recv()) # receive data and decode it 
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