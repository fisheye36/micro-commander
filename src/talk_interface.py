"""
talk_interface.py
--------------
Module responsible for enabling/disabling recording feature.
recording_mode: push_to_talk / toggle

Usage example:

.. code-block:: python

    talk_button = TalkButton()
    talk_button.start()

"""

from pynput.keyboard import Listener
from hot_key import hk
from conf import settings
import logger


class TalkInterface():

    def __init__(self):
        self.hot_key = hk.get_hot_key()
        self.is_toggled = False

    def start(self):
        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

    def on_press(self, key):
        if str(key) == self.hot_key:
            if settings['recording_mode'] == 'toggle':
                if self.is_toggled:
                    self.is_toggled = False
                    logger.info("Toggle off")
                    # Stop recording voice
                    return False
                self.is_toggled = True
                logger.info("Toggle on!")
                # Start recording voice
            else:
                logger.info("Recording button is being pressed...")
                # Start recording voice

    def on_release(self, key):
        if str(key) == self.hot_key and settings['recording_mode'] == 'push_to_talk':
            logger.info("Recording button released.")
            # Stop recording voice
            return False


talk_interface = TalkInterface()
talk_interface.start()
