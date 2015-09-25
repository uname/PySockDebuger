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
        
    def addData(self, data, tag=""):
        self.ui.recvTextBrowser.append(u"%s%s" % (tag, unicode(data, "gbk")))
        
    def sendData(self):
        data = utils.qstr2str(self.ui.sendPlainTextEdit.toPlainText())
        self.addData(data, config.SEND_TAG)
        sigObject.emit(signals.SIG_SEND_DATA, data)