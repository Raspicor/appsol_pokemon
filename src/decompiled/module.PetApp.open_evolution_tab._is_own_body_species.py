# module.PetApp.open_evolution_tab._is_own_body_species
# source line 8323
# Recovered from bytecode; default argument values are not shown.

def _is_own_body_species(dd):
    info = BODY_CHAIN_LOOKUP.get(dd)
    if bool(info):
        bool(info)
    return info['species'] == own_species
