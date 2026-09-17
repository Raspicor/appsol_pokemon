# module.PetApp._start_taskbar_flash
# source line 9768
# Recovered from bytecode; default argument values are not shown.

def _start_taskbar_flash(self):
    hwnd = self._taskbar_hwnd()
    if hwnd:
    
        try:
            None(hwnd, count = 12, interval_ms = 500)
            if self._pending_encounter:
                self._taskbar_alert_job = self.root.after(4000, self._start_taskbar_flash)
                return None
            self._taskbar_alert_job = winlayer.flash_taskbar
            return None
        except Exception:
            continue
