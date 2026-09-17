# module._is_equippable_title
# source line 2185
# Recovered from bytecode; default argument values are not shown.

def _is_equippable_title(tid):
    if is_master_title_id(tid):
        return True
    entry = None.get(tid)
    if entry:
        entry
    return bool(entry.get('equip'))
