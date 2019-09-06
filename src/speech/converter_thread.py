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
        while True:
            if not self.audio_converter.response_queue.is_response_available():
                continue
            response_word = self.audio_converter.get_response()
            responses.extend(response_word)
            if len(responses) >= 3:  # TODO we can't depend on it!
                analyzed_keys = self.analyser.analyse(' '.join(responses))
                print(analyzed_keys)
                self.fake_keyboard.simulate(analyzed_keys)
                responses.clear()
