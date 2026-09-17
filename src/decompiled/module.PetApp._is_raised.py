# module.PetApp._is_raised
# source line 5134
# Recovered from bytecode; default argument values are not shown.

def _is_raised(self, dex):
    try:
        d = int(dex)
        return bool(self.state.get('caught', { }).get(str(d), { }).get('raised'))
    except Exception:
        return False
