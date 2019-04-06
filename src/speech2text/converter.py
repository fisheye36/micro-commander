import queue
import sys
import tempfile
from threading import Thread

import numpy
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr

assert numpy  # avoid "`numpy` imported but not used"


class AudioConverter:

    def __init__(self):
        self.is_active = True
        self.thread = None
        self.result = None
        self.sample_rate = None
        self.queue = queue.Queue()
        self.output_file = tempfile.mktemp(prefix='output', suffix='.wav', dir='')
        self.setup()

    def setup(self):
        sd.default.channels = 1
        sd.default.device = 1  # hardcoded mic on my pc
        device_info = sd.query_devices(device=1, kind='input')
        self.sample_rate = int(device_info['default_samplerate'])

    def callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.queue.put(indata.copy())

    def run_recording(self):
        with sf.SoundFile(self.output_file, mode='x', samplerate=self.sample_rate,
                          channels=1, subtype='PCM_24') as file:
            with sd.InputStream(samplerate=self.sample_rate, callback=self.callback):
                while self.is_active:
                    file.write(self.queue.get())

    def start_listener(self):
        self.thread = Thread(target=self.run_recording)
        self.thread.start()

    def stop_listener(self):
        self.is_active = False
        self.thread.join()
        recognizer = sr.Recognizer()
        harvard = sr.AudioFile(str(self.output_file))
        with harvard as source:
            audio = recognizer.record(source)
        self.result = recognizer.recognize_google(audio, language='pl-PL')


if __name__ == '__main__':
    audio_converter = AudioConverter()
    audio_converter.start_listener()
    input('Press any key to stop recording... ')
    audio_converter.stop_listener()
    print(audio_converter.result)
