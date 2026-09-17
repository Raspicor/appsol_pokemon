# module.save_state_to_disk
# source line 1103
# Recovered from bytecode; default argument values are not shown.

def save_state_to_disk(state):
    ok_primary = _save_state_atomic_to(STATE_PATH, state)

    try:
        _save_state_atomic_to(SECONDARY_STATE_PATH, state)
        return ok_primary
    except Exception:
        return ok_primary
