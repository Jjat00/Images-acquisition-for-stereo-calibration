from DataAcquisition import *

class SharedController():
    def __init__(self):
        super(SharedController).__init__()
        self.camera = DataAcquisition()
    
    def initThermalCamera(self):
        self.camera.initThermalCamera()

    def getFrame(self, whichCamera):
        if (whichCamera == 0):
            frameImage = self.camera.getRgbImage()
        if (whichCamera == 1):
            frameImage = self.camera.getDepthImage()
        if (whichCamera == 2):
            frameImage = self.camera.getThermalImage()
        return frameImage

    def captureFrame(self, whichCamera):
        if (whichCamera == 0):
            frameImage = self.camera.captureRgbImage()
        if (whichCamera == 1):
            frameImage = self.camera.captureDepthImage()
        if (whichCamera == 2):
            frameImage = self.camera.captureThermalImage()
        return frameImage

    def saveImage(self, whichCamera, nameImage):
        try:
            if whichCamera == 0:
                self.camera.saveRgbImage(nameImage)
            if whichCamera == 1:
                self.camera.saveDepthImage(nameImage)
            if whichCamera == 2:
                self.camera.saveThermalImage(nameImage)
        except:
            print("none image")

    def imageResize(self, pathImage, scalePercent):
        if (isinstance(pathImage, str)):
            image = cv2.imread(pathImage, cv2.IMREAD_UNCHANGED)
        else:
            image = pathImage
        width = int(image.shape[1] * scalePercent / 100)
        height = int(image.shape[0] * scalePercent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        return resized
