# module.PetApp.open_preset_editor._mega_off
# source line 15349
# Recovered from bytecode; default argument values are not shown.

def _mega_off(dex):
    mp = (lambda .0: for x in .0:
    int(x).0)(self.state.get('mega_party', [])())
    mp.discard(int(dex))
    self.state['mega_party'] = list(mp)
    self._rebuild_companions()
    self.save_state()
    None()
    None()
