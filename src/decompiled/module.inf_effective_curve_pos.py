# module.inf_effective_curve_pos
# source line 1595
# Recovered from bytecode; default argument values are not shown.

def inf_effective_curve_pos(pos_in_block, gen):
    floor = INF_BLOCK_FLOOR_POS.get(gen, 1)
    t = (max(1, min(100, pos_in_block)) - 1) / 99
    return floor + (100 - floor) * t
