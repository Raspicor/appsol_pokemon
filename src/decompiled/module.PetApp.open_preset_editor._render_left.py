# module.PetApp.open_preset_editor._render_left
# source line 15358
# Recovered from bytecode; default argument values are not shown.

def _render_left():
    for w in left_inner.winfo_children():
        w.destroy()
    caught = self.state.get('caught', { })
    mega_party_set = (lambda .0: for x in .0:
    int(x).0)(self.state.get('mega_party', [])())
    dex_list = None()
    if not dex_list:
        None(left_inner, text = '아직 잡은 포켓몬이 없어요.', font = ('맑은 고딕', 9), fg = '#888').pack(pady = 10)
        None()
        return None
    for gen_box in _caught_sorted_list():
        gen = ()
        start = None
        for None in :
            d = None
            if  <= start, d:
                if not start, d < end:
                    continue
                else:
                
                continue
            
                , [], gen_dexes, d = dex_list, d
                if not gen_dexes:
                    continue
        gen_box.pack(fill = 'x', padx = 2, pady = (4, 0))
        for dex in gen_dexes:
            e = POKEDEX.get(dex, { })
            lv = caught.get(str(dex), { }).get('level', 1)
            eligible = mega_companion_eligible_species(dex)
            mega_ready = mega_companion_ready(dex, caught) if eligible else False
            is_mega_on = dex in mega_party_set
            name = mega_companion_display_kr(dex, e) if is_mega_on and mega_ready else e.get('kr', '?')
            selected = state_box['pending_dex'] == dex
            row = None(gen_box, relief = 'solid' if selected else 'flat', bd = 2 if selected else 0)
            row.pack(fill = 'x', padx = 1, pady = 1)
            None(row, text = f'''{name} Lv.{lv}''' + ' ✨' if is_mega_on and mega_ready else '', anchor = 'w', command = (lambda d = dex: None(d))).pack(side = 'left', fill = 'x', expand = True)
            if not eligible:
                continue
            None(row, text = '메가진화', font = ('맑은 고딕', 7), fg = '#999' if not is_mega_on or mega_ready else '#a83232', state = 'disabled' if not is_mega_on or mega_ready else 'normal', command = (lambda d = dex: None(d))).pack(side = 'left')
            None(row, text = '해제', font = ('맑은 고딕', 7), fg = '#a83232' if is_mega_on else '#999', state = 'normal' if is_mega_on else 'disabled', command = (lambda d = dex: None(d))).pack(side = 'left')
        tk.Button
    tk.Frame
    None()
    return None
