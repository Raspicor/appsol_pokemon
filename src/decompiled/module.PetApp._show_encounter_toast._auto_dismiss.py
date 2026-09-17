# module.PetApp._show_encounter_toast._auto_dismiss
# source line 9670
# Recovered from bytecode; default argument values are not shown.

def _auto_dismiss(w):
    if getattr(self, '_encounter_toast_win', None) is w:
        self._dismiss_encounter_toast()
        return None
