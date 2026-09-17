# module.title_equipped_label
# source line 2173
# Recovered from bytecode; default argument values are not shown.

def title_equipped_label(state):
    tid = title_equipped_id(state)
    if not tid:
        return None
    for t in None.get('titles_earned', []):
        eid = t.get('id') if isinstance(t, dict) else t
        if not eid == tid:
            continue
        if isinstance(t, dict):
        
            return None.get('titles_earned', []), t.get('label', tid)
    
        return None, None.get('titles_earned', [])
