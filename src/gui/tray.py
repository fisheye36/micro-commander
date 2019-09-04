#!/usr/bin/env python

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QMessageBox, QMenu, QSystemTrayIcon,
                             QDialog)

from gui.main_window import MainWindow
from gui.processed_text_window import ProcessedText
from utils import getResource


class TrayWindow(QDialog):
    def __init__(self, *args, **kwargs):
        super(TrayWindow, self).__init__(*args, **kwargs)

        self.createActions()
        self.createTrayIcon()

        self.trayIcon.show()

        self.settingsWindow = MainWindow()
        self.processedText = ProcessedText(self, *args, **kwargs)

    def createActions(self):
        self.windowsProccesing = QAction("Proccesed speech", self, triggered=self.showWindows)
        self.settingsAction = QAction("Settings", self, triggered=self.showSettings)
        self.quitAction = QAction("Quit", self, triggered=QApplication.instance().quit)

    def createTrayIcon(self):
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(self.windowsProccesing)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.settingsAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)

        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)

        self.trayIcon.activated.connect(self.iconActivated)

        icon = QIcon(getResource("speech.png"))
        self.trayIcon.setIcon(icon)
        self.setWindowIcon(icon)

        self.trayIcon.setToolTip("Sample tooltip")

    def iconActivated(self, reason):
        self.showNotification("Micro commander", "Status: running")

    def showSettings(self):
        self.settingsWindow.init_UI()

    def showWindows(self):
        self.processedText.open_window()

    def showNotification(self, title, body):
        icon = QSystemTrayIcon.MessageIcon(QSystemTrayIcon.Critical)
        self.trayIcon.showMessage(title, body, icon)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "Systray",
                             "I couldn't detect any system tray on this system.")
        sys.exit(1)

    app.setQuitOnLastWindowClosed(False)

    window = TrayWindow()
    sys.exit(app.exec_())
