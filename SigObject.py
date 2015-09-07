#-*- coding: utf-8 -*-
from PyQt4.QtCore import QObject

class SigObject(QObject):
    
    def __init__(self):
        QObject.__init__(self)

sigObject = SigObject()