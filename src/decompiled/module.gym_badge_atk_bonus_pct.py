# module.gym_badge_atk_bonus_pct
# source line 1981
# Recovered from bytecode; default argument values are not shown.

def gym_badge_atk_bonus_pct(state):
    return len(gym_badges_held(state)) * GYM_BADGE_ATK_BONUS_PCT
