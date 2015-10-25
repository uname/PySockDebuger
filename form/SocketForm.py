#-*- coding: utf-8 -*-
import utils
import config
import signals
import binascii
from net import socktypes
from log import logger
from SigObject import sigObject
from ui.Ui_SocketForm import Ui_SocketForm
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QKeySequence
from PyQt4.QtCore import Qt

class SocketForm(QWidget):

    def __init__(self, sock, parent=None):
        QWidget.__init__(self, parent)
        self.sock = sock
        self.ui = Ui_SocketForm()
        self.setupUi()
        self.setupSignals()
    
    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.sendBtn.setShortcut(QKeySequence(Qt.Key_Return + Qt.CTRL))
        
        sockType = self.sock.getSockType()
        if sockType == socktypes.TCP_CLIENT_REMOTE:
            self.setupUi_connected()
        
        elif sockType == socktypes.TCP_CLIENT_LOCAL:
            self.ui.connectBtn.setText(config.TEXT_CONNECT)
            self.ui.statusLabel.setText(config.STATUS_NOT_CONNECTED)
    
    def setupUi_connected(self):
        self.ui.connectBtn.setText(config.TEXT_DISCONNECT)
        self.ui.statusLabel.setText(config.STATUS_CONNECTED)
        self.ui.recvTextBrowser.clear()
    
    def setupUi_disconnected(self):
        self.ui.connectBtn.setText(config.TEXT_CONNECT)
        self.ui.statusLabel.setText(config.STATUS_DISCONNECTED)
        
    def setupSignals(self):
        self.ui.sendBtn.clicked.connect(self.sendData)
        self.ui.cleanBtn.clicked.connect(self.ui.recvTextBrowser.clear)
        self.ui.resetBytesBtn.clicked.connect(self.resetBytes)
        self.ui.connectBtn.clicked.connect(self.onConnectBtnClicked)
        
        self.connect(sigObject, signals.SIG_REMOTE_CLOSED, self.onRemoteClosed)
    
    def onRemoteClosed(self):
        sockType = self.sock.getSockType()
        if sockType == socktypes.TCP_CLIENT_LOCAL:
            self.setupUi_disconnected()
            # TODO: remove socket, important!!!!
            
        elif sockType == socktypes.TCP_CLIENT_REMOTE:
            sigObject.emit(signals.SIG_REMOVE_SOCK_TAB, self.sock.getId())
        
    def onConnectBtnClicked(self):
        sockType = self.sock.getSockType()
        if self.sock.isConnected():
            if sockType == socktypes.TCP_CLIENT_LOCAL:
                self.sock.stop(onlyStopSocket=True)
                self.setupUi_disconnected()
                
            elif sockType == socktypes.TCP_CLIENT_REMOTE:
                sigObject.emit(signals.SIG_REMOVE_SOCK_TAB, self.sock.getId())
        
        else:
            if sockType == socktypes.TCP_CLIENT_LOCAL:
                if self.sock.connect():
                    self.sock.start()
                    self.setupUi_connected()
        
    def resetBytes(self):
        self.ui.rxLcdNumber.display(0)
        self.ui.txLcdNumber.display(0)
    
    def isHexMode(self):
        return self.ui.hexModeCkb.isChecked()
    
    def getHexText(self, data, tag=""):
        return "%s%s" % (tag, utils.dumpHex(data))
    
    def getAsciiText(self, data, tag=""):
        try:
            data = data.decode("gbk")
        except UnicodeDecodeError:
            logger.debug("data unable to decode to gbk")
            pass
            
        return "%s%s" % (tag, data)
        
    def addData(self, data, tag="", isend=False):
        text = ""
        if self.isHexMode():
            text = self.getHexText(data, tag)
        else:
            text = self.getAsciiText(data, tag)
            
        self.ui.recvTextBrowser.append(text)
        if isend:
            self.ui.txLcdNumber.display(len(data) + self.ui.txLcdNumber.intValue())
        else:
            self.ui.rxLcdNumber.display(len(data) + self.ui.rxLcdNumber.intValue())
        
    def sendData(self):
        if not self.sock.isConnected():
            return
            
        text = utils.qstr2gbk(self.ui.sendPlainTextEdit.toPlainText())
        if len(text) < 1:
            return False
            
        data = text
        if self.isHexMode():
            try:
                text = "".join(("".join(text.split("\n"))).split(" "))
                data = binascii.unhexlify(text)
            except TypeError:
                logger.error("Non-hexadecimal digit found")
                return False
        n = 0
        try:
            n = self.sock.sendall(data)
        except Exception as e:
            logger.error("send data error")
        
        if n:
            logger.debug("sent bytes: %d" % n)
            self.addData(data, config.SEND_TAG, True)
            self.ui.sendPlainTextEdit.clear()
      
        return n is None