import threading
from abc import ABC, abstractmethod


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

    @abstractmethod
    def get_active_program_name(self):
        pass

