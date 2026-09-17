# module.max_level_for_remaining
# source line 1199
# Recovered from bytecode; default argument values are not shown.

def max_level_for_remaining(remaining):
    remaining = max(0, int(remaining))
    return max(5, MAX_PLAYER_LEVEL - 5 * remaining)
