# module.PetApp._start_jump_visual
# source line 11618
# Recovered from bytecode; default argument values are not shown.

def _start_jump_visual(self, ledge):
    self.behavior_state = 'jump'
    self._jump_ledge = ledge
    self.play_action('Hop', loop = False, on_complete = self._finish_jump_up)
