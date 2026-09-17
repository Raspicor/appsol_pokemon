# module.title_hp_pct_bonus
# source line 2065
# Recovered from bytecode; default argument values are not shown.

def title_hp_pct_bonus(state):
    return _sum_possess(state, 'hp_pct') + _equip_value(state, 'hp_pct')
