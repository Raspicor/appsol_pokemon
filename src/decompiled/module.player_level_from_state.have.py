# module.player_level_from_state.have
# source line 1321
# Recovered from bytecode; default argument values are not shown.

def have(k):
    try:
        return int(cc.get(str(k), 0))
    except Exception:
        return 0
