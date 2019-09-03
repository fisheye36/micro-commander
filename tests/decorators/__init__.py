from conf import settings
from functools import wraps


def override_settings(new_settings, only_active=True):
    """
    This decorator should be used to initialize settings.

    :param new_settings: dict with configuration
    """
    if only_active:
        new_settings = {
            'app_mapping': {},
            'default': new_settings
        }

    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            settings.data = new_settings
            return func(*args, **kwargs)

        return wrapper

    return actual_decorator
