# module.PetApp._stop_blink
# source line 9784
# Recovered from bytecode; default argument values are not shown.

def _stop_blink(self):
    if self._blink_job:
    
        try:
            self.root.after_cancel(self._blink_job)
            self._blink_job = None
            if getattr(self, '_taskbar_alert_job', None):
            
                try:
                    self.root.after_cancel(self._taskbar_alert_job)
                    self._taskbar_alert_job = None
                
                    try:
                        hwnd = self._taskbar_hwnd()
                        if hwnd:
                        
                            try:
                                None(hwnd)
                                self._set_taskbar_icon_alert(False)
                                self._hide_taskbar_icon()
                                if self.tray_icon:
                                
                                    try:
                                        self.tray_icon.icon = self._tray_image()
                                        return None
                                        return None
                                        except Exception:
                                            continue
                                        except Exception:
                                            continue
                                        except Exception:
                                            continue
                                    except Exception:
                                        return None
