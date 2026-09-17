# module.PetApp.begin_jump_down
# source line 11632
# Recovered from bytecode; default argument values are not shown.

def begin_jump_down(self):
    if self.behavior_state != 'idle' or self.ground_mode != 'ledge':
        return None
    self.behavior_state = None
    self.play_action('Hop', loop = False, on_complete = self._finish_jump_down)
