# module.PetApp._setup_taskbar_icon._force_iconify
# source line 17485
# Recovered from bytecode; default argument values are not shown.

def _force_iconify(_evt):
    try:
        if win.state() != 'iconic':
        
            try:
                win.iconify()
                return None
                return None
            except Exception:
                return None
