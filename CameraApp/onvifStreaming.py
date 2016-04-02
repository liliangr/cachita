# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 20:34:19 2016

@author: Lily
"""



from onvif import ONVIFCamera


#mycam = ONVIFCamera('10.9.6.49', 80, 'admin', '12345', 'C:\onvif\wsdl\\')

mycam = ONVIFCamera('10.2.1.49', 80, 'admin', '12345', 'C:\onvif\wsdl\\')
# Create media service object
media_service = mycam.create_media_service()
profiles = media_service.GetProfiles()
token = profiles[0]._token

# Get all video encoder configurations
configurations_list = media_service.GetVideoEncoderConfigurations()

# Use the first profile and Profiles have at least one
video_encoder_configuration = configurations_list[0]

# Get video encoder configuration options
options = media_service.GetVideoEncoderConfigurationOptions({'ProfileToken':token})

# Setup stream configuration
video_encoder_configuration.Encoding = 'H264'
# Setup Resolution
video_encoder_configuration.Resolution.Width = \
                options.H264.ResolutionsAvailable[0].Width
video_encoder_configuration.Resolution.Height = \
                options.H264.ResolutionsAvailable[0].Height
# Setup Quality
video_encoder_configuration.Quality = options.QualityRange.Max
# Setup FramRate
video_encoder_configuration.RateControl.FrameRateLimit = \
                                options.H264.FrameRateRange.Max
# Setup EncodingInterval
video_encoder_configuration.RateControl.EncodingInterval = \
                                options.H264.EncodingIntervalRange.Max
# Setup Bitrate
video_encoder_configuration.RateControl.BitrateLimit = \
                        options.Extension.H264[0].BitrateRange[0].Min[0]

# Create request type instance
request = media_service.create_type('SetVideoEncoderConfiguration')
request.Configuration = video_encoder_configuration
# ForcePersistence is obsolete and should always be assumed to be True
request.ForcePersistence = True

# Set the video encoder configuration
media_service.SetVideoEncoderConfiguration(request)

url =  media_service.GetStreamUri()[0]





