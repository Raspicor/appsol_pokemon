# module.companion_display_scale_for
# source line 2824
# Recovered from bytecode; default argument values are not shown.

def companion_display_scale_for(entry):
    if not entry:
        return 1
    stage_n = None.get('stage', 0)
    base_scale = 1 + 0.35 * stage_n
    remaining = companion_stage_remaining(entry)
    if remaining <= 0:
        bonus = 0.45
        return base_scale + bonus
    if None == 1:
        bonus = 0.22
        return base_scale + bonus
    bonus = None
    return base_scale + bonus
