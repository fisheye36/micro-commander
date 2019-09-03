import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from .edit_mapping_window import EditMapping
from .add_mapping_window import AddMapping


class CustomWindow(QWidget):

    def __init__(self):
        super().__init__()

        qrect = QDesktopWidget().screenGeometry(-1)
        self.left = int(qrect.width()) / 4
        self.top = int(qrect.height()) / 4
        self.width = 640
        self.height = 360
        self.title = "Custom mode"

    def init_UI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(self.p)

        self.main_grid = QGridLayout()
        self.main_grid.setSpacing(10)

        self.main_grid.addWidget(QLabel("Mode name"), 0, 0)
        self.main_grid.addWidget(QPlainTextEdit(), 0, 1)

        self.main_grid.addWidget(QLabel("Executable"), 1, 0)
        self.main_grid.addWidget(QPlainTextEdit(), 1, 1)
        self.main_grid.addWidget(QToolButton(), 1, 2)

        self.main_grid.addWidget(QLabel("Commands to launch"), 2, 0, 1, 3)
        self.main_grid.addWidget(QPlainTextEdit(), 3, 0, 1, 3)

        self.edit_mapping_b = QPushButton("Edit mappings")
        self.edit_mapping_b.clicked.connect(lambda: self.edit_mapping_window_button())
        self.main_grid.addWidget(self.edit_mapping_b, 4, 1, Qt.AlignCenter)

        self.cancel_b = QPushButton("Cancel")
        self. cancel_b.clicked.connect(lambda: self.close_window())
        self.main_grid.addWidget(self.cancel_b, 5, 0)

        self.add_b = QPushButton("Add")
        self.add_b.clicked.connect(lambda: self.add_mapping_window_button())
        self. main_grid.addWidget(self.add_b, 5, 2)

        self.setLayout(self.main_grid)
        self.show()

    def add_mapping_window_button(self):
        self.add_mapping_window = AddMapping()

    def edit_mapping_window_button(self):
        self.edit_mapping_window = EditMapping()

    def close_window(self):
        self.close()




