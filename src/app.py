import sys
sys.path.append('../src/views')
import cv2
from PySide2 import *
from DataAcquisitionWidget import *

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    acquisitionExtrinsicCalibration = DataAcquisitionWidget()
    acquisitionExtrinsicCalibration.show()
    app.exec_()
