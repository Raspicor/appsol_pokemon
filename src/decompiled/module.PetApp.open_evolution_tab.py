# module.PetApp.open_evolution_tab
# source line 8229
# Recovered from bytecode; default argument values are not shown.

def open_evolution_tab(self):
    win = None(self.root)
    win.title('🧬 진화/레벨 탭')
    resolve_species_win(win, 700, 780)

    try:
        sh = win.winfo_screenheight()
        sw = win.winfo_screenwidth()
        win.geometry(f'''700x{min(780, sh - 100)}''')
        self._add_opacity_control(win)
        outer = None(win)
        outer.pack(fill = 'both', expand = True)
        bottom = None(outer)
        bottom.pack(side = 'bottom', pady = 8)
        summary_bar = None(outer, text = '지금 장착 중인 본체·동료 한눈에 보기', padx = 6, pady = 4)
        summary_bar.pack(side = 'bottom', fill = 'x', padx = 10, pady = (0, 4))
        if self.state.get('custom_body_dex'):
            _cb = POKEDEX.get(int(self.state['custom_body_dex']), { })
            None(outer, text = f'''🏠 지금 화면에는 {_cb.get('kr', '?')}이(가) 본체로 나와있어요. (원래 스타터 진행도는 여기서 그대로 추적돼요)''', font = ('맑은 고딕', 8), fg = '#a8681a').pack(side = 'top', fill = 'x', padx = 10, pady = (6, 0))
        today_card = None(outer, text = '📅 오늘 할 일', padx = 8, pady = 4)
        today_card.pack(side = 'top', fill = 'x', padx = 10, pady = (6, 0))
        today = None('%Y-%m-%d')
        train_cnt = self._train_today_count()
        md = self.state.get('minigame_daily', { })
        if md.get('date') != today:
            md = { }
        mg_done_n = (lambda .0: for k in .0:
    if not md.get(k):
    continue1.0)(('feed', 'card', 'quiz', 'throw')())
        today_row = None(today_card)
        today_row.pack(fill = 'x')
        None(today_row, text = self.daily_quest_text(), font = ('맑은 고딕', 8)).pack(side = 'left', padx = (0, 12))
        None(today_row, text = f'''🏋 수련 {train_cnt}/{TRAIN_MAX_PER_DAY}회''', font = ('맑은 고딕', 8)).pack(side = 'left', padx = (0, 12))
        None(today_row, text = f'''🎮 미니게임 {mg_done_n}/4종{'  ✅보너스완료' if md.get('all_bonus_given') else ''}''', font = ('맑은 고딕', 8)).pack(side = 'left')
        None(today_row, text = '자세히', font = ('맑은 고딕', 7), command = self._show_daily_quest_overview).pack(side = 'right')
        top = None(outer)
        top.pack(side = 'top', fill = 'both', expand = True, padx = 10, pady = 10)
        dex_state = self.state.get('dex', { })
        body_dex_now = self.starter_stage_conf().get('dex')
        own_species = self.state.get('starter')
        own_stage_idx = self.state.get('stage', 0)
        own_branch = self.state.get('eevee_branch')
        list_frame = None(top)
        list_frame.pack(side = 'left', fill = 'both', expand = True)
        gen_filter = {
            'v': 'gen1' if all_gen1_caught(self.state) else 'all' }
        tab_row_wrap = ()
        tab_row = self._make_hscroll_row(list_frame)
        tab_row_wrap.pack(side = 'top', fill = 'x', pady = (0, 4))
        all_gen2_caught(self.state) = all_gen1_caught(self.state)
        gen4_unlocked = all_gen3_caught(self.state)
        list_box_frame = None(list_frame)
        list_box_frame.pack(side = 'top', fill = 'both', expand = True)
        scrollbar = None(list_box_frame)
        scrollbar.pack(side = 'right', fill = 'y')
        listbox = None(list_box_frame, width = 28, height = 22, yscrollcommand = scrollbar.set)
        listbox.pack(side = 'left', fill = 'both', expand = True)
        scrollbar.config(command = listbox.yview)
        rows = []
    
        def add_header(text):
            rows.append((None, None))
            listbox.insert('end', text)
            listbox.itemconfig('end', fg = '#888')

    
        def _dex_range_for_filter():
            '''v'''
            f = gen_filter['v']
            if f == 'gen1':
                return range(1, 152)
            if None == 'gen2':
                return range(GEN2_START_DEX, GEN3_START_DEX)
            if None == 'gen3':
                return range(GEN3_START_DEX, GEN4_START_DEX)
            if None == 'gen4':
                return range(GEN4_START_DEX, 494)

    
        def _is_own_body_species(dd):
            '''species'''
            info = BODY_CHAIN_LOOKUP.get(dd)
            if bool(info):
                bool(info)
            return info['species'] == own_species

    
        def _tag_for(dd):
            ''
            tag = ''
            if dd == body_dex_now:
                tag += ' 🏠'
            if set in (lambda .0: for x in .0:
    int(x).0)(self.state.get('party', [])()):
                tag += ' 🤝'
            if dd in EEVEE_DEX_SET:
                tag += ' 🧬'
            if self._is_raised(dd):
                tag += ' 🌱'
            if dd in MEGA_NAME_KR:
                tag += ' 💎'
            return tag

    
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

    
        def _set_filter(name):
            '''v'''
            gen_filter['v'] = name
            for None in tab_buttons.items():
                key = ()
                btn = None
            None()

        tab_buttons = { }
        tab_buttons['all'] = None(tab_row, text = '전체', command = (lambda : None('all')))
        tab_buttons['gen1'] = None(tab_row, text = '1세대', command = (lambda : None('gen1')))
        gen2_label = '2세대' if gen2_unlocked else '2세대🔒'
        tab_buttons['gen2'] = None(tab_row, text = gen2_label, command = (lambda : None('gen2')))
        gen3_label = '3세대' if gen3_unlocked else '3세대🔒'
        tab_buttons['gen3'] = None(tab_row, text = gen3_label, command = (lambda : None('gen3')))
        gen4_label = '4세대' if gen4_unlocked else '4세대🔒'
        tab_buttons['gen4'] = None(tab_row, text = gen4_label, command = (lambda : None('gen4')))
        for b in tab_buttons.values():
            b.pack(side = 'left', padx = (0, 3), ipadx = 2)
        tk.Button
        for key, btn in tab_buttons.items():
            btn.configure(relief = 'sunken' if key == gen_filter['v'] else 'raised')
        tk.Button
        None()
        detail_outer = None(top)
        detail_outer.pack(side = 'left', fill = 'both', expand = True, padx = (14, 0))
        canvas = None(detail_outer, highlightthickness = 0)
        vsb2 = None(detail_outer, orient = 'vertical', command = canvas.yview)
        inner = None(canvas)
        inner_id = canvas.create_window((0, 0), window = inner, anchor = 'nw')
        inner.bind('<Configure>', (lambda e: canvas.configure(scrollregion = canvas.bbox('all'))))
        canvas.bind('<Configure>', (lambda e: canvas.itemconfig(inner_id, width = e.width)))
        canvas.configure(yscrollcommand = vsb2.set)
        canvas.pack(side = 'left', fill = 'both', expand = True)
        vsb2.pack(side = 'right', fill = 'y')
    
        def _wheel(event):
            '''num'''
            delta = -1 if getattr(event, 'num', 0) == 5 or event.delta < 0 else 1
        
            try:
                if canvas.winfo_exists():
                
                    try:
                        canvas.yview_scroll(-delta, 'units')
                        return None
                        return None
                    except Exception:
                        return None



        win.bind('<MouseWheel>', _wheel)
        win.bind('<Button-4>', _wheel)
        win.bind('<Button-5>', _wheel)
    
        def _icon_for(dd, colored):
            entry = POKEDEX.get(dd)
            if not entry:
                return draw_pokeball_image(48)
        
            try:
                aset = None(sprite_folder_path(entry['en']))
                frame = aset.frame(entry['idle'], 0, spriteanim.DIR_DOWN)
                if frame is None:
                    return draw_pokeball_image(48)
                frame = spriteanim.AnimSet.convert('RGBA')
                if not colored:
                    frame = make_silhouette(frame)
                return frame
            except Exception:
                frame = None
                continue


    
        def _icon_label(parent, dd, colored, target_h, highlight):
            '''solid'''
            cell = None(parent, relief = 'solid' if highlight else 'flat', bd = 2 if highlight else 0, padx = 2, pady = 2)
            img = None(dd, colored)
            s = target_h / max(1, img.height)
            img = img.resize((max(8, int(img.width * s)), max(8, int(img.height * s))), Image.NEAREST)
            tkimg = None(img)
            lbl = None(cell, image = tkimg)
            lbl.image = tkimg
            lbl.pack()
            return cell

    
        def _clear_inner():
            for w in inner.winfo_children():
                w.destroy()

    
        def _refresh_and_reopen():
            win.destroy()
            self.open_evolution_tab()

    
        def _render_eevee_chain(parent, sel_d):
            '''133'''
            if not bool(dex_state.get('133')):
                bool(dex_state.get('133'))
            base_colored = own_species == 'eevee'
            cell = None(parent, 133, base_colored, 48, sel_d == 133)
            cell.pack(side = 'left', padx = 4)
            None(cell, text = '이브이' if base_colored else '？？？', font = ('맑은 고딕', 7)).pack()
            None(parent, text = '→', font = ('맑은 고딕', 12)).pack(side = 'left')
            branch_wrap = None(parent)
            branch_wrap.pack(side = 'left')
            branch_cols = 3
            for None(branch_wrap, bd, colored, 36, sel_d == bd) in enumerate(EEVEE_BRANCH_BY_DEX.items()):
                bd = ()
                bkey = (idx,)
                if not bool(dex_state.get(str(bd))):
                    bool(dex_state.get(str(bd)))
                    if own_species == 'eevee':
                        own_species == 'eevee'
                        if own_stage_idx >= 1:
                            own_stage_idx >= 1
                r = ()
                c = divmod(idx, branch_cols)
                bcell.grid(row = r, column = c, padx = 2, pady = 1)
                None(bcell, text = bname, font = ('맑은 고딕', 7)).pack()
            POKEDEX.get(bd, { }).get('kr', '?') if colored else '？？？'

    
        def _render_eevee_stats(parent):
            '''133'''
            if not bool(dex_state.get('133')):
                bool(dex_state.get('133'))
            base_colored = own_species == 'eevee'
            be0 = POKEDEX.get(133, { })
            for own_branch == bkey in EEVEE_BRANCH_BY_DEX.items():
                bd = ()
                bkey = None
                if not bool(dex_state.get(str(bd))):
                    bool(dex_state.get(str(bd)))
                    if own_species == 'eevee':
                        own_species == 'eevee'
                        if own_stage_idx >= 1:
                            own_stage_idx >= 1
                None(parent, text = line, font = ('맑은 고딕', 8), justify = 'left', anchor = 'w').pack(fill = 'x')
            tk.Label if base_colored else tk.Label if colored else EEVEE_BRANCH_BY_DEX.items()

    
        def _render_action(parent, d, entry, status):
            '''branching'''
            is_body_dex = d == body_dex_now
            if is_body_dex:
                sp = SPECIES[own_species]
                max_stage = 1 if sp.get('branching') else len(sp['stages']) - 1
                if own_stage_idx >= max_stage:
                    None(parent, text = '🏠 본체 · 이미 최종 진화 단계예요.', font = ('맑은 고딕', 8), fg = '#888').pack(anchor = 'w')
                    return None
                None(parent, text = f'''🏠 지금 본체(내 포켓몬)예요.\n{self.evolution_progress_text()}''', font = ('맑은 고딕', 8, 'bold'), fg = '#1a6b1a', justify = 'left', wraplength = 340).pack(anchor = 'w')
                ready = self.evolution_ready()
                if sp.get('branching'):
                
                    def _do_evolve(branch, branch_kr):
                        '''PikaPet'''
                        if not self.evolution_ready():
                            None('PikaPet', '아직 진화 조건을 채우지 못했어요.')
                            return None
                        if not None('PikaPet', f'''정말 {branch_kr}(으)로 진화시킬까요?\n(진화 후에는 되돌릴 수 없어요)'''):
                            return None
                        None.askyesno.evolve(forced_branch = branch)
                        None()

                    if eevee_friendship_ready(self.state):
                        hour = None().tm_hour
                        None(parent, text = f'''💞 친밀도 조건 달성! (애정도 {self.state.get('affection', 50):.0f} / {EEVEE_FRIENDSHIP_AFFECTION_MIN}, 불물전기 훈련 안 치우침) 에스피언·블래키 중 골라 진화할 수 있어요.''', font = ('맑은 고딕', 8), fg = '#a83a8a', justify = 'left', wraplength = 340).pack(anchor = 'w', pady = (4, 2))
                        None(parent) = tk.Frame
                        row.pack(anchor = 'w', pady = (0, 4))
                        None(row, text = '☀ 에스피언으로 진화!', state = tk.NORMAL if is_day else tk.DISABLED, command = (lambda : None('psychic', '에스피언'))).pack(side = 'left', padx = (0, 4))
                        None(row, text = '🌙 블래키로 진화!', state = tk.DISABLED if is_day else tk.NORMAL, command = (lambda : None('dark', '블래키'))).pack(side = 'left')
                        None(parent, text = '(낮이라 에스피언만 가능해요. 밤에 다시 와보세요.)' if is_day else '(밤이라 블래키만 가능해요. 낮에 다시 와보세요.)', font = ('맑은 고딕', 7), fg = '#888').pack(anchor = 'w')
                        return None
                    et = None.Label.state.get('element_train', {
                        'electric': 0,
                        'water': 0,
                        'fire': 0 })
                    self._predict_eevee_branch() = tk.Label if tied else tk.Label
                    predicted_kr = sp['branches'][predicted]['kr']
                    None(parent, text = f'''지금 진화하면 예상: {predicted_kr} (원소 훈련 기준)''', font = ('맑은 고딕', 8), fg = '#555').pack(anchor = 'w', pady = (4, 2))
                    None(parent, text = '진화!', state = tk.NORMAL if ready else tk.DISABLED, command = (lambda p = predicted, pk = predicted_kr: None(p, pk))).pack(anchor = 'w', pady = (2, 4))
                    return None
            
                def _do_evolve_body():
                    '''PikaPet'''
                    if not self.evolution_ready():
                        None('PikaPet', '아직 진화 조건을 채우지 못했어요.')
                        return None
                    if not None('PikaPet', '정말 진화시킬까요? (되돌릴 수 없어요)'):
                        return None
                    None.askyesno.evolve()
                    None()

                None(parent, text = '진화!', state = tk.NORMAL if ready else tk.DISABLED, command = _do_evolve_body).pack(anchor = 'w', pady = (4, 4))
                return None
            custom_dex_now = None.state.get('custom_body_dex')
            if custom_dex_now is not None and int(custom_dex_now) == d:
                cstatus = self.companion_evolution_status(d)
                None(parent, text = f'''레벨: Lv.{self.body1_effective_level()} (이 종 자신의 레벨/능력치를 그대로 써요,\n원래 스타터 레벨과는 무관해요)''', font = ('맑은 고딕', 8), fg = '#3a5a9a', justify = 'left', wraplength = 340).pack(anchor = 'w', pady = (0, 4))
                if not cstatus.get('evolvable'):
                    None(parent, text = f'''🔁 지금 화면에 나와있는 본체예요. {cstatus.get('reason', '')}''', font = ('맑은 고딕', 8), fg = '#888', wraplength = 340, justify = 'left').pack(anchor = 'w')
                    return None
                nxt = tk.Label['next_entry']
                None(parent, text = f'''🔁 지금 화면에 나와있는 본체예요 (원래 스타터의 레벨/진행도는 별개로 계속 유지돼요).\n다음 진화: {nxt.get('kr', '?')}\n진행도: {min(cstatus['elapsed_days'], cstatus['days_needed']):.1f} / {cstatus['days_needed']:.1f}일  (동료와 같은 속도예요)''', font = ('맑은 고딕', 8), fg = '#1a6b1a', justify = 'left', wraplength = 340).pack(anchor = 'w', pady = (0, 4))
            
                def _do_evolve_custom_body():
                    '''PikaPet'''
                    if not None('PikaPet', '정말 진화시킬까요? (되돌릴 수 없어요)'):
                        return None
                    if messagebox.askyesno.evolve_custom_body():
                        None()
                        return None
                    None('PikaPet', '아직 진화 조건을 채우지 못했어요.')

                None(parent, text = '진화!', state = tk.NORMAL if cstatus.get('ready') else tk.DISABLED, command = _do_evolve_custom_body).pack(anchor = 'w', pady = (0, 4))
                return None
            party = (lambda .0: for x in .0:
    int(x).0)(self.state.get('party', [])())
            if int(d) in party:
                None(parent, text = f'''레벨: {self.companion_level_progress_text(d)}''', font = ('맑은 고딕', 8), fg = '#3a5a9a', justify = 'left', wraplength = 340).pack(anchor = 'w', pady = (0, 4))
                cstatus = self.companion_evolution_status(d)
                if not cstatus.get('evolvable'):
                    None(parent, text = f'''🤝 장착된 동료예요. {cstatus.get('reason', '')}''', font = ('맑은 고딕', 8), fg = '#888', wraplength = 340, justify = 'left').pack(anchor = 'w')
                    return None
                if tk.Label.get('is_eevee'):
                    sp = SPECIES['eevee']
                    None(parent, text = f'''🤝 장착된 동료 이브이예요.\n진행도: {min(cstatus['elapsed_days'], cstatus['days_needed']):.1f} / {cstatus['days_needed']:.1f}일  (본체와 같은 속도예요)''', font = ('맑은 고딕', 8), fg = '#1a6b1a', justify = 'left', wraplength = 340).pack(anchor = 'w', pady = (0, 4))
                
                    def _do_evolve_companion_eevee(branch, branch_kr, dd = d):
                        '''ready'''
                        if not cstatus.get('ready'):
                            None('PikaPet', '아직 진화 조건을 채우지 못했어요.')
                            return None
                        if not None('PikaPet', f'''정말 {branch_kr}(으)로 진화시킬까요?\n(진화 후에는 되돌릴 수 없어요)'''):
                            return None
                        if None.askyesno.evolve_companion(dd, forced_branch = branch):
                            None()
                            return None
                        None('PikaPet', '아직 진화 조건을 채우지 못했어요.')

                    if eevee_friendship_ready(self.state):
                        hour = None().tm_hour
                        None(parent, text = f'''💞 친밀도 조건 달성! (애정도 {self.state.get('affection', 50):.0f} / {EEVEE_FRIENDSHIP_AFFECTION_MIN}, 불물전기 훈련 안 치우침) 에스피언·블래키 중 골라 진화할 수 있어요.''', font = ('맑은 고딕', 8), fg = '#a83a8a', justify = 'left', wraplength = 340).pack(anchor = 'w', pady = (4, 2))
                        None(parent) = tk.Frame
                        row.pack(anchor = 'w', pady = (0, 4))
                        if cstatus.get('ready'):
                            cstatus.get('ready')
                        e_ok = is_day
                        if cstatus.get('ready'):
                            cstatus.get('ready')
                        u_ok = not is_day
                        None(row, text = '☀ 에스피언으로 진화!', state = tk.NORMAL if e_ok else tk.DISABLED, command = (lambda : None('psychic', '에스피언'))).pack(side = 'left', padx = (0, 4))
                        None(row, text = '🌙 블래키로 진화!', state = tk.NORMAL if u_ok else tk.DISABLED, command = (lambda : None('dark', '블래키'))).pack(side = 'left')
                        None(parent, text = '(낮이라 에스피언만 가능해요. 밤에 다시 와보세요.)' if is_day else '(밤이라 블래키만 가능해요. 낮에 다시 와보세요.)', font = ('맑은 고딕', 7), fg = '#888').pack(anchor = 'w')
                        return None
                    et = tk.Label.state.get('element_train', {
                        'electric': 0,
                        'water': 0,
                        'fire': 0 })
                    self._predict_eevee_branch() = tk.Label if tied else tk.Label
                    predicted_kr = sp['branches'][predicted]['kr']
                    None(parent, text = f'''지금 진화하면 예상: {predicted_kr} (원소 훈련 기준)''', font = ('맑은 고딕', 8), fg = '#555').pack(anchor = 'w', pady = (4, 2))
                    None(parent, text = '진화!', state = tk.NORMAL if cstatus.get('ready') else tk.DISABLED, command = (lambda p = predicted, pk = predicted_kr: None(p, pk))).pack(anchor = 'w', pady = (2, 4))
                    return None
                nxt = None['next_entry']
                None(parent, text = f'''🤝 장착된 동료예요. 다음 진화: {nxt.get('kr', '?')}\n진행도: {min(cstatus['elapsed_days'], cstatus['days_needed']):.1f} / {cstatus['days_needed']:.1f}일  (본체와 같은 속도예요)''', font = ('맑은 고딕', 8), fg = '#1a6b1a', justify = 'left', wraplength = 340).pack(anchor = 'w', pady = (0, 4))
            
                def _do_evolve_companion(dd = d):
                    '''PikaPet'''
                    if not None('PikaPet', f'''정말 {POKEDEX.get(dd, { }).get('kr', '?')}을(를) 진화시킬까요?'''):
                        return None
                    if messagebox.askyesno.evolve_companion(dd):
                        None()
                        return None
                    None('PikaPet', '아직 진화 조건을 채우지 못했어요.')

                None(parent, text = '진화!', state = tk.NORMAL if cstatus.get('ready') else tk.DISABLED, command = _do_evolve_companion).pack(anchor = 'w', pady = (0, 4))
                return None
            if not None:
                None(parent, text = '아직 만나지 못한 포켓몬이에요.', font = ('맑은 고딕', 8), fg = '#888').pack(anchor = 'w')
                return None
            entry_chain_len = None.get('chain_len', 1)
            entry_stage = entry.get('stage', 0)
            if d == EEVEE_BASE_DEX:
                None(parent, text = '이 포켓몬을 동료로 장착하면 진화 타이머가 시작되고, 본체와 똑같이\n부스터/샤미드/쥬피썬더/에스피언/블래키 갈래를 직접 골라 진화시킬 수 있어요.', font = ('맑은 고딕', 8), fg = '#888', justify = 'left', wraplength = 340).pack(anchor = 'w')
                return None
            if None in EEVEE_DEX_SET:
                None(parent, text = '이미 최종 진화 단계예요.', font = ('맑은 고딕', 8), fg = '#888').pack(anchor = 'w')
                return None
            if None < 2 or entry_stage >= entry_chain_len - 1:
                None(parent, text = '이미 최종 진화 단계이거나, 원래 진화하지 않는 종이에요.', font = ('맑은 고딕', 8), fg = '#888').pack(anchor = 'w')
                return None
            if None in COMPANION_EVOLVE_EXCLUDE:
                None(parent, text = '갈래가 여러 개로 나뉘는 종이라 동료 자동진화 대상이 아니에요.', font = ('맑은 고딕', 8), fg = '#888').pack(anchor = 'w')
                return None
            None(parent, text = '이 포켓몬을 동료로 장착하면 진화 타이머가 시작돼요.\n(도감 탭 → 하단 장착 칸에서 장착할 수 있어요)', font = ('맑은 고딕', 8), fg = '#888', justify = 'left', wraplength = 340).pack(anchor = 'w')

    
        def _render(d):
            '''정보 없음'''
            None()
            entry = POKEDEX.get(d)
            if not entry:
                None(inner, text = '정보 없음').pack(pady = 20)
                return None
            status = _clear_inner.get(str(d))
            if not bool(status):
                bool(status)
            known = d == body_dex_now
            if known and None(d):
                info = BODY_CHAIN_LOOKUP[d]
                if info['kind'] == 'stage':
                    known = info['stage'] <= own_stage_idx
                elif own_stage_idx >= 1:
                    own_stage_idx >= 1
                known = own_branch == info.get('branch')
            name = entry['kr'] if known else '？？？'
            if not d == body_dex_now and self.state.get('mega_evolved') and self.state.get('custom_body_dex'):
                if not self.mega_display_name_for():
                    self.mega_display_name_for()
                name = name
            None(inner, text = f'''No.{d:03d}  {name}''', font = ('맑은 고딕', 13, 'bold')).pack(anchor = 'w', pady = (4, 2))
            raised_lineage = self._raised_lineage_text(d)
            if raised_lineage:
                None(inner, text = f'''🌟 직접 키운 계보: {raised_lineage}  (능력치 +{int(round((RAISED_STAT_BONUS_MULT - 1) * 100))}%)''', font = ('맑은 고딕', 8, 'bold'), fg = '#c07a1a', justify = 'left', wraplength = 340).pack(anchor = 'w', pady = (0, 4))
            chain_row = None(inner)
            chain_row.pack(anchor = 'w', pady = (2, 8))
            stat_frame = None(inner, text = '단계별 능력치 / 최대 레벨', padx = 8, pady = 6)
            stat_frame.pack(fill = 'x', pady = (0, 10))
            action_frame = None(inner, text = '진화 조건 / 진화하기', padx = 8, pady = 6)
            action_frame.pack(fill = 'x', pady = (0, 10))
            None(action_frame, d, entry, status)
            if known:
                if entry.get('desc'):
                    None(inner, text = entry.get('desc', ''), font = ('맑은 고딕', 8), fg = '#666', wraplength = 340, justify = 'left').pack(anchor = 'w', pady = (0, 10))
                    return None
                return _render_action
            return _render_action

    
        def _on_select(evt = None):
            sel = listbox.curselection()
            if sel:
                d = ()
                _st = rows[sel[0]]
                if d is not None:
                    None(d)
                    return None
                return None

        listbox.bind('<<ListboxSelect>>', _on_select)
        None(bottom, text = '닫기', command = win.destroy).pack()
    
        def _jump_to(dd):
            for None in enumerate(rows):
                rd = ()
                _rs = (idx,)
                if not rd == dd:
                    continue
                listbox.selection_set(idx)
                listbox.see(idx)
                None(dd)
                _render
                return None
            enumerate(rows)
            if gen_filter['v'] != 'all':
                None('all')
                for None in enumerate(rows):
                    rd = ()
                    _rs = (idx,)
                    if not rd == dd:
                        continue
                    listbox.selection_set(idx)
                    listbox.see(idx)
                    None(dd)
                    _render
                    return None
                enumerate(rows)
            None(dd)

    
        def _build_summary_bar():
            '''body'''
            for w in summary_bar.winfo_children():
                w.destroy()
            entries = [
                ('body', body_dex_now)]
            custom_dex_now = self.state.get('custom_body_dex')
            if custom_dex_now:
            
                try:
                    entries.append(('custom_body', int(custom_dex_now)))
                    dex2_now = second_body_equipped_dex(self.state)
                    if dex2_now:
                        entries.append(('body2', int(dex2_now)))
                    for raw_d in self.state.get('party', []):
                        entries.append(('companion', int(raw_d)))
                    level_up_ready_n = (lambda .0: for raw_d in .0:
    if not self.companion_level_remaining_n(raw_d) == 0:
    continue1.0)(self.state.get('party', [])())
                    evo_ready_n = 1 if self.evolution_ready() else 0
                    if custom_dex_now:
                        cst0 = self.companion_evolution_status(int(custom_dex_now))
                        if cst0.get('evolvable') and cst0.get('ready'):
                            evo_ready_n += 1
                    for raw_d in self.state.get('party', []):
                        st0 = self.companion_evolution_status(raw_d)
                        if not st0.get('evolvable'):
                            continue
                        if not st0.get('ready'):
                            continue
                        evo_ready_n += 1
                    sum
                    overview_fg = '#1a7a3a' if level_up_ready_n or evo_ready_n else '#666'
                    None(summary_bar, text = f'''📊 레벨업 가능한 동료: {level_up_ready_n}마리   ·   진화 준비 완료: {evo_ready_n}개''', font = ('맑은 고딕', 9, 'bold'), fg = overview_fg).pack(anchor = 'w', pady = (0, 4))
                    row_canvas = None(summary_bar, highlightthickness = 0, height = 92)
                    row_hscroll = None(summary_bar, orient = 'horizontal', command = row_canvas.xview)
                    row_canvas.configure(xscrollcommand = row_hscroll.set)
                    row_canvas.pack(side = 'top', fill = 'x')
                    row_hscroll.pack(side = 'top', fill = 'x')
                    row = None(row_canvas)
                    row_win_id = row_canvas.create_window((0, 0), window = row, anchor = 'nw')
                
                    def _on_row_configure(evt = None):
                        '''all'''
                        row_canvas.configure(scrollregion = row_canvas.bbox('all'), height = max(92, row.winfo_reqheight()))

                    row.bind('<Configure>', _on_row_configure)
                
                    def _row_wheel(event):
                        '''num'''
                        delta = -1 if getattr(event, 'num', 0) == 5 or event.delta < 0 else 1
                    
                        try:
                            if row_canvas.winfo_exists():
                            
                                try:
                                    row_canvas.xview_scroll(-delta, 'units')
                                    return None
                                    return None
                                except Exception:
                                    return None



                    row_canvas.bind('<Enter>', (lambda e: row_canvas.bind_all('<MouseWheel>', _row_wheel)))
                    row_canvas.bind('<Leave>', (lambda e: row_canvas.unbind_all('<MouseWheel>')))
                    row_canvas.bind('<Destroy>', (lambda e: row_canvas.unbind_all('<MouseWheel>')), add = '+')
                    for None(row, relief = 'groove', bd = 1, padx = 4, pady = 3) in entries:
                        kind = ()
                        dd = None
                        card.pack(side = 'left', padx = 3)
                        img = None(dd, True)
                        img2 = img.resize((max(8, int(img.width * 1.1)), max(8, int(img.height * 1.1))), Image.NEAREST)
                        tkimg = None(img2)
                        lbl = None(card, image = tkimg, cursor = 'hand2')
                        lbl.image = tkimg
                        lbl.pack()
                        lbl.bind('<Button-1>', (lambda ev, dd = dd: None(dd)))
                        if kind == 'body':
                            pass
                        elif kind == 'body2':
                            pass
                        elif kind == 'custom_body':
                            pass
                    
                        tag = '🤝'
                        disp_kr = e.get('kr', '?')
                        if not kind == 'body' and self.state.get('mega_evolved') and custom_dex_now:
                            if not self.mega_display_name_for():
                                self.mega_display_name_for()
                            disp_kr = disp_kr
                        elif kind == 'body2' and self.state.get('mega_body2'):
                            names = MEGA_NAME_KR.get(dd)
                            if isinstance(names, dict):
                                if not names.get('x'):
                                    names.get('x')
                                disp_kr = disp_kr
                            elif names:
                                disp_kr = names
                            else:
                                disp_kr = f'''{disp_kr}✨'''
                        raised_prefix = '🌟' if self._is_raised(dd) else ''
                        None(card, text = f'''{tag}{raised_prefix}{disp_kr}''', font = ('맑은 고딕', 7, 'bold')).pack()
                        if kind == 'body':
                            lvl_txt = f'''Lv.{self.player_level()}'''
                        elif kind == 'custom_body':
                            lvl_txt = f'''Lv.{self.body1_effective_level()}'''
                        elif kind == 'body2':
                            lvl_txt = f'''Lv.{self.player_level()}(본체 동일)'''
                        else:
                            lvl_txt = self._companion_level_short_text(dd)
                        None(card, text = lvl_txt, font = ('맑은 고딕', 7), fg = '#3a5a9a').pack()
                        ready = False
                        final = False
                        cond_txt = '-'
                        if kind == 'body':
                            sp = SPECIES[own_species]
                            max_stage = 1 if sp.get('branching') else len(sp['stages']) - 1
                            final = own_stage_idx >= max_stage
                            if not final:
                                not final
                            ready = self.evolution_ready()
                            if final:
                                pass
                            elif ready:
                                pass
                        
                            cond_txt = '진행중'
                        elif kind == 'body2':
                            cond_txt = '본체(레벨 공유)'
                        else:
                            st = self.companion_evolution_status(dd)
                        None(card, text = cond_txt, font = ('맑은 고딕', 7), fg = '#1a7a3a' if ready else '#888').pack()
                        if not ready:
                            continue
                        if kind == 'body' and SPECIES[own_species].get('branching'):
                            None(card, text = '선택하러 가기', font = ('맑은 고딕', 7), command = (lambda dd = dd: None(dd))).pack(fill = 'x', pady = (2, 0))
                            continue
                        if kind == 'body':
                        
                            def _do_body_evolve():
                                '''PikaPet'''
                                if not None('PikaPet', '정말 진화시킬까요? (되돌릴 수 없어요)'):
                                    return None
                                messagebox.askyesno.evolve()
                                None()

                            None(card, text = '진화!', font = ('맑은 고딕', 7, 'bold'), fg = '#a83a8a', command = _do_body_evolve).pack(fill = 'x', pady = (2, 0))
                            continue
                        if kind == 'custom_body':
                        
                            def _do_custom_body_evolve():
                                '''PikaPet'''
                                if not None('PikaPet', '정말 진화시킬까요? (되돌릴 수 없어요)'):
                                    return None
                                if messagebox.askyesno.evolve_custom_body():
                                    None()
                                    return None

                            None(card, text = '진화!', font = ('맑은 고딕', 7, 'bold'), fg = '#a83a8a', command = _do_custom_body_evolve).pack(fill = 'x', pady = (2, 0))
                            continue
                    
                        def _do_comp_evolve(dd = dd):
                            '''PikaPet'''
                            if not None('PikaPet', f'''정말 {POKEDEX.get(dd, { }).get('kr', '?')}을(를) 진화시킬까요?'''):
                                return None
                            if messagebox.askyesno.evolve_companion(dd):
                                None()
                                return None

                        None(card, text = '진화!', font = ('맑은 고딕', 7, 'bold'), fg = '#a83a8a', command = _do_comp_evolve).pack(fill = 'x', pady = (2, 0))
                    tk.Button
                    return None
                except Exception:
                    continue
                    except Exception:
                        continue


        None()
        auto_d = None
        shown = False
        if auto_d is not None:
            for rd, _rs in enumerate(rows):
                if not rd == auto_d:
                    continue
                listbox.selection_set(idx)
                listbox.see(idx)
                None(auto_d)
                shown = True
                _render
            enumerate(rows)
        if not shown:
            None(inner, text = '왼쪽 목록에서 포켓몬을 골라보세요.\n🏠 = 현재 본체   🤝 = 장착된 동료   🧬 = 이브이 계열   🌱 = 직접 키운 개체', font = ('맑은 고딕', 9), fg = '#888', justify = 'left').pack(pady = 30)
            return None
        return tk.Scrollbar if self.evolution_ready() else tk.Frame
    except Exception:
        tk.Frame
        continue
        except Exception:
            _rebuild_list
            continue
