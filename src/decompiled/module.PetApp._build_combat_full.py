# module.PetApp._build_combat_full
# source line 10596
# Recovered from bytecode; default argument values are not shown.

def _build_combat_full(self, ctx):
    win = ctx['win']
    for w in win.winfo_children():
        w.destroy()

    try:
        win.withdraw()
        win.overrideredirect(False)
        win.title('야생 포켓몬과 전투 중!')
    
        try:
            win.attributes('-topmost', True)
            ctx['mode'] = 'combat'
            ctx['flags']['started'] = True
            resolve_species_win(win, 480, 600)
        
            try:
                win.deiconify()
                win.protocol('WM_DELETE_WINDOW', (lambda : self._battle_action(ctx, 'flee')))
                entry = ctx['entry']
                wild_level = ctx['wild_level']
                wild_bs = ctx['wild_bs']
                wild_name = ctx['wild_name']
                player_entry = ctx['player_entry']
                player_bs = ctx['player_bs']
                hp = ctx['hp']
                flags = ctx['flags']
                outer = None(win)
                outer.pack(fill = 'both', expand = True)
                bottom_bar = None(outer)
                bottom_bar.pack(side = 'bottom', fill = 'x', padx = 10, pady = 8)
                canvas_holder = None(outer)
                canvas_holder.pack(side = 'top', fill = 'both', expand = True)
                canvas = None(canvas_holder, highlightthickness = 0)
                vsb = None(canvas_holder, orient = 'vertical', command = canvas.yview)
                battle_frame = None(canvas)
                battle_frame.bind('<Configure>', (lambda e: canvas.configure(scrollregion = canvas.bbox('all'))))
                canvas.create_window((0, 0), window = battle_frame, anchor = 'nw')
                canvas.configure(yscrollcommand = vsb.set)
                canvas.pack(side = 'left', fill = 'both', expand = True)
                vsb.pack(side = 'right', fill = 'y')
            
                def _full_wheel(event):
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



            
                def _bind_full_wheel(_e = None):
                    '''<MouseWheel>'''
                    canvas.bind_all('<MouseWheel>', _full_wheel)
                    canvas.bind_all('<Button-4>', _full_wheel)
                    canvas.bind_all('<Button-5>', _full_wheel)

            
                def _unbind_full_wheel(_e = None):
                    '''<MouseWheel>'''
                    canvas.unbind_all('<MouseWheel>')
                    canvas.unbind_all('<Button-4>')
                    canvas.unbind_all('<Button-5>')

                canvas.bind('<Enter>', _bind_full_wheel)
                canvas.bind('<Leave>', _unbind_full_wheel)
                canvas.bind('<Destroy>', _unbind_full_wheel, add = '+')
                has_body2 = ctx.get('has_body2', False)
                img_row = None(battle_frame)
                img_row.pack(pady = 10)
                wild_img_label = None(img_row)
                wild_img_label.pack(side = 'right', padx = 20)
                body2_img_label = None(img_row)
                if has_body2:
                    body2_img_label.pack(side = 'left', padx = 10)
                player_img_label = None(img_row)
                player_img_label.pack(side = 'left', padx = 20)
            
                def render_wild(effect = False, crit = False):
                    '''wild_aset'''
                    if ctx['wild_aset'] is None:
                        ph = draw_pokeball_image(80)
                        tkimg = None(ph)
                        wild_img_label.image = tkimg
                        wild_img_label.configure(image = tkimg)
                        return None
                    frame = None['wild_aset'].frame(entry['idle'], 0, spriteanim.DIR_LEFT)
                    if frame is None:
                        frame = ctx['wild_aset'].frame(entry['idle'], 0, spriteanim.DIR_DOWN)
                    if frame is None:
                        ph = draw_pokeball_image(80)
                        tkimg = None(ph)
                        wild_img_label.image = tkimg
                        wild_img_label.configure(image = tkimg)
                        return None
                    frame = None.convert('RGBA')
                    if effect:
                    
                        try:
                            ov = make_skill_overlay(entry.get('element', 'normal'), 1, frame.size, boost = 2 if crit else 0)
                            frame = None(frame, ov)
                            frame = add_level_glow(frame, wild_level)
                            _combat_scale = 1.5 * sprite_extra_scale(entry.get('dex'))
                            frame = frame.resize((max(8, int(frame.width * _combat_scale)), max(8, int(frame.height * _combat_scale))), Image.NEAREST)
                            tkimg = None(frame)
                            wild_img_label.image = tkimg
                            wild_img_label.configure(image = tkimg)
                            return None
                        except Exception:
                            continue


            
                def render_player(effect = False, crit = False):
                    aset = self.active_anim_set()
                    if aset is None:
                        return None
                    frame = None.frame('Idle', 0, spriteanim.DIR_RIGHT)
                    if frame is None:
                        frame = aset.frame('Idle', 0, spriteanim.DIR_DOWN)
                    if frame is None:
                        return None
                    frame = None.convert('RGBA')
                    if effect:
                    
                        try:
                            ov = make_skill_overlay(self.current_element(), self.state.get('stage', 0), frame.size, boost = 2 if crit else 0)
                            frame = None(frame, ov)
                            if body_hp(ctx, 'player') <= 0:
                                frame.putalpha(90)
                            scale = self.body_display_scale() * 0.85
                            frame = frame.resize((max(8, int(frame.width * scale)), max(8, int(frame.height * scale))), Image.NEAREST)
                            tkimg = None(frame)
                            player_img_label.image = tkimg
                            player_img_label.configure(image = tkimg)
                            return None
                        except Exception:
                            continue


            
                def render_body2(effect = False, crit = False):
                    '''body2_aset'''
                    if has_body2 or ctx.get('body2_aset') is None:
                        return None
                    b2e = None['body2_entry']
                    frame = ctx['body2_aset'].frame(b2e.get('idle', 'Idle'), 0, spriteanim.DIR_RIGHT)
                    if frame is None:
                        return None
                    frame = None.convert('RGBA')
                    if effect:
                    
                        try:
                            ov = make_skill_overlay(b2e.get('element', 'normal'), 1, frame.size, boost = 2 if crit else 0)
                            frame = None(frame, ov)
                            if body_hp(ctx, 'body2') <= 0:
                                frame.putalpha(90)
                            frame = frame.resize((max(8, int(frame.width * 1.1)), max(8, int(frame.height * 1.1))), Image.NEAREST)
                            tkimg = None(frame)
                            body2_img_label.image = tkimg
                            body2_img_label.configure(image = tkimg)
                            return None
                        except Exception:
                            continue


                None()
                None()
                None()
                bars = None(battle_frame)
                bars.pack(fill = 'x', padx = 10, pady = (6, 4))
                wild_types_full = pokedex_types(entry)
            
                def _body_bar(key, name, level, color):
                    '''player'''
                    e = body_entry(ctx, key)
                    bs = body_bs(ctx, key)
                    type_mult = self.my_type_effect_mult(wild_types_full) if key == 'player' else type_effect_multiplier(pokedex_types(e)[0], wild_types_full) + self.companion_type_bonus_pct(wild_types_full) / 100
                    name_var = None()
                    None(bars, textvariable = name_var, anchor = 'w', fg = color, wraplength = 440, justify = 'left').pack(fill = 'x')
                    pb = None(bars, length = 380, maximum = body_hp_max(ctx, key), value = body_hp(ctx, key))
                    pb.pack(fill = 'x', pady = (0, 8))
                
                    def refresh():
                        '''active'''
                        turn_mark = '▶ ' if ctx.get('active') == key else ''
                        fainted = ' (기절)' if body_hp(ctx, key) <= 0 else ''
                        name_var.set(f'''{turn_mark}{name} (Lv.{level}){fainted}  공{type_adjusted_atk_text(bs['atk'], type_mult)}/방{bs['def']}/크리{bs['crit']:.0f}%''')
                    
                        try:
                            pb.configure(value = body_hp(ctx, key), maximum = body_hp_max(ctx, key))
                            return None
                        except Exception:
                            return None


                    None()
                    return refresh

                refresh_p1_bar = None('player', f'''내 {self.display_name()}''', ctx['player_level_disp'], '#1a4a8a')
                refresh_p2_bar = None
                if has_body2:
                    body2_name2 = mega_companion_display_kr(ctx.get('body2_entry', { }).get('dex'), ctx['body2_entry']) if ctx.get('body2_mega') else ctx['body2_entry'].get('kr', '2번 본체')
                    refresh_p2_bar = None('body2', f'''내 {body2_name2}''' + ' 💎' if ctx.get('body2_mega') else '', ctx.get('body2_level_disp', 1), '#8a3a1a')
                wild_atk_mult_full = type_effect_multiplier(wild_types_full[0], [
                    self.current_element()])
                None(bars, text = f'''야생 {wild_name} (Lv.{wild_level})  공{type_adjusted_atk_text(wild_bs['atk'], wild_atk_mult_full)}/방{wild_bs['def']}/크리{wild_bs['crit']:.0f}%''', anchor = 'w', wraplength = 440, justify = 'left').pack(fill = 'x')
                wild_pb = None(bars, length = 380, maximum = hp['wild_max'], value = hp['wild'])
                wild_pb.pack(fill = 'x')
                log_var = None(value = '공격 / 막기 / 필살기 중에서 골라보세요!')
                None(battle_frame, textvariable = log_var, font = ('맑은 고딕', 9), fg = '#333', wraplength = 440).pack(pady = (8, 10))
                action_row = None(bottom_bar)
                action_row.pack()
                atk_btn = None(action_row, text = '⚔ 공격', width = 10)
                def_btn = None(action_row, text = '🛡 막기', width = 10)
                ult_btn = None(action_row, text = '💥 필살기', width = 16, wraplength = 110, justify = 'center')
                flee_btn = None(action_row, text = '🏳 도망', width = 10)
                atk_btn.pack(side = 'left', padx = 4)
                def_btn.pack(side = 'left', padx = 4)
                ult_btn.pack(side = 'left', padx = 4)
                flee_btn.pack(side = 'left', padx = 4)
                all_btns = [
                    atk_btn,
                    def_btn,
                    ult_btn,
                    flee_btn]
            
                def set_locked(locked):
                    '''disabled'''
                    state_ = 'disabled' if locked else 'normal'
                    for b in all_btns:
                        b.configure(state = state_)
                    if not locked:
                        if flags['ultimate_used'].get(ctx.get('active', 'player'), False):
                        
                            try:
                                ult_btn.configure(state = 'disabled')
                                return None
                                return None
                                return None
                                except Exception:
                                    continue
                            except Exception:
                                return None


            
                def refresh_bars():
                    '''wild'''
                
                    try:
                        wild_pb.configure(value = hp['wild'])
                        None()
                        if refresh_p2_bar:
                            None()
                            return None
                        return refresh_p1_bar
                    except Exception:
                        continue


            
                def set_log(text):
                
                    try:
                        log_var.set(text)
                        return None
                    except Exception:
                        return None


            
                def _scaled_h(aset, action_name, dir_idx, scale, fallback):
                    '''그 종의 원래 그림 비율(스케일)을 유지한 채, 지금 실제로 화면에 보이는 높이(px)를 계산.
    (몸집이 큰 갸라도스 같은 애들도 공격 모션 도중에 갑자기 크기가 바뀌어 보이지 않게 하기 위함)'''
                    if aset is None:
                        return fallback
                    fr = None.frame(action_name, 0, dir_idx)
                    if fr is None:
                        return fallback
                    return None(8, int(fr.height * scale))

            
                def _side_info(side):
                    '''wild'''
                    if side == 'wild':
                        idle_act = entry.get('idle', 'Idle')
                        th = None(ctx['wild_aset'], idle_act, spriteanim.DIR_LEFT, 1.5, 80)
                        return (wild_img_label, ctx['wild_aset'], entry, spriteanim.DIR_LEFT, (lambda im: add_level_glow(im, wild_level)), th, render_wild)
                    if None == 'body2':
                        if has_body2 or ctx.get('body2_aset') is None:
                            return None
                        b2e = None['body2_entry']
                        th = None(ctx['body2_aset'], b2e.get('idle', 'Idle'), spriteanim.DIR_RIGHT, 1.1, 60)
                        return (body2_img_label, ctx['body2_aset'], b2e, spriteanim.DIR_RIGHT, None, th, render_body2)
                    scale = None.body_display_scale() * 0.85
                    aset = self.active_anim_set()
                    th = None(aset, 'Idle', spriteanim.DIR_RIGHT, scale, 70)
                    return (player_img_label, aset, player_entry, spriteanim.DIR_RIGHT, None, th, render_player)

            
                def effect(side, crit = False):
                    """공격하는 쪽 스프라이트로 실제 '공격' 동작을 재생하고, 끝나면 원래 모습으로 되돌린다."""
                    info = None(side)
                    if info is None:
                        return None
                    label = ()
                    aset = _side_info
                    ent = None
                    dir_idx = None
                    post = None
                    target_h = None
                    play_sprite_action(self.root, label, aset, action, dir_idx, target_h, frame_post = post, on_done = render_fn)

            
                def effect_faint(side):
                    """방금 쓰러진 쪽 스프라이트로 '기절' 동작을 재생한다. 기절 동작이 없으면(거의 없음)
    예전처럼 반투명 처리로 대신한다."""
                    info = None(side)
                    if info is None:
                        return None
                    label = ()
                    aset = _side_info
                    ent = None
                    dir_idx = None
                    post = None
                    target_h = None
                    if action is None:
                        None()
                        return None
                    entry_faint_action(aset)(self.root, label, aset, action, dir_idx, target_h, frame_post = post, on_done = render_fn)

            
                def refresh_ult():
                    '''active'''
                
                    try:
                        cur = ctx.get('active', 'player')
                        active_entry = body_entry(ctx, cur)
                        used = flags['ultimate_used'].get(cur, False)
                        if used:
                        
                            try:
                                pass
                            return None
                            except Exception:
                                return None



                ctx['update_ui'] = {
                    'refresh_ult': refresh_ult,
                    'effect_faint': effect_faint,
                    'effect': effect,
                    'set_locked': set_locked,
                    'set_log': set_log,
                    'refresh_bars': refresh_bars }
                atk_btn.configure(command = (lambda : self._battle_action(ctx, 'attack')))
                def_btn.configure(command = (lambda : self._battle_action(ctx, 'defend')))
                ult_btn.configure(command = (lambda : self._battle_action(ctx, 'ultimate')))
                flee_btn.configure(command = (lambda : self._battle_action(ctx, 'flee')))
                None()
                return None
                except Exception:
                    tk.Button
                    continue
                except Exception:
                    tk.Button
                    continue
            except Exception:
                continue
