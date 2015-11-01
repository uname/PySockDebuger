#-*- coding: utf-8 -*-
import socket
import threading
import select
import signals
from log import logger
from SigObject import sigObject
from log import logger
from net import socktypes

class UdpServer(threading.Thread):
    
    RECV_SIZE = 262144
    
    def __init__(self, port, ip="0.0.0.0"):
        threading.Thread.__init__(self)
        self.stopflag = False
        self.ip, self.port = ip, port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._id = id(self.sock)
        
        self.remoteAddr = None
    
    def getId(self):
        return self._id
    
    def getAddress(self):
        return "%s:%d" % (self.ip, self.port)
        
    def start_(self):
        try:
            self.sock.bind((self.ip, self.port))
        except:
            logger.error("bind address error: %s" % self.getAddress())
            return
        
        self.start()
        
        return True
    
    def getLocalPort(self):
        return self.port
    
    def getSockType(self):
        return socktypes.UDP_SERVER
    
    def isConnected(self):
        return self.remoteAddr
        
    def sendall(self, data):
        if not self.remoteAddr:
            logger.warning("no remote udp client")
            return
        
        if not isinstance(data, basestring):
            return
      
        n = self.sock.sendto(data, self.remoteAddr)
        total = len(data)
        if n < total:
            logger.warning("not all data sent")
        return n == total
    
    def stop(self):
        self.stopflag = True
    
    def send(self, data):
        self.sock.sendto()
    
    def close(self):
        logger.debug("udp server closed")
        self.sock.close()
        
    def run(self):
        while not self.stopflag:
            rfds, _, efds = select.select([self.sock], [], [self.sock], 0.1)
            if len(efds) > 0:
                logger.error("remote client error")
                break
                
            if len(rfds) < 1:
                continue
            
            try:
                data, self.remoteAddr = self.sock.recvfrom(UdpServer.RECV_SIZE)
                logger.debug("recv data -> %s from -> %s:%d" % (data, self.remoteAddr[0], self.remoteAddr[1]))
                sigObject.emit(signals.SIG_DATA_RECVED, self._id, data)
            except Exception as e:
                logger.debug("recv exp. %s" % e.message)
                break
                
        self.close()