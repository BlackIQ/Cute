# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 200)
        MainWindow.setMinimumSize(QtCore.QSize(250, 200))
        MainWindow.setMaximumSize(QtCore.QSize(250, 200))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(50, 60, 150, 20))
        self.input.setObjectName("input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(90, 90, 75, 23))
        self.button.setObjectName("button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 47, 13))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 211, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 160, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.button.clicked.connect(self.ShutDown)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def ShutDown(self):
        value = self.input.text()
        os.system(f"shutdown /s /t {value}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PySys"))
        self.label.setText(_translate("MainWindow", "Enter Time In Second :)"))
        self.button.setText(_translate("MainWindow", "Shut Down"))
        self.label_2.setText(_translate("MainWindow", "By AmirHossein Mohammadi - Version 1.0.0"))
        self.label_4.setText(_translate("MainWindow", "This Teeny Tiny Program Can Turn Your System Off !"))
        self.label_5.setText(_translate("MainWindow", "Developed By Python ( PyQt )"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
