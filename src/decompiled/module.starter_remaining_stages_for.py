# module.starter_remaining_stages_for
# source line 1188
# Recovered from bytecode; default argument values are not shown.

def starter_remaining_stages_for(state):
    starter = state.get('starter')
    if starter or starter not in SPECIES:
        return 0
    sp = None[starter]
    max_stage = 1 if sp.get('branching') else len(sp['stages']) - 1
    return max(0, max_stage - state.get('stage', 0))
