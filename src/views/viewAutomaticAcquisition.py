import sys
sys.path.append('../src/controllers')
from AutomaticAcquisition import *

class viewAutomaticAcquisition():
    def __init__(self, window):
        super(viewAutomaticAcquisition).__init__()
        self.window = window
        self.controllerAutoAcq = AutomaticAcquisition(self.window)


    def connectButtonsRGbAndDepthCamera(self):
        try:
            self.disconnectButtons()
            self.window.startButton.clicked.connect(
                self.controllerAutoAcq.handlerStartRgbAndDepthImageAcq)
            self.window.stopButton.clicked.connect(
                self.controllerAutoAcq.handlerStopAcquisition)
        except:
            self.window.startButton.clicked.connect(
                self.controllerAutoAcq.handlerStartRgbAndDepthImageAcq)
            self.window.stopButton.clicked.connect(
                self.controllerAutoAcq.handlerStopAcquisition)

    def connectButtonsRgbAndThermalCamera(self):
        try:
            self.disconnectButtons()
            self.window.startButton.clicked.connect(
                self.controllerAutoAcq.handlerStarRgbAndThermalImageAcq)
            self.window.stopButton.clicked.connect(
                self.controllerAutoAcq.handlerStopAcquisition)
        except:
            self.window.startButton.clicked.connect(
                self.controllerAutoAcq.handlerStarRgbAndThermalImageAcq)
            self.window.stopButton.clicked.connect(
                self.controllerAutoAcq.handlerStopAcquisition)

    def disconnectButtons(self):
        self.window.startButton.clicked.disconnect()
        self.window.stopButton.clicked.disconnect()
