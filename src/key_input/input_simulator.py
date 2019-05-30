from time import sleep

from pynput.keyboard import Controller as KeyboardController

from key_input import diacritic_mappings


class FakeKeyboard(KeyboardController):
    """A fake keyboard device that can simulate user pressing keys on a real keyboard."""

    def __init__(self, diacritic_mapping=diacritic_mappings.POLISH):
        super().__init__()
        self._diacritic_mapping = diacritic_mapping

    def simulate_key(self, key, press_duration=0.0):
        """Simulate a user pressing and holding a key for a brief moment.

        :param key: Either a one character string, one of the Key members or a KeyCode.
        :param press_duration: How long the key has been pressed before being released.
        """
        self.press(key)
        self._wait(press_duration)
        self.release(key)

    def _wait(self, duration):
        if duration:
            sleep(duration)

    def simulate_string(self, string, *, press_duration=0.0, delay=0.01):
        """Simulate a user typing a string of text with particular speed.

        Locale-specific characters are simulated just as if the user has typed them using specific key combinations.
        Special characters (like newline) are simulated just as if the corresponding key was pressed (like Enter).

        :param string: A string of text the simulated user wants to type.
        :param press_duration: How long each key has been pressed before being released.
        :param delay: A delay between pressing consecutive keys. Lesser the delay, faster the typing speed.
        """
        char_amount = len(string)
        for i, character in enumerate(string, start=1):
            key = self._CONTROL_CODES.get(character, character)
            try:
                self._simulate_diacritic_key(key, press_duration)
            except KeyError:
                self.simulate_key(key, press_duration)
            if i != char_amount:
                self._wait(delay)

    def _simulate_diacritic_key(self, key, press_duration):
        *modifiers, raw_key = self._diacritic_mapping[key]
        with self.pressed(*modifiers):
            self.simulate_key(raw_key, press_duration)

    @property
    def diacritic_mapping(self):
        return self._diacritic_mapping

    @diacritic_mapping.setter
    def diacritic_mapping(self, diacritic_mapping):
        self._diacritic_mapping = diacritic_mapping


def speed_to_delay(chars_per_minute):
    """Convert typing speed from characters per minute to delay between typing each character (in seconds).

    :param chars_per_minute: Desired speed in characters per minute.

    :return: Desired speed as a delay (in seconds) between typing each character.
    """
    return 60.0 / chars_per_minute


if __name__ == '__main__':
    kbd = FakeKeyboard()
    kbd.simulate_string('echo Hello\n', delay=speed_to_delay(500))
