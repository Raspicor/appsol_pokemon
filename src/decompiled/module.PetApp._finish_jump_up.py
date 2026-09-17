# module.PetApp._finish_jump_up
# source line 11623
# Recovered from bytecode; default argument values are not shown.

def _finish_jump_up(self):
    self.pos_y = self._jump_ledge['top']
    self.ground_mode = 'ledge'
    self.ground_left = self._jump_ledge['left']
    self.ground_right = self._jump_ledge['right']
    self.behavior_state = 'idle'
    self.enter_idle()
    random.randint(None(6000, 15000), self.begin_jump_down)
