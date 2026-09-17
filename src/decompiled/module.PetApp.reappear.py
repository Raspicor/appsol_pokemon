# module.PetApp.reappear
# source line 11398
# Recovered from bytecode; default argument values are not shown.

def reappear(self):
    self._hide_timer_id = None
    if self.state.get('in_ball'):
        return None

    try:
        self.root.deiconify()
        self.behavior_state = 'idle'
        self.enter_idle()
        return None
    except Exception:
        continue
