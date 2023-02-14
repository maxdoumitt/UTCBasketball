#PyQt imports
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    #creates the application object (every application needs this)
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(550,550)
    w.move(300,300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())