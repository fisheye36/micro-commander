"""
converter.py
---------
Module responsible for speech recognition.

Usage example:

.. code-block:: python

audio_converter = AudioConverter()
audio_converter.start()

while 1:
    response = audio_converter.get_response()
    if response:
        print(response)
"""


from recorder import Recorder
from response_queue import PriorityQueue
import speech_recognition


class AudioConverter:

    def __init__(self):
        self.response_queue = None
        self.recognizer = None
        self.recorder = None

    def start(self):
        """
        Starts recording on the separate thread (in background).
        """
        self.__setup_before_start()
        self.recognizer.pause_threshold = 0.51
        self.recorder.listen_in_background()

    def __setup_before_start(self):
        """
        Internal objects must be created before each restart.
        """
        self.response_queue = PriorityQueue()
        self.recognizer = speech_recognition.Recognizer()
        self.recorder = Recorder(self.recognizer, self.response_queue)

    def stop(self):
        """
        Turns off the microphone and stops sending requests.
        """
        self.__clean_up()

    def __clean_up(self):
        del self.response_queue
        del self.recognizer
        del self.recorder

    def get_response(self):
        """
        Returns single word from queue if it is possible.
        Otherwise an empty string.

        Important: This method may be invoked ONLY if the AudioConverter
        is active (between start() and stop()). Calling that on a passive
        object results in an exception!
        """
        return self.response_queue.pull()
