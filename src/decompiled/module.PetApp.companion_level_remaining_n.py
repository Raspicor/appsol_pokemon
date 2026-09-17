# module.PetApp.companion_level_remaining_n
# source line 7865
# Recovered from bytecode; default argument values are not shown.

def companion_level_remaining_n(self, d):
    try:
        d = int(d)
        entry = POKEDEX.get(d)
        if not entry:
            return None
        key = None(d)
        caught = self.state.get('caught', { })
        cur_level = caught.get(key, { }).get('level', 1)
        remaining = max(0, entry.get('chain_len', 1) - 1 - entry.get('stage', 0))
        max_lv = max_level_for_remaining(remaining)
        if cur_level >= max_lv:
            return None
        req = None.get(cur_level)
        if req is None:
            return None
        need_lv = ()
        need_n = None
        self.state.get('companion_catch_baseline', { }).get(key, { }) = ensure_catch_counts(self.state)
        have_n = max(0, int(cc.get(str(need_lv), 0)) - int(base.get(str(need_lv), 0)))
        return max(0, need_n - have_n)
    except Exception:
        return None
