import sys
from PySide2 import *
import time
from SharedController import *

class ControllerAutoAcquisition():
    def __init__(self, window):
        super(ControllerAutoAcquisition).__init__()
        self.window = window
        self.sharedController = SharedController()
        self.countNoImageAutoAcq = 0
        self.scalaImage = 55
        self.clicStart = False
        self.dimensionsCamera = np.array([640, 480])*(self.scalaImage/100)
        self.criteria = (cv2.TERM_CRITERIA_EPS +
                    cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    def setConfigAutoAcq(self, NoImages, patternDimension, pathImages):
        self.patternDimension = patternDimension
        self.NoImagesAutoAcq = NoImages
        self.pathImages = pathImages

    def chooseCamera(self, whichCamera):
        if (whichCamera == 0):
            self.whichCamera = 0
        if (whichCamera == 1):
            self.whichCamera = 1
            self.sharedController.initThermalCamera()

    def turnOnCamera(self, whichCamera):
        self.chooseCamera(whichCamera)
        if (self.clicStart):
            self.viewCamera1.deleteLater()
            self.viewCamera2.deleteLater()
        self.initCamera()
        self.initCounter()
        return self.viewCamera1, self.viewCamera2

    def turnOffCamera(self):
        if (self.clicStart):
            self.viewCamera1.deleteLater()
            self.viewCamera2.deleteLater()
        self.timerCameras.stop()
        self.countNoImageAutoAcq = 0
        self.clicStart = False

    def initCamera(self):
        self.timerCameras = QtCore.QTimer()
        self.timerCameras.setInterval(30)
        self.timerCameras.timeout.connect(self.getFrameDrawPattern)
        self.timerCameras.start()
        self.widgetCamera1()
        self.widgetCamera2()
        self.clicStart = True

    def initCounter(self):
        self.timerCounter = QtCore.QTimer()
        self.timerCounter.setInterval(30)
        self.timerCounter.timeout.connect(self.setValueProgressBar)
        self.timerCounter.start()

    def setValueProgressBar(self):
        value = (self.countNoImageAutoAcq/self.NoImagesAutoAcq)*100
        self.window.progressBarAcq.setValue(value)
        self.window.labelNoImage.setText(str(self.countNoImageAutoAcq))

    def widgetCamera1(self):
        self.viewCamera1 = QtWidgets.QGraphicsView()
        scene1 = QtWidgets.QGraphicsScene()
        self.imagePixmap1 = QtGui.QPixmap(*self.dimensionsCamera)
        self.imagePixmapItem1 = scene1.addPixmap(self.imagePixmap1)
        self.viewCamera1.setScene(scene1)
        
    def widgetCamera2(self):
        self.viewCamera2 = QtWidgets.QGraphicsView()
        scene2 = QtWidgets.QGraphicsScene()
        self.imagePixmap2 = QtGui.QPixmap(*self.dimensionsCamera)
        self.imagePixmapItem2 = scene2.addPixmap(self.imagePixmap2)
        self.viewCamera2.setScene(scene2)

    def getFrameDrawPattern(self):
        if self.countNoImageAutoAcq < self.NoImagesAutoAcq:
            if (self.whichCamera == 0):
                frameCamera1, frameCamera2 = self.detectPattern(
                    self.sharedController.getFrame(0), self.sharedController.getFrame(1))
            if (self.whichCamera == 1):
                frameCamera1, frameCamera2 = self.detectPattern(
                    self.sharedController.getFrame(0), self.sharedController.getFrame(2))
            self.pixMapCamera1(frameCamera1)
            self.pixMapCamera2(frameCamera2)
        else:
            self.timerCameras.stop()

    def pixMapCamera1(self, frameCamera1):
        frameCamera1 = self.sharedController.imageResize(
            frameCamera1, self.scalaImage)
        imageCamera1 = QtGui.QImage(
            frameCamera1, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.imagePixmap1 = QtGui.QPixmap.fromImage(imageCamera1)
        self.imagePixmapItem1.setPixmap(self.imagePixmap1)

    def pixMapCamera2(self, frameCamera2):
        frameCamera2 = self.sharedController.imageResize(
            frameCamera2, self.scalaImage)
        imageCamera2 = QtGui.QImage(
            frameCamera2, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.imagePixmap2 = QtGui.QPixmap.fromImage(imageCamera2)
        self.imagePixmapItem2.setPixmap(self.imagePixmap2)

    def detectPattern(self, image1, image2):        
        grayImage1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        grayImage2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        self.patternDimension = (
            self.patternDimension[1], self.patternDimension[0])
        self.findCorners1, self.corners1 = cv2.findChessboardCorners(
            grayImage1, self.patternDimension, flags=cv2.CALIB_CB_NORMALIZE_IMAGE)
        self.findCorners2, self.corners2 = cv2.findChessboardCorners(
            grayImage2, self.patternDimension, flags=cv2.CALIB_CB_NORMALIZE_IMAGE)
        if self.findCorners1 and self.findCorners2:
            self.subPixCorners(grayImage1, grayImage2)
            self.saveImages(image1, image2)
            image1, image2 = self.drawPattern(image1, image2)
            self.countNoImageAutoAcq += 1
            #time.sleep(0.5)
        return image1, image2

    def subPixCorners(self, grayImage1, grayImage2):
        self.corners1 = cv2.cornerSubPix(
            grayImage1, self.corners1, (11, 11), (-1, -1), self.criteria)
        self.corners2 = cv2.cornerSubPix(
            grayImage2, self.corners2, (11, 11), (-1, -1), self.criteria)

    def drawPattern(self, image1, image2):
        image1 = cv2.drawChessboardCorners(
            image1, self.patternDimension, self.corners1, self.findCorners1)
        image2 = cv2.drawChessboardCorners(
            image2, self.patternDimension, self.corners2, self.findCorners2)
        return image1, image2

    def saveImages(self, image1, image2):
        nameImage1 = self.pathImages + 'Rgb' + \
            str(self.countNoImageAutoAcq)+'.png'
        cv2.imwrite(nameImage1, image1)
        if self.whichCamera == 0:
            nameImage2 = self.pathImages+'Depth' + \
                str(self.countNoImageAutoAcq)+'.png'
            cv2.imwrite(nameImage2, image2)
        if self.whichCamera == 1:
            nameImage2 = self.pathImages+'Thermal' + \
                str(self.countNoImageAutoAcq)+'.png'
            cv2.imwrite(nameImage2, image2)
