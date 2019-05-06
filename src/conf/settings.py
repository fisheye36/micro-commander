import json
from collections import UserDict
from pathlib import Path

import logger
from conf import default_config


class Settings(UserDict):
    """
    This class is responsible for loading and storing the configuration of the application.
    """
    REL_CONFIG_PATH = '.config/micro-commander/config.json'

    def load_configuration(self):
        config_path = self._get_config_path().as_posix()
        logger.info("Loading configuration from {}".format(config_path))
        try:
            with open(config_path) as f:
                self.data = json.load(f)
            logger.info("Configuration loaded successfully from the file.")
        except FileNotFoundError:
            logger.warning("Configuration file not found.")
            self._load_default_configuration()
        except IOError:
            logger.exception("Opening configuration failed")
            self._load_default_configuration()
        logger.debug("Loaded config: {}".format(self.data))

    def _load_default_configuration(self):
        logger.info("Loading default configuration")
        self.data = default_config.data

    def save_configuration(self):
        try:
            config_path = self._get_config_path()
            config_path.parent.mkdir(0o755, parents=True, exist_ok=True)
            with open(config_path.as_posix(), 'w') as f:
                json.dump(self.data, f)
        except IOError:
            logger.exception("Saving configuration failed")
        else:
            logger.info("Configuration successfully updated.")

    @staticmethod
    def _get_config_path():
        return Path.home() / Settings.REL_CONFIG_PATH
