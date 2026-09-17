# module.set_dpi_aware
# source line 148
# Recovered from bytecode; default argument values are not shown.

def set_dpi_aware():
    if not IS_WINDOWS:
        return None

    try:
        hr = ctypes.windll.shcore.SetProcessDpiAwareness(2)
        if hr == 0:
            return None
    
        try:
            ctypes.windll.user32.SetProcessDPIAware()
            return None
            except Exception:
                continue
        except Exception:
            return None
