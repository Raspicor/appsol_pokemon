# module.PetApp._daily_gift_pick
# source line 13831
# Recovered from bytecode; default argument values are not shown.

def _daily_gift_pick(self):
    gen = self._daily_gift_target_gen()
    if gen is None:
        return None
    lo = ()
    hi = None(gen)
    for None in :
        d = ()
        e = None
        if  <= lo, d:
            if not lo, d < hi:
                continue
            else:
            
            if e.get('legendary'):
                continue
        if not str(d) not in caught:
            continue

    , [], normal, d = POKEDEX.items(), d, e
    e = self.state.get('caught', { })
    for None in :
        d = ()
        e = None
        if  <= lo, d:
            if not lo, d < hi:
                continue
            else:
            
            if not e.get('legendary'):
                continue
        if not str(d) not in caught:
            continue

    , [], legend, d = POKEDEX.items(), d, e
    e = None
    if legend and None() < 0.03:
        pool = legend
    elif normal:
        pool = normal
    else:
        pool = legend
    if not pool:
        return None
    return (random.choice, None(pool))
