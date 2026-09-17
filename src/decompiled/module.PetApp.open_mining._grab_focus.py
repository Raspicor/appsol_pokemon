# module.PetApp.open_mining._grab_focus
# source line 12218
# Recovered from bytecode; default argument values are not shown.

def _grab_focus():
    try:
        win.lift()
        win.focus_force()
        return None
    except Exception:
        return None
