"""
conf/__init__.py
-----------------
This package provides singleton instance of `Settings`.

It should be once initialized with start of the application with command:

.. code-block:: python

    from conf import settings
    settings.load_configuration()


After that it should be possible to use it like this:

.. code-block:: python

    from conf import settings
    print(settings['language'])
    settings['my_setting'] = 3

"""
from .settings import Settings

settings = Settings()

