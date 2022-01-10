# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'amir.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 300)
        MainWindow.setMinimumSize(QtCore.QSize(450, 300))
        MainWindow.setMaximumSize(QtCore.QSize(450, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.click = QtWidgets.QPushButton(self.centralwidget)
        self.click.setGeometry(QtCore.QRect(10, 80, 71, 23))
        self.click.setObjectName("click")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 20, 151, 21))
        self.label1.setObjectName("label1")
        self.code = QtWidgets.QLineEdit(self.centralwidget)
        self.code.setGeometry(QtCore.QRect(10, 50, 131, 20))
        self.code.setObjectName("code")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(150, 10, 291, 271))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.me = QtWidgets.QTextBrowser(self.tab)
        self.me.setGeometry(QtCore.QRect(0, 0, 291, 251))
        self.me.setObjectName("me")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.langs = QtWidgets.QTextBrowser(self.tab_2)
        self.langs.setGeometry(QtCore.QRect(0, 0, 291, 251))
        self.langs.setObjectName("langs")
        self.tabWidget.addTab(self.tab_2, "")
        self.result = QtWidgets.QTextBrowser(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(10, 190, 131, 91))
        self.result.setObjectName("result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.click.clicked.connect(self.test)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def me_tab(self):
        self.me.append("Hello World !")
        self.me.append("This a Test For Check ( Me ) Tab . . .")
        self.me.append(" ")
        self.me.append("Test Was Success Full :)")

    def langs_tab(self):
        self.langs.append("After a few years I learned some languages .")

    def test(self):
        self.result.append("Verifying . . .")
        app.processEvents()
        if "code" == self.code.text():
            self.result.clear()
            self.result.append("That Is Right !")
            self.result.append("See Me Now :)")
            self.result.append("- - - - - - - - - - - - - - -")

            self.me_tab()
            self.langs_tab()

            self.click.deleteLater()

        else:
            self.result.clear()
            self.result.append("Try Again :(")
            self.result.append("- - - - - - - - - - - - - - -")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Amir"))
        self.click.setText(_translate("MainWindow", "Verify"))
        self.label1.setText(_translate("MainWindow", "Enter Your Code"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "About Me"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Programming Languages"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
