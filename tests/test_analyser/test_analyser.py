from decorators import settings, override_settings
# from analyser import Analyser

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

# DUMMY_SETTINGS = {'magicWords' : {'dosłownie' : 1}}

# there will be new tests created
# these tests sucked

# @override_settings(DUMMY_SETTINGS)
# def test_shouldReturnCorrectList():
#     text = "Ala ma kota"
#     sut = Analyser()
#     assert ["Ala", "ma", "kota"] == sut.analyse(text)
