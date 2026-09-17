# module.PetApp._build_compact_battle
# source line 10038
# Recovered from bytecode; default argument values are not shown.

def _build_compact_battle(self, ctx):
    win = ctx['win']
    for w in win.winfo_children():
        w.destroy()

    try:
        win.overrideredirect(True)
        win.attributes('-topmost', True)
        win.configure(bg = '#fff6e0')
        ctx['mode'] = 'compact'
        _compact_h = 480 if ctx.get('has_body2') else 380
        self._position_compact(win, 300, _compact_h)
        header = None(win, bg = '#e8a53a', cursor = 'fleur')
        header.pack(side = 'top', fill = 'x')
        header_label = None(header, text = '⚡ 야생 포켓몬 조우! (드래그로 이동)', bg = '#e8a53a', fg = 'white', font = ('맑은 고딕', 9, 'bold'), cursor = 'fleur')
        header_label.pack(side = 'left', padx = 6, pady = 3)
        None(header, text = '✕', width = 2, command = (lambda : self._close_battle(ctx))).pack(side = 'right', pady = 2, padx = (0, 3))
        None(header, text = '－', width = 2, command = (lambda : self._minimize_battle(ctx))).pack(side = 'right', pady = 2)
        None(header, text = '⟲', width = 2, command = (lambda : self._position_compact(win, 300, _compact_h))).pack(side = 'right', pady = 2)
        self._bind_compact_drag(win, header, header_label)
        grip = None(win, text = '⇲', bg = '#e8a53a', fg = 'white', font = ('맑은 고딕', 9, 'bold'), cursor = 'sizing')
        grip.place(relx = 1, rely = 1, anchor = 'se', width = 16, height = 16)
        _resize_state = {
            'h': _compact_h,
            'w': 300,
            'y': 0,
            'x': 0 }
    
        def _resize_press(e):
            '''x'''
        
            try:
                _resize_state['x'] = e.x_root
                _resize_state['y'] = e.y_root
                _resize_state['w'] = win.winfo_width()
                _resize_state['h'] = win.winfo_height()
                return None
            except Exception:
                return None


    
        def _resize_motion(e):
            '''x'''
        
            try:
                dx = e.x_root - _resize_state['x']
                dy = e.y_root - _resize_state['y']
                new_w = max(220, _resize_state['w'] + dx)
                new_h = max(200, _resize_state['h'] + dy)
                win.geometry(f'''{new_w}x{new_h}''')
                return None
            except Exception:
                return None


        grip.bind('<ButtonPress-1>', _resize_press)
        grip.bind('<B1-Motion>', _resize_motion)
        expand_bar = None(win, bg = '#fff6e0')
        expand_bar.pack(side = 'bottom', fill = 'x', pady = (2, 6), padx = (0, 18))
        None(expand_bar, text = '🔍 화면 키우기', command = (lambda : self._expand_battle(ctx))).pack()
        canvas_holder = None(win, bg = '#fff6e0')
        canvas_holder.pack(side = 'top', fill = 'both', expand = True, padx = 4)
        canvas = None(canvas_holder, bg = '#fff6e0', highlightthickness = 0)
        vsb = None(canvas_holder, orient = 'vertical', command = canvas.yview)
        body = None(canvas, bg = '#fff6e0')
        body.bind('<Configure>', (lambda e: canvas.configure(scrollregion = canvas.bbox('all'))))
        canvas.create_window((0, 0), window = body, anchor = 'n')
        canvas.configure(yscrollcommand = vsb.set)
        canvas.pack(side = 'left', fill = 'both', expand = True)
        vsb.pack(side = 'right', fill = 'y')
    
        def _compact_wheel(event):
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



    
        def _bind_compact_wheel(_e = None):
            '''<MouseWheel>'''
            canvas.bind_all('<MouseWheel>', _compact_wheel)
            canvas.bind_all('<Button-4>', _compact_wheel)
            canvas.bind_all('<Button-5>', _compact_wheel)

    
        def _unbind_compact_wheel(_e = None):
            '''<MouseWheel>'''
            canvas.unbind_all('<MouseWheel>')
            canvas.unbind_all('<Button-4>')
            canvas.unbind_all('<Button-5>')

        canvas.bind('<Enter>', _bind_compact_wheel)
        canvas.bind('<Leave>', _unbind_compact_wheel)
        canvas.bind('<Destroy>', _unbind_compact_wheel, add = '+')
        has_body2 = ctx.get('has_body2', False)
        img_row = None(body, bg = '#fff6e0')
        img_row.pack(pady = (4, 2))
        player_img_label = None(img_row, bg = '#fff6e0')
        player_img_label.pack(side = 'left', padx = 6)
        body2_img_label = None(img_row, bg = '#fff6e0')
        if has_body2:
            body2_img_label.pack(side = 'left', padx = 6)
        wild_img_label = None(img_row, bg = '#fff6e0')
        wild_img_label.pack(side = 'left', padx = 6)
        wild_bs_ = ctx['wild_bs']
        wild_types_ = pokedex_types(ctx['entry'])
        wild_type_mult_ = type_effect_multiplier(wild_types_[0], [
            self.current_element()])
        None(body, text = f'''야생 {ctx['wild_name']} Lv.{ctx['wild_level']}''', bg = '#fff6e0', font = ('맑은 고딕', 9, 'bold')).pack()
        None(body, text = f'''공 {type_adjusted_atk_text(wild_bs_['atk'], wild_type_mult_)}  /  방 {wild_bs_['def']}  /  크리 {wild_bs_['crit']:.0f}%''', bg = '#fff6e0', font = ('맑은 고딕', 8), fg = '#7a4a1a').pack()
        wild_pb = None(body, length = 210, maximum = ctx['hp']['wild_max'], value = ctx['hp']['wild'])
        wild_pb.pack(pady = (4, 1))
    
        def _body_row(key, name, level, name_color):
            '''player'''
            e = body_entry(ctx, key)
            bs = body_bs(ctx, key)
            type_mult = self.my_type_effect_mult(wild_types_) if key == 'player' else type_effect_multiplier(pokedex_types(e)[0], wild_types_) + self.companion_type_bonus_pct(wild_types_) / 100
            name_var = None()
            name_lbl = None(body, textvariable = name_var, bg = '#fff6e0', font = ('맑은 고딕', 9, 'bold'), fg = name_color, wraplength = 260, justify = 'center')
            name_lbl.pack(pady = (4, 0))
            None(body, text = f'''공 {type_adjusted_atk_text(bs['atk'], type_mult)}  /  방 {bs['def']}  /  크리 {bs['crit']:.0f}%''', bg = '#fff6e0', font = ('맑은 고딕', 8), fg = name_color).pack()
            pb = None(body, length = 210, maximum = body_hp_max(ctx, key), value = body_hp(ctx, key))
            pb.pack(pady = (0, 4))
        
            def refresh():
                '''active'''
                turn_mark = '▶ ' if ctx.get('active') == key else ''
                fainted = ' (기절)' if body_hp(ctx, key) <= 0 else ''
                name_var.set(f'''{turn_mark}{name} Lv.{level}{fainted}''')
            
                try:
                    pb.configure(value = body_hp(ctx, key), maximum = body_hp_max(ctx, key))
                    return None
                except Exception:
                    return None


            None()
            return refresh

        refresh_p1_row = None('player', f'''내 {self.display_name()}''', ctx['player_level_disp'], '#1a4a8a')
        refresh_p2_row = None
        if has_body2:
            body2_name = mega_companion_display_kr(ctx.get('body2_entry', { }).get('dex'), ctx['body2_entry']) if ctx.get('body2_mega') else ctx['body2_entry'].get('kr', '2번 본체')
            refresh_p2_row = None('body2', f'''내 {body2_name}''' + ' 💎' if ctx.get('body2_mega') else '', ctx.get('body2_level_disp', 1), '#8a3a1a')
        log_var = None(value = '공격하거나, 동료를 바꾸려면 화면을 키워주세요.')
        None(body, textvariable = log_var, bg = '#fff6e0', font = ('맑은 고딕', 8), fg = '#555', wraplength = 210, justify = 'left').pack(pady = (0, 4))
        btn_row = None(body, bg = '#fff6e0')
        btn_row.pack(pady = (0, 6))
        atk_btn = None(btn_row, text = '⚔ 공격', width = 7)
        ult_btn = None(btn_row, text = '💥 필살기', width = 9, wraplength = 62, font = ('맑은 고딕', 8), justify = 'center')
        flee_btn = None(btn_row, text = '🏳 도망', width = 7)
        atk_btn.pack(side = 'left', padx = 2)
        ult_btn.pack(side = 'left', padx = 2)
        flee_btn.pack(side = 'left', padx = 2)
        WILD_TARGET_H = 62
        PLAYER_TARGET_H = 54
    
        def render(effect_side = None, crit = False):
            '''wild_aset'''
            if ctx['wild_aset'] is not None:
                frame = ctx['wild_aset'].frame(ctx['entry']['idle'], 0, spriteanim.DIR_DOWN)
                if frame is not None:
                    frame = frame.convert('RGBA')
                    if effect_side == 'wild':
                    
                        try:
                            ov = make_skill_overlay(ctx['entry'].get('element', 'normal'), 1, frame.size, boost = 2 if crit else 0)
                            frame = None(frame, ov)
                            frame = add_level_glow(frame, ctx['wild_level'])
                            s = WILD_TARGET_H / max(1, frame.height)
                            frame = frame.resize((max(8, int(frame.width * s)), max(8, int(frame.height * s))), Image.NEAREST)
                            tkimg = None(frame)
                            wild_img_label.image = tkimg
                            wild_img_label.configure(image = tkimg)
                        ph = draw_pokeball_image(WILD_TARGET_H)
                        tkimg = None(ph)
                        wild_img_label.image = tkimg
                        except:
                            ph = draw_pokeball_image(WILD_TARGET_H)
                            tkimg = None(ph)
                            wild_img_label.image = tkimg
                            wild_img_label.configure(image = tkimg)

                        aset = self.active_anim_set()
                        if aset is not None:
                            frame = aset.frame('Idle', 0, spriteanim.DIR_RIGHT)
                            if frame is not None:
                                frame = frame.convert('RGBA')
                                if effect_side == 'player':
                                
                                    try:
                                        ov = make_skill_overlay(self.current_element(), self.state.get('stage', 0), frame.size, boost = 2 if crit else 0)
                                        frame = None(frame, ov)
                                        if body_hp(ctx, 'player') <= 0:
                                            frame.putalpha(90)
                                        s = PLAYER_TARGET_H / max(1, frame.height)
                                        frame = frame.resize((max(8, int(frame.width * s)), max(8, int(frame.height * s))), Image.NEAREST)
                                        tkimg = None(frame)
                                        player_img_label.image = tkimg
                                        player_img_label.configure(image = tkimg)
                                        if has_body2:
                                            if ctx.get('body2_aset') is not None:
                                                frame = ctx['body2_aset'].frame(ctx['body2_entry'].get('idle', 'Idle'), 0, spriteanim.DIR_RIGHT)
                                                if frame is not None:
                                                    frame = frame.convert('RGBA')
                                                    if effect_side == 'body2':
                                                    
                                                        try:
                                                            ov = make_skill_overlay(ctx['body2_entry'].get('element', 'normal'), 1, frame.size, boost = 2 if crit else 0)
                                                            frame = None(frame, ov)
                                                            if body_hp(ctx, 'body2') <= 0:
                                                                frame.putalpha(90)
                                                            s = PLAYER_TARGET_H / max(1, frame.height)
                                                            frame = frame.resize((max(8, int(frame.width * s)), max(8, int(frame.height * s))), Image.NEAREST)
                                                            tkimg = None(frame)
                                                            body2_img_label.image = tkimg
                                                            body2_img_label.configure(image = tkimg)
                                                            return None
                                                            return None
                                                            return None
                                                            return None
                                                            except Exception:
                                                                Image.alpha_composite
                                                                continue
                                                            except Exception:
                                                                Image.alpha_composite
                                                                continue
                                                        except Exception:
                                                            Image.alpha_composite
                                                            continue



        None()
    
        def refresh_bars():
            '''hp'''
        
            try:
                wild_pb.configure(value = ctx['hp']['wild'])
                None()
                if refresh_p2_row:
                    None()
                    return None
                return refresh_p1_row
            except Exception:
                continue


    
        def set_log(text):
        
            try:
                log_var.set(text)
                return None
            except Exception:
                return None


    
        def set_locked(locked):
            '''disabled'''
            state_ = 'disabled' if locked else 'normal'
        
            try:
                atk_btn.configure(state = state_)
                flee_btn.configure(state = state_)
                _cur = ctx.get('active', 'player')
                if not locked:
                
                    try:
                        if ctx['flags']['ultimate_used'].get(_cur, False):
                        
                            try:
                                pass
                            return None
                            except Exception:
                                return None




    
        def _side_info(side):
            '''공격/기절 애니메이션을 재생할 때 필요한 (라벨, 스프라이트, 도감데이터, 방향, 후처리, 목표높이).'''
            if side == 'wild':
                return (wild_img_label, ctx['wild_aset'], ctx['entry'], spriteanim.DIR_DOWN, (lambda im: add_level_glow(im, ctx['wild_level'])), WILD_TARGET_H)
            if None == 'body2':
                if not has_body2:
                    return None
                return (None, ctx.get('body2_aset'), ctx.get('body2_entry', { }), spriteanim.DIR_RIGHT, None, PLAYER_TARGET_H)
            return (None, self.active_anim_set(), ctx['player_entry'], spriteanim.DIR_RIGHT, None, PLAYER_TARGET_H)

    
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
            play_sprite_action(self.root, label, aset, action, dir_idx, target_h, frame_post = post, on_done = render)

    
        def effect_faint(side):
            """방금 쓰러진 쪽 스프라이트로 '기절' 동작을 재생한다. 기절 동작이 없는 스프라이트면
    (거의 없음) 예전처럼 반투명 처리로 대신한다."""
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
            entry_faint_action(aset)(self.root, label, aset, action, dir_idx, target_h, frame_post = post, on_done = render)

    
        def refresh_ult():
            '''active'''
        
            try:
                cur = ctx.get('active', 'player')
                active_entry = body_entry(ctx, cur)
                used = ctx['flags']['ultimate_used'].get(cur, False)
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
        ult_btn.configure(command = (lambda : self._battle_action(ctx, 'ultimate')))
        flee_btn.configure(command = (lambda : self._battle_action(ctx, 'flee')))
        None()
    
        try:
            grip.lift()
            return None
            except Exception:
                render
                continue
        except Exception:
            render
            return None
