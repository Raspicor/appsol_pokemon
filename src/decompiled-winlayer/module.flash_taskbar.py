# module.flash_taskbar
# source line 186
# Recovered from bytecode; default argument values are not shown.

def flash_taskbar(hwnd, count, interval_ms):
    if not IS_WINDOWS:
        return False

    try:
        hwnd = int(hwnd)
        if not hwnd:
            return False
        info = None()
        info.cbSize = None(_FLASHWINFO)
        info.hwnd = hwnd
        info.dwFlags = FLASHW_ALL | FLASHW_TIMERNOFG
        info.uCount = max(1, int(count))
        info.dwTimeout = max(1, int(interval_ms))
        ctypes.byref(None(info))
        return True
    except Exception:
        return False
