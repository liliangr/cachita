# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:52:01 2016

@author: lilian
"""
from PyQt4 import QtCore
import time
import logging
import cv2

class CaptureThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.terminated = False
        
    
    def __del__(self):
        ''' lo manda al garbage collector cdo no corre mas'''
        self.wait()
        
    def stop(self):
        self.terminated = True
    
    def load(self, ipcamera):
        self.camera = ipcamera
        self.start()
    
    
    def run(self):
#        print int(QtCore.QThread.currentThreadId())
        url = self.camera.getStreamUri()
        logging.info("Abriendo captura desde " + url)
        self.camera.capture = cv2.VideoCapture(url)
        while (self.camera.capture.isOpened() and not(self.terminated)):
            time.sleep(0.01)
            ret, frame = self.camera.capture.read()
#            '''Current position of the video file in milliseconds or video capture timestamp.'''
#            print str(int(QtCore.QThread.currentThreadId())) +' '+ str(self.camera.capture.get(cv2.cv.CV_CAP_PROP_POS_MSEC))
#            '''0-based index of the frame to be decoded/captured next.'''
#            print self.camera.capture.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) 


            if ret == True:
                self.emit(QtCore.SIGNAL('update(PyQt_PyObject)'), frame)
                
            else:
                print('No se obtuvo frame, sale de while')
                break
            
        self.camera.capture.release()
        cv2.destroyAllWindows()

     
