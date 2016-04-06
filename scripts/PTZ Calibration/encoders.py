# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 16:44:03 2016

@author: Lily
"""
#import cv2
#
##import numpy as np
#
#strfile = r"D:\UNQ\IACI\1_PTZ\PYTHON\Imagenes\encoder\hp2.jpg"
#img = cv2.imread(strfile, cv2.IMREAD_GRAYSCALE)
#cv2.imshow('Home Position', img)
#cv2.waitKey(0)

import matplotlib.pyplot as plt

strfile = r"D:\UNQ\IACI\1_PTZ\PYTHON\Imagenes\encoder\hp2.jpg"
im = plt.imread(strfile)
implot = plt.imshow(im)

# put a blue dot at (10, 20)
#plt.scatter(x=[640, 630], y=[360,386])
plt.scatter(x=[640, 10, 1270], y=[360, 300, 300])

plt.show()