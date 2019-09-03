import sys
from .custom_window import CustomWindow
from .edit_mapping_window import EditMapping
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils import getResource
from conf import settings


class MainWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.qrect = QDesktopWidget().screenGeometry(-1)
        self.left = int(self.qrect.width()) / 4
        self.top = int(self.qrect.height()) / 4
        self.width = 1000
        self.height = 360
        self.main_grid = QGridLayout()

        self.left_top_window = QVBoxLayout()
        self.combo_mode = QComboBox()
        self.add_custom_mode_b = QPushButton("Add custom mode")
        self.edit_mapping_b = QPushButton("Edit mode mappings")
        self.table_mappings = QTableWidget()

        self.logo = QLabel()

        self.console = QPlainTextEdit()

        self.window_custom = CustomWindow()
        self.edit_mapping = EditMapping()

        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Micro Commander")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(self.p)
        self.main_grid.setSpacing(10)

        self.left_top_corner()
        self.right_top_corner()

        self.setLayout(self.main_grid)
        self.show()

    def left_top_corner(self):
        for key in settings.keys():
            if "commands" in settings[key]:
                self.combo_mode.addItem(key)

        self.combo_mode.setContentsMargins(20, 20, 20, 20)
        self.left_top_window.addWidget(self.combo_mode)

        self.add_custom_mode_b.clicked.connect(lambda: self.add_custom_show_window())
        self.left_top_window.addWidget(self.add_custom_mode_b)

        self.edit_mapping_b.clicked.connect(lambda: self.edit_mapping_show_window())
        self.left_top_window.addWidget(self.edit_mapping_b)
        self.main_grid.addLayout(self.left_top_window, 0, 0, 1, 1)

        #TODO
        #qplaintext dla kazgego klucza z settings i ma byc parsowany na json


    def right_top_corner(self):
        self.logo.setMargin(10)
        self.logo.setPixmap(QPixmap(getResource('logomccopy.png')))
        self.main_grid.addWidget(self.logo, 0, 2, 1, 1)

    def edit_mapping_show_window(self):
        self.edit_mapping.init_UI()

    def add_custom_show_window(self):
        self.window_custom.init_UI()


