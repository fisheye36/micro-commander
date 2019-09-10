from time import sleep

from pynput.keyboard import Controller as KeyboardController, Key

import logger
from key_input import diacritic_mappings


class KeyCombination:

    def __init__(self, *modifiers, real_key):
        """Combination of two keys.

        :param modifiers: List of modifier keys. Those keys should not be generally "invasive", e.g. Ctrl, Alt, etc.
        It is important to avoid the situation where before we press the function key, a letter is printed.
        :param real_key: The real and last key. Can be any key.
        """
        self._modifiers = modifiers
        self._real_key = real_key

    @property
    def modifiers(self):
        return self._modifiers

    @property
    def real_key(self):
        return self._real_key

    # def __str__(self):


    # @static
    # def unpack(serialized):
    #     return KeyCombination()


class FakeKeyboard(KeyboardController):
    """A fake keyboard device that can simulate user pressing keys on a real keyboard."""

    DEFAULT_PRESS_DURATION = 0.0

    def __init__(self, diacritic_mapping=diacritic_mappings.POLISH):
        super().__init__()
        self._diacritic_mapping = diacritic_mapping

    def simulate(self, key_list, press_duration=DEFAULT_PRESS_DURATION):
        logger.info('entries to simulate: {}'.format(len(key_list)))
        for entry in key_list:
            if isinstance(entry, str):
                logger.info("entry '{}' is a string".format(entry))
                self.simulate_string(entry, press_duration=press_duration)
            elif isinstance(entry, tuple):
                logger.info("entry '{}' is a key combination".format(entry))
                key_combination = KeyCombination(*entry[:-1], real_key=entry[-1])
                self.simulate_combination(key_combination, press_duration=press_duration)
            elif isinstance(entry, Key):
                logger.info("entry '{}' is a single key".format(entry))
                self.simulate_key(entry, press_duration=press_duration)
            else:
                logger.warning("entry '{}' is a recognizable".format(entry))

    def simulate_key(self, key, press_duration=DEFAULT_PRESS_DURATION):
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

    def simulate_combination(self, key_combination, press_duration=DEFAULT_PRESS_DURATION):
        """Simulate combination of several keys. For example Ctrl+s (to save), Ctrl+Shift+a or similar.

        :param key_combination: an instance of KeyCombination.
        :param press_duration: How long the real key has been pressed before being released.
        """
        with self.pressed(*key_combination.modifiers):
            self.simulate_key(key_combination.real_key, press_duration)

    def simulate_string(self, string, *, press_duration=DEFAULT_PRESS_DURATION, delay=0.01):
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
                self._simulate_diacritic_character(key, press_duration)
            except KeyError:
                self.simulate_key(key, press_duration)
            if i != char_amount:
                self._wait(delay)

    def _simulate_diacritic_character(self, character, press_duration):
        key_combination = self._obtain_key_combination_from_mapping(character)
        self.simulate_combination(key_combination, press_duration)

    def _obtain_key_combination_from_mapping(self, character):
        *modifiers, raw_key = self._diacritic_mapping[character]
        return KeyCombination(*modifiers, real_key=raw_key)

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
