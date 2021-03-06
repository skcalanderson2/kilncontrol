# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\kilncontrol.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import Qt, QtCore, QtGui, QtWidgets
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855
import RPi.GPIO as GPIO
from time import strftime
import math
from getSetTempDialog import Ui_Dialog
import PID
from enum import Enum
# import numpy
# import pyqtgraph as pg

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

PID_GPIO = GPIO.PWM(16, .2)

SPI_PORT = 0
SPI_DEVICE = 0
sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

P = 1.0
I = 1.0
D = 0.001

Temp_Profile = [[1, 2.5, 0, 60, 150],
                [2, 0.0, 61, 240, 150],
                [3, 3.6, 241, 300, 370],
                [4, 0.0, 301, 420, 370],
                [5, 3.1, 421, 540, 750],
                [6, 0.0, 541, 780, 750],
                [7, -2.5, 781, 840, 600]]


class KilnState(Enum):
    IDLE = 1
    MANUAL_HEATING = 2
    PROFILE_HEATING = 3


CURRENT_KILN_STATE = KilnState.IDLE
LAST_KILN_STATE = KilnState.IDLE

CURRENT_Temp_Profile_Number = 1
START_TEMP = 0
PROFILE_TIME = 0
CURRENT_PROFILE_RAMP_TEMP = 0
CURRENT_RAMP = 0.0
CURRENT_SET_POINT = 0

