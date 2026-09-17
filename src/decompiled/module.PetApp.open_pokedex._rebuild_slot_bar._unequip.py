# module.PetApp.open_pokedex._rebuild_slot_bar._unequip
# source line 16615
# Recovered from bytecode; default argument values are not shown.

def _unequip(d):
    for None in :
        x = None
        if not x != d:
            continue

    , [], party2, x = self.state.get('party', []), x
    self.state['party'] = party2
    for None in hidden2,:
        if not int(x) != int(d):
            continue
    hidden2, = , []
    x = self.state.get('party_hidden', []), x
    self.state['party_hidden'] = hidden2
    self._rebuild_companions()
    self.save_state()
    None()
    return None
