#-*- coding: utf-8 -*-
from log import logger
from ServerManager import ServerManager
from net import socktypes

class TcpServerManager(ServerManager):
    
    def __init__(self):
        ServerManager.__init__(self)
    
    def create(self, ip, port):
        return self.create_(ip, port, socktypes.TCP_SERVER)
   
    def removeRemoteClient(self, remoteClientId, parentId):
        tcpServer = self.serverDict.get(parentId)
        if tcpServer:
            tcpServer.removeClientById(remoteClientId)
        else:
            logger.error("tcpServer is None")
        
tcpServerManager = TcpServerManager()