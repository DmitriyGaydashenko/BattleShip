# -*- coding: UTF-8 -*-
from socket import *
__author__="Dmitriy"
__date__ ="$23.09.2012 01:18:26$"
import Data
import Shot
from user import User
import ShotResponse
import json
import time

class netPackage:
    NPTYPE_GENERIC = 0
    NPTYPE_CONNECT = 1
    NPTYPE_OK = 200
    __pType = NPTYPE_GENERIC
    def jsonize(self,data):
        return json.dumps({"type":self.__pType,"data":data})
    def __init__(self,type=NPTYPE_GENERIC):
        self.__pType = type


class GameProtocol :
    __socket = 0
    def __init__(self, user):
        self.__socket = socket(AF_INET, SOCK_STREAM)
        # get server IP if player is't server
        if(user.isServer) :
            self.__socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            ip = raw_input("Enter server IP\n")
            print("Please wait, connecting..")
            self.__socket.bind((ip, 1234))
            self.__socket.listen(1)
            conn, arrn = self.__socket.accept()# open connection
            data = json.loads(conn.recv(1024))
            if(data["type"] == netPackage.NPTYPE_CONNECT):
                conn.send(netPackage(netPackage.NPTYPE_OK).jsonize({"timestamp":time.time()}))
                print "Connected. Delta time = %.3f"%(time.time()-float(data["data"]["timestamp"]))
            conn.close()
        else :
            ip = raw_input("Enter server IP\n")
            print("Please wait, connecting..")
            self.__socket.connect((ip, 1234))
            self.__socket.send(netPackage(netPackage.NPTYPE_CONNECT).jsonize({"timestamp":time.time()}))
            data = json.loads(self.__socket.recv(1024))
            if(data["type"] == netPackage.NPTYPE_OK):
                print "Connected. Delta time = %.3f"%(time.time()-float(data["data"]["timestamp"]))
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