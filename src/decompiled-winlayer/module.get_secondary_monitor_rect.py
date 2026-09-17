# module.get_secondary_monitor_rect
# source line 291
# Recovered from bytecode; default argument values are not shown.

def get_secondary_monitor_rect():
    if not IS_WINDOWS:
        return None

    try:
        found = {
            'rect': None }
    
        def _cb(hmonitor, hdc, lprect, lparam):
            '''rect'''
        
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


        proc = MonitorEnumProc(_cb)
        user32.EnumDisplayMonitors(None, None, proc, 0)
        rect = found['rect']
        if rect and rect[2] > 0 and rect[3] > 0:
            return rect
        return None
    except Exception:
        return None
