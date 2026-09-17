# module.PetApp._ensure_gacha_pool
# source line 12272
# Recovered from bytecode; default argument values are not shown.

def _ensure_gacha_pool(self):
    n = GACHA_GRID_N * GACHA_GRID_N
    pool = self.state.get('coin_gacha_pool')
    if not not isinstance(pool, dict):
        not isinstance(pool, dict)
        if not len(pool.get('cells', [])) != n:
            len(pool.get('cells', [])) != n
    need_new = len(pool.get('revealed', [])) != n
    if need_new and all(pool.get('revealed', [])):
        need_new = True
    if not need_new:
        expected_multiset = { }
        for None in GACHA_POOL_COMPOSITION:
            amount = ()
            count = None
        GACHA_POOL_COMPOSITION
        { } = None
        for c in pool.get('cells', []):
            actual_multiset[c] = actual_multiset.get(c, 0) + 1
        if actual_multiset != expected_multiset:
            need_new = True
    if need_new:
        pool = self._new_gacha_pool()
        self.state['coin_gacha_pool'] = pool
        self.save_state()
    return pool
