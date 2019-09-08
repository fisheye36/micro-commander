import json

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from conf import settings
from gui.add_mode_window import AddModeWindow
from utils import getResource


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.init_UI()
        self.add_mode_window = AddModeWindow()

    def init_UI(self):
        self.main_window_preparation()
        self.logo = QLabel()

        self.top_side()
        self.middle_side()
        self.bottom_side()

        self.setLayout(self.main_grid)

    def main_window_preparation(self):
        self.qrect = QDesktopWidget().screenGeometry(-1)
        self.main_grid = QGridLayout()
        self.left = int(self.qrect.width()) / 4
        self.top = int(self.qrect.height()) / 4
        self.width = 500
        self.height = 360
        self.setWindowTitle("Micro Commander")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), Qt.green)
        self.setPalette(self.p)
        self.main_grid.setSpacing(10)

    def top_side(self):
        self.logo.setMargin(10)
        self.logo.setPixmap(QPixmap(getResource('logomccopy.png')))
        self.main_grid.addWidget(self.logo, 0, 0, 1, 3, Qt.AlignCenter)

    def middle_side(self):
        self.menu = QHBoxLayout()

        self.combo_mode = QComboBox()
        for key in settings.keys():
            if "commands" in settings[key]:
                self.combo_mode.addItem(key)
        self.combo_mode.setContentsMargins(20, 20, 20, 20)
        self.combo_mode.currentIndexChanged.connect(lambda: self.current_mode_in_console())
        self.menu.addWidget(self.combo_mode)

        self.add_mode_b = QPushButton("Add mode")
        self.add_mode_b.clicked.connect(lambda: self.add_mode_show_window())
        self.menu.addWidget(self.add_mode_b)

        self.remove_mode_b = QPushButton("Remove mode")
        self.remove_mode_b.clicked.connect(lambda: self.remove_window())
        self.menu.addWidget(self.remove_mode_b)

        self.main_grid.addLayout(self.menu, 1, 0, 1, 3)

    def bottom_side(self):
        self.console = QPlainTextEdit()
        self.console.insertPlainText(str(settings[self.combo_mode.currentText()]))
        self.console.textChanged.connect(lambda: self.add_buttons_to_console())
        self.main_grid.addWidget(self.console, 2, 0, 1, 3)

        self.save_b = QPushButton("Save")
        self.save_b.setVisible(False)
        self.save_b.clicked.connect(lambda: self.validation_settings())
        self.main_grid.addWidget(self.save_b, 3, 0)

        self.cancel_b = QPushButton("Cancel")
        self.cancel_b.setVisible(False)
        self.cancel_b.clicked.connect(lambda: self.return_to_last_settings())
        self.main_grid.addWidget(self.cancel_b, 3, 2)

    def current_mode_in_console(self):
        self.console.clear()
        if self.combo_mode.currentText() is None or self.combo_mode.currentText() is '':
            self.console.insertPlainText("{'commands': []}")
        else:
            self.console.insertPlainText(str(settings[self.combo_mode.currentText()]))

    def add_buttons_to_console(self):
        self.save_b.setVisible(True)
        self.cancel_b.setVisible(True)

    def validation_settings(self):
        try:
            json.loads(self.console.toPlainText().replace("'", "\""))
            settings[self.combo_mode.currentText()] = self.console.toPlainText()
        except ValueError:
            #TODO notification error
            print("blad")
        else:
            self.save_b.setVisible(False)
            self.cancel_b.setVisible(False)

    def return_to_last_settings(self):
        self.console.clear()
        self.console.insertPlainText(str(settings[self.combo_mode.currentText()]))
        self.save_b.setVisible(False)
        self.cancel_b.setVisible(False)

    def add_mode_show_window(self):
        self.add_mode_window.show()
        self.add_mode_window.exec_()
        self.refresh()

    def remove_window(self):
        buttonReply = QMessageBox.question(self, 'Confirm',
                                           "Do you really want to remove mode named " + self.combo_mode.currentText() + "?",
                                           QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            settings.pop(self.combo_mode.currentText())
            self.refresh()

    def refresh(self):
        self.combo_mode.clear()
        for key in settings.keys():
            if "commands" in settings[key]:
                self.combo_mode.addItem(key)
