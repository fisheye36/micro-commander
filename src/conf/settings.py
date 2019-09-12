import copy
import pickle
from collections import UserDict
from pathlib import Path

import logger
from conf import default_config
from gui.tray import TrayWindow


class Settings(UserDict):
    """
    This class is responsible for loading and storing the configuration of the application.
    """
    REL_CONFIG_PATH = '.config/micro-commander/config'

    def __init__(self, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)
        self._active_mode = 'default'

    def load_configuration(self):
        config_path = self._get_config_path().as_posix()
        logger.info("Loading configuration from {}".format(config_path))
        try:
            with open(config_path, 'rb') as f:
                self.data = pickle.load(f)
        except FileNotFoundError:
            logger.warning("Configuration file not found.")
            self._load_default_configuration()
        except IOError:
            logger.exception("Opening configuration failed")
            self._load_default_configuration()
        else:
            logger.info("Configuration loaded successfully from the file.")
        logger.debug("Loaded config: {}".format(self.data))

    def _load_default_configuration(self):
        logger.info("Loading default configuration")
        self.data = default_config.data

    def save_configuration(self):
        try:
            config_path = self._get_config_path()
            config_path.parent.mkdir(0o755, parents=True, exist_ok=True)
            with open(config_path.as_posix(), 'wb') as f:
                pickle.dump(self.data, f)
        except IOError:
            logger.exception("Saving configuration failed")
        else:
            logger.info("Configuration successfully updated.")

    def active(self):
        merged_config = copy.deepcopy(self.data.get('common', {}))
        active_config = self.data[self._active_mode]
        merged_config.update(active_config)
        return merged_config

    def notify(self, program_name):
        self.active_mode = program_name

    @property
    def active_mode(self):
        return self._active_mode

    @active_mode.setter
    def active_mode(self, program_name):
        self._active_mode = self.data['app_mapping'].get(program_name, 'default')
        logger.info("Context changed - [{}] - [{}]".format(program_name, self._active_mode))
        # TrayWindow.showNotification('Context changed', self._active_mode)

    @staticmethod
    def _get_config_path():
        return Path.home() / Settings.REL_CONFIG_PATH
