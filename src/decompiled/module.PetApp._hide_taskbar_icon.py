# module.PetApp._hide_taskbar_icon
# source line 17529
# Recovered from bytecode; default argument values are not shown.

def _hide_taskbar_icon(self):
    win = getattr(self, '_taskbar_win', None)
    if not win:
        return None

    try:
        win.withdraw()
        return None
    except Exception:
        return None
