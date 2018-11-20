# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\kilncontrol.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855
import RPi.GPIO as GPIO
from time import strftime
import math
import os
from getSetTempDialog import Ui_Dialog

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

SPI_PORT = 0
SPI_DEVICE = 0
sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT,SPI_DEVICE))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.targetTemp = 0.0
        self.t = 0
        logdatetime = strftime("%Y-%m-%d %H:%M:%S")
        self.filename = "/home/pi/kilncontrol/kilnlog/" + logdatetime
        

        MainWindow.setObjectName("Kiln Control")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setBaseSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 251, 41))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.current_temp = QtWidgets.QLabel(self.centralwidget)
        self.current_temp.setGeometry(QtCore.QRect(40, 80, 271, 91))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.current_temp.setFont(font)
        self.current_temp.setText("")
        self.current_temp.setObjectName("current_temp")

#        self.pBSetKilnTargetTemp = QtWidgets.QPushButton(self.centralwidget)
#        self.pBSetKilnTargetTemp.setGeometry(QtCore.QRect(20, 320, 221, 51))
#        self.pBSetKilnTargetTemp.setObjectName("pBSetKilnTargetTemp")
#        self.pBSetKilnTargetTemp.clicked.connect(self.setNewTargetTemp)
		
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(440, 290, 200, 104))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 200, 24))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(18)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 80, 200, 24))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(18)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")

        self.setTempText = QtWidgets.QTextEdit(self.centralwidget)
        self.setTempText.setGeometry(QtCore.QRect(70, 280, 121, 48))
        self.setTempText.setObjectName("setTempText")
        self.setTempText.mousePressEvent = self.showgetSetTempDialog

        self.current_target_temp = QtWidgets.QLabel(self.centralwidget)
        self.current_target_temp.setGeometry(QtCore.QRect(250, 240, 111, 41))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.current_target_temp.setFont(font)
        self.current_target_temp.setText("")
        self.current_target_temp.setObjectName("current_target_temp")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 240, 221, 41))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.sBKilnTargetTemp = QtWidgets.QSpinBox(self.centralwidget)
        self.sBKilnTargetTemp.setGeometry(QtCore.QRect(250, 310, 171, 61))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(14)
        self.sBKilnTargetTemp.setFont(font)
        self.sBKilnTargetTemp.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sBKilnTargetTemp.setAccelerated(True)
        self.sBKilnTargetTemp.setMinimum(0)
        self.sBKilnTargetTemp.setMaximum(1300)
        self.sBKilnTargetTemp.setProperty("value", 0)
        self.sBKilnTargetTemp.setObjectName("sBKilnTargetTemp")
        self.sBKilnTargetTemp.valueChanged[int].connect(self.targetTempChange)
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 30, 381, 201))
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.setPixmap(QtGui.QPixmap("/home/pi/kilncontrol/coilTransparentOff.png"))

        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(8)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setFont(font)
        self.exitButton.setGeometry(QtCore.QRect(690,400,81,31))
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(MainWindow.close)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.tempTimer = QtCore.QTimer()
        self.tempTimer.timeout.connect(self.getTemperatures)
        self.tempTimer.start(1000)
        self.retranslateUi(MainWindow)
                # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Current Temperature"))
#        self.pBSetKilnTargetTemp.setText(_translate("MainWindow", "Set Kiln Target Temperature"))
        self.groupBox.setTitle(_translate("MainWindow", "Kiln Control"))
        self.radioButton_2.setText(_translate("MainWindow", "Kiln Control On"))
        self.radioButton.setText(_translate("MainWindow", "Kiln Control Off"))
        self.label_2.setText(_translate("MainWindow", "Current Target Temperature"))
        self.sBKilnTargetTemp.setSuffix(_translate("MainWindow", "°C"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
	
    def targetTempChange(self):
        self.targetTemp = self.sBKilnTargetTemp.value()
        self.setTempText.setText(str(self.targetTemp)+ '\N{DEGREE SIGN}C')
	
    def setNewTargetTemp(self):
        self.targetTemp = int(self.setTempText.toPlainText())
        self.sBKilnTargetTemp.setValue(self.targetTemp)
        self.setTempText.setText(str(self.targetTemp) + '\N{DEGREE SIGN}C')
    
    def getTemperatures(self):
        temp = sensor.readTempC()
        #temp = 100.0
        self.current_temp.setText(str(temp) + '\N{DEGREE SIGN}C')
        if self.radioButton_2.isChecked():
            self.logData(temp)
            if math.isnan(temp):
                print(sensor.readState())
            if temp < self.targetTemp or math.isnan(temp):
                self.label_3.setPixmap(QtGui.QPixmap("/home/pi/kilncontrol/coilTransparentOn.png"))
                GPIO.output(16, GPIO.HIGH)
            else:
                self.label_3.setPixmap(QtGui.QPixmap("/home/pi/kilncontrol/coilTransparentOff.png"))
                GPIO.output(16, GPIO.LOW)
        else:
            self.label_3.setPixmap(QtGui.QPixmap("/home/pi/kilncontrol/coilTransparentOff.png"))
            GPIO.output(16, GPIO.LOW)

    def logData(self, theTemp):
        log = open(self.filename, "a")        
        log.write("{0}, {1}\n".format(str(self.t), str(theTemp)))
        log.close()
        self.t = self.t + 1

    def showgetSetTempDialog(self, event):

        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        rsp = Dialog.exec_()
        if ui.lineEdit.text() != '' and rsp == QtWidgets.QDialog.Accepted:
            self.targetTemp = int(ui.lineEdit.text())
            self.sBKilnTargetTemp.setValue(self.targetTemp)
            self.setTempText.setText(str(self.targetTemp) + '\N{DEGREE SIGN}C')


        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setOverrideCursor(QtCore.Qt.BlankCursor)  # Hides the cursor
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    # MainWindow.show()
    sys.exit(app.exec_())

