#-*- coding: utf-8 -*-
from PyQt4 import QtGui
import config

class CreateDialog(QtGui.QDialog):
    
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setWindowIcon(QtGui.QIcon(config.LOGO_ICON))