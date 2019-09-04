import threading

from speech.converter import AudioConverter
from analyser import Analyser


class AudioManager(threading.Thread):

    def __init__(self):
        super().__init__()
        self.daemon = True
        self.audio_converter = AudioConverter()
        self.analyser = Analyser()

    def run(self):
        self.audio_converter.start()
        while 1:
            response = self.audio_converter.get_response()
            if response:
                print(self.analyser.analyse(response))
