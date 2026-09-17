# module.perm_atk_bonus_pct
# source line 2043
# Recovered from bytecode; default argument values are not shown.

def perm_atk_bonus_pct(state):
    return gym_badge_atk_bonus_pct(state) + title_atk_bonus_pct(state)
