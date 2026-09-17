# module.gym_by_index
# source line 1956
# Recovered from bytecode; default argument values are not shown.

def gym_by_index(idx):
    for g in GYM_LEADERS:
        if not g['idx'] == int(idx):
            continue
    
        return GYM_LEADERS, g
