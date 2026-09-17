# module.PetApp.begin_visit_icon
# source line 11644
# Recovered from bytecode; default argument values are not shown.

def begin_visit_icon(self, icon_xy):
    x = ()
    _y = icon_xy
    (lambda : self.direction = spriteanim.DIR_UPself.behavior_state = 'acting'if not self.resolve('react'):
    self.resolve('react')react_name = 'Idle'self.play_action(react_name, loop = False, on_complete = self._finish_to_idle)) = max(self.screen_left + 30, min(self.screen_left + self.screen_w - 30, x))
    self.start_targeted_walk(x, _arrive)
