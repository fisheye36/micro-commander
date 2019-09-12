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
    sut.analyse("ustawienia capital off")
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
    sut.analyse("ustawienia auto Space")
    result = sut.analyse("alias spacja to do równe cudzysłów vim spacja tylda kropka ukośnik to do cudzysłów")
    assert 'alias todo=\"vim ~./todo\"' == "".join(result)
    

@override_settings(data, only_active=False)
def test_lalalalala3():
    sut = Analyser()
    text = "ustawienia auto Space"
    assert ["Ala"," ", "ma"," ", "kota"] == sut.analyse("Ala ma kota")
    sut.analyse(text)
    assert ["Ala", "ma", "kota"] == sut.analyse("Ala ma kota")
    sut.analyse(text)
    assert ["Ala"," ", "ma"," ", "kota"] == sut.analyse("Ala ma kota")

@override_settings(data, only_active=False)
def test_lalalalala5():
    sut = Analyser()
    sut.analyse("ustawienia auto Space")
    assert [(Key.alt, Key.f4)] == sut.analyse("komenda zamknij")

@override_settings(data, only_active=False)
def test_lalalala7():
    sut = Analyser()
    sut.analyse('ustawienia capital off')
    assert 'dzień dobry, nazywam się czesio. lubię jeść muchy' == ''.join(sut.analyse("Dzień dobry przecinek nazywam się Czesio kropka lubię jeść muchy"))

@override_settings(data, only_active=False)
def test_shouldUseAutoCapitalLettersAfterDots():
    sut = Analyser()
    sut.analyse('ustawienia capital Auto')
    assert 'Dzień dobry, nazywam się Czesio. Lubię jeść muchy... Troche to dziwne.' == ''.join(sut.analyse("duża dzień dobry przecinek nazywam się Czesio kropka lubię jeść muchy kropka kropka kropka troche to dziwne kropka"))

@override_settings(data, only_active=False)
def test_shoundUseCapitalLetters():
    sut = Analyser()
    sut.analyse('ustawienia auto space')
    sut.analyse('ustawienia capital on')
    assert 'DZIEŃ DOBRY, NAZYWAM SIĘ CZESIO. CHCIAŁEM SPRAWDZIĆ JESZCZE, CZY DZIAŁA "CAPSLOCK" CUDZYSŁÓW.' == ''.join(sut.analyse("dzień spacja dobry przecinek spacja nazywam spacja się spacja Czesio kropka spacja chciałem spacja sprawdzić spacja jeszcze przecinek spacja czy spacja działa spacja cudzysłów capslock cudzysłów spacja dosłownie cudzysłów kropka"))




    