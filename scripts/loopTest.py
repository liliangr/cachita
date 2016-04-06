# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 21:06:24 2016

@author: lilian
"""

from PyQt4 import QtGui, QtCore
import sys, time
import window
import logging

class WorkThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        
    
    def __del__(self):
        self.wait()
    
    def load(self, numero):
        self.i = numero
        self.start()
    
    
    def run(self):
        while 1:
            self.i += 1
            time.sleep(0.1)
            self.emit(QtCore.SIGNAL('update(PyQt_PyObject)'), self.i)

    def emitsignal(self):
        ret, frame = self.camera.capture.read()
        if ret:
            self.emit(QtCore.SIGNAL('update(PyQt_PyObject)'), frame)
            
            

class PrincipalForm(QtGui.QMainWindow, window.Ui_LaWindow):
    
    def __init__(self, parent=None):
        
        logging.info('Inicio de interfaz gráfica')
        super(PrincipalForm, self).__init__(parent)
        self.setupUi(self)
        self.feLabelSelected = False
        self.ptzLabelSelected = False
     
        ''' Accion de los botones '''
        self.btnCalibrate.clicked.connect(self.open_stream)
       
        self.threadPool = []


    def open_stream(self):
        ''' thread 1'''        
        self.threadPool.append(WorkThread())
        self.connect(self.threadPool[len(self.threadPool)-1], QtCore.SIGNAL("update(PyQt_PyObject)"), self.sumaUno)
        self.threadPool[len(self.threadPool)-1].load(1)
        
        ''' thread 2'''        
        self.threadPool.append(WorkThread())
        self.connect(self.threadPool[len(self.threadPool)-1], QtCore.SIGNAL("update(PyQt_PyObject)"), self.sumaCeroUno)
        self.threadPool[len(self.threadPool)-1].load(0.1)
        
     
    def sumaUno(self, numero):
        print  'sumaUno'
        self.feLabel.setText(str(numero))
        
        QtGui.QApplication.processEvents()

    
    def sumaCeroUno(self, numero):
        print  'sumaCeroUno'
        self.ptzLabel.setText(str(numero))
        QtGui.QApplication.processEvents()


    #override    
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Esta seguro que desea salir?", 
            QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            if self.cameraManager.ptzCam != None:
                if self.cameraManager.ptzCam.capture.isOpened == True:
                    self.cameraManager.ptzCam.capture.release()
            
            if self.cameraManager.feCam != None:
                if self.cameraManager.feCam.capture.isOpened()==True:
                    self.cameraManager.feCam.capture.release()
            event.accept()
        else:
            event.ignore()


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Inicio')
    app = QtGui.QApplication(sys.argv)
    form = PrincipalForm()
    form.show()
    app.exec_()
    
if __name__ == '__main__':
    main()