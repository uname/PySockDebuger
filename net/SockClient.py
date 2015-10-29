#-*- coding: utf-8 -*-
from log import logger
from SigObject import sigObject
from net import socktypes
import signals
import socket
import select
import socktypes
import threading

class SockClient():
    
    RECV_SIZE = 262144
    
    def __init__(self, parentId, sock, addr, sockType):
        self.parentId = parentId
        self._id = id(self)
        self.sockType = sockType
        self.conFlag = sockType == socktypes.TCP_CLIENT_REMOTE
        self.onlyStopSocket = False
        self.receiver = None
        if sock:
            self.sock = sock
        else:
            self.createSockByType(sockType)
            
        self.sock.setblocking(0)
        self.ip, self.port = addr[0:]
    
    def createSockByType(self, sockType):
        if sockType == socktypes.UDP_CLIENT_LOCAL:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        elif sockType == socktypes.TCP_CLIENT_LOCAL:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            logger.error("***** ERROR SOCKTYPE *****")
    
    def getAddress(self):
        return "%s:%d" % (self.ip, self.port)
    
    def getSockType(self):
        return self.sockType
    
    def isConnected(self):
        return self.conFlag
        
    def connect(self):
        try:
            if self.sock is None:
                self.createSockByType(self.sockType)
                
            self.sock.settimeout(0.5)
            self.sock.connect((self.ip, self.port))
            self.sock.setblocking(0)
            self.conFlag = True
            return True
            
        except Exception as e:
            logger.error("connect exp: %s" % e.message)
            return
        
    def sendall(self, data):
        if data is None:
            return False
        
        return self.sock.sendall(data) is None
    
    def getId(self):
        return self._id
        
    def close(self, stopflag):
        logger.debug("------ CLOSE ------")
        if self.sock is None:
            return
        
        self.sock.close()
        self.sock = None
        self.conFlag = False

        if not stopflag:
            logger.debug("emit SIG_REMOTE_CLOSED")
            sigObject.emit(signals.SIG_REMOTE_CLOSED, self._id, self.parentId)
        
        elif not self.onlyStopSocket:
            logger.debug("emit SIG_REMOVE_SOCK_TAB")
            sigObject.emit(signals.SIG_REMOVE_SOCK_TAB, self._id)
            
    def stop(self, onlyStopSocket=False):
        if self.receiver:
            self.onlyStopSocket = onlyStopSocket
            self.receiver.stop()
    
    def start(self):
        self.receiver = SockClient.Receiver(self)
        self.receiver.start()
    
    class Receiver(threading.Thread):
        def __init__(self, parent):
            threading.Thread.__init__(self)
            self.parent = parent
            self.stopflag = False
        
        def stop(self):
            self.stopflag = True
        
        def run(self):
            if self.parent.sock is None:
                return
                
            while not self.stopflag:
                rfds, _, efds = select.select([self.parent.sock], [], [self.parent.sock], 0.1)
                if len(efds) > 0:
                    logger.error("remote client error")
                    break
                    
                if len(rfds) < 1:
                    continue
                    
                data = self.parent.sock.recv(SockClient.RECV_SIZE)
                if data == "":
                    logger.error("socket closed")
                    break
                
                logger.debug("data from %s:%d -> %s" % (self.parent.ip, self.parent.port, data))
                sigObject.emit(signals.SIG_DATA_RECVED, self.parent._id, self.parent.parentId, data)
            
            self.parent.close(self.stopflag)
            logger.debug("tcp client stopped")
        