import threading
import time

import speech_recognition
import logger


class Recorder:

    def __init__(self, recognizer, queue):
        self.recognizer = recognizer
        self.microphone = speech_recognition.Microphone()
        self.indicator = 0
        self.queue = queue
        self.is_actually_run = None

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
        with self.microphone as mic:
            while self.is_actually_run[0]:
                try:
                    audio = self.recognizer.listen(self.microphone, timeout=timeout)
                except speech_recognition.WaitTimeoutError:
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
            text_output = self.recognizer.recognize_google(audio, language='pl-PL')
            self.queue.push(self.get_indicator(), text_output)
        except:
            logger.info(msg='Unable to transcript the sound data.')
        else:
            logger.info(msg="The recording has been converted successfully.")
