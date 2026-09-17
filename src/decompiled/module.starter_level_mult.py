# module.starter_level_mult
# source line 2805
# Recovered from bytecode; default argument values are not shown.

def starter_level_mult(level, remaining):
    level = max(1, int(level))
    remaining = max(0, min(2, int(remaining)))
    base_at_tier = 1 + STARTER_STAGE_MULT_STEP * 2 - STARTER_STAGE_MULT_STEP * remaining
    return base_at_tier + STARTER_LEVEL_STEP * (level - 1)
