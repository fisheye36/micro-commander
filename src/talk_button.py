"""
talk_button.py
---------
Module responsible for push-to-talk feature.

Usage example:

.. code-block:: python

    talk_button = TalkButton()
    talk_button.start()

"""

from pynput.keyboard import Listener
from hot_key import HotKey
import logger


class TalkButton(HotKey):

    def start(self):
        """5
        Starts recording on the separate thread.
        """
        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

    def on_press(self, key):
        if str(key) == self.hotKey:
            logger.info("Recording button is being pressed...")

    def on_release(self, key):
        if str(key) == self.hotKey:
            logger.info("Recording button released.")

