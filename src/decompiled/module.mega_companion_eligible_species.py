# module.mega_companion_eligible_species
# source line 496
# Recovered from bytecode; default argument values are not shown.

def mega_companion_eligible_species(dex):
    try:
        return int(dex) in MEGA_COMPANION_ELIGIBLE_DEX
    except Exception:
        return False
