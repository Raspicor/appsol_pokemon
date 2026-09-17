# module.PetApp.open_pokedex._rebuild_slot_bar._toggle_hidden
# source line 16624
# Recovered from bytecode; default argument values are not shown.

def _toggle_hidden(d):
    hidden = (lambda .0: for x in .0:
    int(x).0)(self.state.get('party_hidden', [])())
    self.state['party_hidden'] = list(hidden)
    self._rebuild_companions()
    self.save_state()
    None()
