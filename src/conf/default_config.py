from pynput.keyboard import Key


data = {
    'keyboard_mapping': {
        'enter': '\n',
        'spacja': ' ',
        'cudzysłów': '\"',
        'tylda': "~",
        'wykrzyknik': '!',
        'małpa': '@',
        'kratka': '#',
        'dolar': '$',
        'procent': '%',
        'kareta': '^',
        'ampersand': '&',
        'gwiazdka': '*',
        'minus': '-',
        'podkreślenie': '_',
        'plus': '+',
        'równe': '=',
        'dwukropek': ':',
        'średnik': ';',
        'kropka': '.',
        'przecinek': ',',
        'ukośnik': '/',
        'apostrof': '\'',
        'lewy nawias' : '(',
        'prawy nawias' : ')',
        'lewy nawias kwadratowy' : '[',
        'prawy nawias kwadratowy' : ']',
        'lewy nawias klamrowy' : '{',
        'prawy nawias klamrowy' : '}',
        'mniej niż' : '<',
        'więcej niż' : '>',
        'jeden': '1',
        '2': 'dwa',
        '3': 'trzy',
        '4': 'cztery',
        '5': 'pięć',
        '6': 'sześć',
        '7': 'siedem',
        '8': 'osiem',
        '9': 'dziewięć',
        '10': 'dziesięć',
        '11': 'jedenaście',
        '12': 'dwanaście',
        '13': 'trzynaście',
        '14': 'czternaście',
        '15': 'piętnaście',
        '16': 'szesnaście',
        '17': 'siedemnaście',
        '18': 'osiemnaście',
        '19': 'dziewiętnaście',
        '20': 'dwadzieścia'
    },
    'analysersettings': {
        'autospace': 'auto space',
        'explicit': 'dosłownie',
        'deleteAll': 'wszystko',
        'micOn': 'włącz',
        'micOff': 'wyłącz'
    },
    'servicemapping': {
        'komenda': 'CommandService',
        'uruchom': 'ExecutionService',
        'usuń': 'BackspaceService',
        'ustawienia' : 'SettingsService',
    },
    'execute': {
        'edytor kodu' : '/snap/bin/code',
        'przeglądarka' : 'chromium-browser'
    },
    'general': {
        'language': 'pl',
    },
    'app_mapping': {
        'plasmashell': 'desktop',
        'konsole': 'terminal',
    },
    'default': {
        'commands': {
            'zamknij': [(Key.alt, Key.f4)],
            'vim zapisz i zamknij': [':', 'wq', Key.enter],
            'vim wyjdź': [':', 'q', Key.enter],
            'vim zapisz': [':', 'w', Key.enter],
            'vim insert': ['i', Key.enter],
            'vim cofnij': ['u'],
            'vim tryb normalny': [Key.esc]
        }
    },
    'chromium-browser': {
        'commands': {
            'nowa-karta': [(Key.ctrl, 't')],
            'zamknij-kartę': [(Key.ctrl, 'w')],
            'cofnij': [(Key.backspace)],
            'odśwież': [Key.f5],
            'strona-domowa': [(Key.alt, Key.home)],
            'wyszukaj': [(Key.ctrl, 'l')],
            'znajdź': [(Key.ctrl, 'f')],
            'historia': [(Key.ctrl, 'h')],
            'pobrane': [(Key.ctrl, 'j')],
            'nowe-okno': [(Key.ctrl, 'd')],
            'konsola': [Key.f12],
            'enter': [Key.enter],
            'incognito': [(Key.ctrl, Key.shift, 'n')],
        }
    },
    'terminal': {
        'commands': []
    },
    'desktop': {
        'commands': []
    }
}
