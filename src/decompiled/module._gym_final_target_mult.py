# module._gym_final_target_mult
# source line 2577
# Recovered from bytecode; default argument values are not shown.

def _gym_final_target_mult(g_max):
    return (1 + 0.12 * max(1, g_max)) * GYM_FINAL_BOSS_EXTRA_MULT
