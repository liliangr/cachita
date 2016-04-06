"""
Created on Mon Nov 30 18:45:26 2015
"""

import cv2
import glob
import numpy as np

class CameraCalibrator():
#images = glob.glob(r"D:\UNQ\IACI\1_PTZ\PYTHON\Imagenes\*.jpg")
images = glob.glob(r"D:\UNQ\IACI\1_PTZ\PYTHON\Imagenes\zoom 20\*.jpg")
corners = ()
patternSize = (9, 6) # los cuadraditos del chessboard -1
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
imageSize = (1280,720)

# Se arma un vector con la identificacion de cada cuadrito
objp = np.zeros((6*9,3), np.float32)
objp[:,:2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2) #rellena las columnas 1 y 2


#Arrays to store object points and image points from all the images.
objpoints = [] #3d points in real world
imgpoints = [] #2d points in image plane


for strfile in images:
    img = cv2.imread(strfile, cv2.IMREAD_GRAYSCALE)
    
    found, corners = cv2.findChessboardCorners(img, patternSize)
    if found:
         #cornerSubPix no se usa pq findChessboardCorners ya devuelve con precision de subpixel
         #corners2 = cv2.cornerSubPix(img, corners, patternSize, (-1, -1), criteria)
         imgpoints.append(corners)#corners2
         objpoints.append(objp)
         
#         cv2.drawChessboardCorners(img, patternSize, corners, found)
#         cv2.imshow('Puntos detectados', img)
#         cv2.waitKey(0)
    else:
        print 'No se encontraron esquinas en ' + strfile
            
rvecs = ()
tvecs = ()
cameraMatrix = ()
distCoeffs = ()
rms, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(objpoints,  imgpoints, imageSize, cameraMatrix,  distCoeffs,  
                    rvecs, tvecs, 0)
                              
apertureWidth = 4.8
apertureHeight = 3.6
fovx, fovy, focalLength, principalPoint, aspectRatio = cv2.calibrationMatrixValues(cameraMatrix, imageSize, apertureWidth, apertureHeight)



# Cuentas a mano para el fov
fx = cameraMatrix[0,0]
fy = cameraMatrix[1,1]

print 'fx:' + str(fx) + ' fy:' + str(fy) + ' fovx:' + str(fovx) + ' fovy:' + str(fovy) + ' focalLength:' + str(focalLength)
#
#fovx = 2 * np.arctan(imageSize[0] / (2 * fx)) * 180.0 / np.pi
#fovy = 2 * np.arctan(imageSize[1] / (2 * fy)) * 180.0 / np.pi
