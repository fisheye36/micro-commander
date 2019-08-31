from decorators import settings, override_settings
# from analyser import Analyser



# DUMMY_SETTINGS = {'magicWords' : {'dosłownie' : 1}}


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

# @override_settings(DUMMY_SETTINGS)
# def test_shouldReturnCorrectList():
#     a = Analyser()
#     a.analyse("dosłownie dosłownie")
#     assert ["dosłownie"] == a.getFinalCommand()

# @override_settings(DUMMY_SETTINGS)
# def test_shouldReturnCorrfdfsdfdsectList():
#     a = Analyser()
#     a.analyse("dosłownie dosłownie dosłownie dosłownie")
#     assert ["dosłownie", "dosłownie"] == a.getFinalCommand()