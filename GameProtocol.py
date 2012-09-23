# -*- coding: UTF-8 -*-
from socket import *
__author__="Dmitriy"
__date__ ="$23.09.2012 01:18:26$"
import Shot
import ShotResponse
import json
import time

class netPackage:
    NPTYPE_GENERIC = 0
    NPTYPE_CONNECT = 1
    NPTYPE_OK = 200
    NPTYPE_SHOT = 2
    NPTYPE_SHOTRESPONSE = 3
    __pType = NPTYPE_GENERIC
    def jsonize(self,data):
        return json.dumps({"type":self.__pType,"data":data})
    def __init__(self,type=NPTYPE_GENERIC):
        self.__pType = type


class GameProtocol :
    __socket = 0
    __ip = "127.0.0.1"
    __conn = 0
    def __init__(self, user):
        self.__socket = socket(AF_INET, SOCK_STREAM)
        # get server IP if player is't server
        if(user.isServer) :
            self.__socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            self.__ip = raw_input("Enter server IP\n")
            print("Please wait, connecting..")
            self.__socket.bind((self.__ip, 1234))
            self.__socket.listen(1)
            self.__conn, arrn = self.__socket.accept()# open connection
            data = json.loads(self.__conn.recv(1024))
            if(data["type"] == netPackage.NPTYPE_CONNECT):
                self.__conn.send(netPackage(netPackage.NPTYPE_OK).jsonize({"timestamp":time.time()}))
                print "Connected. Delta time = %.3f"%(time.time()-float(data["data"]["timestamp"]))
            self.__conn.close()
        else :
            self.__ip = raw_input("Enter server IP\n")
            print("Please wait, connecting..")
            self.__socket.connect((self.__ip, 1234))
            self.__socket.send(netPackage(netPackage.NPTYPE_CONNECT).jsonize({"timestamp":time.time()}))
            data = json.loads(self.__socket.recv(1024))
            if(data["type"] == netPackage.NPTYPE_OK):
                print "Connected. Delta time = %.3f"%(time.time()-float(data["data"]["timestamp"]))
        #socket configuration
        #set connecting IP and port
    def send(self, data):
        self.__socket = socket(AF_INET, SOCK_STREAM)
        #conn, addr = self.__socket.accept()# open connection
        self.__socket.connect((self.__ip, 1234))
        self.__socket.send(data)#send it
    def recive(self):
        self.__socket = socket(AF_INET, SOCK_STREAM)
        self.__socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.__socket.bind((self.__ip, 1234))
        self.__socket.listen(1)
        self.__conn, arrn = self.__socket.accept()# open connection
        data = json.loads(self.__conn.recv(1024)) # receive data and decode it
        self.__conn.close()# close connection
        resultingData = 0
        #define received data type
        if (data["type"] == netPackage.NPTYPE_SHOT):
            resultingData = Shot.Shot(data["data"]["x"], data["data"]["y"])
        elif (data["type"] == netPackage.NPTYPE_SHOTRESPONSE) :
            resultingData = ShotResponse.ShotResponse(data["data"]["shotResult"])
        else :
            raise ValueError("Internal error, invalid data type")
        return resultingData