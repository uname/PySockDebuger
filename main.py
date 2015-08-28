#-*- coding: utf-8 -*-
import sys
sys.dont_write_bytecode = 1
from PyQt4 import QtGui
from MainWindow import MainWindow


__author__  = "Uname"
__version__ = "0.1"
__email__   = "hqwemail@163.com"

def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()