from PySide2 import  *
from SharedController import *

class ControllerManualAcquisition():
    def __init__(self):
        super(ControllerManualAcquisition).__init__()
        self.sharedController = SharedController()
        self.viewCamera = QtWidgets.QGraphicsView()
        self.scalaImage = 55
        self.clicPlay = False
        self.clicCapture = False
        self.dimensionsCamera = np.array([640, 480])*(self.scalaImage/100)

    def chooseCamera(self, whichCamera):
        if (whichCamera == 0):
            self.whichCamera = 0
        if (whichCamera == 1):
            self.whichCamera = 1
        if (whichCamera == 2):
            self.sharedController.initThermalCamera()
            self.whichCamera = 2

    def turnOnCamera(self, whichCamera):
        self.chooseCamera(whichCamera)
        if (self.clicPlay or self.clicCapture):
            self.viewCamera.deleteLater()
        self.initCamera()
        self.clicPlay = True
        return self.viewCamera

    def captureImage(self, whichCamera):
        self.turnOffCamera()
        frameImage = self.sharedController.captureFrame(whichCamera)
        self.imageToQtWidget(frameImage)
        self.clicCapture = True
        return self.viewCamera

    def saveImage(self, whichCamera, nameImage):
        self.sharedController.saveImage(whichCamera, nameImage)

    def turnOffCamera(self):
        if (self.clicPlay or self.clicCapture):
            self.viewCamera.deleteLater()
        self.timerCamera.stop()
        self.clicCapture = False
        self.clicPlay = False

    def initCamera(self):
        self.timerCamera = QtCore.QTimer()
        self.timerCamera.setInterval(30)
        self.timerCamera.timeout.connect(self.getFrame)            
        self.timerCamera.start()
        self.viewCamera = QtWidgets.QGraphicsView()
        scene = QtWidgets.QGraphicsScene()
        self.imagePixmap = QtGui.QPixmap(*self.dimensionsCamera)
        self.imagePixmapItem = scene.addPixmap(self.imagePixmap)
        self.viewCamera.setScene(scene)
        
    def getFrame(self):
        if (self.whichCamera == 0):
            frame = self.sharedController.getFrame(0)
        if (self.whichCamera == 1):
            frame = self.sharedController.getFrame(1)
        if (self.whichCamera == 2):
            frame = self.sharedController.getFrame(2)
        frame = self.sharedController.imageResize(frame, self.scalaImage)
        image = QtGui.QImage(frame, *self.dimensionsCamera,QtGui.QImage.Format_RGB888).rgbSwapped()
        self.imagePixmap = QtGui.QPixmap.fromImage(image)
        self.imagePixmapItem.setPixmap(self.imagePixmap)

    def imageToQtWidget(self, frame):
        frame = self.sharedController.imageResize(frame, self.scalaImage)
        image = QtGui.QImage(frame, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
        imagePixmap = QtGui.QPixmap.fromImage(image)
        imageScene = QtWidgets.QGraphicsScene()
        framePixmap = QtGui.QPixmap(*self.dimensionsCamera)
        imagePixmapItem = imageScene.addPixmap(framePixmap)
        imagePixmapItem.setPixmap(imagePixmap)
        self.viewCamera = QtWidgets.QGraphicsView()
        self.viewCamera.setScene(imageScene)

