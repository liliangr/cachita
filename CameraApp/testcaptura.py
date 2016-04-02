# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 19:27:25 2016

@author: Lily
"""
from numpy import *
from matplotlib import *
from onvif import ONVIFCamera
import cv2


mycam = ONVIFCamera('10.2.1.49', 80, 'admin', '12345')
# Create media service object
media_service = mycam.create_media_service()

url =  media_service.GetStreamUri()[0]
print url
#url = 'rtsp://10.2.1.49:554/Streaming/Channels/1?transportmode=unicast&profile=Profile_1'

cap = cv2.VideoCapture(url)


while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow('Captura', frame)
        cv2.waitKey(1)
    else:
        break

if cap.isOpened()==False:
    disp('No se pudo abrir la interfaz!')


cap.release()
cv2.destroyAllWindows()
