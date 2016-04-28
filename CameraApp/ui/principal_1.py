# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(840, 580)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.feFrame = QtGui.QFrame(self.centralwidget)
        self.feFrame.setGeometry(QtCore.QRect(20, 10, 390, 390))
        self.feFrame.setFrameShape(QtGui.QFrame.Panel)
        self.feFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.feFrame.setLineWidth(0)
        self.feFrame.setMidLineWidth(0)
        self.feFrame.setObjectName(_fromUtf8("feFrame"))

        self.feLabel = QtGui.QLabel(self.feFrame)
        self.feLabel.setGeometry(QtCore.QRect(10, 10, 370, 370))
        self.feLabel.setText(_fromUtf8(""))
        self.feLabel.setObjectName(_fromUtf8("feLabel"))
        
        self.ptzFrame = QtGui.QFrame(self.centralwidget)
        self.ptzFrame.setGeometry(QtCore.QRect(420, 10, 390, 390))
        self.ptzFrame.setFrameShape(QtGui.QFrame.Panel)
        self.ptzFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.ptzFrame.setLineWidth(0)
        self.ptzFrame.setMidLineWidth(0)
        self.ptzFrame.setObjectName(_fromUtf8("ptzFrame"))

        self.ptzLabel = QtGui.QLabel(self.ptzFrame)
        self.ptzLabel.setGeometry(QtCore.QRect(10, 10, 370, 370))
        self.ptzLabel.setText(_fromUtf8(""))
        self.ptzLabel.setObjectName(_fromUtf8("ptzLabel"))
        
        self.btnCalibrate = QtGui.QPushButton(self.centralwidget)
        self.btnCalibrate.setGeometry(QtCore.QRect(20, 400, 180, 27))
        self.btnCalibrate.setObjectName(_fromUtf8("btnCalibrate"))
        self.btnCalibrate.setText("Calibrar")
        
        self.btn_Left = QtGui.QPushButton(self.centralwidget)
        self.btn_Left.setGeometry(QtCore.QRect(500, 450, 98, 27))
        self.btn_Left.setObjectName(_fromUtf8("btn_Left"))
        
        self.btn_Right = QtGui.QPushButton(self.centralwidget)
        self.btn_Right.setGeometry(QtCore.QRect(620, 450, 98, 27))
        self.btn_Right.setObjectName(_fromUtf8("btn_Right"))
        
        self.btn_Down = QtGui.QPushButton(self.centralwidget)
        self.btn_Down.setGeometry(QtCore.QRect(570, 490, 98, 27))
        self.btn_Down.setObjectName(_fromUtf8("btn_Down"))
        
        self.btn_Up = QtGui.QPushButton(self.centralwidget)
        self.btn_Up.setGeometry(QtCore.QRect(560, 410, 98, 27))
        self.btn_Up.setObjectName(_fromUtf8("btn_Up"))
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 773, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
 

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Principal", None))
        self.btnCalibrate.setText(_translate("MainWindow", "Buscar cámaras", None))
        self.btn_Left.setText(_translate("MainWindow", "Izquierda", None))
        self.btn_Right.setText(_translate("MainWindow", "Derecha", None))
        self.btn_Down.setText(_translate("MainWindow", "Abajo", None))
        self.btn_Up.setText(_translate("MainWindow", "Arriba", None))

