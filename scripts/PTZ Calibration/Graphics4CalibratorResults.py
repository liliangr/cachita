# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 19:25:48 2015

@author: Lily
"""
import numpy as np
import matplotlib.pyplot as plt



plt.close(1)
plt.close(2)
plt.close(3)
m = np.loadtxt(r"D:\UNQ\IACI\1_PTZ\PYTHON\Camera\calibratorResults.txt", skiprows=1)

plt.figure(1)
plt.plot(m[:,0], m[:,1], 'bs', label='fx')
plt.plot(m[:,0], m[:,2], 'rs', label='fy')
plt.plot(m[:,0], m[:,1], 'b', m[:,0], m[:,2], 'r')
plt.title('Zoom vs f')
plt.xlabel('fx, fy [pixel]')
plt.ylabel('zoom [%]')
plt.legend(loc=2)
deg = 1
p = np.polyfit(m[:,0], m[:,2],deg)
plt.text(40,10000, 'y = ' + str(p[0]) + 'x + ' + str(p[1]))
plt.show()

plt.figure(2)
plt.plot(m[:,0], m[:,3], 'bs', label='fovx')
plt.plot(m[:,0], m[:,4], 'rs', label='fovy')
plt.plot(m[:,0], m[:,3], 'b', m[:,0], m[:,4], 'r')
plt.title('Zoom vs fov')
plt.xlabel('fovx, fovy [º]')
plt.ylabel('zoom [%]')
plt.legend(loc=1)
deg = 2
p = np.polyfit(m[:,0], m[:,3],deg)
plt.text(15,5, 'y = ' + str(p[0]) + 'x^2 + ' + str(p[1]) + 'x + ' + str(p[2]))
p = np.polyfit(m[:,0], m[:,4],deg)
plt.text(20,45, 'y = ' + str(p[0]) + 'x^2 + ' + str(p[1]) + 'x + ' + str(p[2]))

plt.show()

plt.figure(3)
plt.plot(m[:,0], m[:,5], 'gs', label='focalLength')
plt.plot(m[:,0], m[:,5], 'g')
plt.title('Zoom vs focalLength')
plt.xlabel('focalLength [mm]')
plt.ylabel('zoom [%]')
plt.legend(loc=1)
deg = 1
p = np.polyfit(m[:,0], m[:,5],deg)
plt.text(20,5, 'y = ' + str(p[0]) + 'x + ' + str(p[1]))
plt.show()


#deg = 1
#p = np.polyfit(m[:,0], m[:,5],deg)
## p(x) = p[0] * x**deg + ... + p[deg] 
#print 'y = ' + str(p[0]) + 'x + ' + str(p[1])
