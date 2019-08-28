from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMessageBox

from conf import settings
import sys

from gui.tray import TrayWindow
from windowmanager import WindowManager


class Application:
    APP_NAME = 'MicroCom'

    def __init__(self):
        self.wm = WindowManager()

    def start(self):
        settings.load_configuration()
        self.wm.subscribe(settings)
        self.wm.start()

        app = QApplication(sys.argv)

        if not QSystemTrayIcon.isSystemTrayAvailable():
            QMessageBox.critical(None, self.APP_NAME,
                                 "I couldn't detect any system tray on this system.")
            sys.exit(1)

        app.setQuitOnLastWindowClosed(False)

        window = TrayWindow()
        sys.exit(app.exec_())


if __name__ == "__main__":
    a = Application()
    a.start()
