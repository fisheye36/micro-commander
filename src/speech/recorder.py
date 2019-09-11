import threading
import time

from speech_recognition import Microphone, RequestError, WaitTimeoutError, UnknownValueError

import logger
from utils import getResource


class Recorder:

    def __init__(self, recognizer, queue):
        self.recognizer = recognizer
        self.microphone = Microphone()
        self.indicator = 0
        self.queue = queue
        self.is_actually_run = None
        self.err_no_net = False
        self.service_json = None
        self.load_service_json()
        self.service_key = 'AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw'
        self.for_free = False

    def load_service_json(self):
        with open(getResource('service-account-file.json')) as f:
            self.service_json = f.read()

    def get_indicator(self):
        """
        Returns new id number for separate request.
        """
        self.indicator += 1
        return self.indicator

    def listen_in_background(self):
        """
        Adds a new thread responsible for sound input.
        """

        def stop_lister(wait_for_listener=True):
            """
            Waits until the recorder finishes work.
            """
            self.is_actually_run[0] = False
            if wait_for_listener:
                sound_input_thread.join()

        sound_input_thread = threading.Thread(target=self.threaded_listen)
        sound_input_thread.daemon = True
        sound_input_thread.start()
        return stop_lister

    def threaded_listen(self, timeout=1):
        """
        Starts to listen to user. When the beginning silence is longer
        than 'timeout' then that recording will be skipped and new
        recording will start again.
        """
        self.is_actually_run = [True]
        with self.microphone as _:
            while self.is_actually_run[0]:
                try:
                    audio = self.recognizer.listen(self.microphone, timeout=timeout)
                except WaitTimeoutError:
                    pass
                else:
                    if self.is_actually_run[0]:
                        logger.info("Recorder: New recording [{}]".format(
                            time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())))
                        self.callback(audio)

    def callback(self, audio):
        """
        Works in background. Sends a request containing sound data and pushes
        transcripted text into the queue.

        Requested audio can consist of noises only. In that case 'recognize_google'
        raises an exception. It is not an error so it should be logged as info.
        """
        try:
            if self.for_free:
                text_output = self.recognizer.recognize_google(audio, language='pl-PL', key=self.service_key)
            else:
                text_output = self.recognizer.recognize_google_cloud(audio, language='pl-PL',
                                                                     credentials_json=self.service_json)
            self.queue.push(self.get_indicator(), text_output)
        except RequestError:
            self.err_no_net = True
            logger.exception('ERR_NO_NET: Network connection lost.')
        except UnknownValueError:
            logger.info('Unable to transcript the sound data.')
        except:
            logger.exception('Unknown error')
        else:
            logger.info(msg="The recording has been converted successfully.")
