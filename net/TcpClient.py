#-*- coding: utf-8 -*-
from log import logger
from SigObject import sigObject
import signals
import socket
import select
import threading

class TcpClient(threading.Thread):
    
    RECV_SIZE = 1024
    
    def __init__(self, parentId, sock, addr):
        threading.Thread.__init__(self)
        self.stopflag = False
        self.parentId = parentId
        self._id = id(self)
        self.sock = sock
        self.sock.setblocking(0)
        self.ip, self.port = addr[0:]
    
    def sendall(self, data):
        if data is None:
            return False
        
        return self.sock.sendall(data) is None
    
    def getId(self):
        return self._id
        
    def close(self):
        if self.sock is None:
            return
        
        self.sock.close()
    
    def stop(self):
        self.stopflag = True
        
    def run(self):
        if self.sock is None:
            return
            
        while not self.stopflag:
            rfds, _, efds = select.select([self.sock], [], [self.sock], 0.5)
            if len(efds) > 0:
                logger.error("remote client error")
                break
                
            if len(rfds) < 1:
                continue
                
            data = self.sock.recv(self.RECV_SIZE)
            if data == "":
                logger.error("socket closed")
                break
            
            logger.debug("data from %s:%d -> %s" % (self.ip, self.port, data))
        
        self.sock.close()
        logger.debug("tcp client stopped")
        sigObject.emit(signals.SIG_REMOTE_CLOSED, self.getId(), self.parentId)