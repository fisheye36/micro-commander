"""
Command definitions.

The following commands are defined for each available
program separately.
"""

from pynput.keyboard import Key
from key_input.input_simulator import KeyCombination

data = {
    'Microsoft Word': {
        'zapisz': KeyCombination(Key.ctrl, 's'),
        'otwórz': KeyCombination(Key.ctrl, 'o'),
        'kopiuj': KeyCombination(Key.ctrl, 'c'),
        'wklej': KeyCombination(Key.ctrl, 'v'),
        'drukuj': KeyCombination(Key.ctrl, 'p'),
        'wyjdź': KeyCombination(Key.alt, Key.f4),
        'zaznacz': KeyCombination(Key.ctrl, 'a'),
    },
    'Vim Editor': {
        'wyjdź': [':', 'q', Key.enter],
        'zapisz': [':', 'w', Key.enter],
    },
    'Google Chrome': {
        'nowa-karta':[('ALT', 'F4')],
        'zamknij-kartę': KeyCombination(Key.ctrl, 'w'),
        'wyszukaj': KeyCombination(Key.ctrl, 'l'),
        'znajdź': KeyCombination(Key.ctrl, 'f'),
        'historia': KeyCombination(Key.ctrl, 'h'),
        'pobrane': KeyCombination(Key.ctrl, 'j'),
        'nowe-okno': KeyCombination(Key.ctrl, 'd'),
        'otworz word' : ['exec', ['bash']]
        'otworz word' : ['exec', ['/word']]
    }
}
