# module.PetApp._show_taskbar_icon
# source line 17518
# Recovered from bytecode; default argument values are not shown.

def _show_taskbar_icon(self):
    win = getattr(self, '_taskbar_win', None)
    if not win:
        return None

    try:
        win.deiconify()
        win.update_idletasks()
        return None
    except Exception:
        return None
