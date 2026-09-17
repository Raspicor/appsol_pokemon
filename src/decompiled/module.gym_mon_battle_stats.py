# module.gym_mon_battle_stats
# source line 2628
# Recovered from bytecode; default argument values are not shown.

def gym_mon_battle_stats(dex, gym_idx, position):
    entry = POKEDEX.get(int(dex), { })
    level = ()
    mult = gym_mon_level_and_mult(gym_idx, position)
    return battle_stats(entry, level, mega_mult = mult)
