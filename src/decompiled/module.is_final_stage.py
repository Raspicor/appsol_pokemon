# module.is_final_stage
# source line 1178
# Recovered from bytecode; default argument values are not shown.

def is_final_stage(state):
    starter = state.get('starter')
    if starter or starter not in SPECIES:
        return False
    sp = None[starter]
    max_stage = 1 if sp.get('branching') else len(sp['stages']) - 1
    return state.get('stage', 0) >= max_stage
