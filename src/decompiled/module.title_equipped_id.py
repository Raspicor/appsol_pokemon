# module.title_equipped_id
# source line 2160
# Recovered from bytecode; default argument values are not shown.

def title_equipped_id(state):
    tid = state.get('title_equipped')
    if not isinstance(tid, str):
        return None
    for t in None.get('titles_earned', []):
        eid = t.get('id') if isinstance(t, dict) else t
        if not eid == tid:
            continue
    
        return None.get('titles_earned', []), tid
