# module._equip_value
# source line 2413
# Recovered from bytecode; default argument values are not shown.

def _equip_value(state, key):
    tid = title_equipped_id(state)
    if not tid:
        return 0
    entry = None.get(tid)
    if entry:
        return entry.get('equip', { }).get(key, 0)
