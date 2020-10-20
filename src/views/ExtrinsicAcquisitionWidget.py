from PySide2 import QtCore, QtUiTools, QtWidgets
import sys
import os
dirs = ['views','styles', 'controllers', 'models']
for nameDir in dirs:
    path = os.path.join(sys.path[0], nameDir)
    sys.path.append(path)

from Styles import *

import cv2

class ExtrinsicAcquisitionWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(ExtrinsicAcquisitionWidget, self).__init__(*args, **kwargs)
        self.loadForm()
        self.initUI()
        Styles(self)

    def initUI(self):
        self.setWindowTitle("Data Acquisition")
        self.setGeometry(300, 100, 753, 460)

    def loadForm(self):
        formUI = os.path.join(sys.path[0], 'views/dataAcquisition.ui')
        file = QtCore.QFile(formUI)
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    acquisitionExtrinsicCalibration = ExtrinsicAcquisitionWidget()
    acquisitionExtrinsicCalibration.show()
    app.exec_()
