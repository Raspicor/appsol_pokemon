# module.inf_stage_level_and_mult
# source line 1603
# Recovered from bytecode; default argument values are not shown.

def inf_stage_level_and_mult(stage, mode):
    cycle = ()
    gen = inf_stage_cycle_info(stage)
    pos_in_block = None
    _pos_in_cycle = None
    max(0, uncapped_level - 15) = int(round(min(15, max(1, uncapped_level))))
    base_mult = 0.55 * (1 + curve_pos / 100) ** 3
    overflow_mult = 1 + 0.05 * overflow
    cycle_mult = 1 + INF_CYCLE_POWER_GROWTH * cycle
    mode_mult = INF_MODE_DIFFICULTY_MULT.get(mode, 1)
    kind = inf_stage_kind(pos_in_block)
    if kind == 'mirror' and gen == 4:
        kind_mult = 1.15
    elif kind == 'mirror' and gen == 3:
        kind_mult = 1.05
    elif kind in ('boss', 'mirror'):
        kind_mult = 0.9
    else:
        kind_mult = 1
    return (level, base_mult * overflow_mult * cycle_mult * mode_mult * kind_mult)
