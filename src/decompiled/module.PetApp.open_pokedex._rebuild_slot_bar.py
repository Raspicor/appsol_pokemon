# module.PetApp.open_pokedex._rebuild_slot_bar
# source line 16527
# Recovered from bytecode; default argument values are not shown.

def _rebuild_slot_bar():
    for w in slot_holder.winfo_children():
        w.destroy()
    for w in tail_frame.winfo_children():
        w.destroy()
    if mode_box['mode'] != 'default':
        None(mode_box['mode'])
        return None
    cap = None(self.state)
    party = self.state.get('party', [])[:cap]
    caught = self.state.get('caught', { })
    _slot_total = 7 if self.state.get('mega_evolved') else 5 + 1
    slot_bar.configure(text = f'''장착 동료 (최대 {_slot_total}칸: 1번은 항상 본체, 나머지는 동료 · 다 안 보이면 아래를 좌우로 스크롤하세요)''')
    content = None(slot_holder)
    content.pack(fill = 'both')
    slot_row = None(content)
    slot_row.pack(side = 'left', anchor = 'n')
    col0 = None(slot_row, relief = 'groove', bd = 2, padx = 6, pady = 4)
    col0.pack(side = 'left', padx = 4)
    None(col0, text = '1번 (본체)', font = ('맑은 고딕', 8)).pack()
    None(col0, text = self.display_name(), font = ('맑은 고딕', 9, 'bold'), wraplength = 100, justify = 'center').pack()
    unlocked2 = second_body_unlocked(self.state)
    dex2 = second_body_equipped_dex(self.state) if unlocked2 else None

    def _toggle_body_visible(key):
        '''PikaPet'''
        ok = self.set_body_visibility(key, not self.body_visibility(key))
        if not ok:
            None('PikaPet', '본체는 최소 1개는 화면에 보이고 있어야 해요!')
            return None
        None._apply_body1_visibility()
        self._rebuild_body2()
        self.save_state()
        None()

    if unlocked2:
        None(col0, text = '보이기' if not self.body_visibility('p1') else '안보이기', font = ('맑은 고딕', 7), command = (lambda : None('p1'))).pack(fill = 'x')
    if self.state.get('custom_body_dex'):
        None(col0, text = '↩ 스타터로 되돌리기', font = ('맑은 고딕', 7), command = _revert_body).pack(fill = 'x')
    None(col0, height = 1, bg = '#ccc').pack(fill = 'x', pady = 3)
    None(col0, text = '2번 (본체)', font = ('맑은 고딕', 8)).pack()
    if not unlocked2:
        None(col0, text = '🔒 2세대 도감\n완료 필요', font = ('맑은 고딕', 8), fg = '#aaa', justify = 'center').pack()
    elif not dex2:
        None(col0, text = '(비어있음)', font = ('맑은 고딕', 8), fg = '#888').pack()
        None(col0, text = "도감에서 골라\n'2번 본체로 장착'", font = ('맑은 고딕', 7), fg = '#888', justify = 'center').pack()
    else:
        e2 = POKEDEX.get(int(dex2), { })
        lv2 = self.player_level()
        mega2_ready = mega_companion_ready(dex2, caught)
        if bool(self.state.get('mega_body2')):
            bool(self.state.get('mega_body2'))
        mega2_on = mega2_ready
        show_name2 = mega_companion_display_kr(dex2, e2) if mega2_on else e2.get('kr', '?')
        None(col0, text = f'''{show_name2}{' ✨' if mega2_on else ''}\nLv.{lv2}''', font = ('맑은 고딕', 9, 'bold'), justify = 'center').pack()
        None(col0, text = '보이기' if not self.body_visibility('p2') else '안보이기', font = ('맑은 고딕', 7), command = (lambda : None('p2'))).pack(fill = 'x')
    
        def _unequip_body2():
            self.state['second_body_dex'] = None
            self.state['mega_body2'] = False
            self._rebuild_body2()
            self.save_state()
            None()

        None(col0, text = '해제', font = ('맑은 고딕', 7), command = _unequip_body2).pack(fill = 'x')
        if mega_companion_eligible_species(dex2):
        
            def _toggle_mega_body2():
                '''caught'''
                if not mega_companion_ready(dex2, self.state.get('caught', { })):
                    None('PikaPet', f'''이 개체는 아직 최고 레벨(Lv.{MAX_PLAYER_LEVEL})로 잡지 못했어요.''')
                    return None
                self.state['mega_body2'] = not None(self.state.get('mega_body2'))
                self._rebuild_body2()
                self.save_state()
                None()

            mega2_btn_text = '메가진화' if mega2_ready else f'''메가✗(Lv{MAX_PLAYER_LEVEL}필요)'''
            None(col0, text = mega2_btn_text, font = ('맑은 고딕', 7), fg = '#a83232' if mega2_ready else '#999', command = _toggle_mega_body2).pack(fill = 'x')

    def _unequip(d):
        '''party'''
        for None in :
            x = None
            if not x != d:
                continue
    
        , [], party2, x = self.state.get('party', []), x
        self.state['party'] = party2
        for None in hidden2,:
            if not int(x) != int(d):
                continue
        hidden2, = , []
        x = self.state.get('party_hidden', []), x
        self.state['party_hidden'] = hidden2
        self._rebuild_companions()
        self.save_state()
        None()
        return None
    
    


    def _toggle_hidden(d):
        hidden = (lambda .0: for x in .0:
    int(x).0)(self.state.get('party_hidden', [])())
        self.state['party_hidden'] = list(hidden)
        self._rebuild_companions()
        self.save_state()
        None()


    def _toggle_lock_slot(d):
        locked = (lambda .0: for x in .0:
    int(x).0)(self.state.get('party_locked', [])())
        self.state['party_locked'] = list(locked)
        self.save_state()
        None()

    hidden_set = (lambda .0: for x in .0:
    int(x).0)(self.state.get('party_hidden', [])())
    max_slots = 7 if self.state.get('mega_evolved') else 5

    def _toggle_mega_party(d):
        '''caught'''
        if not mega_companion_ready(d, self.state.get('caught', { })):
            None('PikaPet', f'''이 동료는 메가진화 대상 종이 아니거나, 아직 최고 레벨(Lv.{MAX_PLAYER_LEVEL})로\n잡지 못했어요. 최고 레벨 개체를 잡아서 장착해보세요.''')
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

    for i in range(max_slots):
        col = None(slot_row, relief = 'groove', bd = 2, padx = 5, pady = 4)
        col.pack(side = 'left', padx = 3)
        slot_no = i + 2
        if i < cap and i < len(party):
            d = party[i]
            e = POKEDEX.get(d, { })
            lv = caught.get(str(d), { }).get('level', '?')
            is_hidden = int(d) in hidden_set
            is_mega_on = set in (lambda .0: for x in .0:
    int(x).0)(self.state.get('mega_party', [])())
            mega_ready = mega_companion_ready(d, caught)
            show_name = mega_companion_display_kr(d, e) if is_mega_on and mega_ready else e.get('kr', '?')
            is_locked_slot = is_dex_locked(self.state, d)
            None(col, text = f'''{slot_no}번''' + ' ✨' if is_mega_on and mega_ready else '', font = ('맑은 고딕', 8)).pack()
            name_lbl = None(col, text = f'''{'🔒 ' if is_locked_slot else ''}{show_name}\nLv.{lv}''', font = ('맑은 고딕', 9, 'bold'), justify = 'center', cursor = 'hand2', fg = '#1a4a8a')
            name_lbl.pack()
            name_lbl.bind('<Button-1>', (lambda e, dd = d: self._show_companion_evolve_info(dd)))
            None(col, text = '보이기' if is_hidden else '안보이기', font = ('맑은 고딕', 7), command = (lambda dd = d: None(dd))).pack(fill = 'x')
            None(col, text = '🔓잠금해제' if is_locked_slot else '🔒잠금', font = ('맑은 고딕', 7), command = (lambda dd = d: None(dd))).pack(fill = 'x')
            None(col, text = '해제', font = ('맑은 고딕', 7), command = (lambda dd = d: None(dd))).pack(fill = 'x')
            if mega_companion_eligible_species(d):
                mega_btn_text = '메가진화' if mega_ready else '메가✗(Lv10필요)'
                None(col, text = mega_btn_text, font = ('맑은 고딕', 7), fg = '#a83232' if mega_ready else '#999', command = (lambda dd = d: None(dd))).pack(fill = 'x')
                continue
            continue
        if i < cap:
            None(col, text = f'''{slot_no}번''', font = ('맑은 고딕', 8)).pack()
            None(col, text = '(비어있음)', font = ('맑은 고딕', 8), fg = '#888').pack()
            continue
        if i < 5:
            None(col, text = f'''{slot_no}번 🔒''', font = ('맑은 고딕', 8), fg = '#aaa').pack()
            None(col, text = '레벨업\n필요', font = ('맑은 고딕', 8), fg = '#aaa', justify = 'center').pack()
            continue
        None(col, text = f'''{slot_no}번 🔒''', font = ('맑은 고딕', 8), fg = '#aaa').pack()
        None(col, text = '메가진화\n필요', font = ('맑은 고딕', 8), fg = '#aaa', justify = 'center').pack()
    tk.Label
    synergy_frame = None(content, text = '동료별 장착 효과', padx = 6, pady = 4)
    synergy_frame.pack(side = 'left', fill = 'y', padx = (10, 0))
    bd_rows = companion_synergy_breakdown(party, caught, self.state.get('mega_party', []))
    (a, ddp, c) = companion_synergy_bonus(party, caught, self.state.get('mega_party', []))
    None(tail_frame, text = f'''합산 보너스: 공격 +{a:.1f}%   방어 +{ddp:.1f}%   크리티컬 +{c:.1f}%p   (레벨 {self.player_level()})''', font = ('맑은 고딕', 9, 'bold'), fg = '#1a4a8a').pack(pady = (6, 0))
    layout_row = None(tail_frame)
    layout_row.pack(pady = (4, 0))
    None(layout_row, text = '👥 동료 진열 방식:', font = ('맑은 고딕', 8)).pack(side = 'left', padx = (0, 4))

    def _set_layout(name):
        '''companion_layout'''
        self.state['companion_layout'] = name
        self.save_state()
        self._rebuild_companions()
        None()

    cur_layout = self.state.get('companion_layout', 'line')
    for key, label in (('line', '일자로'), ('group32', '앞3-뒤2 세로로'), ('free', '자유롭게 배회')):
        None(layout_row, text = label, font = ('맑은 고딕', 8), relief = 'sunken' if cur_layout == key else 'raised', command = (lambda k = key: None(k))).pack(side = 'left', padx = 2)
    (('line', '일자로'), ('group32', '앞3-뒤2 세로로'), ('free', '자유롭게 배회'))

    def _toggle_body_free_dir():
        '''body_free_direction'''
        self.state['body_free_direction'] = not bool(self.state.get('body_free_direction'))
        self.save_state()
        None()

    body_free_on = bool(self.state.get('body_free_direction'))
    if cur_layout in ('line', 'group32'):
        None(layout_row, text = '🧭 본체 자유방향 ON' if body_free_on else '🧭 본체 자유방향 OFF', font = ('맑은 고딕', 8), relief = 'sunken' if body_free_on else 'raised', command = _toggle_body_free_dir).pack(side = 'left', padx = (10, 2))
    if cur_layout in ('line', 'group32') and body_free_on:
        None(tail_frame, text = '※ 본체 자유방향이 켜지면, 알아서 돌아다닐 때 좌우뿐 아니라 위아래로도\n움직여요. 동료들은 대형(일자/3-2)을 유지한 채 본체가 보는 방향의 뒤쪽에 붙어 따라와요.\n(키보드로 직접 조작할 때는 지금처럼 좌우로만 움직여요)', font = ('맑은 고딕', 8), fg = '#888', justify = 'left').pack(pady = (2, 0))
    if cur_layout == 'free':
        None(tail_frame, text = '※ 자유롭게 배회 모드에서는 동료들이 화면(바탕화면) 안에서 각자 알아서\n돌아다니다가 서로 부딪히면 잠깐 넘어져요. 키보드로 직접 조작할 땐 혼자만 움직여요.', font = ('맑은 고딕', 8), fg = '#888', justify = 'left').pack(pady = (2, 0))
    None(tail_frame, text = f'''※ \'안보이기\'로 숨겨도 능력치 보너스는 그대로 유지돼요. 화면에만 안 보여요.\n✨ 메가진화: 리자몽·후딘·팬텀 등 실제 스프라이트가 있는 22종을 최고 레벨(Lv.{MAX_PLAYER_LEVEL})로\n잡아서 장착하면 켤 수 있어요. 켜두면 그 동료의 보너스가 훨씬 세져요.\n🔎 동료 이름을 클릭하면 그 동료의 진화 조건과 진행도를 볼 수 있어요.\n🔒 잠금을 켜두면 같은 종을 야생에서 다시 잡아도 이 동료의 레벨 기록이 안 바뀌어요.''', font = ('맑은 고딕', 8), fg = '#888', justify = 'left').pack(pady = (2, 0))
