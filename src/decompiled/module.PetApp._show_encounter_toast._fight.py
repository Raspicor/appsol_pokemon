# module.PetApp._show_encounter_toast._fight
# source line 9658
# Recovered from bytecode; default argument values are not shown.

def _fight():
    self._dismiss_encounter_toast()
    if self._pending_encounter:
        if self._pending_encounter[3] == token:
            self._open_pending_encounter()
            return None
        return None
