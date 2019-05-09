"""
converter.py
---------
Module responsible for speech recognition.

Usage example:

.. code-block:: python

    audio_converter = AudioConverter()
    audio_converter.start()

    while True:
        response = audio_converter.get_response()
        if response:
            print(response, end=' ')

"""

import os
from threading import Thread

from network_agent import NetworkAgent
from recorder import Recorder
from response_queue import PriorityQueue


class AudioConverter:

    def __init__(self):
        self.threads = []
        self.is_active = False
        self.agent = NetworkAgent()
        self.response_queue = PriorityQueue()
        self.recorder = Recorder()
        self.path_prefix = 'temp_wav_file_'
        self.file_indicator = 0

    def start_listener(self):
        """
        Creates new file path and adds new listener.
        """
        while True:
            if not self.is_active:
                self.is_active = True
                new_file = "{}{}.wav".format(self.path_prefix, self.file_indicator)
                self.file_indicator += 1
                self._add_new_listener(new_file)

    def _add_new_listener(self, file):
        self.threads.append(Thread(target=self.run_recording, args=[file]))
        self.threads[-1].start()

    def start(self):
        """
        Starts recording on the separate thread.
        """
        thread = Thread(target=self.start_listener)
        thread.start()

    def run_recording(self, file):
        """
        Records sound using device microphone. Sound is recorded to open file. When any
        file is not open (time between writing the current file and creating next one)
        sound will be buffered. When an silence is detected, file will be closed an
        prepared to send.
        """
        self.recorder.record_to_file(path=file)
        self.is_active = False
        self.response_queue.push(*self.agent.request(file))
        os.remove(file)

    def stop_listener(self):
        """
        Waits for end of each thread execution.
        """
        for thread in self.threads:
            thread.join()

    def get_response(self):
        """
        Returns single word from queue if it is possible.
        Otherwise an empty string.
        """
        return self.response_queue.pull()
