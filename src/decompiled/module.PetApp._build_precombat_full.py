# module.PetApp._build_precombat_full
# source line 10414
# Recovered from bytecode; default argument values are not shown.

def _build_precombat_full(self, ctx):
    win = ctx['win']
    for w in win.winfo_children():
        w.destroy()

    try:
        win.withdraw()
        win.overrideredirect(False)
        win.title('야생 포켓몬과 조우!')
    
        try:
            win.attributes('-topmost', True)
            ctx['mode'] = 'precombat'
            resolve_species_win(win, 480, 580)
        
            try:
                win.deiconify()
                win.protocol('WM_DELETE_WINDOW', (lambda : self._close_battle(ctx, caught = False, entered_fight = False)))
                entry = ctx['entry']
                wild_level = ctx['wild_level']
                wild_bs = ctx['wild_bs']
                wild_name = ctx['wild_name']
                player_entry = ctx['player_entry']
                outer = None(win)
                outer.pack(fill = 'both', expand = True)
                bottom_bar = None(outer)
                bottom_bar.pack(side = 'bottom', fill = 'x', padx = 10, pady = 8)
                body = None(outer)
                body.pack(side = 'top', fill = 'both', expand = True, padx = 10, pady = (10, 0))
                card = None(body, text = f'''야생 {wild_name} 발견! (Lv.{wild_level})''', padx = 10, pady = 8)
                card.pack(fill = 'x')
                img_row = None(card)
                img_row.pack(side = 'left')
                wild_img_label = None(img_row)
                wild_img_label.pack()
                _wild_frame_ok = False
                if ctx['wild_aset'] is not None:
                    frame = ctx['wild_aset'].frame(entry['idle'], 0, spriteanim.DIR_DOWN)
                    if frame is not None:
                        frame = add_level_glow(frame.convert('RGBA'), wild_level)
                        _portrait_scale = 1.6 * sprite_extra_scale(entry.get('dex'))
                        frame = frame.resize((max(8, int(frame.width * _portrait_scale)), max(8, int(frame.height * _portrait_scale))), Image.NEAREST)
                        tkimg = None(frame)
                        wild_img_label.image = tkimg
                        wild_img_label.configure(image = tkimg)
                        _wild_frame_ok = True
                if not _wild_frame_ok:
                    ph = draw_pokeball_image(96)
                    tkimg = None(ph)
                    wild_img_label.image = tkimg
                    wild_img_label.configure(image = tkimg)
                info_col = None(card)
                info_col.pack(side = 'left', padx = (14, 0), fill = 'both', expand = True)
                types_txt = (lambda .0: for t in .0:
    TYPE_KR.get(t, t).0)(entry.get('types', [
                    entry.get('element', 'normal')])())
                my_atk_mult = self.my_type_effect_mult(pokedex_types(entry))
                wild_atk_mult = type_effect_multiplier(pokedex_types(entry)[0], [
                    self.current_element()])
                None(info_col, text = f'''상대 타입: {types_txt}''', anchor = 'w', font = ('맑은 고딕', 9, 'bold'), wraplength = 240, justify = 'left').pack(fill = 'x')
                None(info_col, text = f'''상대 HP {wild_bs['hp']}  공격 {type_adjusted_atk_text(wild_bs['atk'], wild_atk_mult)}  방어 {wild_bs['def']}  크리 {wild_bs['crit']:.0f}%''', anchor = 'w', font = ('맑은 고딕', 9), wraplength = 240, justify = 'left').pack(fill = 'x', pady = (2, 0))
                if my_atk_mult > wild_atk_mult + 0.05:
                    matchup_color = '#1a6b1a'
                    matchup_txt = '🔺 상성: 내가 유리해요'
                elif wild_atk_mult > my_atk_mult + 0.05:
                    matchup_color = '#a03030'
                    matchup_txt = '🔻 상성: 내가 불리해요'
                else:
                    matchup_color = '#777'
                    matchup_txt = '◾ 상성: 비슷해요'
                None(info_col, text = matchup_txt, anchor = 'w', font = ('맑은 고딕', 8, 'bold'), fg = matchup_color, wraplength = 220, justify = 'left').pack(fill = 'x', pady = (1, 0))
                pb = ctx['player_bs']
                None(info_col, text = f'''내 {self.display_name()} (Lv.{ctx['player_level_disp']})''', anchor = 'w', font = ('맑은 고딕', 9, 'bold'), fg = '#1a4a8a', wraplength = 240, justify = 'left').pack(fill = 'x', pady = (8, 0))
                None(info_col, text = f'''내 HP {pb['hp']}  공격 {type_adjusted_atk_text(pb['atk'], my_atk_mult)}  방어 {pb['def']}  크리 {pb['crit']:.0f}%''', anchor = 'w', font = ('맑은 고딕', 9), fg = '#1a4a8a', wraplength = 240, justify = 'left').pack(fill = 'x')
                if entry.get('legendary'):
                    None(info_col, text = '⭐ 전설의 포켓몬 - 잡으려면 강한 동료가 많이 필요해요!', fg = '#b8860b', anchor = 'w', font = ('맑은 고딕', 9, 'bold'), wraplength = 240, justify = 'left').pack(fill = 'x', pady = (6, 0))
                setup_frame = None(body, text = '⚔ 전투 전 동료 세팅 (전투 시작 전에만 바꿀 수 있어요)', padx = 10, pady = 8)
                setup_frame.pack(fill = 'both', expand = True, pady = (10, 0))
                slot_cap = companion_slot_count(self.state)
                caught_dex_all = (lambda .0: for d in .0:
    int(d).0)(self.state.get('caught', { }).keys()())
                check_vars = { }
                list_holder = None(setup_frame)
                list_holder.pack(fill = 'both', expand = True)
                canvas = None(list_holder, height = 130, highlightthickness = 0)
                vsb = None(list_holder, orient = 'vertical', command = canvas.yview)
                inner = None(canvas)
                inner.bind('<Configure>', (lambda e: canvas.configure(scrollregion = canvas.bbox('all'))))
                canvas.create_window((0, 0), window = inner, anchor = 'nw')
                canvas.configure(yscrollcommand = vsb.set)
                canvas.pack(side = 'left', fill = 'both', expand = True)
                vsb.pack(side = 'right', fill = 'y')
            
                def _precombat_wheel(event):
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



            
                def _bind_precombat_wheel(_e = None):
                    '''<MouseWheel>'''
                    canvas.bind_all('<MouseWheel>', _precombat_wheel)
                    canvas.bind_all('<Button-4>', _precombat_wheel)
                    canvas.bind_all('<Button-5>', _precombat_wheel)

            
                def _unbind_precombat_wheel(_e = None):
                    '''<MouseWheel>'''
                    canvas.unbind_all('<MouseWheel>')
                    canvas.unbind_all('<Button-4>')
                    canvas.unbind_all('<Button-5>')

                canvas.bind('<Enter>', _bind_precombat_wheel)
                canvas.bind('<Leave>', _unbind_precombat_wheel)
                canvas.bind('<Destroy>', _unbind_precombat_wheel, add = '+')
                synergy_var = None()
            
                def _refresh_synergy():
                    '''caught'''
                    for None in :
                        d = ()
                        v = None
                        if not v.get():
                            continue
                
                    , [], checked, d = check_vars.items(), d, v
                    v = None
                    a = ()
                    dd = companion_synergy_bonus(checked, self.state.get('caught', { }), self.state.get('mega_party', []))
                    synergy_var.set(f'''현재 세팅 보너스: 공격 +{a:.1f}%  방어 +{dd:.1f}%  크리티컬 +{c:.1f}%p   (선택 {len(checked)}/{slot_cap}칸)''')
                    return None
                

            
                def _on_toggle(d):
                    for None in :
                        x = ()
                        v = None
                        if not v.get():
                            continue
                
                    , [], checked, x = check_vars.items(), x, v
                    v = None
                    if len(checked) > slot_cap:
                        check_vars[d].set(False)
                        None('PikaPet', f'''지금 내 레벨({self.player_level()})로는 동료를 {slot_cap}칸까지만 데려갈 수 있어요.''')
                    None()
                    return None
                

                if slot_cap <= 0:
                    None(inner, text = '아직 동료를 데려갈 수 없어요. (플레이어 레벨 2 이상 필요)', fg = '#888').pack(anchor = 'w', padx = 4, pady = 4)
                elif not caught_dex_all:
                    None(inner, text = '아직 잡은 포켓몬이 없어요. 먼저 야생 포켓몬을 잡아보세요!', fg = '#888').pack(anchor = 'w', padx = 4, pady = 4)
                else:
                    for d in caught_dex_all:
                        e = POKEDEX.get(d)
                        if not e:
                            continue
                        lv = self.state.get('caught', { }).get(str(d), { }).get('level', 1)
                        var = None(value = d in ctx['chosen_party'])
                        check_vars[d] = var
                        txt = f'''No.{d:03d} {e['kr']} (Lv.{lv}) - 공{e.get('atk', 0)}/방{e.get('def', 0)}/HP{e.get('hp', 0)}'''
                        None(inner, text = txt, variable = var, anchor = 'w', command = (lambda dd = d: None(dd))).pack(fill = 'x', padx = 4, pady = 1)
                    tk.BooleanVar
                None()
                None(setup_frame, textvariable = synergy_var, font = ('맑은 고딕', 9, 'bold'), fg = '#1a6b1a').pack(anchor = 'w', pady = (6, 0))
            
                def do_pre_flee():
                    self._close_battle(ctx, caught = False, entered_fight = False)

            
                def do_fight():
                    '''chosen_party'''
                    for None in :
                        d = ()
                        v = None
                        if not v.get():
                            continue
                
                    , [], chosen, d = check_vars.items(), d, v
                    v = None
                    ctx['chosen_party'] = chosen
                    a = ()
                    dd = companion_synergy_bonus(chosen, self.state.get('caught', { }), self.state.get('mega_party', []))
                    ctx['player_bs']['hp'] = self.player_battle_stats(atk_pct = a, def_pct = dd, crit_bonus = c)
                    ctx['hp']['player'] = ctx['player_bs']['hp']
                    self._apply_body2_to_ctx(ctx, chosen)
                    ctx['active'] = 'player'
                    self._build_combat_full(ctx)
                    return None
                

                None(bottom_bar, text = '⚔ Fight!', width = 16, bg = '#ffd54a', command = do_fight).pack(side = 'left', padx = 6)
                None(bottom_bar, text = '🏳 도망', width = 16, command = do_pre_flee).pack(side = 'left', padx = 6)
                return None
                except Exception:
                    tk.Button
                    continue
                except Exception:
                    tk.Button
                    continue
            except Exception:
                continue
