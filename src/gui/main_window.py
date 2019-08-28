import sys
from .custom_window import CustomWindow
from .edit_mapping_window import EditMapping
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

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

        self.right_bottom_top_window = QVBoxLayout()
        self.radio_mute = QRadioButton("Mute")
        self.threshold_voice = QSlider(Qt.Horizontal, self)

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
        self.left_bottom_corner()
        self.right_bottom_corner()

        self.setLayout(self.main_grid)
        self.show()

    def left_top_corner(self):
        self.left_top_window.addWidget(QLabel("Current mode"))

        self.combo_mode.addItem("Terminal")
        self.combo_mode.addItem("Vim")
        self.combo_mode.addItem("Office")
        self.combo_mode.setContentsMargins(20, 20, 20, 20)
        self.left_top_window.addWidget(self.combo_mode)

        self.add_custom_mode_b.clicked.connect(lambda: self.add_custom_show_window())
        self.left_top_window.addWidget(self.add_custom_mode_b)

        self.edit_mapping_b.clicked.connect(lambda: self.edit_mapping_show_window())
        self.left_top_window.addWidget(self.edit_mapping_b)
        self.main_grid.addLayout(self.left_top_window, 0, 0, 1, 1)

        self.table_mappings.setRowCount(100)
        self.table_mappings.setColumnCount(2)
        self.table_mappings.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_mappings.resizeColumnsToContents()
        self.table_mappings.setHorizontalHeaderLabels("Commands;Mappings".split(";"))
        self.table_mappings.setMinimumSize(300, 200)
        self.header = self.table_mappings.horizontalHeader()
        self.header.setSectionResizeMode(0, QHeaderView.Stretch)
        self.header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.fill_table(self.combo_mode.itemData(self.combo_mode.currentIndex()))

        self.main_grid.addWidget(self.table_mappings, 0, 1, 1, 1)

    def right_top_corner(self):
        self.logo.setMargin(10)
        self.logo.setPixmap(QPixmap('logomccopy.png'))
        self.main_grid.addWidget(self.logo, 0, 2, 1, 1)

    def left_bottom_corner(self):
        self.console.setReadOnly(True)
        self.main_grid.addWidget(self.console, 1, 0, 1, 2)

    def right_bottom_corner(self):
        self.right_bottom_top_window.addWidget(QLabel("Get help about program?"))
        self.right_bottom_top_window.addWidget(self.radio_mute)
        self.right_bottom_top_window.addWidget(QLabel("Microphone threshold"))
        self.main_grid.addLayout(self.right_bottom_top_window, 1, 2, 1, 1)

        self.threshold_voice.actionEvent(self.change_threshold_voice())
        self.threshold_voice.setMinimum(0)
        self.threshold_voice.setMaximum(100)
        self.main_grid.addWidget(self.threshold_voice, 2, 2, 1, 1)

    def fill_table(self, mode):
        pass
    def mute_voice(self):
        pass
    def change_threshold_voice(self):
        pass
    def edit_mapping_show_window(self):
        self.edit_mapping.init_UI(self.combo_mode.itemData(self.combo_mode.currentIndex()))

    def add_custom_show_window(self):
        self.window_custom.init_UI(self.combo_mode.itemData(self.combo_mode.currentIndex()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
