import socket
import threading
import time

import logger
from analyser import Analyser
from key_input.input_simulator import FakeKeyboard
from speech.converter import AudioConverter


class AudioManager(threading.Thread):

    def __init__(self, state):
        super().__init__()
        self.daemon = True
        self.audio_converter = None
        self.analyser = Analyser(state)
        self.fake_keyboard = FakeKeyboard()
        self.responses = None
        
    def set_up(self):
        self.audio_converter = AudioConverter()
        self.audio_converter.start()
        self.responses = []

    def run(self):
        self.set_up()
        while True:
            if self.audio_converter.recorder.err_no_net:
                # hold this loop until connected
                self.try_connect_to_network(probe_period=3)
                self.set_up()

            if not self.audio_converter.response_queue.is_response_available():
                # no more resources to analyse
                continue

            response_sentence = self.audio_converter.get_response()
            self.responses.extend(response_sentence)
            
            analyzed_keys = self.analyser.analyse(' '.join(self.responses))
            self.fake_keyboard.simulate(analyzed_keys)
            self.responses.clear()

    @staticmethod
    def try_connect_to_network(probe_period):
        """Check connection every `probe_period` seconds."""
        # TODO display notification connection lost
        while True:
            # Execution of the main loop does not make a sense when
            # we can't connect to the internet. Stay in this loop
            # until the connection is established.
            try:
                socket.setdefaulttimeout(3)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
                logger.info("Connection probe succeeded: Back to online")
                # TODO display notification connection back
                return
            except socket.error:
                logger.info("Connection probe failed: No internet")
                time.sleep(probe_period)
