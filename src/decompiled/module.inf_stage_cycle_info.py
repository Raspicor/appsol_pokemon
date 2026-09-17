# module.inf_stage_cycle_info
# source line 1572
# Recovered from bytecode; default argument values are not shown.

def inf_stage_cycle_info(stage):
    stage = max(1, int(stage))
    cycle = (stage - 1) // 400
    pos_in_cycle = (stage - 1) % 400 + 1
    gen = (pos_in_cycle - 1) // 100 + 1
    pos_in_block = (pos_in_cycle - 1) % 100 + 1
    return (cycle, gen, pos_in_block, pos_in_cycle)
