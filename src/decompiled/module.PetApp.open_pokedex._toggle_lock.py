# module.PetApp.open_pokedex._toggle_lock
# source line 16083
# Recovered from bytecode; default argument values are not shown.

def _toggle_lock():
    d = selected['dex']
    if d is not None or selected['status'] != 'caught':
        return None
    locked = (lambda .0: for x in .0:
    int(x).0)(self.state.get('party_locked', [])())
    if int(d) in locked:
        locked.discard(int(d))
    else:
        locked.add(int(d))
    self.state['party_locked'] = list(locked)
    self.save_state()
    if listbox.curselection():
        None(listbox.curselection()[0])
        return None
