# module.player_level_from_state
# source line 1313
# Recovered from bytecode; default argument values are not shown.

def player_level_from_state(state):
    cc = ensure_catch_counts(state)
    max_level = max_level_for_remaining(starter_remaining_stages_for(state))

    def have(k):
    
        try:
            return int(cc.get(str(k), 0))
        except Exception:
            return 0


    level = 1
    for cur in range(1, MAX_PLAYER_LEVEL):
        if cur not in LEVEL_UP_REQUIREMENTS:
            range(1, MAX_PLAYER_LEVEL)
        else:
            need_lv = ()
            need_n = LEVEL_UP_REQUIREMENTS[cur]
            if level == cur and None(need_lv) >= need_n:
                continue
            cur + 1
    range(1, MAX_PLAYER_LEVEL)
    return min(level, max_level)
