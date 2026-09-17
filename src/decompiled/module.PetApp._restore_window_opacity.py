# module.PetApp._restore_window_opacity
# source line 18310
# Recovered from bytecode; default argument values are not shown.

def _restore_window_opacity(self):
    self.state['window_opacity'] = 1
    self.save_state()
    _apply_opacity_to_all_open_windows(1)
