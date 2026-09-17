# module.genN_gym_badges_complete
# source line 1447
# Recovered from bytecode; default argument values are not shown.

def genN_gym_badges_complete(state, gen):
    region = GYM_REGION_BY_GEN.get(gen)
    if not region:
        return False
    for None in :
        g = None
        if not g['region'] == region:
            continue

    , {}, idxs, g = None, g
    if not idxs:
        return False
    return None.issubset(gym_badges_held(state))
