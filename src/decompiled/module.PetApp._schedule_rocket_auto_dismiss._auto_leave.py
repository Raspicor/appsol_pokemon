# module.PetApp._schedule_rocket_auto_dismiss._auto_leave
# source line 14155
# Recovered from bytecode; default argument values are not shown.

def _auto_leave():
    if not gctx.get('_rocket_compact_active'):
        return None
    if None.get('flags', { }).get('ended'):
        return None

    try:
        if not win.winfo_exists():
            return None
        self._gym_concede(gctx)
        return None
    except Exception:
        return None
