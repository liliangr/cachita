# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 13:04:06 2016

@author: lilian
"""

#from onvif import ONVIFCamera
from IPCamera import IPCamera
import urllib

class PTZCamera(IPCamera):

    def __init__(self, host, port ,user, passwd):
        IPCamera.__init__(self, host, port, user, passwd)
        self.ptzService = self.create_ptz_service()
        
        
    def getStreamUri(self):
#        return self.mediaService.GetStreamUri()[0]
        return 'rtsp://10.2.1.49:554/Streaming/Channels/1?transportmode=unicast&profile=Profile_1'
        
        
    def getStatus(self):
        media_profile = self.mediaService.GetProfiles()[0]
        
        request = self.ptzService.create_type('GetStatus')
        request.ProfileToken = media_profile._token
        
        ptzStatus = self.ptzService.GetStatus(request)
        pan = ptzStatus.Position.PanTilt._x
        tilt = ptzStatus.Position.PanTilt._y
        zoom = ptzStatus.Position.Zoom._x

        return (pan, tilt, zoom)
        
        
    def moveRight(self):
        status = self.getStatus()
        print "Movimiento hacia derecha desde " + str(status)
        actualPan = status[0]
        actualTilt = status[1]
        
        media_profile = self.mediaService.GetProfiles()[0]
        
        request = self.ptzService.create_type('AbsoluteMove')
        request.ProfileToken = media_profile._token
        pan = actualPan - float(2)/360
        if pan <= -1:
            pan = 1

        request.Position.PanTilt._x = pan
        request.Position.PanTilt._y = actualTilt
        absoluteMoveResponse = self.ptzService.AbsoluteMove(request)
        
    def moveLeft(self):
        status = self.getStatus()
        print "Movimiento hacia izquierda desde " + str(status)
        actualPan = status[0]
        actualTilt = status[1]
        
        media_profile = self.mediaService.GetProfiles()[0]
        
        request = self.ptzService.create_type('AbsoluteMove')
        request.ProfileToken = media_profile._token
        pan =  round(actualPan + float(2)/360 , 6)
        if pan >= 1:
            pan = -1
        print pan
        request.Position.PanTilt._x = pan
        request.Position.PanTilt._y = actualTilt
        absoluteMoveResponse = self.ptzService.AbsoluteMove(request)
        
        
    def moveUp(self):
        status = self.getStatus()
        print "Movimiento hacia arriba desde " + str(status)
        actualPan = status[0]
        actualTilt = status[1]
        
        media_profile = self.mediaService.GetProfiles()[0]
        
        request = self.ptzService.create_type('AbsoluteMove')
        request.ProfileToken = media_profile._token
        tilt =  round(actualTilt - float(2)/90, 6)
        pan = actualPan
        if tilt <= -1:
            tilt = -1
            pan = actualPan
        elif tilt >= 1:
                tilt = 1
                pan = actualPan + 180*float(2)/360
                
        request.Position.PanTilt._x = pan
        request.Position.PanTilt._y = tilt
        absoluteMoveResponse = self.ptzService.AbsoluteMove(request)
        
        
        
    def moveDown(self):
        status = self.getStatus()
        print "Movimiento hacia abajo desde " + str(status)
        actualPan = status[0]
        actualTilt = status[1]
        
        media_profile = self.mediaService.GetProfiles()[0]
        
        request = self.ptzService.create_type('AbsoluteMove')
        request.ProfileToken = media_profile._token
        tilt = round(actualTilt + float(2)/90, 6)
        pan = actualPan
        if tilt <= -1:
            tilt = -1
            pan = actualPan
        elif tilt >= 1:
                tilt = 1
                pan = actualPan + 180*float(2)/360

        request.Position.PanTilt._x = pan
        request.Position.PanTilt._y = tilt
        absoluteMoveResponse = self.ptzService.AbsoluteMove(request)
        
        
    def zoomIn(self):
        status = self.getStatus()
        print "Zoom in desde " + str(status)
        media_profile = self.mediaService.GetProfiles()[0]
        
        request = self.ptzService.create_type('AbsoluteMove')
        request.ProfileToken = media_profile._token
        
        if status[2] < 0.05:
            paso = 0.07
        else:
            paso = 0.035
            
        pZoom = status[2] + paso
        if pZoom > 1:
            pZoom = 1
        
        request.Position.Zoom._x = pZoom
        absoluteMoveResponse = self.ptzService.AbsoluteMove(request)
        
    def zoomOut(self):
        status = self.getStatus()
        print "Zoom out desde " + str(status)
        media_profile = self.mediaService.GetProfiles()[0]
        
        request = self.ptzService.create_type('AbsoluteMove')
        request.ProfileToken = media_profile._token
        
        pZoom = status[2] - 0.01    # Con este paso anda bien
        if pZoom < 0:
            pZoom = 0

        request.Position.Zoom._x = pZoom
        absoluteMoveResponse = self.ptzService.AbsoluteMove(request)
        
    def moveAbsolute(self, pan, tilt, zoom = 0):
        media_profile = self.mediaService.GetProfiles()[0]
        
        request = self.ptzService.create_type('AbsoluteMove')
        request.ProfileToken = media_profile._token
        
        pPan = round(1 - float(pan)/180, 6)
        pTilt = round(1 - float(tilt)/45, 6)
        pZoom = round(float(zoom/100), 6)
       
        request.Position.PanTilt._x = pPan
        request.Position.PanTilt._y = pTilt
        request.Position.Zoom._x = pZoom
        absoluteMoveResponse = self.ptzService.AbsoluteMove(request)
        
        
    def setHomePosition(self):
        media_profile = self.mediaService.GetProfiles()[0]
        
        request = self.ptzService.create_type('SetHomePosition')
        request.ProfileToken = media_profile._token
        self.ptzService.SetHomePosition(request)
        
    def gotoHomePosition(self):
        media_profile = self.mediaService.GetProfiles()[0]
        
        request = self.ptzService.create_type('GotoHomePosition')
        request.ProfileToken = media_profile._token
        self.ptzService.GotoHomePosition(request)
        
    def getSnapshotUri(self):
        media_profile = self.mediaService.GetProfiles()[0]
        
        request = self.mediaService.create_type('GetSnapshotUri')
        request.ProfileToken = media_profile._token
        response = self.mediaService.GetSnapshotUri(request)
        
        print response.Uri
        urllib.urlretrieve("http://10.2.1.49/onvif-http/snapshot", "local-filename.jpeg")
                    
   