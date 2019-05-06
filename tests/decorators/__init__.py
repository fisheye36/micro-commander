from conf import settings as glob_settings
from functools import wraps


def settings(new_settings):
    """
    This decorator should be used to initialize settings.

    :param new_settings: dict with configuration
    """
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            glob_settings.data = new_settings
            return func(*args, **kwargs)

        return wrapper

    return actual_decorator
