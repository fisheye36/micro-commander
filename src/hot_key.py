"""
hot_key.py
---------
Module responsible for setting a hot_key for recording voice.

Usage example:

.. code-block:: python

    hk = HotKey()
    hk.listen_hot_key()

"""
from pynput.keyboard import Listener
from conf.default_config import data
from conf.settings import Settings
import json
import logger


class HotKey:

    def __init__(self):
        self.hotKey = data['hotKey']

    def listen_hot_key(self):
        with Listener(on_release=self.set_hot_key) as listener:
            listener.join()

    def set_hot_key(self, key):
        self.hotKey = str(key)

        try:
            config_path = Settings._get_config_path()
            with open(config_path.as_posix(), "r") as f:
                config = json.load(f)

            config['hotKey'] = self.hotKey

            with open(config_path.as_posix(), "w") as f:
                json.dump(config, f)

        except IOError:
            logger.exception("Saving hot_key configuration failed")
        else:
            logger.info("Configuration of hot_key successfully updated.")

        return False

    def get_hot_key(self):
        return self.hotKey
