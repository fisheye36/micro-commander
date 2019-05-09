from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave

from conf.default_config import data


class Recorder:

    def __init__(self):
        self.format = pyaudio.paInt16

    def record(self):
        """
        Records a word or words from the microphone and
        returns the data as an array of signed shorts.
        Trims silence from the start and end.
        """
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16,
                            channels=data['channelsNumber'],
                            rate=data['sampleRate'],
                            input=True, output=True,
                            frames_per_buffer=data['chunkSize'])
        sample_width, recording = self.__record(stream, audio)
        stream.stop_stream()
        stream.close()
        audio.terminate()
        return sample_width, recording

    def __record(self, stream, audio):
        num_silent = 0
        snd_started = False
        recording = array('h')
        while True:
            snd_data = array('h', stream.read(data['chunkSize']))
            if byteorder == 'big':
                snd_data.byteswap()
            recording.extend(snd_data)
            silent = self.is_silent(snd_data)
            if silent and snd_started:
                num_silent += 1
            elif not silent and not snd_started:
                snd_started = True
            if snd_started and num_silent > data['minSilence']:
                break
        sample_width = audio.get_sample_size(self.format)
        recording = self.trim(recording)
        return sample_width, recording

    def record_to_file(self, path):
        """"Records from the microphone and outputs the resulting data to 'path'"""
        sample_width, sample_data = self.record()
        sample_data = pack('<' + ('h' * len(sample_data)), *sample_data)
        wf = wave.open(path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(sample_width)
        wf.setframerate(data['sampleRate'])
        wf.writeframes(sample_data)
        wf.close()

    @staticmethod
    def is_silent(data_segment):
        """
        Returns True if the 'data_segment' is below the minimum
        threshold, False otherwise. That segment is treated as
        noise.
        """
        return max(data_segment) < data['minThreshold']

    def trim(self, snd_data):
        """Trim the blank spots at the start and end"""
        # Trim to the left
        snd_data = self.__trim(snd_data)
        # Trim to the right
        snd_data.reverse()
        snd_data = self.__trim(snd_data)
        snd_data.reverse()
        return snd_data

    def __trim(self, sound_data):
        snd_started = False
        r = array('h')
        for i in sound_data:
            if not snd_started and abs(i) > data['minThreshold']:
                snd_started = True
                r.append(i)
            elif snd_started:
                r.append(i)
        return r
