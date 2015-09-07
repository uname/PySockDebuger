#-*- coding: utf-8 -*-
from log import logger
from TcpServer import TcpServer

class TcpServerManager(object):
    
    def __init__(self):
        self.serverDict = {}
    
    def create(self, port, ip="0.0.0.0"):
        # Check ip and port
        tcpServer = TcpServer(port, ip)
        address = tcpServer.getAddress()
        if self.serverDict.has_key(address):
            logger.error("server already exists")
            del tcpServer
            return
            
        if not tcpServer.start_():
            return
            
        self.serverDict[address] = tcpServer
        logger.info("server create ok")
        
        return address
        
    def remove(self, address):
        if not isinstanceof(address, basestring):
            return False
            
        tcpServer = self.serverDict.get(address)
        if tcpServer is None:
            logger.error("no such tcp server")
            return False
            
        logger.debug("try to remove server %s" % address)
        tcpServer.stop()
        tcpServer.join()
        del self.serverDict[address]
        
tcpServerManager = TcpServerManager()