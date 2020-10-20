from PySide2 import QtGui, QtCore
relativePathIcons = '../public/icons/'

class Styles():
    def __init__(self, widget):
        super(Styles).__init__()
        self.widgetAcq = widget
        self.theme1()
        self.setIcons()
        self.formStyle()

    def theme1(self):
        self.primaryColor = '#F44336'
        self.secondaryColor = '#263238'
        self.buttons = '#00E676'
        self.frameCamera = '#212121'
        self.primaryText = '#212121'
        self.secondaryText = '#757575'
        self.lineEdit = '#f5f5f5'
        self.progressBar = '#ff795e'

    def theme2(self):
        self.primaryColor = '#7f0000'
        self.secondaryColor = '#ffffff'
        self.buttons = '#b71c1c'
        self.frameCamera = '#e0e0e0'
        self.primaryText = '#212121'
        self.secondaryText = '#000a12'
        self.lineEdit = '#f5f5f5'
        self.progressBar = '#ff795e'

    def setIcons(self):
        self.widgetAcq.window.onButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'playCamera.png'))
        self.widgetAcq.window.onButton.setIconSize(QtCore.QSize(30, 30))

        self.widgetAcq.window.offButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'stop.png'))
        self.widgetAcq.window.offButton.setIconSize(QtCore.QSize(20, 20))

        self.widgetAcq.window.captureButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'capture.png'))
        self.widgetAcq.window.captureButton.setIconSize(QtCore.QSize(25, 25))

        self.widgetAcq.window.saveButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'storage.png'))
        self.widgetAcq.window.saveButton.setIconSize(QtCore.QSize(25, 25))

        self.widgetAcq.window.startButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'play.png'))
        self.widgetAcq.window.startButton.setIconSize(QtCore.QSize(25, 25))

        self.widgetAcq.window.stopButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'stop.png'))
        self.widgetAcq.window.stopButton.setIconSize(QtCore.QSize(20, 20))

    def formStyle(self):
        styleWindow = """
            QWidget{
                    background: """+self.secondaryColor+""";
                    color:  """+self.primaryText+""";
                    border: none;
                    font: Ubuntu;
                    font-size: 12pt;
                }
                QTabWidget::tab-bar{
                    alignment: right;
                }
                QTabBar{
                    background: """+self.primaryColor+""";
                }
                QTabBar::tab {
                    background: """+self.primaryColor+""";
                    min-width: 10px;
                    margin: 5px;
                    margin-bottom: 10px;
                }
                QTabBar::tab:hover {
                    color: """+self.secondaryColor+""";
                }            
                QTabBar::tab:selected {
                    background: """+self.primaryColor+""";
                    Color: """+self.secondaryColor+""";
                }
                QTabBar::tab:!selected {
                    Color: """+self.primaryText+""";
                }
                QTabBar::tab:!selected:hover {
                    Color: """+self.secondaryColor+""";
                }
                QPushButton{
                    Background: """+self.buttons + """;
                    Background: """+self.buttons + """;
                    color: """+self.secondaryColor + """;
                    min-height: 40px;
                    border-radius: 2px;
                }       
                QPushButton:pressed {
                    background-color: rgb(224, 0, 0);
                    border-style: inset;
                } 
                QPushButton:hover {
                    background-color: """+self.primaryColor+""";
                    border-style: inset;
                } 
                QComboBox{
                    Background: """+self.buttons + """;
                    border-radius: 3px;
                    color: """+self.primaryText + """;
                    min-height: 40px;
                }        
                QComboBox QAbstractItemView {
                    border: 2px solid darkgray;
                    selection-background-color: lightgray;
                }
                QLineEdit { 
                    Background: """+self.lineEdit + """;    
                    color:  """+self.secondaryText+""";
                    border: 1px solid """+self.primaryColor + """;    
                    text-align: center;
                }
                QLabel {
                    color: """+self.secondaryText + """;
                    font-size: 11pt;
                }
                QProgressBar {
                    color: """+self.secondaryText + """;
                    background: """+self.secondaryColor+""";
                    border: none;
                }
                QProgressBar::chunk {
                    color: """+self.progressBar+""";
                    background: """+self.progressBar+""";
                    border: none;
                }                
            """
        self.widgetAcq.setStyleSheet(styleWindow)

        styleHeader = """
            padding-left: 5px;
            background: """+self.primaryColor+""";
            font: bold, Ubuntu sans-serif;
            font-size: 13pt;
            color: """+self.secondaryColor+""";
            min-width:200px;
            padding-bottom: 0;
        """
        self.widgetAcq.window.labelHeader.setStyleSheet(styleHeader)

        styleFrameCamera = """
            background: """+self.frameCamera+""";
        """
        self.widgetAcq.window.frameCameraM.setStyleSheet(styleFrameCamera)
        self.widgetAcq.window.frameCameraA.setStyleSheet(styleFrameCamera)

        styleLabelNoImage = """
            background: """+self.secondaryColor+""";
            color: """+self.primaryText+""";
            font: bold, Ubuntu sans-serif;
            font-size: 14pt;
        """
        self.widgetAcq.window.labelNoImage.setStyleSheet(styleLabelNoImage)
