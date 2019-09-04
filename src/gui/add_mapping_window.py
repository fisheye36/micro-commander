import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class AddMapping(QWidget):

    def __init__(self):
        super().__init__()

        qrect = QDesktopWidget().screenGeometry(-1)
        self.left = int(qrect.width()) / 4
        self.top = int(qrect.height()) / 4
        self.width = 640
        self.height = 360
        self.main_grid = QGridLayout()
        self.cancel_b = QPushButton("Cancel")
        self.confirm_b = QPushButton("Confirm")

    def init_UI(self):
        self.setWindowTitle("Add mapping")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(self.p)
        self.main_grid.setSpacing(20)

        self.main_grid.addWidget(QLabel("Command"), 0, 0)
        self.main_grid.addWidget(QPlainTextEdit(), 0, 1, 1, 2)
        self.main_grid.addWidget(QLabel("Mapping"), 1, 0)
        self.main_grid.addWidget(QPlainTextEdit(), 1, 1, 1, 2)

        self.cancel_b.clicked.connect(lambda: self.close_window())
        self.main_grid.addWidget(self.cancel_b, 2, 0, Qt.AlignCenter)

        self.confirm_b.clicked.connect(lambda: self.close_window())
        self.main_grid.addWidget(self.confirm_b, 2, 2, Qt.AlignCenter)

        self.setLayout(self.main_grid)
        self.show()

    def close_window(self):
        self.close()

