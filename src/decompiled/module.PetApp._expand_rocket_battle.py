# module.PetApp._expand_rocket_battle
# source line 14174
# Recovered from bytecode; default argument values are not shown.

def _expand_rocket_battle(self, gctx):
    win = gctx['win']
    gctx['_rocket_compact_active'] = False

    try:
        win.withdraw()
        win.overrideredirect(False)
        self._code_build_ui(gctx)
    
        try:
            win.deiconify()
            return None
            except Exception:
                continue
        except Exception:
            return None
