# module._mode_master_cond
# source line 2240
# Recovered from bytecode; default argument values are not shown.

def _mode_master_cond(mode, need_stage):
    return (lambda state: int(state.get('inf_meter_best', { }).get(mode, 0)) >= need_stage)
