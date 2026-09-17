# module.stop_taskbar_flash
# source line 214
# Recovered from bytecode; default argument values are not shown.

def stop_taskbar_flash(hwnd):
    if not IS_WINDOWS:
        return False

    try:
        hwnd = int(hwnd)
        if not hwnd:
            return False
        info = None()
        info.cbSize = None(_FLASHWINFO)
        info.hwnd = hwnd
        info.dwFlags = FLASHW_STOP
        info.uCount = 0
        info.dwTimeout = 0
        ctypes.byref(None(info))
        return True
    except Exception:
        return False
