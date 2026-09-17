# module._earned_ids
# source line 2395
# Recovered from bytecode; default argument values are not shown.

def _earned_ids(state):
    out = set()
    for t in state.get('titles_earned', []):
        tid = t.get('id') if isinstance(t, dict) else t
        if not isinstance(tid, str):
            continue
        out.add(tid)
    return out
