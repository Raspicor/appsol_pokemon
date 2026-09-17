# module.get_taskbar_rect
# source line 350
# Recovered from bytecode; default argument values are not shown.

def get_taskbar_rect():
    if not IS_WINDOWS:
        return None

    try:
        hwnd = user32.FindWindowW('Shell_TrayWnd', None)
        if not hwnd:
            return None
        rect = None.RECT()
        if hwnd(ctypes.byref, None(rect)):
        
            try:
                return (rect.left, rect.top, rect.right, rect.bottom)
                return None
            except Exception:
                return None
