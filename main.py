from ui import *
import sys
import random
from PyQt5.Qt import QApplication

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

    def randomPasswort(self):
        for i in range(self.LAENGE):
            self.passwort += random.choice(self.LISTE)
    
    def generate(self):
        self.passwort = ''
        self.LAENGE = self.sliderLaenge.value()

        if self.createList():
            self.randomPasswort()
            self.pwOutput.setText(self.passwort)
            

    def copyPW(self):
        QApplication.clipboard().setText(self.passwort)

    def displaySliderValue(self):
        self.labelAnzeigeLaenge.setText(str(self.sliderLaenge.value()))

    def info(self):
        TEXT = '''<b>Passwort Generator</b> <br>
        &copy; 2020 by Benjamin Grau <br> <br>
        Ein einfaches in Python geschriebenes Programm mit GUI zum generieren von zufälligen Passwörtern. <br>
        <a href="https://greygit.de/benjamin/Passwort-Generator">Code</a>
        '''
        popup = QtWidgets.QMessageBox(self.MainWindow)
        popup.setWindowTitle('Passwort Generator Info')
        popup.setText(TEXT)
        popup.setIcon(QtWidgets.QMessageBox.Information)
        # Schriftgröße
        font = QtGui.QFont()
        font.setPointSize(12)
        popup.setFont(font)
        popup.exec_()

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
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.connect()
        self.generate()
        self.MainWindow.show()
        sys.exit(app.exec_())



if __name__ == "__main__":
    programm = PW()
    programm.run()
