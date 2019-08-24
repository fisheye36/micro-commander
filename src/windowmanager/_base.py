from abc import ABC, abstractmethod


class AbstractWindowManager(ABC):
    def __init__(self):
        self._observers = []

    def notify_all(self):
        for observer in self._observers:
            observer.notify(self.get_active_program_name().lower())

    def subscribe(self, obj):
        self._observers.append(obj)

    @abstractmethod
    def get_active_program_name(self):
        pass

