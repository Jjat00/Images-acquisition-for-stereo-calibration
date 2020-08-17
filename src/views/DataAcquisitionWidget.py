import sys
sys.path.append('../src/styles')
sys.path.append('../src/views')
from Styles import *
from ViewManualAcquisition import *
from viewAutomaticAcquisition import *
from PySide2 import *
import cv2

class DataAcquisitionWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(DataAcquisitionWidget, self).__init__(*args, **kwargs)
        self.loadForm()
        self.initUI()
        self.viewAutoAcquisition = viewAutomaticAcquisition(self.window)
        self.viewManualAcquisition = ViewManualAcquisition(self.window)
        Styles(self)

    def initUI(self):
        self.setWindowTitle("Data Acquisition")
        self.setGeometry(300, 100, 753, 460)
        self.manualAcquisition()
        self.window.comboBoxManual.currentIndexChanged.connect(
            self.manualAcquisition)
        self.automaticAcquisition()
        self.window.comboBoxAuto.currentIndexChanged.connect(
            self.automaticAcquisition)

    def loadForm(self):
        file = QtCore.QFile("../src/views/dataAcquisition.ui")
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)

    def manualAcquisition(self):
        chosenCamera = self.window.comboBoxManual.currentText()
        if chosenCamera == "RGB-DEPTH":
            self.viewManualAcquisition.connectButtonsRgbCamera()
            self.viewManualAcquisition.connectButtonsDepthCamera()
        if chosenCamera == "RGB-THERMAL":
            self.viewManualAcquisition.connectButtonsRgbCamera()
            self.viewManualAcquisition.connectButtonsThermalCamera()
        if chosenCamera == "NONE":
            pass

    def automaticAcquisition(self):
        chosenCamera = self.window.comboBoxAuto.currentText()
        if chosenCamera=="RGB-DEPTH":
            self.viewAutoAcquisition.connectButtonsRGbAndDepthCamera()
        if chosenCamera=="RGB-THERMAL":
            self.viewAutoAcquisition.connectButtonsRgbAndThermalCamera()
        if chosenCamera=="NONE":
            pass

