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
        'lewy nawias zwykły' : '(',
        'prawy nawias zwykły' : ')',
        'lewy nawias kwadratowy' : '[',
        'prawy nawias kwadratowy' : ']',
        'lewy nawias klamrowy' : '{',
        'prawy nawias klamrowy' : '}',
        'mniej' : '<',
        'więcej' : '>',
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
        'switchShift': 'duża',
        'deleteAll': 'wszystko',
        'micOn': 'włącz',
        'micOff': 'wyłącz',
        'capitalOn': 'capital włącz',
        'capitalAuto': 'capital auto',
        'capitalOff': 'capital wyłącz'
    },
    'servicemapping': {
        'komenda': 'CommandService',
        'uruchom': 'ExecutionService',
        'usuń': 'BackspaceService',
        'ustawienia': 'SettingsService'
    },
    'execute': {
        'edytor kodu': ['/snap/bin/code'],
        'przeglądarka': ['chromium-browser', 'facebook.com']
    },
    'general': {
        'language': 'pl',
    },
    'app_mapping': {
        'plasmashell': 'desktop',
        'konsole': 'terminal',
        'chromium-browser': 'browser',
        'gnome-terminal': 'terminal',
        'libreoffice-writer' : 'word'
    },
    'common': {
        'commands': {
            'zamknij': [(Key.alt, Key.f4)],
            'terminal': [(Key.ctrl, Key.alt, 't')],
            'pulpit': [(Key.ctrl, Key.alt, 'd')],
            'wyloguj': [(Key.ctrl, Key.alt, Key.delete)],
        }
    },
    'default': {
        'commands': {}
    },
    'browser': {
        'commands': {
            'nowa karta': [(Key.ctrl, 't')],
            'zamknij kartę': [(Key.ctrl, 'w')],
            'cofnij': [Key.backspace],
            'odśwież': [Key.f5],
            'strona domowa': [(Key.alt, Key.home)],
            'wyszukaj': [(Key.ctrl, 'l')],
            'znajdź': [(Key.ctrl, 'f')],
            'historia': [(Key.ctrl, 'h')],
            'pobrane': [(Key.ctrl, 'j')],
            'nowe okno': [(Key.ctrl, 'd')],
            'konsola': [Key.f12],
            'enter': [Key.enter],
            'incognito': [(Key.ctrl, Key.shift, 'n')]
        }
    },
    'terminal': {
        'commands': {
            'vim zapisz i zamknij': [':', 'wq', Key.enter],
            'vim wyjdź': [':', 'q', Key.enter],
            'vim zapisz': [':', 'w', Key.enter],
            'vim insert': ['i', Key.enter],
            'vim cofnij': ['u'],
            'vim tryb normalny': [Key.esc],
            'zatrzymaj': [(Key.ctrl, 'c')],
            'wyloguj': [(Key.ctrl, 'd')],
            'wyczyść': [(Key.ctrl, 'l')],
            'szukaj w historii': [(Key.ctrl, 'r')]
        }
    },
    'desktop': {
        'commands': []
    },
    'word': {
        'commands': {
            'zapisz': [(Key.ctrl, 's')],
            'otwórz': [(Key.ctrl, 'o')],
            'kopiuj': [(Key.ctrl, 'c')],
            'nowy': [(Key.ctrl, 'n')],
            'wyjdź': [(Key.alt, Key.f4)],
            'wytnij': [(Key.ctrl, 'x')],
            'wklej': [(Key.ctrl, 'v')],
            'drukuj': [(Key.ctrl, 'p')],
            'pogrub': [(Key.ctrl, 'b')],
            'kursywa': [(Key.ctrl, 'i')],
            'podkreśl': [(Key.ctrl, 'u')],
            'cofnij': [(Key.ctrl, 'z')],
            'zaznacz': [(Key.ctrl, 'a')]
        }
    },
}
