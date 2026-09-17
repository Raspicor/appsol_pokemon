# module.PetApp.begin_visit_icon._arrive
# source line 11648
# Recovered from bytecode; default argument values are not shown.

def _arrive():
    self.direction = spriteanim.DIR_UP
    self.behavior_state = 'acting'
    if not self.resolve('react'):
        self.resolve('react')
    react_name = 'Idle'
    self.play_action(react_name, loop = False, on_complete = self._finish_to_idle)
