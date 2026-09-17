# module.PetApp.open_mega_evolve
# source line 12403
# Recovered from bytecode; default argument values are not shown.

def open_mega_evolve(self):
    win = None(self.root)
    win.title('메가진화')
    resolve_species_win(win, 360, 440)
    bottom = None(win)
    bottom.pack(side = 'bottom', pady = 10)
    body = None(win)
    body.pack(side = 'top', fill = 'both', expand = True, padx = 14, pady = (14, 0))
    conf = self.stage_conf()
    None(body, text = '💎 메가진화', font = ('맑은 고딕', 13, 'bold')).pack(pady = (0, 6))
    if self.state.get('mega_evolved'):
        starter_kr = self.starter_stage_conf().get('kr', '스타터')
        None(body, text = f'''{starter_kr}는 이미 메가진화 상태예요!\n능력치 상한선이 약 2배로 강해졌고,\n동료도 7칸까지 데리고 다닐 수 있어요.\n(오로라 효과 강도는 설정에서 바꿀 수 있어요)''', font = ('맑은 고딕', 9), justify = 'left', fg = '#333', wraplength = 310).pack(pady = 8)
        if not self.mega_has_dual_form() and self.state.get('custom_body_dex'):
            if not self.mega_display_name_for():
                self.mega_display_name_for()
            form_label_var = None(value = f'''지금 폼: {'?'}''')
            None(body, textvariable = form_label_var, font = ('맑은 고딕', 9, 'bold'), fg = '#7a3fc4').pack(pady = (2, 4))
            form_row = None(body)
            form_row.pack(pady = (0, 6))
        
            def _switch_mega_form(f):
                '''mega_form'''
                if self.state.get('mega_form') == f:
                    return None
                self.state['mega_form'] = None
                self.save_state()
            
                try:
                    self.redraw()
                    if not self.mega_display_name_for():
                        self.mega_display_name_for()
                    form_label_var.set(f'''지금 폼: {'?'}''')
                    return None
                except Exception:
                    continue


            if not self.mega_display_name_for('x'):
                self.mega_display_name_for('x')
            x_name = 'X폼'
            if not self.mega_display_name_for('y'):
                self.mega_display_name_for('y')
            y_name = 'Y폼'
            None(form_row, text = f'''💠 {x_name}''', wraplength = 140, justify = 'center', command = (lambda : None('x'))).pack(side = 'left', padx = 4)
            None(form_row, text = f'''💠 {y_name}''', wraplength = 140, justify = 'center', command = (lambda : None('y'))).pack(side = 'left', padx = 4)
            None(body, text = '※ 폼은 횟수 제한 없이 아무 때나 서로 바꿀 수 있어요.', font = ('맑은 고딕', 8), fg = '#888', justify = 'left', wraplength = 310).pack(pady = (0, 4))
        if self.state.get('custom_body_dex'):
            None(body, text = '※ 지금은 본체를 다른 포켓몬으로 바꿔서 보여주는 중이라\n메가진화(오로라/전용 그림/이름/능력치 배율)는 원래\n스타터로 돌아왔을 때만 적용돼요. 지금 나와있는 본체는\n그 종 자신의 레벨/능력치를 그대로 써요(상한선 없음).', font = ('맑은 고딕', 8), justify = 'left', fg = '#7a3fc4', wraplength = 310).pack(pady = (0, 6))
        None(bottom, text = '닫기', command = win.destroy).pack()
        self._add_opacity_control(win)
        return None
    reasons = tk.Label
    if not is_final_stage(self.state):
        reasons.append('· 최종 진화(예: 거북왕)까지 진화해야 해요.')
    elif self.player_level() < MAX_PLAYER_LEVEL:
        reasons.append(f'''· 지금 형태에서 레벨 {MAX_PLAYER_LEVEL}까지 올려야 해요. (지금 레벨 {self.player_level()})''')
    if not all_gen1_caught(self.state):
        n = len(self.state.get('caught', { }))
        reasons.append(f'''· 1세대 포켓몬 151마리를 전부 잡아야 해요. (지금 {n}/151)''')
    if reasons:
        None(body, text = '아직 메가진화 조건을 다 채우지 못했어요:', font = ('맑은 고딕', 9, 'bold'), fg = '#a00000').pack(anchor = 'w', pady = (4, 4))
        for r in reasons:
            None(body, text = r, font = ('맑은 고딕', 9), fg = '#555', justify = 'left', wraplength = 310).pack(anchor = 'w', pady = 1)
        reasons
        None(bottom, text = '닫기', command = win.destroy).pack()
        self._add_opacity_control(win)
        return None
    my_element = tk.Frame.current_element()
    candidates = self.mega_sacrifice_candidates()
    None(body, text = f'''조건은 다 채웠어요! 이제 같은 속성({TYPE_KR.get(my_element, my_element)}) 레벨{MAX_PLAYER_LEVEL} 포켓몬 {MEGA_SACRIFICE_N}마리를 재물로 바치면 메가진화할 수 있어요.\n재물로 바친 포켓몬은 도감 기록(잡았다는 사실)은 그대로 남고, 더 이상 장착만 못 하게 돼요.''', font = ('맑은 고딕', 9), fg = '#333', justify = 'left', wraplength = 310).pack(pady = (4, 8))
    if len(candidates) < MEGA_SACRIFICE_N:
        None(body, text = f'''아직 조건에 맞는 포켓몬이 {len(candidates)}/{MEGA_SACRIFICE_N}마리뿐이에요.\n같은 속성의 포켓몬을 야생에서 레벨{MAX_PLAYER_LEVEL}로 더 잡아주세요.''', font = ('맑은 고딕', 9), fg = '#a00000', justify = 'left', wraplength = 310).pack(pady = 6)
        None(bottom, text = '닫기', command = win.destroy).pack()
        self._add_opacity_control(win)
        return None
    list_frame = None(body, relief = 'groove', bd = 1)
    list_frame.pack(fill = 'both', expand = True, pady = 6)
    canvas = None(list_frame, height = 170, highlightthickness = 0)
    vsb = None(list_frame, orient = 'vertical', command = canvas.yview)
    inner = None(canvas)
    inner.bind('<Configure>', (lambda e: canvas.configure(scrollregion = canvas.bbox('all'))))
    canvas.create_window((0, 0), window = inner, anchor = 'nw')
    canvas.configure(yscrollcommand = vsb.set)
    canvas.pack(side = 'left', fill = 'both', expand = True)
    vsb.pack(side = 'right', fill = 'y')
    check_vars = { }
    for d in candidates:
        e = POKEDEX.get(d, { })
        v = None(value = False)
        check_vars[d] = v
        None(inner, text = f'''No.{d:03d} {e.get('kr', '?')} (Lv.{MAX_PLAYER_LEVEL})''', variable = v, anchor = 'w').pack(anchor = 'w', fill = 'x')
    tk.BooleanVar
    count_var = None(value = f'''선택: 0/{MEGA_SACRIFICE_N}''')
    None(body, textvariable = count_var, font = ('맑은 고딕', 9, 'bold')).pack(pady = (4, 2))

    def _refresh_count():
        n = (lambda .0: for None in .0:
    v = Noneif not v.get():
    continue1)(check_vars.values()())
        count_var.set(f'''선택: {n}/{MEGA_SACRIFICE_N}''')

    for v in check_vars.values():
        v.trace_add('write', (lambda : None()))
    tk.Label

    def _confirm():
        '''PikaPet'''
        for None in :
            d = ()
            v = None
            if not v.get():
                continue
    
        , [], chosen, d = check_vars.items(), d, v
        v = None
        if len(chosen) != MEGA_SACRIFICE_N:
            None('PikaPet', f'''정확히 {MEGA_SACRIFICE_N}마리를 골라주세요.''')
            return None
        if not None('메가진화', f'''고른 {MEGA_SACRIFICE_N}마리를 재물로 바치고 메가진화할까요?\n(도감 기록은 남지만, 더는 장착할 수 없게 돼요)'''):
            return None
        if None.askyesno.mega_has_dual_form():
            form = self._ask_mega_form_choice()
            if form is None:
                return None
            self.state['mega_form'] = None
        ok = ()
        msg = self.do_mega_evolve(chosen)
        None('PikaPet', msg)
        if ok:
            win.destroy()
            return None
        return messagebox.showinfo
    

    None(bottom, text = '메가진화하기!', command = _confirm).pack(side = 'left', padx = 4)
    None(bottom, text = '닫기', command = win.destroy).pack(side = 'left', padx = 4)
    self._add_opacity_control(win)
