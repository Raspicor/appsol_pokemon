# module.title_hp_flat_bonus
# source line 2060
# Recovered from bytecode; default argument values are not shown.

def title_hp_flat_bonus(state):
    return _sum_possess(state, 'hp_flat') + _equip_value(state, 'hp_flat')
