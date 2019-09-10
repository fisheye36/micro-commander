"""
Command definitions.

The following commands are defined for each available
program separately.
"""

from pynput.keyboard import Key
from key_input.input_simulator import KeyCombination

data = {
    'Default': {
        'terminal': KeyCombination(Key.ctrl, Key.alt, 't'),
        'zablokuj': KeyCombination(Key.ctrl, Key.alt, 'l'),
        'pulpit': KeyCombination(Key.ctrl, Key.alt, 'd'),
        'zamknij': KeyCombination(Key.ctrl, 'q'),
        'wyloguj': KeyCombination(Key.ctrl, Key.alt, Key.delete),
    },
    'Terminal': {
        'zatrzymaj': KeyCombination(Key.ctrl, 'c'),
        'wyloguj': KeyCombination(Key.ctrl, 'd'),
        'wyczyść': KeyCombination(Key.ctrl, 'l'),
        'szukaj-w-historii': KeyCombination(Key.ctrl, 'r'),
    },
    'Microsoft Word': {
        'zapisz': KeyCombination(Key.ctrl, 's'),
        'otwórz': KeyCombination(Key.ctrl, 'o'),
        'kopiuj': KeyCombination(Key.ctrl, 'c'),
        'nowy': KeyCombination(Key.ctrl, 'n'),
        'wyjdź': KeyCombination(Key.alt, Key.f4),
        'wytnij': KeyCombination(Key.ctrl, 'x'),
        'wklej': KeyCombination(Key.ctrl, 'v'),
        'drukuj': KeyCombination(Key.ctrl, 'p'),
        'pogrub': KeyCombination(Key.ctrl, 'b'),
        'kursywa': KeyCombination(Key.ctrl, 'i'),
        'podkreśl': KeyCombination(Key.ctrl, 'u'),
        'cofnij': KeyCombination(Key.ctrl, 'z'),
        'zaznacz': KeyCombination(Key.ctrl, 'a')
    },
    'Vim Editor': {
        'wyjdź': [':', 'q', Key.enter],
        'zapisz': [':', 'w', Key.enter],
        'insert': ['i', Key.enter],
        'cofnij': ['u', Key.u],
        'tryb normalny': [Key.escape],
        'tryb-zamień': [Key.R],
        'zapisz-i-wyjdź': [':', 'w', 'q', Key.enter],
    },
    'Internet browser': {
        'nowa-karta': KeyCombination(Key.ctrl, 't'),
        'zamknij-kartę': KeyCombination(Key.ctrl, 'w'),
        'cofnij': KeyCombination(Key.backspace),
        'odśwież': KeyCombination(Key.f5),
        'strona-domowa': KeyCombination(Key.alt, Key.home),
        'wyszukaj': KeyCombination(Key.ctrl, 'l'),
        'znajdź': KeyCombination(Key.ctrl, 'f'),
        'historia': KeyCombination(Key.ctrl, 'h'),
        'pobrane': KeyCombination(Key.ctrl, 'j'),
        'nowe-okno': KeyCombination(Key.ctrl, 'd'),
        'konsola': KeyCombination(Key.f12),
        'enter': [Key.enter],
        'inkognito': KeyCombination(Key.ctrl, Key.shift, Key.f5),
    }
}
