from pynput._util.xorg import X11Error
from pynput.keyboard import Controller, Key


def _return_proper_right_alt():
    keyboard = Controller()
    try:
        with keyboard.pressed(Key.alt_r):
            pass
    except X11Error:
        return Key.alt_gr
    else:
        return Key.alt_r


ALT_R = _return_proper_right_alt()

POLISH = {
    'ą': (ALT_R, 'a'),
    'ć': (ALT_R, 'c'),
    'ę': (ALT_R, 'e'),
    'ł': (ALT_R, 'l'),
    'ń': (ALT_R, 'n'),
    'ó': (ALT_R, 'o'),
    'ś': (ALT_R, 's'),
    'ź': (ALT_R, 'x'),
    'ż': (ALT_R, 'z'),
}
