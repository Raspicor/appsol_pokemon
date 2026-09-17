# module.title_crit_bonus_pct
# source line 2055
# Recovered from bytecode; default argument values are not shown.

def title_crit_bonus_pct(state):
    return _sum_possess(state, 'crit_pct') + _equip_value(state, 'crit_pct')
