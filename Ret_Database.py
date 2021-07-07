from retDataBase import *
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class retDataBase(Ui_MainWindow):
    def __init__ (self):
        self.childWindow=QtGui.QMainWindow()
        print('sangeeta')
        super().setupUi(self.childWindow)
if __name__=='__main__':
    app= QtGui.QApplication([])
    retDataBase()
    app.exec_()