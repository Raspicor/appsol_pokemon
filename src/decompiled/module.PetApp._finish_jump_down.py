# module.PetApp._finish_jump_down
# source line 11638
# Recovered from bytecode; default argument values are not shown.

def _finish_jump_down(self):
    self.ground_mode = 'floor'
    self.pos_y = self._get_floor_y()
    self.behavior_state = 'idle'
    self.enter_idle()
