# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:49:21 2015

@author: Lily
"""

from onvif import ONVIFCamera
#import time

mycam = ONVIFCamera('10.2.1.49', 80, 'admin', '12345', 'C:\onvif\wsdl\\')

#mycam = ONVIFCamera('10.2.1.49', 80, 'admin', '12345', 'C:\onvif\wsdl\\')
# Create media service object

media = mycam.create_media_service()
# Create ptz service object
ptz = mycam.create_ptz_service()

# Get target profile
media_profile = media.GetProfiles()[0];

#media = mycam.create_media_service()
#device = mycam.create_devicemgmt_service()


# Get target profile

#print mycam.devicemgmt.GetServices({'IncludeCapability': False })
#print media.GetStreamUri()

# Get PTZ configuration options for getting continuous move range
request = ptz.create_type('GetConfigurationOptions')
request.ConfigurationToken = media_profile.PTZConfiguration._token
ptz_configuration_options = ptz.GetConfigurationOptions(request)

request = ptz.create_type('ContinuousMove')
request.ProfileToken = media_profile._token

ptz.Stop({'ProfileToken': media_profile._token})


# Get range of pan and tilt
# NOTE: X and Y are velocity vector
global XMAX, XMIN, YMAX, YMIN
XMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Max
XMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Min
YMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Max
YMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Min


request.Velocity.PanTilt._x = 0.6
request.Velocity.PanTilt._y = 0
ptz.ContinuousMove(request)
# Wait a certain time
time.sleep(3)
# Stop continuous move
ptz.Stop({'ProfileToken': request.ProfileToken})