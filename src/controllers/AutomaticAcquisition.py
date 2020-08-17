from PySide2 import  *
import sys
sys.path.append('../src/controllers')
from ControllerAutoAcquisition import *

class AutomaticAcquisition():
    def __init__(self, window):
        super(AutomaticAcquisition).__init__()
        self.window = window
        self.controllerCamera = ControllerAutoAcquisition(self.window)
        self.whichCameras = 0

    def configAdqcquisition(self):
        NoImages = int(self.window.NoImages.text())
        patternDimension = (int(self.window.cornerX.text()),
                            int(self.window.cornerY.text()))
        pathImages = self.saveDialog()
        self.controllerCamera.setConfigAutoAcq(
            NoImages, patternDimension, pathImages)

    def handlerStartRgbAndDepthImageAcq(self):
        self.whichCameras = 1
        self.configAdqcquisition()
        rgbImage, depthImage = self.controllerCamera.turnOnCamera(0)
        self.window.displayAuto.addWidget(rgbImage)
        self.window.displayAuto.addWidget(depthImage)
        #self.window.labelNoImage.setText(str(NoImage))

    def handlerStarRgbAndThermalImageAcq(self):
        self.whichCameras = 2
        self.configAdqcquisition()
        rgbImage, themalImage = self.controllerCamera.turnOnCamera(1)
        self.window.displayAuto.addWidget(rgbImage)
        self.window.displayAuto.addWidget(themalImage)

    def handlerStopAcquisition(self):
        self.controllerCamera.turnOffCamera()

    def saveDialog(self):
        pathImages, info = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save as', '../data/images', selectedFilter='*.png')
        return pathImages
