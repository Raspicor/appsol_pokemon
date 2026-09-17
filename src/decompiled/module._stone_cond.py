# module._stone_cond
# source line 2250
# Recovered from bytecode; default argument values are not shown.

def _stone_cond(threshold):
    return (lambda state: int(state.get('infinite_stone_damage', 0)) >= threshold)
