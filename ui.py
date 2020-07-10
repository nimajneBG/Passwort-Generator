# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pw.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(418, 450)
        MainWindow.setMinimumSize(QtCore.QSize(418, 450))
        MainWindow.setMaximumSize(QtCore.QSize(418, 450))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 110, 401, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkGrossbuchstaben = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkGrossbuchstaben.setChecked(True)
        self.checkGrossbuchstaben.setObjectName("checkGrossbuchstaben")
        self.verticalLayout.addWidget(self.checkGrossbuchstaben)
        self.checkKleinbuchstaben = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkKleinbuchstaben.setChecked(True)
        self.checkKleinbuchstaben.setObjectName("checkKleinbuchstaben")
        self.verticalLayout.addWidget(self.checkKleinbuchstaben)
        self.checkSonderzeichen = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkSonderzeichen.setChecked(True)
        self.checkSonderzeichen.setObjectName("checkSonderzeichen")
        self.verticalLayout.addWidget(self.checkSonderzeichen)
        self.checkZahlen = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkZahlen.setChecked(True)
        self.checkZahlen.setObjectName("checkZahlen")
        self.verticalLayout.addWidget(self.checkZahlen)
        self.checkUmlaute = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkUmlaute.setObjectName("checkUmlaute")
        self.verticalLayout.addWidget(self.checkUmlaute)
        self.btnCopy = QtWidgets.QPushButton(self.centralwidget)
        self.btnCopy.setGeometry(QtCore.QRect(328, 320, 81, 30))
        self.btnCopy.setObjectName("btnCopy")
        self.labelZeichen = QtWidgets.QLabel(self.centralwidget)
        self.labelZeichen.setGeometry(QtCore.QRect(10, 80, 201, 16))
        self.labelZeichen.setObjectName("labelZeichen")
        self.sliderLaenge = QtWidgets.QSlider(self.centralwidget)
        self.sliderLaenge.setGeometry(QtCore.QRect(10, 40, 361, 20))
        self.sliderLaenge.setMinimum(4)
        self.sliderLaenge.setMaximum(25)
        self.sliderLaenge.setSliderPosition(8)
        self.sliderLaenge.setOrientation(QtCore.Qt.Horizontal)
        self.sliderLaenge.setObjectName("sliderLaenge")
        self.labelLaenge = QtWidgets.QLabel(self.centralwidget)
        self.labelLaenge.setGeometry(QtCore.QRect(10, 10, 57, 21))
        self.labelLaenge.setObjectName("labelLaenge")
        self.labelAnzeigeLaenge = QtWidgets.QLabel(self.centralwidget)
        self.labelAnzeigeLaenge.setGeometry(QtCore.QRect(380, 40, 41, 21))
        self.labelAnzeigeLaenge.setObjectName("labelAnzeigeLaenge")
        self.pwOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.pwOutput.setGeometry(QtCore.QRect(10, 320, 311, 30))
        self.pwOutput.setObjectName("pwOutput")
        self.btnGenerieren = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerieren.setGeometry(QtCore.QRect(10, 360, 401, 30))
        self.btnGenerieren.setObjectName("btnGenerieren")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 418, 31))
        self.menubar.setObjectName("menubar")
        self.menuGenerator = QtWidgets.QMenu(self.menubar)
        self.menuGenerator.setObjectName("menuGenerator")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGenerate = QtWidgets.QAction(MainWindow)
        self.actionGenerate.setObjectName("actionGenerate")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.actionBeenden = QtWidgets.QAction(MainWindow)
        self.actionBeenden.setObjectName("actionBeenden")
        self.menuGenerator.addAction(self.actionGenerate)
        self.menuGenerator.addSeparator()
        self.menuGenerator.addAction(self.actionInfo)
        self.menuGenerator.addAction(self.actionBeenden)
        self.menubar.addAction(self.menuGenerator.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Passwort Generator"))
        self.checkGrossbuchstaben.setText(_translate("MainWindow", "Großbuchstaben"))
        self.checkKleinbuchstaben.setText(_translate("MainWindow", "Kleinbuchstaben"))
        self.checkSonderzeichen.setText(_translate("MainWindow", "Sonderzeichen"))
        self.checkZahlen.setText(_translate("MainWindow", "Zahlen"))
        self.checkUmlaute.setText(_translate("MainWindow", "Umlaute"))
        self.btnCopy.setText(_translate("MainWindow", "Kopieren"))
        self.labelZeichen.setText(_translate("MainWindow", "Enthaltene Zeichen"))
        self.labelLaenge.setText(_translate("MainWindow", "Länge"))
        self.labelAnzeigeLaenge.setText(_translate("MainWindow", "8"))
        self.btnGenerieren.setText(_translate("MainWindow", "Neu Generieren"))
        self.menuGenerator.setTitle(_translate("MainWindow", "Generator"))
        self.actionGenerate.setText(_translate("MainWindow", "Generate"))
        self.actionGenerate.setShortcut(_translate("MainWindow", "Ctrl+Return"))
        self.actionQuit.setText(_translate("MainWindow", "Beenden"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionBeenden.setText(_translate("MainWindow", "Beenden"))
        self.actionBeenden.setShortcut(_translate("MainWindow", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
