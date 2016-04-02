# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:13:34 2016

@author: lilian
"""

from PyQt4 import QtGui, QtCore
import sys
from ui import principal
import cv2
from FishEyeCamera import FishEyeCamera
import logging

class WorkThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.tframe = []
    
    def __del__(self):
        self.wait()
    
    def load(self, camera):
        self.cam = camera
        self.start()
    
    def run(self):
        feUrl = self.cam.getStreamUri() 
        logging.info("Abriendo captura desde " + feUrl)
        self.cam.capture = cv2.VideoCapture(feUrl)
        while (self.cam.capture.isOpened()):
            ret, frame = self.cam.capture.read()

            if ret == True:
                self.emit(QtCore.SIGNAL('update(PyQt_PyObject)'), frame)

  

  
     

class PrincipalForm(QtGui.QMainWindow, principal.Ui_MainWindow):
    
    def __init__(self, parent=None):
        
        logging.info('Inicio de interfaz gráfica')
        super(PrincipalForm, self).__init__(parent)
        self.setupUi(self)
        
        logging.debug('Inicializacion del manager de camaras')
        self.feCam = self.createFishEyeCamera()
       
        ''' Accion de los botones '''
        self.btnCalibrate.clicked.connect(self.open_stream)
        
        self.thread = None
        self.customFrame = []
        
    
    def open_stream(self):
        if self.feCam != None:
            self.getFEStreaming()
        
 
                     
    def getFEStreaming(self):
        self.thread = WorkThread()
        self.connect(self.thread, QtCore.SIGNAL("update(PyQt_PyObject)"), self.showFEStreaming)
        self.thread.load(self.feCam)
       
                
            
        
    def showFEStreaming(self, frame):
        print len(frame)
        image = QtGui.QImage(frame.tostring(), frame.shape[1], 
                                 frame.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
     
        pixmap = QtGui.QPixmap.fromImage(image)
        pixmap = pixmap.scaled(self.feLabel.width(), self.feLabel.height(), 
                               QtCore.Qt.KeepAspectRatio)
                               
        painter = QtGui.QPainter()
        painter.begin(pixmap)
        painter.setPen(QtGui.QColor(255, 0, 0))
        painter.setFont(QtGui.QFont('Decorative', 11))
        painter.drawText(self.feLabel.width()/2, self.feLabel.height()/2, '+')
        painter.end()

        self.feLabel.setPixmap(pixmap)
        QtGui.QApplication.processEvents()
        
    def createFishEyeCamera(self):
        logging.info('Se crea camara fe con parametros por defecto')
        #feHost = '10.9.6.48' #labo 127
        feHost = '10.2.1.48' #labo 126
        fePort = 80
        feUser = 'admin'
        fePwd = '12345'
#        try:
        feCam = FishEyeCamera(feHost, fePort, feUser, fePwd)
        logging.info('Creacion de camara fe: OK')
#        except:
#            feCam = None
#            logging.error('No se encontro una camara con estos parametros')
        return feCam
        
def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Inicio')
    app = QtGui.QApplication(sys.argv)
    form = PrincipalForm()
    form.show()
    app.exec_()
    
if __name__ == '__main__':
    main()