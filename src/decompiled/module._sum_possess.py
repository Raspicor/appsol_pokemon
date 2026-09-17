# module._sum_possess
# source line 2404
# Recovered from bytecode; default argument values are not shown.

def _sum_possess(state, key):
    total = 0
    earned = _earned_ids(state)
    for entry in NEW_TITLE_TABLE:
        if not entry['id'] in earned:
            continue
        total += entry.get('possess', { }).get(key, 0)
    return total
