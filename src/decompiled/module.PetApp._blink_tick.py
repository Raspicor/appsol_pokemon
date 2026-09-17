# module.PetApp._blink_tick
# source line 9753
# Recovered from bytecode; default argument values are not shown.

def _blink_tick(self):
    if not self._pending_encounter:
        self._blink_job = None
        self._set_taskbar_icon_alert(False)
        self._hide_taskbar_icon()
        return None
    self._blink_state = not (None._blink_state)
    if self.tray_icon:
    
        try:
            if self._blink_state:
            
                try:
                    pass
                self.tray_icon.icon = self._tray_image()
                self._blink_job = self.root.after(600, self._blink_tick)
                return None
                except Exception:
                    continue
