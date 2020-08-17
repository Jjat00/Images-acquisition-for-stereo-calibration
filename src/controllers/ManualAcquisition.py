from PySide2 import  *
import sys
sys.path.append('../src/controllers')
from ControllerManualAcquisition import *

class ManualAcquisition():
    def __init__(self, window):
        super(ManualAcquisition).__init__()
        self.window = window
        self.controllerCameraRgb = ControllerManualAcquisition()
        self.controllerCameraDepth = ControllerManualAcquisition()
        self.controllerCameraThermal = ControllerManualAcquisition()
        self.whichCameras = 0

    def handlerTurnOnRGBCamera(self):
        rgbImage = self.controllerCameraRgb.turnOnCamera(0)
        self.window.displayManual.addWidget(rgbImage)

    def handlerTurnOnDepthCamera(self):
        self.whichCameras = 1
        depthImage = self.controllerCameraDepth.turnOnCamera(1)
        self.window.displayManual.addWidget(depthImage)

    def handlerTurnOnThermalCamera(self):
        self.whichCameras = 2
        thermalImage = self.controllerCameraThermal.turnOnCamera(2)
        self.window.displayManual.addWidget(thermalImage)

    def handlerCaptureRGBImage(self):
        rgbImage = self.controllerCameraRgb.captureImage(0)
        self.window.displayManual.addWidget(rgbImage)

    def handlerCaptureDepthmage(self):
        depthImage = self.controllerCameraDepth.captureImage(1)
        self.window.displayManual.addWidget(depthImage)

    def handlerCaptureThermalImage(self):
        thermalImage = self.controllerCameraThermal.captureImage(2)
        self.window.displayManual.addWidget(thermalImage)
        
    def handlerSaveRgbAndDepthImage(self):
        nameImage = self.saveDialog()
        self.controllerCameraRgb.saveImage(0, nameImage+"Rgb.png")
        self.controllerCameraDepth.saveImage(1, nameImage+"Depth.png")

    def handlerSaveRgbAndThermalImage(self):
        nameImage = self.saveDialog()
        self.controllerCameraRgb.saveImage(0, nameImage+"Rgb.png")
        self.controllerCameraThermal.saveImage(2, nameImage+"Depth.png")

    def handlerTurnOffCamera(self):
        if self.whichCameras == 1:
            self.controllerCameraRgb.turnOffCamera()
            self.controllerCameraDepth.turnOffCamera()
        if self.whichCameras == 2:
            self.controllerCameraRgb.turnOffCamera()
            self.controllerCameraThermal.turnOffCamera()


    def handlerNone(self):
        print("NONE")

    def saveDialog(self):
        nameImage = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save as', '../data/images', selectedFilter='*.png')
        nameImage = nameImage[0]
        return nameImage
