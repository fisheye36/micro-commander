"""
listener_interface.py
----------
Module responsible for sending logs to GUI and bridge between recording module / analyser

Usage example:

.. code-block:: python

    listener_interface  = ListenerInterface()

"""

import logger


class ListenerInterface:

    def __init__(self):
        pass

    def log_raw_input(self, string):
        logger.info("Sent raw input to GUI")
        # Send to GUI

    def log_performed_actions(self, string):
        logger.info("Sent performed actions to GUI")
        # Send to GUI

    def bridge_data(self, data_string):
        self.log_raw_input(data_string)
        # analyser.analize(data_string)
