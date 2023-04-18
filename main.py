import sys
from PyQt5.QtWidgets import QApplication
from controller import Controller

def main():
    app = QApplication([])
    window = Controller()
    window.setWindowTitle('Test10')
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
