from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 250)
        MainWindow.setMinimumSize(QtCore.QSize(350, 250))
        MainWindow.setMaximumSize(QtCore.QSize(350, 250))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inp = QtWidgets.QLineEdit(self.centralwidget)
        self.inp.setGeometry(QtCore.QRect(10, 60, 110, 25))
        self.inp.setFrame(False)
        self.inp.setObjectName("inp")
        self.cal = QtWidgets.QPushButton(self.centralwidget)
        self.cal.setGeometry(QtCore.QRect(30, 100, 75, 25))
        self.cal.setAutoDefault(False)
        self.cal.setObjectName("cal")
        self.out = QtWidgets.QTextBrowser(self.centralwidget)
        self.out.setGeometry(QtCore.QRect(130, 10, 211, 231))
        self.out.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.out.setObjectName("out")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(30, 190, 75, 25))
        self.close.setAutoDefault(False)
        self.close.setDefault(False)
        self.close.setFlat(False)
        self.close.setObjectName("close")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(30, 130, 75, 25))
        self.clear.setAutoDefault(False)
        self.clear.setDefault(False)
        self.clear.setFlat(False)
        self.clear.setObjectName("clear")
        self.about = QtWidgets.QPushButton(self.centralwidget)
        self.about.setGeometry(QtCore.QRect(30, 160, 75, 25))
        self.about.setAutoDefault(False)
        self.about.setDefault(False)
        self.about.setFlat(False)
        self.about.setObjectName("about")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.close.clicked.connect(MainWindow.close)
        self.cal.clicked.connect(self.Per)
        self.clear.clicked.connect(self.output)
        # self.about.clicked.connect(self.About)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Per(self):
        money = float(self.inp.text())
        all = 7
        person = money / all
        unit1 = person * 3
        unit2 = person * 4

        self.out.append("Unit 1 Must Pay :")
        self.out.append(str(unit1))
        self.out.append("")
        self.out.append("Unit 2 Must Pay :")
        self.out.append(str(unit2))

    def output(self):
        self.out.clear()
        
    # def About(self):
        # wp = '"' + sys.executable '"'
        # os.system(wp + 'include/about.py')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PerFamily"))
        self.inp.setPlaceholderText(_translate("MainWindow", "Money"))
        self.cal.setText(_translate("MainWindow", "Calculate"))
        self.label.setText(_translate("MainWindow", "Money"))
        self.about.setText(_translate("MainWindow", "About"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.close.setText(_translate("MainWindow", "Close"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
