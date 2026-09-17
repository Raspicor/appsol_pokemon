# module.get_virtual_screen_rect
# source line 273
# Recovered from bytecode; default argument values are not shown.

def get_virtual_screen_rect():
    if not IS_WINDOWS:
        return None

    try:
        left = user32.GetSystemMetrics(SM_XVIRTUALSCREEN)
        top = user32.GetSystemMetrics(SM_YVIRTUALSCREEN)
        width = user32.GetSystemMetrics(SM_CXVIRTUALSCREEN)
        height = user32.GetSystemMetrics(SM_CYVIRTUALSCREEN)
        if width <= 0 or height <= 0:
            return None
        return (None, None, width, height)
    except Exception:
        return None
