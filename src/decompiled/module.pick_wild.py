# module.pick_wild
# source line 2686
# Recovered from bytecode; default argument values are not shown.

def pick_wild(player_level, gen1_complete, gen2_complete, gen3_complete, gen4_complete):
    if not POKEDEX:
        return (None, 1)
    if None:
        pass
    elif gen1_complete:
        pass

    lvl_cap = 5
    weights_tbl = _wild_level_weights(max(1, min(MAX_PLAYER_LEVEL, player_level)), lvl_cap)
    levels = list(range(1, lvl_cap + 1))
    level = None(levels, weights = weights_tbl, k = 1)[0]
    time_bucket = time_of_day_bucket()
    candidates = []
    weights = []
    for d >= GEN4_START_DEX in POKEDEX.items():
        d = ()
        e = None
        if not is_gen2 and gen1_complete:
            continue
        if not is_gen3 and gen2_complete:
            continue
        if not is_gen4 and gen3_complete:
            continue
        stage = e.get('stage', 0)
        if stage == 1 and level < 3:
            continue
        if stage == 2 and level < 4:
            continue
        remaining = max(0, e.get('chain_len', 1) - 1 - stage)
        if level > max_level_for_remaining(remaining):
            continue
        if is_gen4:
            gen_done = gen4_complete
        elif is_gen3:
            gen_done = gen3_complete
        elif is_gen2:
            gen_done = gen2_complete
        else:
            gen_done = gen1_complete
        if gen_done:
            w *= COMPLETED_GEN_WILD_WEIGHT_MULT
        candidates.append(d)
        weights.append(w)
    if not candidates:
        return (None, level)
    d = None(candidates, weights = weights, k = 1)[0]
    return (POKEDEX[d], level)
