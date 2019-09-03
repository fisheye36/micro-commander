from decorators import settings, override_settings
from analyser import Analyser
from conf.default_config import data

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


@override_settings({'keyboard_mapping' : {
        'cudzysłów' : '\"'
    },'general': {
        'language': 'pl',
        'key_words': {
            'explicit' : 'dosłownie'
        },
    }, 'servicemapping': {'komenda': 'InsertService'}}, only_active=False)
def test_shoud_correctly_set_service():
    text = "komenda Ala ma kota"
    sut = Analyser()
    assert ["komenda", " ", "Ala"," ", "ma"," ", "kota"] == sut.analyse(text)

@override_settings(data, only_active=False)
def test_lalalalala1():
    text = "dosłownie cudzysłów cudzysłów"
    sut = Analyser()
    assert ['cudzysłów', ' ', '\"'] == sut.analyse(text)

@override_settings(data, only_active=False)
def test_lalalalala2():
    text = "dosłownie cudzysłów cudzysłów 12 dosłownie 12 dosłownie dosłownie"
    sut = Analyser()
    assert ['cudzysłów', ' ', '\"', ' ', 'dwanaście', ' ', '12', ' ', 'dosłownie'] == sut.analyse(text)
    

@override_settings(data, only_active=False)
def test_lalalalala2():
    sut = Analyser()
    result = sut.analyse("alias to")
    result += sut.analyse("do")
    result += sut.analyse("równe")
    result += sut.analyse("cudzysłów")
    result += sut.analyse("vim tylda")
    result += sut.analyse("kropka")
    result += sut.analyse("ukośnik")
    result += sut.analyse("to")
    result += sut.analyse("do")
    result += sut.analyse("cudzysłów")

    assert 'alias todo=\"vim ~./todo\"' == "".join(result)
    