import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from conf import settings
from .tray import TrayWindow


class AddModeWindow(QDialog):

    def __init__(self):
        QWidget.__init__(self, None, Qt.WindowStaysOnTopHint)
        self.init_UI()

    def init_UI(self):
        self.add_mode_window_preparation()
        self.textbox = QLineEdit()
        self.main_grid.addWidget(self.textbox, 0, 0, 1, 3)

        self.confirm_b = QPushButton("Confirm")
        self.confirm_b.clicked.connect(lambda: self.confirm_and_close_window())
        self.main_grid.addWidget(self.confirm_b, 1, 0, Qt.AlignCenter)

        self.cancel_b = QPushButton("Cancel")
        self.cancel_b.clicked.connect(lambda: self.close_window())
        self.main_grid.addWidget(self.cancel_b, 1, 2, Qt.AlignCenter)

        self.setWindowModality(Qt.ApplicationModal)
        self.setLayout(self.main_grid)

    def add_mode_window_preparation(self):
        qrect = QDesktopWidget().screenGeometry(-1)
        self.left = int(qrect.width()) / 2
        self.top = int(qrect.height()) / 2
        self.width = 200
        self.height = 100
        self.setWindowTitle("Add mode")
        self.main_grid = QGridLayout()
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), Qt.green)
        self.setPalette(self.p)
        self.main_grid.setSpacing(20)

    def confirm_and_close_window(self):
        if self.textbox.text() is not "":
            if self.textbox.text() not in settings:
                settings.update({self.textbox.text(): {'commands': []}})
                self.textbox.setText('')
            else:
                TrayWindow.showNotification("Error", "Podany klucz istnieje")
        self.close()

    def close_window(self):
        self.close()

