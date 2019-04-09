import json

from conf import settings as glob_settings, default_config
from decorators import settings

DUMMY_SETTINGS = {'dummy': 123}


@settings(DUMMY_SETTINGS)
def test_check_if_settings_decorator_overrides_with_settings():
    assert glob_settings == DUMMY_SETTINGS


def test_check_if_global_settings_singleton_is_empty():
    assert glob_settings == {}


def test_load_configuration_should_load_default_settings_when_config_file_not_found(mocker):
    m = mocker.mock_open()
    m.side_effect = FileNotFoundError()
    mocker.patch('builtins.open', m)
    glob_settings.load_configuration()
    assert glob_settings == default_config.data


def test_load_configuration_should_load_default_settings_when_IOError(mocker):
    m = mocker.mock_open()
    m.side_effect = IOError()
    mocker.patch('builtins.open', m)
    glob_settings.load_configuration()
    assert glob_settings == default_config.data


def test_load_configuration_should_successfully_load_config_from_file(mocker):
    settings_json = json.dumps(DUMMY_SETTINGS)
    m = mocker.mock_open(read_data=settings_json)
    mocker.patch('builtins.open', m)
    glob_settings.load_configuration()
    assert glob_settings == DUMMY_SETTINGS


@settings(DUMMY_SETTINGS)
def test_save_configuration_should_save_config_to_file(mocker):
    mocker.patch('builtins.open', mocker.mock_open())
    mocker.patch('pathlib.Path.mkdir')
    m = mocker.patch('json.dump')
    glob_settings.save_configuration()
    m.assert_called_once_with(DUMMY_SETTINGS, mocker.ANY)
