# module.get_secondary_monitor_rect._cb
# source line 300
# Recovered from bytecode; default argument values are not shown.

def _cb(hmonitor, hdc, lprect, lparam):
    try:
        if found['rect'] is not None:
            return 1
        mi = None()
        mi.cbSize = None(MONITORINFO)
        if not hmonitor(ctypes.byref, None(mi)):
            return 1
        if user32.GetMonitorInfoW.dwFlags & MONITORINFOF_PRIMARY:
            return 1
        r = None.rcMonitor
        found['rect'] = (r.left, r.top, r.right - r.left, r.bottom - r.top)
        return 1
    except Exception:
        return 1
