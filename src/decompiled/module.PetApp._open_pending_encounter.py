# module.PetApp._open_pending_encounter
# source line 9698
# Recovered from bytecode; default argument values are not shown.

def _open_pending_encounter(self):
    self._dismiss_encounter_toast()
    if not self._pending_encounter:
        return None
    entry = ()
    level = None._pending_encounter
    is_retry = None
    _token = None
    self._stop_blink()

    try:
        if self.tray_icon:
            self.tray_icon.update_menu()
    
        try:
            self.open_battle(entry, level, is_retry = is_retry, is_shiny = is_shiny)
            return None
            except Exception:
                'acting'
                continue
        except Exception:
            'acting'
            False = None
            self.behavior_state = 'idle'
            self.enter_idle()
            return None
