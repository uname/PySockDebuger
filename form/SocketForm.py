#-*- coding: utf-8 -*-
import utils
import config
import signals
from log import logger
from SigObject import sigObject
from ui.Ui_SocketForm import Ui_SocketForm
from PyQt4.QtGui import QWidget

class SocketForm(QWidget):

    def __init__(self, sock, parent=None):
        QWidget.__init__(self, parent)
        self.sock = sock
        self.ui = Ui_SocketForm()
        self.ui.setupUi(self)
    
        self.setupSignals()
        
    def setupSignals(self):
        self.ui.sendBtn.clicked.connect(self.sendData)
        self.ui.cleanBtn.clicked.connect(self.ui.recvTextBrowser.clear)
        self.ui.resetBytesBtn.clicked.connect(self.resetBytes)
    
    def resetBytes(self):
        self.ui.rxLcdNumber.display(0)
        self.ui.txLcdNumber.display(0)
        
    def addData(self, data, tag="", isend=False):
        try:
            data = data.decode("gbk")
        except UnicodeDecodeError:
            logger.debug("data unable to decode to gbk")
            pass
        text = "%s%s" % (tag, data)
        self.ui.recvTextBrowser.append(text)
        if isend:
            self.ui.txLcdNumber.display(len(data) + self.ui.txLcdNumber.intValue())
        else:
            self.ui.rxLcdNumber.display(len(data) + self.ui.rxLcdNumber.intValue())
        
    def sendData(self):
        data = utils.qstr2gbk(self.ui.sendPlainTextEdit.toPlainText())
        self.addData(data, config.SEND_TAG, True)
        n = 0
        try:
            n = self.sock.sendall(data)
        except Exception as e:
            logger.error("send data error")
        
        if n:
            logger.debug("sent bytes: %d" % n)
      
        return n is None