# module.evolution_chain_for_dex
# source line 219
# Recovered from bytecode; default argument values are not shown.

def evolution_chain_for_dex(d):
    entry = POKEDEX.get(d)
    if not entry:
        return [
            d]
    chain_len = None.get('chain_len', 1)
    stage = entry.get('stage', 0)
    cur = d
    cur_stage = stage
    guard = 0
    if cur_stage > 0 and guard < 10:
        guard += 1
        prev = REVERSE_COMPANION_EVOLVE_OVERRIDE.get(cur, cur - 1)
        prev_entry = POKEDEX.get(prev)
        if prev_entry and prev_entry.get('chain_len', 1) != chain_len or prev_entry.get('stage', -1) != cur_stage - 1:
            return [
                d]
        cur = None
        cur_stage -= 1
        continue
    chain = [
        cur]
    nd = cur
    for i in range(1, chain_len):
        nxt = COMPANION_EVOLVE_OVERRIDE.get(nd, nd + 1)
        nxt_entry = POKEDEX.get(nxt)
        if nxt_entry and nxt_entry.get('chain_len', 1) != chain_len or nxt_entry.get('stage', -1) != i:
            range(1, chain_len)
            return chain
        range(1, chain_len).append(nxt)
        nd = nxt
    return chain
