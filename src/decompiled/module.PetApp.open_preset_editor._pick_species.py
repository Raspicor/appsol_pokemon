# module.PetApp.open_preset_editor._pick_species
# source line 15329
# Recovered from bytecode; default argument values are not shown.

def _pick_species(dex):
    if state_box['pending_dex'] == dex:
        state_box['pending_dex'] = None
    else:
        state_box['pending_dex'] = dex
    None()
