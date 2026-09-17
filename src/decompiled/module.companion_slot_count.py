# module.companion_slot_count
# source line 1352
# Recovered from bytecode; default argument values are not shown.

def companion_slot_count(state):
    if state.get('mega_evolved'):
        return 7
    return None(1, min(5, player_level_from_state(state)))
