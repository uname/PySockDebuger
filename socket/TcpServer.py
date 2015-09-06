#-*- coding: utf-8 -*-
from TcpClient import TcpClient
from log import logger
import socket

class TcpServer(object):
    
    RCVBUF_SIZE = 262144
    SNDBUF_SIZE = 262144
    BACKLOG     = 10
    
    def __init__(self, port, ip="0.0.0.0"):
        self.ip, self.port = ip, port
        self.tcpClients = []
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, self.RCVBUF_SIZE)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, self.SNDBUF_SIZE)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.TCP_NODELAY, 1)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR , 1)

        
    def run(self):
        try:
            self.sock.bind((self.ip, self.port))
            logger.debug("TCP server bind on %s:%d success" % (self.ip, self.port))
        except sock.error:
            logger.error("TCP server bind on %s:%d error" % (self.ip, self.port))
            return
            
        self.sock.listen(self.BACKLOG)
        while 1:
            logger.debug("waiting for client...")
            client, addr = self.sock.accept()
            logger.debug("new client %s:%d connected" % addr)
            tcpClient = TcpClient(client, addr)
            tcpClient.start()
            self.tcpClients.append(tcpClient)
        
if __name__ == "__main__":
    tcpServer = TcpServer(8083)
    tcpServer.run()