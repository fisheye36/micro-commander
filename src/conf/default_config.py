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
        '20': 'dwadzieścia'  # TODO

    },
    'analysersettings': {
        'autospace': 'autospace',
        'explicit': 'dosłownie'

    },
    'servicemapping': {
        'komenda': 'CommandService'
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
            'vim zapisz i zamknij': [':', 'wq', Key.enter]
        }
    },
    'terminal': {
        'commands': []
    },
    'desktop': {
        'commands': []
    }
}
