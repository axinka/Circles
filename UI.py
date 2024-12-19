from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6 import QtCore


class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Circle Drawer')
        self.setGeometry(100, 100, 800, 600)

        self.button = QPushButton('Add Circles', self)
        self.button.setGeometry(QtCore.QRect(350, 250, 131, 41))
