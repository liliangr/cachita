# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 11:48:30 2016

@author: Lily
"""
from IPCamera import IPCamera


class FishEyeCamera(IPCamera):
    
     def __init__(self, host, port ,user, passwd):
        IPCamera.__init__(self, host, port, user, passwd)
        

        
     def getStreamUri(self):
#        media_service = self.create_media_service()
#        return media_service.GetStreamUri()
        return 'rtsp://10.2.1.48/live.sdp'
        
  
        
#     def test(self):
         
#        media_service = self.create_media_service()
#        print media_service.GetStreamUri()
#         profiles = self.devicemgmt.GetProfiles()
#         print str(profiles)
         
#         
#         resp1 = self.devicemgmt.GetCapabilities()
#         print 'My camera`s hostname: ' + str(resp1)
##         print 'My camera`s hostname: ' + str(resp1.Media.XAddr)
#         
#         resp3 = self.devicemgmt.GetServices({'IncludeCapability': True})
#         print 'My camera`s hostname: ' + str(resp3)
         
#         
#         resp2 = self.devicemgmt.GetNetworkProtocols()
#         print 'My camera`s hostname: ' + str(resp2)
#         resp = self.devicemgmt.GetHostname()
#         print 'My camera`s hostname: ' + str(resp.Name)
#         
#         dt = self.devicemgmt.GetSystemDateAndTime()
#         tz = dt.TimeZone
#         year = dt.UTCDateTime.Date.Year
#         hour = dt.UTCDateTime.Time.Hour
#         print str(tz) + ' ' + str(year) + ' ' + str(hour)
#
#         di = self.devicemgmt.GetDeviceInformation()
#         print 'Device Information: ' + str(di)
#         
#         su = self.devicemgmt.GetWsdlUrl()
#         print 'Uris: ' + str(su)
         