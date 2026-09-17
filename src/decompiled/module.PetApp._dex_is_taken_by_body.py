# module.PetApp._dex_is_taken_by_body
# source line 4765
# Recovered from bytecode; default argument values are not shown.

def _dex_is_taken_by_body(self, d):
    try:
        d = int(d)
        if not self.state.get('custom_body_dex'):
            self.state.get('custom_body_dex')
        if d == int(-1):
            return True
        dex2 = None(self.state)
        if dex2 is not None and d == int(dex2):
            return True
        return None
    except Exception:
        return False
