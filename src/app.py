import sys

from PyQt5.QtWidgets import QApplication, QMessageBox, QSystemTrayIcon

from conf import settings
from gui.tray import TrayWindow
from gui.main_window import MainWindow
from speech.audio_manager import AudioManager
from windowmanager import WindowManager


class Application:
    APP_NAME = 'MicroCom'

    def __init__(self):
        self.window_manager = WindowManager()
        self.state = {
            'muted': False,
            'connectivity': False
        }
        self.audio_manager = AudioManager(self.state)

    def start(self):
        settings.load_configuration()
        settings.set_window_manager(self.window_manager)

        self.window_manager.start()
        self.audio_manager.start()

        app = QApplication(sys.argv)
        main_window = MainWindow()

        if not QSystemTrayIcon.isSystemTrayAvailable():
            QMessageBox.critical(None, self.APP_NAME,
                                 "I couldn't detect any system tray on this system.")
            sys.exit(1)

        app.setQuitOnLastWindowClosed(False)

        window = TrayWindow(main_window)
        sys.exit(app.exec_())


if __name__ == "__main__":
    a = Application()
    a.start()
