# module.PetApp._schedule_rocket_auto_dismiss
# source line 14152
# Recovered from bytecode; default argument values are not shown.

def _schedule_rocket_auto_dismiss(self, gctx):
    win = gctx['win']

    def _auto_leave():
        '''_rocket_compact_active'''
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



    try:
        win.after(7000, _auto_leave)
        return None
    except Exception:
        return None
