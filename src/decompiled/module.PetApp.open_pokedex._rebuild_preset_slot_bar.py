# module.PetApp.open_pokedex._rebuild_preset_slot_bar
# source line 16447
# Recovered from bytecode; default argument values are not shown.

def _rebuild_preset_slot_bar(category):
    cap = self._preset_cap(category)
    slots = self._get_preset_slots(category)
    caught = self.state.get('caught', { })
    slot_bar.configure(text = f'''{PRESET_CATEGORY_LABEL.get(category, category)} 전용 동료 장착 (최대 {cap}칸 · 본체는 상황과 상관없이 항상 그대로예요)''')

    def _mega_toggle_in_preset(d):
        '''caught'''
        if not mega_companion_ready(d, self.state.get('caught', { })):
            None('PikaPet', f'''이 동료는 메가진화 대상 종이 아니거나, 아직 최고 레벨(Lv.{MAX_PLAYER_LEVEL})로\n잡지 못했어요. 최고 레벨 개체를 잡아서 켜보세요.''')
            return None
        mp = (lambda .0: for x in .0:
    int(x).0)(self.state.get('mega_party', [])())
        if int(d) in mp:
            mp.discard(int(d))
        else:
            mp.add(int(d))
        self.state['mega_party'] = list(mp)
        self._rebuild_companions()
        self.save_state()
        None()

    for None in enumerate(slots):
        i = ()
        dex = None
        cell.bind('<Button-1>', (lambda e, idx = i: None(category, idx)))
        None(cell, text = f'''{i + 1}번''', font = ('맑은 고딕', 8), width = 4, anchor = 'w', cursor = 'hand2') = tk.Label
        num_lbl.pack(side = 'left')
        num_lbl.bind('<Button-1>', (lambda e, idx = i: None(category, idx)))
        if dex:
            e = POKEDEX.get(dex, { })
            lv = caught.get(str(dex), { }).get('level', 1)
            eligible = mega_companion_eligible_species(dex)
            mega_ready = mega_companion_ready(dex, caught) if eligible else False
            is_mega_on = set in (lambda .0: for x in .0:
    int(x).0)(self.state.get('mega_party', [])())
            show_name = mega_companion_display_kr(dex, e) if is_mega_on and mega_ready else e.get('kr', '?')
            name_lbl = None(cell, text = f'''{show_name}{' ✨' if is_mega_on and mega_ready else ''} Lv.{lv}''', font = ('맑은 고딕', 9, 'bold'), anchor = 'w', justify = 'left', cursor = 'hand2')
            name_lbl.pack(side = 'left', fill = 'x', expand = True)
            name_lbl.bind('<Button-1>', (lambda e, idx = i: None(category, idx)))
            if eligible:
                mega_btn_text = '메가진화' if mega_ready else f'''메가✗(Lv{MAX_PLAYER_LEVEL}필요)'''
                None(cell, text = mega_btn_text, font = ('맑은 고딕', 7), fg = '#a83232' if mega_ready else '#999', command = (lambda d = dex: None(d))).pack(side = 'left', padx = (4, 0))
            None(cell, text = '✕ 해제', font = ('맑은 고딕', 7), fg = '#a83232', command = (lambda idx = i: None(category, idx))).pack(side = 'right', padx = (4, 0))
            continue
        empty_lbl = None(cell, text = '(빈 칸) - 왼쪽 도감에서 포켓몬을 고른 뒤 여기를 클릭하세요', font = ('맑은 고딕', 8), fg = '#999', anchor = 'w', justify = 'left', cursor = 'hand2')
        empty_lbl.pack(side = 'left', fill = 'x', expand = True)
        empty_lbl.bind('<Button-1>', (lambda e, idx = i: None(category, idx)))
    tk.Button
    customized = self._preset_is_customized(category)
    dex_list = self._get_preset_dex_list(category)

    try:
        (a, ddp, c) = companion_synergy_bonus(dex_list, caught, self.state.get('mega_party', []))
        None(tail_frame, text = '👈 왼쪽 도감에서 포켓몬을 클릭해 고른 뒤, 위 빈 칸을 클릭하면 이 상황 전용으로\n장착돼요. 이미 채워진 칸을 클릭하면 해제돼요. 다른 상황으로 바꿔도 여기서\n설정한 내용은 그대로 남아있어요.', font = ('맑은 고딕', 8), fg = '#888', justify = 'left').pack(anchor = 'w', pady = (4, 0))
        return None
    except Exception:
        '메가해제'
        c = 0
        ddp = 0
        a = 0
        continue
