import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from add_mapping_window import AddMapping


class EditMapping(QWidget):

    def __init__(self):
        super().__init__()

        qrect = QDesktopWidget().screenGeometry(-1)
        self.left = int(qrect.width()) / 4
        self.top = int(qrect.height()) / 4
        self.width = 640
        self.height = 360
        self.title = "Edit mappings"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(self.p)

        self.main_grid = QGridLayout()
        self.main_grid.setSpacing(20)

        self.table = QTableWidget()
        self.table.setRowCount(100)
        self.table.setColumnCount(2)
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table.resizeColumnsToContents()
        self.table.setHorizontalHeaderLabels("Commands;Mappings".split(";"))
        self.header = self.table.horizontalHeader()
        self.header.setSectionResizeMode(0, QHeaderView.Stretch)
        self.header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.main_grid.addWidget(self.table, 0, 0, 1, 3)

        self.add_new_b = QPushButton("Add new")
        self.add_new_b.clicked.connect(lambda: self.add_mapping_button())
        self.main_grid.addWidget(self.add_new_b, 1, 1, Qt.AlignCenter)

        self.cancel_b = QPushButton("Cancel")
        self.cancel_b.clicked.connect(lambda: self.close_window())
        self.main_grid.addWidget(self.cancel_b, 2, 0, Qt.AlignCenter)

        self.ok_b = QPushButton("Ok")
        self.ok_b.clicked.connect(lambda: self.close_window())
        self.main_grid.addWidget(self.ok_b, 2, 2, Qt.AlignCenter)

        self.setLayout(self.main_grid)
        self.show()

    def close_window(self):
        self.close()

    def add_mapping_button(self):
        self.add_mapping = AddMapping()


