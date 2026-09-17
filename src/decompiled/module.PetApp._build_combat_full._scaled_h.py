# module.PetApp._build_combat_full._scaled_h
# source line 10848
# Recovered from bytecode; default argument values are not shown.

def _scaled_h(aset, action_name, dir_idx, scale, fallback):
    if aset is None:
        return fallback
    fr = None.frame(action_name, 0, dir_idx)
    if fr is None:
        return fallback
    return None(8, int(fr.height * scale))
