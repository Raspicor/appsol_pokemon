# module.gen_dex_ranges
# source line 1390
# Recovered from bytecode; default argument values are not shown.

def gen_dex_ranges():
    starts = {
        1: 1 }
    for None in globals().items():
        name = ()
        val = None
        if not name.startswith('GEN'):
            continue
        if not name.endswith('_START_DEX'):
            continue
        if not mid.isdigit():
            continue
        int(val) = name[len('GEN'):-len('_START_DEX')]
    ordered = sorted(starts.items())
    max_dex = max(POKEDEX.keys()) if POKEDEX else 0
    ranges = []
    for None in enumerate(ordered):
        gen = ()
        start = (i,)
        if not end > start:
            continue
    return ranges
