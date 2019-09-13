import os
import re
import threading

from google.cloud import speech_v1p1beta1 as speech

import logger
from analyser import Analyser
from input_simulator import FakeKeyboard
from logic.distributor import Distributor
from speech.microphone_stream import ResumableMicrophoneStream
from utils import get_current_time, getResource
from .microphone_settings import *


class AudioManager(threading.Thread):
    def __init__(self, state):
        super().__init__()
        self.analyser = Analyser(state)
        self.fake_keyboard = FakeKeyboard()
        self.distributor = Distributor(self.analyser, self.fake_keyboard)
        self.daemon = True
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = getResource('service-account-file.json')

        self.client = speech.SpeechClient()
        config = speech.types.RecognitionConfig(
            encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=SAMPLE_RATE,
            language_code=LANGUAGE_CODE,
            max_alternatives=1)
        self.streaming_config = speech.types.StreamingRecognitionConfig(
            config=config,
            interim_results=True)

        self.mic_manager = ResumableMicrophoneStream(SAMPLE_RATE, CHUNK_SIZE)
        logger.debug('Chunk size: {}'.format(self.mic_manager.chunk_size))
        logger.info('AudioManager initialized')

    def listen_print_loop(self, responses, stream):
        for response in responses:
            if get_current_time() - stream.start_time > STREAMING_LIMIT:
                stream.start_time = get_current_time()
                break

            if not response.results:
                continue

            result = response.results[0]

            if not result.alternatives:
                continue

            transcript = result.alternatives[0].transcript

            result_seconds = 0
            result_nanos = 0

            if result.result_end_time.seconds:
                result_seconds = result.result_end_time.seconds

            if result.result_end_time.nanos:
                result_nanos = result.result_end_time.nanos

            stream.result_end_time = int((result_seconds * 1000)
                                         + (result_nanos / 1000000))

            corrected_time = (stream.result_end_time - stream.bridging_offset
                              + (STREAMING_LIMIT * stream.restart_counter))
            # Display interim results, but with a carriage return at the end of the
            # line, so subsequent lines will overwrite them.

            if result.is_final:
                self.distributor.final(transcript, corrected_time)
                stream.is_final_end_time = stream.result_end_time
                stream.last_transcript_was_final = True
            else:
                self.distributor.interim(transcript, corrected_time)
                stream.last_transcript_was_final = False

    def run(self):
        """start bidirectional streaming from microphone input to speech API"""
        with self.mic_manager as stream:
            while not stream.closed:
                logger.info('[{}]: NEW REQUEST'.format(str(STREAMING_LIMIT * stream.restart_counter)))

                stream.audio_input = []
                audio_generator = stream.generator()

                requests = (speech.types.StreamingRecognizeRequest(
                    audio_content=content) for content in audio_generator)

                responses = self.client.streaming_recognize(self.streaming_config,
                                                            requests)

                # Now, put the transcription responses to use.
                self.listen_print_loop(responses, stream)

                if stream.result_end_time > 0:
                    stream.final_request_end_time = stream.is_final_end_time
                stream.result_end_time = 0
                stream.last_audio_input = []
                stream.last_audio_input = stream.audio_input
                stream.audio_input = []
                stream.restart_counter = stream.restart_counter + 1

                if not stream.last_transcript_was_final:
                    logger.info('\n')
                stream.new_stream = True
