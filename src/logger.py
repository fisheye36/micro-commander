"""
logger.py
---------
Module responsible for configuring loggers for the application.

Usage example:

.. code-block:: python

    import logger
    logger.info("Example log")
    try:
        raise KeyError()
    except:
        logger.exception("Opening configuration failed")

"""

from logging import *

basicConfig(format='%(levelname)s: %(message)s', level=DEBUG)
