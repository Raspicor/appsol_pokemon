# module.PetApp.open_pokedex._rebuild_slot_bar._set_layout
# source line 16725
# Recovered from bytecode; default argument values are not shown.

def _set_layout(name):
    self.state['companion_layout'] = name
    self.save_state()
    self._rebuild_companions()
    None()
