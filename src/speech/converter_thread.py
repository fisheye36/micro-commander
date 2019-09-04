import threading

from key_input.input_simulator import FakeKeyboard
from speech.converter import AudioConverter
from analyser import Analyser


class AudioManager(threading.Thread):

    def __init__(self):
        super().__init__()
        self.daemon = True
        self.audio_converter = AudioConverter()
        self.analyser = Analyser()
        self.fake_keyboard = FakeKeyboard()

    def run(self):
        self.audio_converter.start()
        responses = []
        while 1:
            response_word = self.audio_converter.get_response()
            if response_word:
                responses.append(response_word)
            if len(responses) >= 3:
                analyzed_keys = self.analyser.analyse(' '.join(responses))
                print(analyzed_keys)
                self.fake_keyboard.simulate(analyzed_keys)
                responses.clear()
