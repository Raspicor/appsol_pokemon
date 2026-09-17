# module.PetApp.companion_level_progress_text
# source line 7905
# Recovered from bytecode; default argument values are not shown.

def companion_level_progress_text(self, d):
    try:
        d = int(d)
        entry = POKEDEX.get(d)
        if not entry:
            return ''
        key = None(d)
        caught = self.state.get('caught', { })
        cur_level = caught.get(key, { }).get('level', 1)
        remaining = max(0, entry.get('chain_len', 1) - 1 - entry.get('stage', 0))
        max_lv = max_level_for_remaining(remaining)
        if cur_level >= max_lv:
            return f'''Lv.{max_lv} (지금 진화단계 최고 레벨)'''
        req = None.get(cur_level)
        if req is None:
            return f'''Lv.{cur_level}'''
        need_lv = ()
        need_n = None
        self.state.get('companion_catch_baseline', { }).get(key, { }) = ensure_catch_counts(self.state)
        have_n = max(0, int(cc.get(str(need_lv), 0)) - int(base.get(str(need_lv), 0)))
        return f'''Lv.{cur_level} · 다음 레벨: 레벨{need_lv}+ {min(have_n, need_n)}/{need_n}마리 포획(장착 후)'''
    except Exception:
        return ''
