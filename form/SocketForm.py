#-*- coding: utf-8 -*-
import utils
import config
import signals
from SigObject import sigObject
from ui.Ui_SocketForm import Ui_SocketForm
from PyQt4.QtGui import QWidget

class SocketForm(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
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
        self.ui.recvTextBrowser.append(u"%s%s" % (tag, unicode(data, "gbk")))
        if isend:
            self.ui.txLcdNumber.display(len(data) + self.ui.txLcdNumber.intValue())
        else:
            self.ui.rxLcdNumber.display(len(data) + self.ui.rxLcdNumber.intValue())
        
    def sendData(self):
        data = utils.qstr2gbk(self.ui.sendPlainTextEdit.toPlainText())
        self.addData(data, config.SEND_TAG, True)
        sigObject.emit(signals.SIG_SEND_DATA, data)