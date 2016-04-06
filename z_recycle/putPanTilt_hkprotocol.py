# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:58:19 2015
@author: Lily

ip labo126: 10.2.1.49
ip labo127: 10.9.6.49
"""
import requests
import time
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement
from requests.auth import HTTPBasicAuth

authentication = HTTPBasicAuth('admin', '12345')
command = 'http://10.9.6.49/PTZCtrl/channels/1/continuous'

#root = Element('xml')
#root.set('version', '1.0')
ptzdata = Element('PTZData')
pan = SubElement(ptzdata, 'pan')
pan.text = "60"
tilt = SubElement(ptzdata, 'tilt')
tilt.text = "0"
zoom = SubElement(ptzdata, 'zoom')
zoom.text = "0"

payload = ElementTree.tostring(ptzdata, 'utf-8')

response = requests.put(command, auth=authentication, data=payload)

#print response.status_code
#print response.content


tree = ElementTree.fromstring(response.content)
statusCode = tree[1].text
print statusCode

if (statusCode == "1"):
    time.sleep(5)
    ptzdata = Element('PTZData')
    pan = SubElement(ptzdata, 'pan')
    pan.text = "0"
    tilt = SubElement(ptzdata, 'tilt')
    tilt.text = "0"
    zoom = SubElement(ptzdata, 'zoom')
    zoom.text = "0"
    payload = ElementTree.tostring(ptzdata, 'utf-8')
    response = requests.put(command, auth=authentication, data=payload)

        





