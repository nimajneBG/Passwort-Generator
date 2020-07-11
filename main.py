from ui import *
import sys

class PW(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    
if __name__ == "__main__":
    programm = PW()
    programm.run()
