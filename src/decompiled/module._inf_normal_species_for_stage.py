# module._inf_normal_species_for_stage
# source line 1669
# Recovered from bytecode; default argument values are not shown.

def _inf_normal_species_for_stage(gen, pos_in_block):
    pool = _inf_sorted_pool(gen)
    if not pool:
        return (None, False)
    n = None(pool)
    if pos_in_block <= n:
        idx = pos_in_block - 1
        is_repeat = False
    elif not pool[n // 2:]:
        pool[n // 2:]
    strong_half = pool
    idx = n // 2 + (pos_in_block - n - 1) % len(strong_half)
    is_repeat = True
    dex = pool[idx]
    return (dex, is_repeat)
