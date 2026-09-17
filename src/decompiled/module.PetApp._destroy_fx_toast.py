# module.PetApp._destroy_fx_toast
# source line 7328
# Recovered from bytecode; default argument values are not shown.

def _destroy_fx_toast(self, win):
    try:
        win.destroy()
        if getattr(self, '_fx_toast_win', None) is win:
            self._fx_toast_win = None
            return None
        return None
    except Exception:
        continue
