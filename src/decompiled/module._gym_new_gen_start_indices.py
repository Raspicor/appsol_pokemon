# module._gym_new_gen_start_indices
# source line 2584
# Recovered from bytecode; default argument values are not shown.

def _gym_new_gen_start_indices():
    starts = []
    prev_region = None
    for g in GYM_LEADERS:
        if not g['region'] != prev_region:
            continue
        starts.append(g['idx'])
        prev_region = g['region']
    return set(starts)
