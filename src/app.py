"""
Images Acquisition for Extrinsic Calibration
Author: Jaimen Aza
Email: userjjat00@gmail.com
"""


"""
Add directories to path
"""
from PySide2 import QtWidgets
import sys
import os

dirs = ['views',
        'acquisition',
        'controllers']
        
for nameDir in dirs:
    path = os.path.join(sys.path[0], nameDir)
    sys.path.append(path)


""" 
Add controller to main widget and run QApplication
"""
from controllers.MainController import MainController
from views.ExtrinsicAcquisitionWidget import ExtrinsicAcquisitionWidget

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    extrinsicAcquisitionWidget = ExtrinsicAcquisitionWidget()
    mainController = MainController(extrinsicAcquisitionWidget)
    app.exec_()
