# module.companion_stage_remaining
# source line 2817
# Recovered from bytecode; default argument values are not shown.

def companion_stage_remaining(entry):
    return max(0, entry.get('chain_len', 1) - 1 - entry.get('stage', 0))
