# module.record_catch_for_leveling
# source line 1171
# Recovered from bytecode; default argument values are not shown.

def record_catch_for_leveling(state, wild_level):
    cc = ensure_catch_counts(state)
    for k in range(1, min(int(wild_level), MAX_PLAYER_LEVEL) + 1):
        cc[str(k)] = cc.get(str(k), 0) + 1
