# module.PetApp.open_pokedex._retry_selected
# source line 16403
# Recovered from bytecode; default argument values are not shown.

def _retry_selected():
    d = selected['dex']
    if d is not None or str(d) not in missed:
        return None
    lv = None[str(d)].get('level', 1)
    win.destroy()
    self.start_retry_encounter(d, lv)
