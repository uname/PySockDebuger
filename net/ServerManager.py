#-*- coding: utf-8 -*-
from log import logger
from TcpServer import TcpServer
from UdpServer import UdpServer
from net import socktypes

class ServerManager(object):
    
    def __init__(self):
        self.serverDict = {}
    
    def create_(self, ip, port, sockType):
        # Check ip and port
        server = None
        if sockType == socktypes.TCP_SERVER:
            server = TcpServer(port, ip)
        elif sockType == socktypes.UDP_SERVER:
            server = UdpServer(port, ip)
        else:
            logger.error("sockType not supported")
            return 0, ""
            
        _id = server.getId()
        if self.serverDict.has_key(_id):
            logger.error("server already exists")
            del server
            return 0, ""
            
        if not server.start_():
            return 0, ""
        
        self.serverDict[_id] = server
        logger.info("server create ok")
        
        return _id, server.getAddress()
        
    def removeServer(self, _id):
        server = self.serverDict.get(_id)
        if server is None:
            logger.error("no such tcp server")
            return False
            
        logger.debug("try to remove server %d(address=%s)" % (_id, server.getAddress()))
        server.stop()
        server.join()
        del self.serverDict[_id]
        logger.info("removed")
            
    def removeAllSevrer(self):
        for _id, server in self.serverDict.items():
            logger.debug("stopping %s ..." % _id)
            self.removeServer(_id)