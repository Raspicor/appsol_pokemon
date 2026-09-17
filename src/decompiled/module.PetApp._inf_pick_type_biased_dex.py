# module.PetApp._inf_pick_type_biased_dex
# source line 14295
# Recovered from bytecode; default argument values are not shown.

def _inf_pick_type_biased_dex(self, gen, pos_in_block, player_roster):
    pool = _inf_sorted_pool(gen)
    if not pool:
        return (None, False)
    n = None(pool)
    if pos_in_block <= n:
        idx_center = pos_in_block - 1
        is_repeat = False
    elif not pool[n // 2:]:
        pool[n // 2:]
    strong_half = pool
    idx_center = n // 2 + (pos_in_block - n - 1) % len(strong_half)
    is_repeat = True
    window = max(3, n // 10)
    lo_i = max(0, idx_center - window)
    hi_i = min(n, idx_center + window + 1)
    if not pool[lo_i:hi_i]:
        pool[lo_i:hi_i]
    candidates = pool
    front = player_roster[0] if player_roster else None
    front_types = pokedex_types(front['entry']) if front else []
    weights = []
    for d in candidates:
        etypes = pokedex_types(POKEDEX.get(d, { }))
        mult = type_effect_multiplier(etypes[0], front_types) if front_types else 1
        weights.append(max(0.2, mult))
    dex = None(candidates, weights = weights, k = 1)[0]
    return (dex, is_repeat)
