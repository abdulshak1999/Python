import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("SpinBox")
        self.setGeometry(50, 50, 500, 300)
        layout = QHBoxLayout()
        self.setLayout(layout)
        spin = QSpinBox()
        spin.setRange(18, 35)
        spin.setValue(21)
        spin.setPrefix("age: ")
        layout.addWidget(spin)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
