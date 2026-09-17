# module.PetApp.open_pokedex._rebuild_list
# source line 15887
# Recovered from bytecode; default argument values are not shown.

def _rebuild_list():
    rows.clear()
    listbox.delete(0, 'end')
    rng = None()
    keys = (lambda .0: for d in .0:
    if not rng is not None and d in rng:
    continueif not None(d):
    continued_matches_search)(POKEDEX.keys()())
    dex_state = self.state.get('dex', { })
    caught = self.state.get('caught', { })
    missed = self.state.get('missed', { })
    pinned_dex = self.starter_stage_conf().get('dex')
    party_now = None()
    caught_by_level = { }
    uncaught = []
    for d in keys:
        if d == pinned_dex:
            continue
        status = dex_state.get(str(d))
        if status == 'caught':
            lv = caught.get(str(d), { }).get('level', 1)
            caught_by_level.setdefault(lv, []).append(d)
            continue
        uncaught.append(d)
    _equipped_dex_set
    if not keys:
        None('── 아직 없음 ──────────')
    if gen_filter['v'] == 'gen1':
        if not self.state.get('shiny_caught', { }):
            self.state.get('shiny_caught', { })
        shiny_dict = { }
        shiny_keys = (lambda .0: for d in .0:
    if not int(d) in POKEDEX:
    continueif not None(int(d)):
    continueint(d)_matches_search)(shiny_dict.keys()())
        if shiny_keys:
            None('── ✨ 이로치 (모아보기) ──────────')
            for d in shiny_keys:
                s_entry = POKEDEX[d]
                s_info = shiny_dict.get(str(d), { })
                s_lv = s_info.get('level', 1) if isinstance(s_info, dict) else 1
                text = f'''✨No.{d:03d} {s_entry['kr']} (Lv.{s_lv}) 이로치'''
                rows.append((d, 'caught'))
                listbox.insert('end', text)
                listbox.itemconfig('end', fg = '#b8860b')
            add_header
    if pinned_dex is not None and pinned_dex in POKEDEX and None(pinned_dex):
        None('── 🌟 스타터 (고정) ──────────')
        entry = POKEDEX[pinned_dex]
        lv = self.player_level()
        mark = ' ⟲재도전가능' if str(pinned_dex) in missed else ''
        lock_mark = ' 🔒' if is_dex_locked(self.state, pinned_dex) else ''
        party_mark = ' 🤝' if int(pinned_dex) in party_now else ''
        pinned_kr = entry['kr']
        if not self.state.get('mega_evolved') and self.state.get('custom_body_dex'):
            if not self.mega_display_name_for():
                self.mega_display_name_for()
            pinned_kr = pinned_kr
        raised_mark = ' 🌱' if self._is_raised(pinned_dex) else ''
        mega_mark = ' 💎' if pinned_dex in MEGA_NAME_KR else ''
        text = f'''No.{pinned_dex:03d} {pinned_kr} (Lv.{lv}) 🌟스타터{party_mark}{lock_mark}{mark}{raised_mark}{mega_mark}'''
        rows.append((pinned_dex, 'caught'))
        listbox.insert('end', text)
    for lv in sorted(caught_by_level.keys(), reverse = True):
        None(f'''── Lv.{lv} ──────────''')
        for d in sorted(caught_by_level[lv]):
            entry = POKEDEX[d]
            mark = ' ⟲재도전가능' if str(d) in missed else ''
            lock_mark = ' 🔒' if is_dex_locked(self.state, d) else ''
            party_mark = ' 🤝' if int(d) in party_now else ''
            raised_mark = ' 🌱' if self._is_raised(d) else ''
            mega_mark = ' 💎' if d in MEGA_NAME_KR else ''
            text = f'''No.{d:03d} {entry['kr']} (Lv.{lv}){party_mark}{lock_mark}{mark}{raised_mark}{mega_mark}'''
            rows.append((d, 'caught'))
            listbox.insert('end', text)
        add_header
    add_header
    if uncaught:
        if not caught_only_var.get():
            None('── 미포획 ──────────')
            for d in uncaught:
                status = dex_state.get(str(d))
                mark = ' ⟲재도전가능' if str(d) in missed else ''
                rows.append((d, status))
                listbox.insert('end', text)
            _matches_search
            return None
        return _matches_search
    return _matches_search
    except Exception:
        continue
