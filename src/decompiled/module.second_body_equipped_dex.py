# module.second_body_equipped_dex
# source line 1296
# Recovered from bytecode; default argument values are not shown.

def second_body_equipped_dex(state):
    if not second_body_unlocked(state):
        return None
    dex2 = None.get('second_body_dex')
    if not dex2:
        return None

    try:
        dex2 = int(dex2)
        if str(dex2) not in state.get('caught', { }):
            return None
        return None
    except Exception:
        return None
