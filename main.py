from ui import *
import sys
import random

class PW(Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Variablen
        self.ZEICHEN = {
            'Grossbuchstaben' : 'QWERTZUIOPASDFGHJKLYXCVBNM',
            'Kleinbuchstaben' : 'qwertzuiopasdfghjklyxcvbnm',
            'Zahlen' : '0123456789',
            'Sonderzeichen' : '^°!"§$%&/()=?`´*-_.:,;<>|@€²³{[]}#+~',
            'Umlaute' : 'üäöÜÄÖß'
        }

    def errorOut(self, errorMessage: str):
        print(errorMessage)

    def createList(self):
        self.LISTE = ''

        if self.checkGrossbuchstaben.isChecked() or self.checkKleinbuchstaben.isChecked() or self.checkUmlaute.isChecked() or self.checkZahlen.isChecked() or self.checkSonderzeichen.isChecked():
            if self.checkGrossbuchstaben.isChecked():
                self.LISTE += self.ZEICHEN.get('Grossbuchstaben')

            if self.checkKleinbuchstaben.isChecked():
                self.LISTE += self.ZEICHEN.get('Kleinbuchstaben')

            if self.checkUmlaute.isChecked():
                self.LISTE += self.ZEICHEN.get('Umlaute')

            if self.checkZahlen.isChecked():
                self.LISTE += self.ZEICHEN.get('Zahlen')

            if self.checkSonderzeichen.isChecked():
                self.LISTE += self.ZEICHEN.get('Sonderzeichen')

            return True
        
        else:
            self.errorOut('Keine Zeichengruppe ausgewählt')
            return False
    
    def generate(self):
        if self.createList():
            print(self.LISTE)

    def copyPW(self):
        print('Passwort kopieren')

    def displaySliderValue(self):
        self.labelAnzeigeLaenge.setText(str(self.sliderLaenge.value()))

    def info(self):
        pass

    # Signale usw. verbinden
    def connect(self):
        # Buttons
        self.btnGenerieren.clicked.connect(self.generate)
        self.btnCopy.clicked.connect(self.copyPW)

        # Slider
        self.sliderLaenge.valueChanged.connect(self.displaySliderValue)

        # Actions
        self.actionBeenden.triggered.connect(QtCore.QCoreApplication.instance().quit)
        self.actionGenerate.triggered.connect(self.generate)
        self.actionInfo.triggered.connect(self.info)

    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.setupUi(MainWindow)
        self.connect()
        self.generate()
        MainWindow.show()
        sys.exit(app.exec_())



if __name__ == "__main__":
    programm = PW()
    programm.run()
