# module.PetApp._toast_duration_ms
# source line 9460
# Recovered from bytecode; default argument values are not shown.

def _toast_duration_ms(self):
    try:
        sec = float(self.state.get('toast_duration_sec', 5))
        return int(max(0, sec) * 1000)
    except Exception:
        sec = 5
        continue
