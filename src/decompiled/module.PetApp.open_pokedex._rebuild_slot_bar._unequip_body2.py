# module.PetApp.open_pokedex._rebuild_slot_bar._unequip_body2
# source line 16593
# Recovered from bytecode; default argument values are not shown.

def _unequip_body2():
    self.state['second_body_dex'] = None
    self.state['mega_body2'] = False
    self._rebuild_body2()
    self.save_state()
    None()
