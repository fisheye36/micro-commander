"""
network_agent.py
---------
The module is responsible for Google communication.
"""

import socket

import speech_recognition

import logger


class NetworkAgent:

    request_number: int = 0

    def __init__(self):
        self.__check_network_connection()
        self.recognizer = speech_recognition.Recognizer()

    @staticmethod
    def get_request_number() -> int:
        """
        Calculates and returns a new request number.
        """
        NetworkAgent.request_number += 1
        return NetworkAgent.request_number

    @staticmethod
    def __check_network_connection() -> None:
        """
        Tries to connect with google host.

        Rises an exception if we are not able to connect to network.
        """
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            soc.connect(('google.com', 80))
            soc.send(b'GET / HTTP/1.1\n\n')
            soc.recv(10)
            soc.close()
        except socket.error as e:
            raise ConnectionError('Cannot connect to the network. '
                                  'Check your connection.') from e

    def request(self, buffer):
        """
        Sends a request with audio file to a Google. Each request is handled
        on the another thread. It is important because while waiting for one
        response, we can send another requests.
        """
        req_number = NetworkAgent.get_request_number()
        return req_number, self.__request(buffer)

    def __request(self, buffer) -> str:
        """
        Returns received string or empty string when recognition failed.
        This method must work at the another process because it can last
        a long period of time. Duration depends on the network speed.
        """
        try:
            harvard = speech_recognition.AudioFile(buffer)
            with harvard as source:
                audio = self.recognizer.record(source)
            res = self.recognizer.recognize_google(audio, language='pl-PL')
            return res
        except speech_recognition.UnknownValueError as e:
            logger.info(e)
        except Exception as e:
            logger.info('exception: ', e)
        return ''
