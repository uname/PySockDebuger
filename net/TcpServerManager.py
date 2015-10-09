#-*- coding: utf-8 -*-
from log import logger
from TcpServer import TcpServer

class TcpServerManager(object):
    
    def __init__(self):
        self.serverDict = {}
    
    def create(self, ip, port):
        # Check ip and port
        tcpServer = TcpServer(port, ip)
        _id = tcpServer.getId()
        if self.serverDict.has_key(_id):
            logger.error("server already exists")
            del tcpServer
            return 0, ""
            
        if not tcpServer.start_():
            return 0, ""
        
        self.serverDict[_id] = tcpServer
        logger.info("server create ok")
        
        return _id, tcpServer.getAddress()
        
    def removeServer(self, _id):
        tcpServer = self.serverDict.get(_id)
        if tcpServer is None:
            logger.error("no such tcp server")
            return False
            
        logger.debug("try to remove server %d(address=%s)" % (_id, tcpServer.getAddress()))
        tcpServer.stop()
        tcpServer.join()
        del self.serverDict[_id]
        logger.info("removed")
   
    def removeRemoteClient(self, remoteClientId, parentId):
        tcpServer = self.serverDict.get(parentId)
        if tcpServer:
            tcpServer.removeClientById(remoteClientId)
        else:
            logger.error("tcpServer is None")
            
    def removeAllTcpSevrer(self):
        for _id, tcpServer in self.serverDict.items():
            logger.debug("stopping %s ..." % _id)
            self.removeServer(_id)
        
tcpServerManager = TcpServerManager()