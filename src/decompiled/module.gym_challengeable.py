# module.gym_challengeable
# source line 1973
# Recovered from bytecode; default argument values are not shown.

def gym_challengeable(state, idx):
    idx = int(idx)
    if idx <= 1:
        return True
    return None - 1 in gym_badges_held(state)
