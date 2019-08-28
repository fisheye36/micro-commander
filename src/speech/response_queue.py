"""
response_queue.py
---------
Module responsible for responses queuing.

It may happen that we will get a response for a later request
earlier than the request sent directly after it.

The Queue is waiting for the earliest request and prevents
pulling later responses.

Each request has its own unique number. Smaller number has
a higher priority.
"""

from typing import Dict, List


class PriorityQueue(Dict[int, List[str]]):
    """
    Represents a priority queue.
    """
    def __init__(self):
        """
        indicator - actual request that queue is waiting for.
        """
        super().__init__({})
        self.indicator: int = 1

    def push(self, request_number: int, response: str):
        """
        Inserts response (trans-scripted text) into queue. 'response'
        must be an instance of str.
        """
        self.__push(request_number, response)

    def __push(self, request_number: int, response: str):
        """
        Splits sentence by words separated by whitespaces an insets
        them into the queue.

        Important: First word of the sentence should be pushed into
        a queue at the beginning.
        """
        words = response.split()
        self[request_number] = words

    def pull(self) -> str:
        """
        Returns one word from queue if is not empty, empty str otherwise.
        """
        return self.__get_word()

    def __get_word(self) -> str:
        """
        Returns single word or empty string when we are still
        waiting for the response.
        """
        if self.indicator in self:
            if self[self.indicator]:
                word = self[self.indicator][0]
                del self[self.indicator][0]
                return word
            else:
                self.indicator += 1
                return self.__get_word()
        return ''
