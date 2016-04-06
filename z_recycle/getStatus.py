# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:58:19 2015

@author: Lily
"""
import requests
from xml.etree import ElementTree
from requests.auth import HTTPBasicAuth

authentication = HTTPBasicAuth('admin', '12345')
command = 'http://10.2.1.49/PTZCtrl/channels/1/status'

response = requests.get(command, auth=authentication)

tree = ElementTree.fromstring(response.content)
elevation = tree[0][0].text
azimuth = tree[0][1].text
absoluteZoom = tree[0][1].text





