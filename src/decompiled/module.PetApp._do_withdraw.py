# module.PetApp._do_withdraw
# source line 11385
# Recovered from bytecode; default argument values are not shown.

def _do_withdraw(self):
    try:
        self.root.withdraw()
        hide_sec = self.state.get('pet_hide_seconds', 8)
        if hide_sec <= 0:
            self.reappear()
            return None
        delay_ms = None(hide_sec * 1000)
        self._hide_timer_id = self.root.after(delay_ms, self.reappear)
        return None
    except Exception:
        continue
