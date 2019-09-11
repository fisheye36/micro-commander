import threading
from abc import ABC, abstractmethod
from time import sleep

import logger


class AbstractWindowManager(threading.Thread, ABC):
    def __init__(self):
        super(AbstractWindowManager, self).__init__()
        self.daemon = True
        self._observers = []

    def notify_all(self):
        for observer in self._observers:
            observer.notify(self.get_active_program_name().lower())

    def register(self, obj):
        self._observers.append(obj)

    def run(self):
        while True:
            try:
                self.main()
            except:
                logger.exception("Window Manager thread crashed")
            else:
                logger.info("Window Manager thread exited")
            sleep(1)

    @abstractmethod
    def main(self):
        pass

    @abstractmethod
    def get_active_program_name(self):
        pass

