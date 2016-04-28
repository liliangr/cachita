# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 12:53:05 2016

@author: Lily
"""

from FishEyeCamera import FishEyeCamera
from PTZCamera import PTZCamera
import logging


class CameraManager():
    
    def __init__(self, fe=True, ptz=True):
        self.feCam = None
        self.ptzCam = None
        if fe:
            self.feCam = self.createFishEyeCamera()
        if ptz:
            self.ptzCam = self.createPTZCamera()
        
        self.capture = None
    
    def createFishEyeCamera(self):
        logging.info('Se crea camara fe con parametros por defecto')
        #feHost = '10.9.6.48' #labo 127
        feHost = '10.2.1.48' #labo 126
        fePort = 80
        feUser = 'admin'
        fePwd = '12345'
        try:
            feCam = FishEyeCamera(feHost, fePort, feUser, fePwd)
            logging.info('Creacion de camara fe: OK')
        except:
            feCam = None
            logging.error('No se encontro una camara con estos parametros')
        return feCam
        
        
    def createPTZCamera(self):
        logging.info('Se crea camara ptz con parametros por defecto')
        ##ptzHost = "10.9.6.49" #labo 127
        ptzHost = '10.2.1.49' #labo 126
        ptzPort = 80
        ptzUser = 'admin'
        ptzPwd = '12345'
        try:
            ptzCam = PTZCamera(ptzHost, ptzPort, ptzUser, ptzPwd)
            logging.info('Creacion de camara ptz: OK')
        except:
            ptzCam = None
            logging.error('No se encontro una camara con estos parametros')
        return ptzCam

