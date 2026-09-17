# module.gym_mon_level_and_mult
# source line 2596
# Recovered from bytecode; default argument values are not shown.

def gym_mon_level_and_mult(gym_idx, position):
    g_max = max(1, len(GYM_LEADERS))
    g = max(1, min(g_max, int(gym_idx)))
    p = max(0, min(2, int(position)))
    late_bonus = max(0, g - 16)
    uncapped_level = 2 + g // 3 + late_bonus
    level = min(MAX_PLAYER_LEVEL, uncapped_level)
    overflow = max(0, uncapped_level - MAX_PLAYER_LEVEL)
    pos_mult = [
        1,
        1.15,
        1.35][p]
    target_mult = _gym_final_target_mult(g_max)
    start_mult = target_mult * GYM_START_MULT_RATIO
    t = (g - 1) / (g_max - 1) if g_max > 1 else 1
    base_mult = start_mult * (target_mult / start_mult) ** t
    overflow_mult = 1 + GYM_LEVEL_CAP_OVERFLOW_MULT_PER_LEVEL * overflow
    gen_bonus_mult = 1 + GYM_NEW_GEN_ENTRY_BONUS_MULT if g in _gym_new_gen_start_indices() and g > 1 else 1
    gym_info = gym_by_index(g)
    sinnoh_mult = 1 + GYM_SINNOH_EXTRA_MULT if gym_info and gym_info.get('region') == 'sinnoh' else 1
    last5_mult = 1 + GYM_LAST5_EXTRA_MULT.get(g, 0)
    mult = base_mult * pos_mult * overflow_mult * gen_bonus_mult * sinnoh_mult * last5_mult
    return (level, mult)
