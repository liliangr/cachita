# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:54:40 2015

@author: Lily
"""
'''
Para instalar requests:
pip install requests
'''
import requests
import time
from xml.etree import ElementTree
from requests.auth import HTTPBasicAuth

class Camera():
    
    def __init__(self):
        #self.IP = "10.9.6.49" labo 127
        self.IP = "10.2.1.49" #labo 126
        self.auth = HTTPBasicAuth('admin', '12345')
    
    def status(self):
        response = self.get('status')
        # Procesa resultado xml
        tree = ElementTree.fromstring(response.content)
        elevation = tree[0][0].text
        azimuth = tree[0][1].text
        absoluteZoom = tree[0][2].text
        print 'elevation: ' + elevation + ' azimuth: ' + azimuth + ' zoom: ' + absoluteZoom

        #velocidad
    def continuous(self, pan, tilt, zoom):
        """ Se mueve en la direccion que se proporcione en los parámetros dte 5 segundos  """
        # Arma xml para pasar como parametro
        ptzdata = ElementTree.Element('PTZData')
        childPan = ElementTree.SubElement(ptzdata, 'pan')
        childPan.text = str(pan)
        childTilt = ElementTree.SubElement(ptzdata, 'tilt')
        childTilt.text = str(tilt)
        childZoom = ElementTree.SubElement(ptzdata, 'zoom')
        childZoom.text = str(zoom)
        payload = ElementTree.tostring(ptzdata, 'utf-8')

        # Ejecuta comando 
        response = self.put('continuous', payload)
        
        # Procesa resultado xml
        tree = ElementTree.fromstring(response.content)
        statusCode = tree[1].text
#        print statusCode
        
        if (statusCode == "1"):
            time.sleep(5)
            
            childPan.text = "0"
            childTilt.text = "0"
            childZoom.text = "0"
            payload = ElementTree.tostring(ptzdata, 'utf-8')
            response = self.put('continuous', payload)


    def absolute(self, elevation, azimuth, absoluteZoom):
        """ Se mueve a la posicion que se especifique en los parametros  """
        """ Los parametros tienen un decimal de precision  """
        """ Elevation -900 a 2700  """
        """ Azimuth      0 a 3600  """
        """ Zoom         0 a 300  """
        # Arma xml para pasar como parametro
        ptzData = ElementTree.Element('PTZData')
        absoluteHigh = ElementTree.SubElement(ptzData, 'AbsoluteHigh')
        childElevation = ElementTree.SubElement(absoluteHigh, 'elevation')
        childElevation.text = str(elevation)
        childAzimuth = ElementTree.SubElement(absoluteHigh, 'azimuth')
        childAzimuth.text = str(azimuth)
        childZoom = ElementTree.SubElement(absoluteHigh, 'absoluteZoom')
        childZoom.text = str(absoluteZoom)
        payload = ElementTree.tostring(ptzData, 'utf-8')

        # Ejecuta comando 
        response = self.put('absolute', payload)
        
        # Procesa resultado xml
        tree = ElementTree.fromstring(response.content)
        statusCode = tree[1].text
        statusText = tree[2].text
        print 'statusCode: ' + statusCode + ' statusText: ' + statusText
        
        

    def get(self, command):
        query = 'http://{}/PTZCtrl/channels/1/{}'.format(self.IP, command)
        return requests.get(query, auth=self.auth)
    
    def put(self, command, payload):
        query = 'http://{}/PTZCtrl/channels/1/{}'.format(self.IP, command)
        return requests.put(query, auth=self.auth, data=payload)
    
