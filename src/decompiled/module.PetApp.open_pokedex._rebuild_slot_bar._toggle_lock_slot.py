# module.PetApp.open_pokedex._rebuild_slot_bar._toggle_lock_slot
# source line 16635
# Recovered from bytecode; default argument values are not shown.

def _toggle_lock_slot(d):
    locked = (lambda .0: for x in .0:
    int(x).0)(self.state.get('party_locked', [])())
    self.state['party_locked'] = list(locked)
    self.save_state()
    None()
