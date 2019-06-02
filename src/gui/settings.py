import sys
from custom_window import CustomWindow
from edit_mapping_window import EditMapping
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class SettingsWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.title = "Micro Commander"
        self.qrect = QDesktopWidget().screenGeometry(-1)
        self.left = int(self.qrect.width()) / 4
        self.top = int(self.qrect.height()) / 4
        self.width = 1000
        self.height = 360
        self.window_custom = CustomWindow()
        self.edit_mapping = EditMapping()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(self.p)

        self.main_grid = QGridLayout()
        self.main_grid.setSpacing(10)

        self.main_grid.addWidget(QLabel("Current mode"), 1, 2, 1, 2, Qt.AlignCenter)

        self.combo = QComboBox()
        self.combo.addItem("Terminal mode")
        self.combo.addItem("Vim mode")
        self.combo.addItem("Office mode")
        self.combo.setContentsMargins(20, 20, 20, 20)
        self.main_grid.addWidget(self.combo, 2, 2, 1, 2)

        self.add_custom_mode_b = QPushButton("Add custom mode")
        self.add_custom_mode_b.clicked.connect(lambda: self.add_custom_button())
        self.main_grid.addWidget(self.add_custom_mode_b, 3, 2, 1, 2)

        self.edit_mapping_b = QPushButton("Edit mode mappings")
        self.edit_mapping_b.clicked.connect(lambda: self.edit_mapping_button())
        self.main_grid.addWidget(self.edit_mapping_b, 4, 2, 1, 2)

        self.table = QTableWidget()
        self.table.setRowCount(100)
        self.table.setColumnCount(2)
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table.resizeColumnsToContents()
        self.table.setHorizontalHeaderLabels("Commands;Mappings".split(";"))
        self.table.setMinimumSize(200, 200)
        self.header = self.table.horizontalHeader()
        self.header.setSectionResizeMode(0, QHeaderView.Stretch)
        self.header.setSectionResizeMode(1, QHeaderView.Stretch)

        self.main_grid.addWidget(self.table, 1, 5, 5, 7)

        self.logo = QLabel()
        self.logo.setMargin(10)
        self.logo.setPixmap(QPixmap('logomccopy.png'))
        self.main_grid.addWidget(self.logo, 1, 12, 4, 4)

        self.console = QPlainTextEdit()
        self.console.insertPlainText("awwww")

        self.main_grid.addWidget(QScrollBar(), 6, 2, 5, 1)
        self.main_grid.addWidget(self.console, 6, 3, 5, 9)
        self.main_grid.addWidget(QLabel("Get help about program?"), 6, 12, 1, 3)
        self.main_grid.addWidget(QRadioButton("Mute"), 7, 13)
        self.main_grid.addWidget(QLabel("Microphone threshold"), 9, 13)
        self.main_grid.addWidget(QSlider(Qt.Horizontal), 10, 12, 1, 5)

        self.setLayout(self.main_grid)

        self.show()

    def edit_mapping_button(self):
        self.edit_mapping.initUI()

    def add_custom_button(self):
        self.window_custom.initUI()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SettingsWindow()
    sys.exit(app.exec_())
