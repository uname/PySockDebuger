#-*- coding: utf-8 -*-
from ServerManager import ServerManager
from net import socktypes

class UdpServerManager(ServerManager):
    
    def __init__(self):
        ServerManager.__init__(self)
    
    def create(self, ip, port):
        _id, address = self.create_(ip, port, socktypes.UDP_SERVER)
        return self.serverDict.get(_id), _id, address
        
udpServerManager = UdpServerManager()