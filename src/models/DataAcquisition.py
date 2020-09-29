import freenect
import numpy as np
import cv2
class DataAcquisition():
        def __init__(self):
                self.depthImage = []
                self.rgbImage = []

        def getDepthData(self):
                depthData, _ = freenect.sync_get_depth()
                return depthData

        def getDepthImage(self):
                self.depthData, _ = freenect.sync_get_depth()
                self.depthImage = self.depthData.astype(np.uint8)
                self.depthImage = cv2.cvtColor(
                    self.depthImage, cv2.COLOR_GRAY2BGR)
                return self.depthImage

        def getRgbImage(self):
                self.rgbImage, _  = freenect.sync_get_video()
                self.rgbImage = cv2.cvtColor(self.rgbImage, cv2.COLOR_RGB2BGR)
                return self.rgbImage

        def getThermalImage(self):
                ret, self.thermalImage = self.thermalCamera.read()
                return self.thermalImage

        def captureRgbImage(self):
                self.rgbImageCaptured = self.rgbImage
                return self.rgbImageCaptured

        def captureDepthImage(self):
                self.depthImageCaptured = self.depthImage
                self.depthDataCaptured = self.depthData
                return self.depthImageCaptured

        def captureThermalImage(self):
                self.thermalImageCaptured = self.thermalImage
                return self.thermalImageCaptured
                
        def saveRgbImage(self, nameImage):                                
                cv2.imwrite(nameImage, self.rgbImageCaptured)

        def saveDepthImage(self, nameImage):
                np.save(nameImage, self.depthDataCaptured)
                cv2.imwrite(nameImage, self.depthImageCaptured)

        def saveThermalImage(self, nameImage):                
                cv2.imwrite(nameImage, self.thermalImageCaptured)

        def initThermalCamera(self):
                self.thermalCamera = cv2.VideoCapture()
                self.thermalCamera.open(0)


