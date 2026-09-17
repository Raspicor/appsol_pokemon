# module.PetApp.open_pokedex
# source line 15686
# Recovered from bytecode; default argument values are not shown.

def open_pokedex(self):
    win = None(self.root)
    win.title('포켓몬 도감')
    (_dex_w, _dex_h) = (780, 780) if self.state.get('mega_evolved') else (700, 700)
    resolve_species_win(win, _dex_w, _dex_h)

    try:
        sh = win.winfo_screenheight()
        win.geometry(f'''{_dex_w}x{min(_dex_h, sh - 80)}''')
        _opacity_row = self._add_opacity_control(win)
        outer = None(win)
        outer.pack(fill = 'both', expand = True)
        slot_bar = None(outer, text = '장착 동료', padx = 8, pady = 6)
        slot_bar.pack(side = 'bottom', fill = 'x', padx = 10, pady = (4, 10))
        slot_canvas = None(slot_bar, highlightthickness = 0)
        slot_hscroll = None(slot_bar, orient = 'horizontal', command = slot_canvas.xview)
        slot_canvas.configure(xscrollcommand = slot_hscroll.set)
        slot_canvas.pack(side = 'top', fill = 'x')
        slot_hscroll.pack(side = 'top', fill = 'x')
        slot_holder = None(slot_canvas)
        _slot_win_id = slot_canvas.create_window((0, 0), window = slot_holder, anchor = 'nw')
        tail_frame = None(slot_bar)
        tail_frame.pack(side = 'top', fill = 'x')
    
        def _on_slot_configure(evt = None):
            '''all'''
            slot_canvas.configure(scrollregion = slot_canvas.bbox('all'), width = slot_holder.winfo_reqwidth(), height = slot_holder.winfo_reqheight())

        slot_holder.bind('<Configure>', _on_slot_configure)
        MODE_ORDER = [
            'default'] + PRESET_CATEGORIES
        MODE_LABEL = {
            'default': '🤝 기본 세팅 (데리고 다니는 동료)' }
        MODE_LABEL.update(PRESET_CATEGORY_LABEL)
        mode_box = {
            'mode': 'default' }
        situ_bar = None(outer)
        situ_bar.pack(side = 'top', fill = 'x', padx = 10, pady = (10, 0))
        None(situ_bar, text = '⚔ 동료 장착 상황:', font = ('맑은 고딕', 9, 'bold')).pack(side = 'left', padx = (0, 6))
        mode_var = None(value = MODE_LABEL['default'])
        for None in :
            pass
        mode_var('readonly', textvariable = MODE_ORDER, m, state = , [], , values = m,, width = 32) = situ_bar
        mode_combo.pack(side = 'left')
    
        def _equipped_dex_set():
            '''지금 고른 상황(기본 세팅 또는 체육관/코드대결/로켓단습격/무한성장 각 모드)에서
    이미 장착 중인 도감번호 집합. 도감 목록에 🤝 표시를 뭘 기준으로 붙일지도 이걸로 정한다.'''
            if mode_box['mode'] == 'default':
                return (lambda .0: for x in .0:
    int(x).0)(self.state.get('party', [])())
            return None(self._get_preset_dex_list(mode_box['mode']))

    
        def _on_mode_change(evt = None):
            '''mode'''
            label = mode_var.get()
            for m in MODE_ORDER:
                if not MODE_LABEL[m] == label:
                    continue
                mode_box['mode'] = m
                MODE_ORDER
            None()

        mode_combo.bind('<<ComboboxSelected>>', _on_mode_change)
        top = None(outer)
        top.pack(side = 'top', fill = 'both', expand = True, padx = 10, pady = 10)
        dex_state = self.state.get('dex', { })
        missed = self.state.get('missed', { })
        list_frame = None(top)
        list_frame.pack(side = 'left', fill = 'both', expand = True)
        None(list_frame, text = '🌟스타터 🤝동료 🔒잠금 ⟲재도전가능 🌱직접키운개체 💎메가진화가능', font = ('맑은 고딕', 7), fg = '#888').pack(anchor = 'w', pady = (0, 2))
    
        def _bulk_lock(lock_on):
            '''지금 보유(포획) 중인 모든 포켓몬을 한 번에 잠그거나 해제한다.
    잠그면, 같은 종을 야생에서 다시 잡아도 도감 기록(레벨)이 자동으로 안 바뀐다.'''
            caught_dex = (lambda .0: for d in .0:
    int(d).0)(self.state.get('caught', { }).keys()())
            pinned = self.starter_stage_conf().get('dex')
            if pinned is not None:
                caught_dex.add(int(pinned))
            if lock_on:
                if not caught_dex:
                    None('PikaPet', '아직 보유 중인 포켓몬이 없어요.')
                    return None
                if not None('PikaPet', f'''지금 보유 중인 포켓몬 {len(caught_dex)}마리를 전부 잠글까요?'''):
                    return None
                self.state['party_locked'] = set.askyesno(caught_dex)
            elif not None('PikaPet', '잠긴 포켓몬을 전부 해제할까요?'):
                return None
            self.state['party_locked'] = []
            self.save_state()
            None()

        bulk_lock_row = None(list_frame)
        bulk_lock_row.pack(anchor = 'w', pady = (0, 4))
        None(bulk_lock_row, text = '🔒 보유중 전체 잠금', font = ('맑은 고딕', 7), command = (lambda : None(True))).pack(side = 'left', padx = (0, 4))
        None(bulk_lock_row, text = '🔓 전체 잠금 해제', font = ('맑은 고딕', 7), command = (lambda : None(False))).pack(side = 'left')
        caught_only_var = None(value = False)
        None(list_frame, text = '보유중만 보기', variable = caught_only_var, font = ('맑은 고딕', 8), command = (lambda : None())).pack(anchor = 'w', pady = (0, 2))
        search_row = None(list_frame)
        search_row.pack(anchor = 'w', fill = 'x', pady = (0, 4))
        None(search_row, text = '🔍', font = ('맑은 고딕', 8)).pack(side = 'left')
        search_var = None(value = '')
        search_entry = None(search_row, textvariable = search_var, font = ('맑은 고딕', 8), width = 16)
        search_entry.pack(side = 'left', padx = (2, 4))
    
        def _matches_search(d):
