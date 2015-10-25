#-*- coding: utf-8 -*-
from log import logger
from TcpClient import TcpClient
from net import socktypes

class TcpClientManager(object):
    
    def __init__(self):
        self.clientDict = {}
    
    def create(self, ip, port):
        # Check ip and port
        tcpClient = TcpClient(0, None, (ip, port), socktypes.TCP_CLIENT_LOCAL)
        
        # 在创建时不连接
        # if not tcpClient.connect():
            # logger.error("fail to connect to server")
            # return None, -1, ""
        # tcpClient.start()
        # logger.debug("tcp client connect success")    
        
        _id = tcpClient.getId()
        self.clientDict[_id] = tcpClient
        logger.info("tcp client create ok")
        
        return tcpClient, _id, tcpClient.getAddress()
        
    def removeClient(self, _id):
        tcpClient = self.clientDict.get(_id)
        if not tcpClient:
            logger.error("tcpClient is None")
            return
            
        tcpClient.stop()
        logger.debug("remove Client ok")
            
    def removeAllTcpClient(self):
        for _id, tcpClient in self.clientDict.items():
            logger.debug("stopping %s ..." % _id)
            self.removeClient(_id)
        
tcpClientManager = TcpClientManager()