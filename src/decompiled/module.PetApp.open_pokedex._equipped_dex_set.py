# module.PetApp.open_pokedex._equipped_dex_set
# source line 15758
# Recovered from bytecode; default argument values are not shown.

def _equipped_dex_set():
    if mode_box['mode'] == 'default':
        return (lambda .0: for x in .0:
    int(x).0)(self.state.get('party', [])())
    return None(self._get_preset_dex_list(mode_box['mode']))
