from key_input import input_simulator
from analyser.predefined import definitions


class AppCommandDef:

    def __init__(self):
        self.simulator = input_simulator.FakeKeyboard()

    def execute_command(self, current_focused_app, command):
        """
        Execute defined command for actual focused application.

        Returns true if command was executed, False otherwise.
        """
        keys = definitions.data[current_focused_app][command]
        if isinstance(keys, input_simulator.KeyCombination):
            self.simulator.simulate_combination(keys)
        elif isinstance(keys, list):
            for key in keys:
                self.simulator.simulate_key(key)
        elif isinstance(keys, str):
            self.simulator.simulate_key(keys)
        else:
            return False
        return True

    @staticmethod
    def check_command_definition(current_focused_app, command):
        """
        Returns true if passed command is available for currently
        focused app, False otherwise.
        """
        if current_focused_app not in definitions.data:
            return False
        if command not in definitions.data[current_focused_app]:
            return False
        return True
