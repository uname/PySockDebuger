#-*- coding: utf-8 -*-
from TcpClient import TcpClient
from SigObject import sigObject
from log import logger
import signals
import socket
import threading

class TcpServer(threading.Thread):
    
    RCVBUF_SIZE = 262144
    SNDBUF_SIZE = 262144
    BACKLOG     = 10
    
    def __init__(self, port, ip="0.0.0.0"):
        threading.Thread.__init__(self)
        self.ip, self.port = ip, port
        self.tcpClients = []
        self.stopflag = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, self.RCVBUF_SIZE)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, self.SNDBUF_SIZE)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.TCP_NODELAY, 1)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR , 1)
        self.sock.settimeout(1)

    def getAddress(self):
        return "%s:%d" % (self.ip, self.port)
    
    def start_(self):
        try:
            self.sock.bind((self.ip, self.port))
            self.sock.listen(self.BACKLOG)
            logger.debug("TCP server bind on %s:%d success" % (self.ip, self.port))
        except sock.error:
            logger.error("TCP server bind on %s:%d error" % (self.ip, self.port))
            return
        
        self.start()
        
        return True
        
    def stop(self):
        self.stopflag = True
        
    def run(self):
        while not self.stopflag:
            logger.debug("waiting for client...")
            try:
                client, addr = self.sock.accept()
                logger.debug("new client %s:%d connected" % addr)
                tcpClient = TcpClient(client, addr)
                tcpClient.start()
                self.tcpClients.append(tcpClient)
            
            except socket.timeout:
                pass
        
        logger.debug("server stopped")
                
if __name__ == "__main__":
    tcpServer = TcpServer(8083)
    tcpServer.run()