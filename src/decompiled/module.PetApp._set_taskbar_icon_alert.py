# module.PetApp._set_taskbar_icon_alert
# source line 17539
# Recovered from bytecode; default argument values are not shown.

def _set_taskbar_icon_alert(self, alert):
    win = getattr(self, '_taskbar_win', None)
    if not win:
        return None

    try:
        if win.state() != 'withdrawn':
            win.withdraw()
            return None
        return None
    except Exception:
        return None
