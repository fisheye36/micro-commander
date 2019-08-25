"""
hot_key.py
----------
Module responsible for setting a hot_key for recording voice.


Usage example:

.. code-block:: python

    hk = HotKey()
    hk.listen_hot_key()

"""

from pynput.keyboard import Listener
from conf import settings
import logger


class HotKey:

    def __init__(self):
        self.hotKey = settings['hotKey']

    def listen_hot_key(self):
        with Listener(on_release=self.set_hot_key) as listener:
            listener.join()

    def set_hot_key(self, key):
        self.hotKey = str(key)
        settings['hotKey'] = self.hotKey
        logger.info("Configuration of hot_key successfully updated.")
        return False

    def get_hot_key(self):
        return self.hotKey

hk = HotKey()