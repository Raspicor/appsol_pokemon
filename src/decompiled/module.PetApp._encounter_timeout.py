# module.PetApp._encounter_timeout
# source line 9687
# Recovered from bytecode; default argument values are not shown.

def _encounter_timeout(self, token):
    if self._pending_encounter:
        if self._pending_encounter[3] == token:
            self._pending_encounter = None
            self._stop_blink()
            self._dismiss_encounter_toast()
        
            try:
                if self.tray_icon:
                
                    try:
                        self.tray_icon.update_menu()
                        return None
                        return None
                        return None
                        return None
                    except Exception:
                        return None
