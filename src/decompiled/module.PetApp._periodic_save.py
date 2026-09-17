# module.PetApp._periodic_save
# source line 7497
# Recovered from bytecode; default argument values are not shown.

def _periodic_save(self, now):
    if now - self._last_save > 15:
        self.save_state()
        self._last_save = now
        return None
