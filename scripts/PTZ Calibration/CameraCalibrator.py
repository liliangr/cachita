"""
Created on Mon Nov 30 18:45:26 2015
"""

import cv2
import glob
import numpy as np

class CameraCalibrator():

        
    def __init__(self):
         
        self.images = glob.glob(r"D:\UNQ\IACI\1_PTZ\PYTHON\Imagenes\zoom 20\*.jpg")
        self.patternSize = (9, 6) # los cuadraditos del chessboard -1
        self.imageSize = (1280,720)
        
        # Vector con la identificacion de cada cuadrito
        self.objp = np.zeros((6*9,3), np.float32)
        self.objp[:,:2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2) #rellena las columnas 1 y 2
        
        # Vectores con puntos de objetos y de la imagen de todas las capturas
        self.objpoints = [] #3d points in real world
        self.imgpoints = [] #2d points in image plane
       
       
           
    def calibrate(self):
        
        rvecs = ()
        tvecs = ()
        cameraMatrix = ()
        distCoeffs = ()
        
        self.findCorners()
        rms, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(
            self.objpoints, self.imgpoints, self.imageSize, cameraMatrix, distCoeffs, rvecs, tvecs, 0)
                                      
        apertureWidth = 4.8
        apertureHeight = 3.6
        fovx, fovy, focalLength, principalPoint, aspectRatio = cv2.calibrationMatrixValues(
            cameraMatrix, self.imageSize, apertureWidth, apertureHeight)
        
        
        
        # Cuentas a mano para el fov
        fx = cameraMatrix[0,0]
        fy = cameraMatrix[1,1]
        
        print 'fx:' + str(fx) + ' fy:' + str(fy) + ' fovx:' + str(fovx) + ' fovy:' + str(fovy) + ' focalLength:' + str(focalLength)


    def findCorners(self):
        corners = ()
        corners2 = ()
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        
        for strfile in self.images:
            img = cv2.imread(strfile, cv2.IMREAD_GRAYSCALE)
            
            found, corners = cv2.findChessboardCorners(img, self.patternSize)
            if found:
                 #cornerSubPix para devolver `recision de subpixel (tdv no se que es)
                 corners2 = cv2.cornerSubPix(img, corners, self.patternSize, (-1, -1), criteria)
                 self.imgpoints.append(corners2)
                 self.objpoints.append(self.objp)
                 
        #         cv2.drawChessboardCorners(img, patternSize, corners, found)
        #         cv2.imshow('Puntos detectados', img)
        #         cv2.waitKey(0)
            else:
                print 'No se encontraron esquinas en ' + strfile
        

#
#fovx = 2 * np.arctan(imageSize[0] / (2 * fx)) * 180.0 / np.pi
#fovy = 2 * np.arctan(imageSize[1] / (2 * fy)) * 180.0 / np.pi
