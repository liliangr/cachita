# -*- coding: utf-8 -*-
"""
Created on Sun Jan 04 03:09:52 2015

@author: LaLily
"""

# Importo librerias
from numpy import *
import scipy.io
import time
from matplotlib import *
import urllib2  # Libreria para captura online
import cv2      # Libreria de OpenCV  
import timeit   # Libreria de performance  


p = urllib2.HTTPPasswordMgrWithDefaultRealm()

#p.add_password(None, 'http://192.169.1.101:81/videostream.cgi', 'admin', '')

p.add_password(None, 'http://192.169.1.101:81/camera_control.cgi', 'admin', '')

handler = urllib2.HTTPBasicAuthHandler(p)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)

#stream = urllib2.urlopen('http://192.169.1.101:81/videostream.cgi')
# ZOOM IN: 16
# ZOOM OUT:18
#for i in range(1,120):
        
stream = urllib2.urlopen('http://192.169.1.101:81/camera_control.cgi?param=1&value=-16')
#    time.sleep(0.1)
#    stream = urllib2.urlopen('http://192.169.1.101:81/decoder_control.cgi?command=7')
#    time.sleep(0.1)
#    stream = urllib2.urlopen('http://192.169.1.101:81/decoder_control.cgi?command=4')
#    time.sleep(0.1)
#    stream = urllib2.urlopen('http://192.169.1.101:81/decoder_control.cgi?command=5')    
#   
Output = stream.read(1024).strip()

#
#
#
#bytes=''
#k = 0
#
#while True:
#       
#    # Descargo la imagen
#    bytes+=stream.read(1024)
#    a = bytes.find('\xff\xd8')
#    b = bytes.find('\xff\xd9')
#    
#    # Si logré una imágen
#    if a!=-1 and b!=-1:
#    
#        jpg = bytes[a:b+2]
#        bytes= bytes[b+2:]
#        
#        im_frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
#        
#        # Incremento numero de iteracion
#        k += 1
#        
#        # Grafico lo deseado
#        figura = cv2.imshow('Autopista',im_frame)
#        
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
#
### Libero la interfaz y cierro ventanas
##cv2.destroyAllWindows()