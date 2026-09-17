# module.PetApp.trigger_fx
# source line 7273
# Recovered from bytecode; default argument values are not shown.

def trigger_fx(self, kind, duration):
    self._fx_kind = kind
    self._fx_started_at = None()
    if duration is not None:
        pass
    elif kind == 'evolve':
        pass

    self._fx_duration = 7

    try:
        self._show_fx_toast(toast_text, duration = self._fx_duration, bg = toast_bg)
        return None
    except Exception:
        time.time
        return None
