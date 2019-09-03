from decorators import settings, override_settings
from analyser import Analyser

@override_settings({'commands': {'exit': '\ALT+\F4'}})
def test_by_default_should_override_only_active_settings():
    assert settings.active()['commands']['exit'] == '\ALT+\F4'


@override_settings({
        'general': {
            'language': 'pl'
        },
        'default': {
            'commands': {
                'exit': '\ALT+\F4'
            }
        }
    }, only_active=False)
def test_when_only_active_should_override_whole_settings():
    assert settings.active()['commands']['exit'] == '\ALT+\F4'
    assert settings['general']['language'] == 'pl'


@override_settings({'servicemapping': {'komenda': 'InsertService'}})
def test_shoud_correctly_set_service():
    text = "komenda Ala ma kota"
    sut = Analyser()
    assert ["komenda", "Ala", "ma", "kota"] == sut.analyse(text)
