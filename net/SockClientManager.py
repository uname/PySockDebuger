#-*- coding: utf-8 -*-
from log import logger
from UdpClient import UdpClient
from TcpClient import TcpClient
from net import socktypes

class SockClientManager(object):
    
    def __init__(self):
        self.clientDict = {}
        self.sockClientClsDict = { socktypes.UDP_CLIENT_LOCAL: UdpClient,
                                   socktypes.TCP_CLIENT_LOCAL: TcpClient}
    
    def create_(self, ip, port, sockType, connect=True):
        sockCls = self.sockClientClsDict.get(sockType)
        if not sockCls:
            return None, -1, ""
            
        sockClient = sockCls(0, None, (ip, port), sockType)
        
        if connect:
            if not sockClient.connect():
                logger.error("fail to connect to server")
                return None, -1, ""
            sockClient.start()
            logger.debug("sock client connect success")  
        
        _id = sockClient.getId()
        self.clientDict[_id] = sockClient
        logger.info("sock client create ok")
        
        return sockClient, _id, sockClient.getAddress()
        
    def removeClient(self, _id):
        logger.debug("**** remove client: %d" % _id)
        sockClient = self.clientDict.get(_id)
        if not sockClient:
            logger.error("sockClient is None")
            return
            
        sockClient.stop()
        del self.clientDict[_id]
        logger.debug("remove Client ok")
            
    def removeAllClient(self):
        for _id, sockClient in self.clientDict.items():
            logger.debug("stopping %s ..." % _id)
            self.removeClient(_id)
