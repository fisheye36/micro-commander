from decorators import settings, override_settings
from analyser import Analyser
from conf.default_config import data
from pynput.keyboard import Key

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


@override_settings(data, only_active=False)
def test_shoud_correctly_set_service():
    text = "Ala ma kota"
    sut = Analyser()
    assert ["Ala"," ", "ma"," ", "kota"] == sut.analyse(text)

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

@override_settings(data, only_active=False)
def test_lalalalalala2():
    sut = Analyser()
    sut.analyse("komenda auto Space")
    result = sut.analyse("alias spacja to do równe cudzysłów vim spacja tylda kropka ukośnik to do cudzysłów")
    assert 'alias todo=\"vim ~./todo\"' == "".join(result)
    

@override_settings(data, only_active=False)
def test_lalalalala3():
    sut = Analyser()
    text = "komenda auto Space"
    assert ["Ala"," ", "ma"," ", "kota"] == sut.analyse("Ala ma kota")
    sut.analyse(text)
    assert ["Ala", "ma", "kota"] == sut.analyse("Ala ma kota")
    sut.analyse(text)
    assert ["Ala"," ", "ma"," ", "kota"] == sut.analyse("Ala ma kota")

@override_settings(data, only_active=False)
def test_lalalalala5():
    sut = Analyser()
    sut.analyse("komenda auto Space")
    assert [(Key.alt, Key.f4)] == sut.analyse("komenda zamknij")

@override_settings(data, only_active=False)
def test_lalalalala6():
    sut = Analyser()
    assert [':', 'wq', Key.enter] == sut.analyse("komenda vim zapisz i zamknij")
    sut.analyse("komenda auto Space")
    assert [':', 'wq', Key.enter] == sut.analyse("komenda vim spacja zapisz spacja i spacja zamknij")







    