# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
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

class Ui_LaWindow(object):
    def setupUi(self, LaWindow):
        LaWindow.setObjectName(_fromUtf8("LaWindow"))
        LaWindow.resize(840, 570)
        self.centralwidget = QtGui.QWidget(LaWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnCalibrate = QtGui.QPushButton(self.centralwidget)
        self.btnCalibrate.setGeometry(QtCore.QRect(20, 430, 158, 27))
        self.btnCalibrate.setObjectName(_fromUtf8("btnCalibrate"))
        self.feFrame = QtGui.QFrame(self.centralwidget)
        self.feFrame.setGeometry(QtCore.QRect(20, 10, 390, 390))
        self.feFrame.setFrameShape(QtGui.QFrame.Panel)
        self.feFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.feFrame.setLineWidth(3)
        self.feFrame.setMidLineWidth(0)
        self.feFrame.setObjectName(_fromUtf8("feFrame"))
        self.feLabel = QtGui.QLabel(self.feFrame)
        self.feLabel.setGeometry(QtCore.QRect(10, 10, 370, 370))
        self.feLabel.setText(_fromUtf8(""))
        self.feLabel.setWordWrap(False)
        self.feLabel.setIndent(-1)
        self.feLabel.setObjectName(_fromUtf8("feLabel"))
        self.felistWidget = QtGui.QListWidget(self.feFrame)
        self.felistWidget.setGeometry(QtCore.QRect(10, 10, 251, 371))
        self.felistWidget.setObjectName(_fromUtf8("felistWidget"))
        self.ptzFrame = QtGui.QFrame(self.centralwidget)
        self.ptzFrame.setGeometry(QtCore.QRect(420, 10, 390, 390))
        self.ptzFrame.setFrameShape(QtGui.QFrame.Panel)
        self.ptzFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.ptzFrame.setLineWidth(3)
        self.ptzFrame.setMidLineWidth(0)
        self.ptzFrame.setObjectName(_fromUtf8("ptzFrame"))
        self.ptzLabel = QtGui.QLabel(self.ptzFrame)
        self.ptzLabel.setGeometry(QtCore.QRect(10, 10, 370, 370))
        self.ptzLabel.setText(_fromUtf8(""))
        self.ptzLabel.setWordWrap(False)
        self.ptzLabel.setIndent(-1)
        self.ptzLabel.setObjectName(_fromUtf8("ptzLabel"))
        self.ptzlistWidget = QtGui.QListWidget(self.ptzFrame)
        self.ptzlistWidget.setGeometry(QtCore.QRect(10, 0, 261, 381))
        self.ptzlistWidget.setObjectName(_fromUtf8("ptzlistWidget"))
        LaWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(LaWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        LaWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(LaWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        LaWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LaWindow)
        QtCore.QMetaObject.connectSlotsByName(LaWindow)

    def retranslateUi(self, LaWindow):
        LaWindow.setWindowTitle(_translate("LaWindow", "LaWindow", None))
        self.btnCalibrate.setText(_translate("LaWindow", "Testear", None))

