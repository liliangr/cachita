# -*- coding: utf-8 -*-
import cv2     
import numpy as np
import datetime
import matplotlib.pyplot as plt

#ptzUrl='rtsp://10.2.1.49:554/Streaming/Channels/1?transportmode=unicast&profile=Profile_1'
#url = ptzUrl

feUrl = 'rtsp://10.2.1.48/live.sdp'
url = feUrl
tIni = datetime.datetime.now()
tFin = tIni + datetime.timedelta(minutes=1)

capture = cv2.VideoCapture(url)


out = cv2.VideoWriter("tester.avi", cv2.cv.CV_FOURCC('M','J','P','G'), 10,(1280, 1280),True) 

i = 0
j = 0

timeDone = False
fps= []
secs = []
now1 = datetime.datetime.now()
#out = cv2.VideoWriter("video1.avi", fourcc, 25, (800, 600))
frameant = []
while not(timeDone):
    try:
        timeant = datetime.datetime.now()
        frameant = frame.copy()
    except:
        pass
    
    ret, frame = capture.read()
    
    if ret == True:
        j += 1
        if np.sum(frame - frameant) == 0:
            i += 1
#        cv2.imshow("test", frame)
#        out.write(frame)
        cv2.waitKey(1)
        
        timeDone = (datetime.datetime.now() >= tFin)
        fps.append(1/(datetime.datetime.now()-timeant).total_seconds())
        delta = (datetime.datetime.now() - now1).total_seconds()
        secs.append(delta)
    else:
        break
print i 
print fps


plt.plot(secs,fps)

out.release()
capture.release()
cv2.destroyAllWindows()
    
if capture.isOpened()==False:
    print('No se pudo abrir la interfaz!')


