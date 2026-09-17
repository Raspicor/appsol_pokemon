# module.PetApp._mark_minigame_started
# source line 5512
# Recovered from bytecode; default argument values are not shown.

def _mark_minigame_started(self, key):
    d = self._minigame_ensure_daily()
    if d.get(key) is None:
        d[key] = 'in_progress'
        self.save_state()
        return None
