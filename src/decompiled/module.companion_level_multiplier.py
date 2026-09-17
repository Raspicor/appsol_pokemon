# module.companion_level_multiplier
# source line 2857
# Recovered from bytecode; default argument values are not shown.

def companion_level_multiplier(level):
    if not level:
        level
    lv = max(1, min(int(1), COMPANION_LEVEL_BONUS_MAX_LEVEL))
    return 1 + COMPANION_LEVEL_BONUS_STEP * (lv - 1)
