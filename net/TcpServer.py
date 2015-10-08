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
        
        self.tcpClients = {}
        self.stopflag = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, self.RCVBUF_SIZE)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, self.SNDBUF_SIZE)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.TCP_NODELAY, 1)
        #self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR , 1) # do not turn on SO_REUSEADDR
        self.sock.settimeout(0.1)
        
        self._id = id(self.sock)

    def getId(self):
        logger.debug("id: %d" % self._id)
        return self._id
        
    def getAddress(self):
        return "%s:%d" % (self.ip, self.port)
    
    def start_(self):
        try:
            self.sock.bind((self.ip, self.port))
            self.sock.listen(self.BACKLOG)
            logger.debug("TCP server bind on %s:%d success" % (self.ip, self.port))
        except socket.error:
            logger.error("TCP server bind on %s:%d error" % (self.ip, self.port))
            return False
        
        self.start()
        
        return True
        
    def stop(self):
        self.removeAllClients()
        self.stopflag = True
    
    def removeClientById(self, clientId):
        logger.debug("client id is --> %d" % clientId)
        tcpClient = self.tcpClients.get(clientId)
        if tcpClient is None:
            logger.error("fail to get tcp Client")
            return
        
        tcpClient.stop()
        del self.tcpClients[clientId]
        
    def removeAllClients(self):
        for _id, tcpClient in self.tcpClients.items():
            tcpClient.stop()
        
    def run(self):
        while not self.stopflag:
            #logger.debug("waiting for client...")
            try:
                client, addr = self.sock.accept()
                tcpClient = TcpClient(self._id, client, addr)
                sigObject.emit(signals.SIG_REMOTE_TCP_CLIENT_CONNECTED, tcpClient, self._id, tcpClient.getId(), addr[0], addr[1])
                logger.debug("new client %s:%d connected" % addr)
                tcpClient.start()
                self.tcpClients[tcpClient.getId()] = tcpClient
            
            except socket.timeout:
                pass
        
        logger.debug("server stopped")
                
if __name__ == "__main__":
    tcpServer = TcpServer(8083)
    tcpServer.run()