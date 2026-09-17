# module.rocket_ambush_reward_gold
# source line 1491
# Recovered from bytecode; default argument values are not shown.

def rocket_ambush_reward_gold(defeat_count_after):
    n = max(1, int(defeat_count_after))
    base = ROCKET_BASE_GOLD + ROCKET_GOLD_PER_DEFEAT * min(n, ROCKET_GOLD_PER_DEFEAT_CAP)
    bonus = ROCKET_MILESTONE_BONUS if n % ROCKET_MILESTONE_EVERY == 0 else 0
    return base + bonus
