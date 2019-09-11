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

