#-*- coding: utf-8 -*-
from SockClientManager import SockClientManager
from net import socktypes

class TcpClientManager(SockClientManager):
    
    def __init__(self):
        SockClientManager.__init__(self)
    
    def create(self, ip, port):
        return self.create_(ip, port, socktypes.TCP_CLIENT_LOCAL, connect=False)
        
tcpClientManager = TcpClientManager()