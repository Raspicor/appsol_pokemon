# module.PetApp.begin_hide_sequence
# source line 11377
# Recovered from bytecode; default argument values are not shown.

def begin_hide_sequence(self):
    self.behavior_state = 'acting'
    hide_name = self.resolve('hide')
    if hide_name:
        self.play_action(hide_name, loop = False, on_complete = self._do_withdraw)
        return None
    None._do_withdraw()
