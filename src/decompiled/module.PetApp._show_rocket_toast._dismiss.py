# module.PetApp._show_rocket_toast._dismiss
# source line 14029
# Recovered from bytecode; default argument values are not shown.

def _dismiss():
    try:
        if getattr(self, '_rocket_toast_win', None) is win:
            self._rocket_toast_win = None
        win.destroy()
        return None
    except Exception:
        return None
