# module.PetApp.open_evolution_tab._rebuild_list
# source line 8344
# Recovered from bytecode; default argument values are not shown.

def _rebuild_list():
    rows.clear()
    listbox.delete(0, 'end')
    rng = None()
    keys = (lambda .0: for d in .0:
    if not rng is not None and d in rng:
    continued.0)(POKEDEX.keys()())
    caught = self.state.get('caught', { })
    caught_by_level = { }
    uncaught = []
    for d in keys:
        status = dex_state.get(str(d))
        if status == 'caught' or d == body_dex_now:
            lv = caught.get(str(d), { }).get('level', self.player_level() if d == body_dex_now else 1)
            caught_by_level.setdefault(lv, []).append(d)
            continue
        uncaught.append(d)
    sorted
    if not keys:
        None('── 아직 없음 ──────────')
    for lv in sorted(caught_by_level.keys(), reverse = True):
        None(f'''── Lv.{lv} ──────────''')
        for d in sorted(caught_by_level[lv]):
            entry = POKEDEX[d]
            disp_kr = entry['kr']
            if not d == body_dex_now and self.state.get('mega_evolved') and self.state.get('custom_body_dex'):
                if not self.mega_display_name_for():
                    self.mega_display_name_for()
                disp_kr = disp_kr
            text = f'''{d:03d} {disp_kr}{None(d)}'''
            rows.append((d, 'caught'))
            listbox.insert('end', text)
        sorted(caught_by_level[lv])
    sorted(caught_by_level.keys(), reverse = True)
    if uncaught:
        None('── 미포획 ──────────')
        for d in uncaught:
            status = dex_state.get(str(d))
            text = f'''No.{d:03d} ？？？ (만남)''' if status == 'seen' else f'''No.{d:03d} ??????'''
            rows.append((d, status))
            listbox.insert('end', text)
        add_header
        return None
    return add_header
