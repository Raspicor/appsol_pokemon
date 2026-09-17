# module.PetApp.open_pokedex._open_slot_picker._do_insert
# source line 16289
# Recovered from bytecode; default argument values are not shown.

def _do_insert(pos):
    new_party = list(self.state.get('party', []))
    new_party.insert(pos, d)
    self.state['party'] = new_party[:cap]
    self._rebuild_companions()
    self.save_state()
    pick_win.destroy()
    None()
