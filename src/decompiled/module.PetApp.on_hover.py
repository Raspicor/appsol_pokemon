# module.PetApp.on_hover
# source line 11774
# Recovered from bytecode; default argument values are not shown.

def on_hover(self, event):
    if self.state.get('in_ball') and self.behavior_state in ('held', 'falling') or self.battle_open:
        return None
    now = None()
    if now - self._last_hover_react < 4:
        return None
    None.time._last_hover_react = None
    self._do_one_shot('react', bonus_quota = False)
