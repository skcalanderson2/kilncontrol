from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QStyle
from PyQt5.QtWidgets import QSizePolicy
from functools import partial

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 300)

        self.textValue = ''

        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 450, 300))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 2, 0, 1, 1)
        self.pushButton_11.clicked.connect(Dialog.accept)

        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_2.clicked.connect(partial(self.setText, '2'))

        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton.clicked.connect(partial(self.setText, '1'))


        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_3.clicked.connect(partial(self.setText, '3'))

        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_6.clicked.connect(partial(self.setText, '6'))

        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_4.clicked.connect(partial(self.setText, '4'))

        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_5.clicked.connect(partial(self.setText, '5'))

        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.pushButton_9.clicked.connect(partial(self.setText, '9'))

        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_7.clicked.connect(partial(self.setText, '7'))

        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_8.clicked.connect(partial(self.setText, '8'))

        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.gridLayout.addWidget(self.pushButton_10, 3, 1, 1, 1)
        self.pushButton_10.clicked.connect(partial(self.setText, '0'))

        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        #self.pushButton_11.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.retranslateUi(Dialog)
        self.pushButton.released.connect(self.lineEdit.selectAll)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pushButton, self.pushButton_2)
        Dialog.setTabOrder(self.pushButton_2, self.pushButton_3)
        Dialog.setTabOrder(self.pushButton_3, self.pushButton_4)
        Dialog.setTabOrder(self.pushButton_4, self.pushButton_5)
        Dialog.setTabOrder(self.pushButton_5, self.pushButton_6)
        Dialog.setTabOrder(self.pushButton_6, self.pushButton_7)
        Dialog.setTabOrder(self.pushButton_7, self.pushButton_8)
        Dialog.setTabOrder(self.pushButton_8, self.pushButton_9)
        Dialog.setTabOrder(self.pushButton_9, self.pushButton_10)
        Dialog.setTabOrder(self.pushButton_10, self.pushButton_11)
        Dialog.setTabOrder(self.pushButton_11, self.lineEdit)

        Dialog.setModal(True)
        #Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_11.setText(_translate("Dialog", "Set Temperature"))
        self.pushButton_2.setText(_translate("Dialog", "2"))
        self.pushButton.setText(_translate("Dialog", "1"))
        self.pushButton_3.setText(_translate("Dialog", "3"))
        self.pushButton_6.setText(_translate("Dialog", "6"))
        self.pushButton_4.setText(_translate("Dialog", "4"))
        self.pushButton_5.setText(_translate("Dialog", "5"))
        self.pushButton_9.setText(_translate("Dialog", "9"))
        self.pushButton_7.setText(_translate("Dialog", "7"))
        self.pushButton_8.setText(_translate("Dialog", "8"))
        self.pushButton_10.setText(_translate("Dialog", "0"))

    def setText(self, value):
        self.textValue = self.textValue + value
        self.lineEdit.setText(self.textValue)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())