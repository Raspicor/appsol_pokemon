# module.stat_at_level
# source line 2778
# Recovered from bytecode; default argument values are not shown.

def stat_at_level(base, level, reference):
    level = max(1, min(MAX_PLAYER_LEVEL, int(level)))
    if level <= 5:
        mult = 0.55 + 0.22 * level
    else:
        mult = 1.65 + 0.12 * (level - 5)
    if reference is None:
        return max(1, int(round(base * mult)))
    t = None(1, (level - 1) / 4)
    real_weight = 0.15 + 0.85 * t
    blended = reference * (1 - real_weight) + base * real_weight
    return max(1, int(round(blended * mult)))
