# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\nanowire\nanowire.ui'
#
# Created by: PyQt5 UI code generator 5.6
#  
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
#from PyQt5.QtCore import QIODevice, QTextStream
from PyQt5.QtWidgets import (QDialog, QFileDialog,
         QMessageBox)
import examplexlsx as xls
import nanowire_multi as multi

class Ui_Dialog(QDialog):
    fileName = ''
    def __init__(self):
        super(Ui_Dialog,self).__init__()
        self.setupUi(self)
        

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(470, 308)
        Dialog.setSizeGripEnabled(True)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(50, 20, 301, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_open=QtWidgets.QPushButton(Dialog)
        self.pushButton_open.setGeometry(QtCore.QRect(350, 20, 81, 31))
        self.pushButton_open.setObjectName("pushButton_open")
        self.pushButton_Run = QtWidgets.QPushButton(Dialog)
        self.pushButton_Run.setGeometry(QtCore.QRect(170, 90, 75, 23))
        self.pushButton_Run.setObjectName("pushButton_Run")
        self.pushButton_exit = QtWidgets.QPushButton(Dialog)
        self.pushButton_exit.setGeometry(QtCore.QRect(260, 90, 75, 23))
        self.pushButton_exit.setObjectName("pushButton_exit")
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_open.clicked.connect(self.openf)
        self.pushButton_Run.clicked.connect(self.Run)
        self.pushButton_exit.clicked.connect(self.exitc)
        
        self.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SNSPD Device Plot"))
        self.pushButton_open.setText(_translate("Dialog", "open file"))
        self.pushButton_Run.setText(_translate("Dialog", "Run"))
        self.pushButton_exit.setText(_translate("Dialog", "exit"))
        
    def openf(self):
        self.fileName, _ = QFileDialog.getOpenFileName(self, "Open xlsx file",
                '', "excel file (*.xlsx);")
        self.textBrowser.setText(self.fileName)
        self.textBrowser.show()

  
        if not self.fileName:
            return

        
    def Run(self):
        self.fileName.replace('\/','\\')
        if self.fileName == '':
            QMessageBox.information(self, "Unable to open file",
                    "There was an error opening \"%s\"" % self.fileName)
            return
#        xls.plot(self.fileName)  #调用普通纳米线的画法
        multi.plot(self.fileName)
        QMessageBox.information(self, "successful ","successful plot gdsfile in current path")
            
    def exitc(self):
        self.close()
        
        
        

        
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Dialog()      
    sys.exit(app.exec_()) 
