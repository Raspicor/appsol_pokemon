# module.PetApp._dismiss_encounter_toast
# source line 9678
# Recovered from bytecode; default argument values are not shown.

def _dismiss_encounter_toast(self):
    win = getattr(self, '_encounter_toast_win', None)
    if win is not None:
        self._encounter_toast_win = None
    
        try:
            win.destroy()
            return None
            return None
        except Exception:
            return None