PID_GPIO.stop()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.targetTemp = 0.0
        self.t = 0
        logdatetime = strftime("%Y-%m-%d %H:%M:%S")
        self.filename = "/home/pi/kilncontrol/kilnlog/" + logdatetime
        self.pid = PID.PID(P, I, D)
        self.pid.SetPoint = 0.0
        self.pid.setSampleTime(1.0)
        self.pid_output = 0.0
        self.pid_status = 'off'

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
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.current_temp = QtWidgets.QLabel(self.centralwidget)
        self.current_temp.setGeometry(QtCore.QRect(40, 35, 140, 91))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(14)
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

        self.radioButton_profile = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_profile.setGeometry(QtCore.QRect(10, 30, 200, 24))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(18)
        self.radioButton_profile.setFont(font)
        self.radioButton_profile.setObjectName("radioButton_profile")
        # self.sBKilnTargetTemp.valueChanged[int].connect(self.targetTempChange)
        self.radioButton_profile.toggled.connect(lambda: self.btnstate(self.radioButton_profile))
        # self.radioButton_profile.setEnabled(False)

        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 55, 200, 24))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(18)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(lambda: self.btnstate(self.radioButton_2))
        self.radioButton_2.setEnabled(False)

        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 80, 200, 24))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(18)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(lambda: self.btnstate(self.radioButton))

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

        self.statelabel = QtWidgets.QLabel(self.centralwidget)
        self.statelabel.setGeometry(QtCore.QRect(540, 270, 240, 61))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.statelabel.setFont(font)
        self.statelabel.setObjectName("statelabel")

        self.pidoutputlabel = QtWidgets.QLabel(self.centralwidget)
        self.pidoutputlabel.setGeometry(QtCore.QRect(250, 280, 130, 61))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pidoutputlabel.setFont(font)
        self.pidoutputlabel.setObjectName("statelabel")

        self.sBKilnTargetTemp = QtWidgets.QSpinBox(self.centralwidget)
        self.sBKilnTargetTemp.setGeometry(QtCore.QRect(250, 350, 171, 61))
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

        self.element_image = QtWidgets.QLabel(self.centralwidget)
        # self.element_image.setGeometry(QtCore.QRect(400, 30, 381, 201))
        self.element_image.setGeometry(QtCore.QRect(70, 350, 100, 53))
        self.element_image.setText("")
        self.element_image.setScaledContents(True)
        self.element_image.setObjectName("element_image")

        self.element_image.setPixmap(QtGui.QPixmap("/home/pi/kilncontrol/coilTransparentOff.png"))

        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(8)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setFont(font)
        self.exitButton.setGeometry(QtCore.QRect(690, 350, 81, 31))
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(MainWindow.close)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.profileTempTimer = QtCore.QTimer()
        self.profileTempTimer.timeout.connect(self.updateProfileTime)
        # self.profileTempTimer.start(60000)

        self.tempTimer = QtCore.QTimer()
        self.tempTimer.timeout.connect(self.updateState)
        self.tempTimer.start(1000)
        self.retranslateUi(MainWindow)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # self.setupProfile()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Current Temperature"))
        #        self.pBSetKilnTargetTemp.setText(_translate("MainWindow", "Set Kiln Target Temperature"))
        self.groupBox.setTitle(_translate("MainWindow", "Kiln Control"))
        self.radioButton_profile.setText(_translate("MainWindow", "Kiln Profile On"))
        self.radioButton_2.setText(_translate("MainWindow", "Kiln Manual On"))
        self.radioButton.setText(_translate("MainWindow", "Kiln  Off"))
        self.label_2.setText(_translate("MainWindow", "Current Target Temperature"))
        self.sBKilnTargetTemp.setSuffix(_translate("MainWindow", "°C"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))

    def targetTempChange(self):
        print("targetTempChange Called")
        self.targetTemp = self.sBKilnTargetTemp.value()
        if CURRENT_KILN_STATE == KilnState.MANUAL_HEATING:
            self.pid.SetPoint = self.targetTemp
        self.setTempText.setText(str(self.targetTemp) + '\N{DEGREE SIGN}C')
        self.radioButton_2.setEnabled(True)

    def setNewTargetTemp(self):
        print("setNewTargetTemp Called")
        self.targetTemp = int(self.setTempText.toPlainText())
        self.pid.SetPoint = self.targetTemp
        self.sBKilnTargetTemp.setValue(self.targetTemp)
        self.setTempText.setText(str(self.targetTemp) + '\N{DEGREE SIGN}C')

    def setupProfile(self):
        global Temp_Profile
        global START_TEMP
        global CURRENT_Temp_Profile_Number
        global CURRENT_PROFILE_RAMP_TEMP
        global PROFILE_TIME
        global CURRENT_SET_POINT
        global CURRENT_RAMP

        # once I get spinner widget to set profile point the will will update the current temp profile number

        temp_profile0 = Temp_Profile[0]
        temp_final_temp = temp_profile0[4]
        temp_starting_temp = sensor.readTempC()
        temp_profile0[1] = (temp_final_temp - temp_starting_temp) / 60.0
        print("Profile Temperature: " + str(temp_starting_temp))
        START_TEMP = temp_starting_temp
        CURRENT_PROFILE_RAMP_TEMP = START_TEMP
        PROFILE_TIME = 0
        CURRENT_RAMP = temp_profile0[1]
        CURRENT_SET_POINT = temp_final_temp
        self.setTempText.setText('{:{width}.{prec}f}'.format(CURRENT_PROFILE_RAMP_TEMP, width=6, prec=2) + '\N{DEGREE SIGN}C')

        self.profileTempTimer.start(60000)
        # print(self.profileTempTimer.isActive())

    def btnstate(self, b):
        global CURRENT_KILN_STATE
        global LAST_KILN_STATE
        print("btnstate called " + b.text())
        if b.text() == "Kiln Profile On":
            if b.isChecked() == True:
                if LAST_KILN_STATE != CURRENT_KILN_STATE:
                    LAST_KILN_STATE = CURRENT_KILN_STATE
                CURRENT_KILN_STATE = KilnState.PROFILE_HEATING
                self.setupProfile()
                self.pid_status = 'on'
                PID_GPIO.start(0)    
        if b.text() == "Kiln Manual On":
            if b.isChecked() == True:
                if LAST_KILN_STATE != CURRENT_KILN_STATE:
                    LAST_KILN_STATE = CURRENT_KILN_STATE
                CURRENT_KILN_STATE = KilnState.MANUAL_HEATING
                self.pid_status = 'on'
                self.profileTempTimer.stop()
                if not math.isnan(self.sBKilnTargetTemp.value()):
                    self.targetTemp = self.sBKilnTargetTemp.value()
                    self.pid.SetPoint = self.targetTemp
                    print('sBKilnTargetTemp: ' + str(self.sBKilnTargetTemp.value()))
                    self.pid.SetPoint = self.targetTemp
                    # self.statelabel.setText("")
                    self.setTempText.setText(
                        '{:{width}.{prec}f}'.format(self.targetTemp, width=6, prec=2) + '\N{DEGREE SIGN}C')
                    PID_GPIO.start(0)
                    self.updateProfileTime()
        if b.text() == "Kiln  Off":
            if b.isChecked() == True:
                if LAST_KILN_STATE != CURRENT_KILN_STATE:
                    LAST_KILN_STATE = CURRENT_KILN_STATE
                    CURRENT_KILN_STATE = KilnState.IDLE
                    self.pid_status = 'off'
                    # self.statelabel.setText("")
                    self.profileTempTimer.stop()
                    PID_GPIO.stop()

    def updatePIDTemp(self, temp):
        # print("UpdatePIDTemp Called")
        if not math.isnan(temp):  # We are going to make sure temp is not NaN then set to the new value if it isn't
            self.pid.update(temp)
        if self.pid.output > 100:
            self.pid_output = 100
        elif self.pid.output < 0:
            self.pid_output = 0
        else:
            self.pid_output = self.pid.output  # gonna store the pid output in a class variable just to have it on hand
        # print("Pid_output" + str(self.pid.output))

        self.pidoutputlabel.setText('PID out:{:{width}.{prec}f}'.format(self.pid_output, width=6, prec=2))


    def updateProfileTime(self):
        global PROFILE_TIME
        global CURRENT_PROFILE_RAMP_TEMP
        global CURRENT_RAMP
        global CURRENT_SET_POINT
        print("updateProfileTime called")
        if CURRENT_KILN_STATE == KilnState.PROFILE_HEATING:
            PROFILE_TIME = PROFILE_TIME + 1
            if CURRENT_RAMP > 0.0 and CURRENT_PROFILE_RAMP_TEMP < CURRENT_SET_POINT:
                CURRENT_PROFILE_RAMP_TEMP = CURRENT_PROFILE_RAMP_TEMP + CURRENT_RAMP

            if CURRENT_PROFILE_RAMP_TEMP > CURRENT_SET_POINT:
                self.pid.SetPoint = CURRENT_SET_POINT
                self.setTempText.setText(
                    '{:{width}.{prec}f}'.format(CURRENT_SET_POINT, width=6, prec=2) + '\N{DEGREE SIGN}C')
            else:
                self.pid.SetPoint = CURRENT_PROFILE_RAMP_TEMP
                self.setTempText.setText(
                    '{:{width}.{prec}f}'.format(CURRENT_PROFILE_RAMP_TEMP, width=6, prec=2) + '\N{DEGREE SIGN}C')
            
            print('current profile ramp temp: ' + str(CURRENT_PROFILE_RAMP_TEMP))

    def updateCurrentTemperatureText(self, temp):
        self.current_temp.setText(str(temp) + '\N{DEGREE SIGN}C')

    def updateManualHeatingState(self, current_temperature):
        self.updatePIDTemp(current_temperature)

    def updateProfileHeatingState(self, current_temperature):
        global CURRENT_Temp_Profile_Number
        global CURRENT_PROFILE_RAMP_TEMP
        global CURRENT_RAMP
        global CURRENT_SET_POINT

        # check to see if we need to switch profile steps because profile time moved to next step
        profilePoint = Temp_Profile[CURRENT_Temp_Profile_Number]
        if PROFILE_TIME > profilePoint[3] and CURRENT_Temp_Profile_Number < 7:
            CURRENT_Temp_Profile_Number = CURRENT_Temp_Profile_Number + 1
            profilePoint = Temp_Profile[CURRENT_Temp_Profile_Number]
            ramp = profilePoint[1]
            setPointTemp = profilePoint[4]
            CURRENT_RAMP = ramp
            self.pid.SetPoint = setPointTemp

        self.updatePIDTemp(current_temperature)

    def updateState(self):
        if self.pid.output > 0.0 and self.pid_status == 'on':
            self.element_image.setPixmap(QtGui.QPixmap("/home/pi/kilncontrol/coilTransparentOn.png"))
        else:
            self.element_image.setPixmap(QtGui.QPixmap("/home/pi/kilncontrol/coilTransparentOff.png"))

        temp = sensor.readTempC()
        self.logData(temp)
        self.updateCurrentTemperatureText(temp)
        if CURRENT_KILN_STATE == KilnState.MANUAL_HEATING:
            self.updateManualHeatingState(temp)
        elif CURRENT_KILN_STATE == KilnState.PROFILE_HEATING:
            self.updateProfileHeatingState(temp)

        if self.pid_status == 'on':
            print("PID is ON updating duty cycle:" + str(self.pid_output))
            PID_GPIO.ChangeDutyCycle(self.pid_output)
            print("GPIO function:" + str(GPIO.gpio_function(16)))
        elif self.pid_status == 'off':
            PID_GPIO.stop()
        self.statelabel.setText(str(CURRENT_KILN_STATE))


    # def updateProfileTemperature(self):
    #     global PROFILE_TIME
    #     PROFILE_TIME = PROFILE_TIME + 1
    #     print("PROFILE_TIME:" + str(PROFILE_TIME))
    #
    #     for profile in Temp_Profile:
    #         startTime = profile[1]
    #         endTime = profile[2]
    #         finalTemp = profile[3]
    #         ramp = profile[0]
    #         if startTime <= PROFILE_TIME <= endTime:
    #             #OK we got the current profile
    #             break
    #         elif endTime < PROFILE_TIME:
    #             #So we are at the last profile so we just need to hold the temp
    #             self.targetTemp = finalTemp
    #             self.pid.SetPoint = finalTemp
    #             self.setTempText.setText(str(finalTemp) + '\N{DEGREE SIGN}C')
    #
    #     ramp_temp = START_TEMP + PROFILE_TIME * ramp
    #     if ramp_temp > finalTemp or ramp == 0.0:
    #         ramp_temp = finalTemp
    #
    #     self.targetTemp = ramp_temp
    #     self.setTempText.setText(str(self.targetTemp) + '\N{DEGREE SIGN}C')
    #     print ("Ramp_temp:" + str(ramp_temp))
    #     self.pid.SetPoint = ramp_temp
    #     self.setTempText.setText(str(ramp_temp) + '\N{DEGREE SIGN}C')

    def logData(self, theTemp):
        log = open(self.filename, "a")
        log.write("{0}, {1}\n".format(str(self.t), str(theTemp)))
        log.close()
        self.t = self.t + 1

    def logInfo(self, info):
        log = open(self.filename, "a")
        log.write("{0}\n".format(info))
        log.close()

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
    # MainWindow.showFullScreen()
    MainWindow.show()
    sys.exit(app.exec_())
    PID_GPIO.stop()
    GPIO.cleanup()
