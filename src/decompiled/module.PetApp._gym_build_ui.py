# module.PetApp._gym_build_ui
# source line 17059
# Recovered from bytecode; default argument values are not shown.

def _gym_build_ui(self, gctx):
    win = gctx['win']
    for w in win.winfo_children():
        w.destroy()
    g = gctx['gym']
    win.title(f'''{g['name']} - 전투 중!''' + ' (재미 도전)' if gctx.get('fun_mode') else '')

    try:
        win.attributes('-topmost', True)
        resolve_species_win(win, 460, 560)
        outer = None(win)
        outer.pack(fill = 'both', expand = True)
        bottom_bar = None(outer)
        bottom_bar.pack(side = 'bottom', fill = 'x', padx = 10, pady = 8)
        body = None(outer)
        body.pack(side = 'top', fill = 'both', expand = True, padx = 10, pady = (10, 0))
        None(body, text = g['name'], font = ('맑은 고딕', 12, 'bold')).pack(pady = (2, 6))
        if gctx.get('fun_mode'):
            None(body, text = '🎮 재미 도전 - 이기든 지든 보상은 없어요!', font = ('맑은 고딕', 8, 'bold'), fg = '#a8681a').pack(pady = (0, 4))
        face_row = None(body)
        face_row.pack(pady = (0, 6))
        trainer_img = load_static_image(gym_trainer_image_path(g), target_h = 92)
        trainer_label = None(face_row)
        trainer_label.pack(side = 'left', padx = (0, 12))
        sprite_row = None(face_row)
        sprite_row.pack(side = 'left')
        p_img_label = None(sprite_row)
        p_img_label.pack(side = 'left', padx = 6)
        None(sprite_row, text = '⚔', font = ('맑은 고딕', 14, 'bold')).pack(side = 'left', padx = 4)
        e_img_label = None(sprite_row)
        e_img_label.pack(side = 'left', padx = 6)
        gctx['p_img_label'] = p_img_label
        gctx['e_img_label'] = e_img_label
        e_card = None(body, text = '상대 체육관', padx = 8, pady = 6)
        e_card.pack(fill = 'x')
        e_name_var = None()
        None(e_card, textvariable = e_name_var, font = ('맑은 고딕', 10, 'bold'), fg = '#a03030').pack(anchor = 'w')
        e_stat_var = None()
        None(e_card, textvariable = e_stat_var, font = ('맑은 고딕', 8), fg = '#7a1a1a').pack(anchor = 'w')
        e_pb = None(e_card, length = 300, maximum = 100, value = 100)
        e_pb.pack(fill = 'x', pady = (4, 2))
        e_roster_var = None()
        None(e_card, textvariable = e_roster_var, font = ('맑은 고딕', 8), fg = '#888').pack(anchor = 'w')
        p_card = None(body, text = '내 팀', padx = 8, pady = 6)
        p_card.pack(fill = 'x', pady = (10, 0))
        p_name_var = None()
        None(p_card, textvariable = p_name_var, font = ('맑은 고딕', 10, 'bold'), fg = '#1a4a8a').pack(anchor = 'w')
        p_stat_var = None()
        None(p_card, textvariable = p_stat_var, font = ('맑은 고딕', 8), fg = '#1a3a6a').pack(anchor = 'w')
        p_pb = None(p_card, length = 300, maximum = 100, value = 100)
        p_pb.pack(fill = 'x', pady = (4, 2))
        p_roster_var = None()
        None(p_card, textvariable = p_roster_var, font = ('맑은 고딕', 8), fg = '#888').pack(anchor = 'w')
        log_var = None(value = f'''🎮 {g['name']}에 재미로 재도전! 순서대로 한 마리씩 싸워요. (보상 없음)''' if gctx.get('fun_mode') else f'''{g['name']}에 도전합니다! 순서대로 한 마리씩 싸워요.''')
        None(body, textvariable = log_var, font = ('맑은 고딕', 9), fg = '#333', wraplength = 400, justify = 'left', anchor = 'w').pack(fill = 'x', pady = (10, 0))
    
        def _roster_line(roster, hp_list, active):
            parts = []
            for None in enumerate(roster):
                i = ()
                m = None
                if i == active and hp_list[i] > 0:
                    pass
                elif hp_list[i] <= 0:
                    pass
            
            '✕'
            return '  '.join(parts)

    
        def _refresh():
            '''e_active'''
            ei = gctx['e_active']
            pi = gctx['p_active']
            if ei < len(gctx['enemy']):
                em = gctx['enemy'][ei]
                e_name_var.set(f'''{em['name']} Lv.{em['level']}''')
                e_stat_var.set(f'''체력 {max(0, gctx['e_hp'][ei])}/{gctx['e_hp_max'][ei]}   공 {em['bs']['atk']}  방 {em['bs']['def']}  크리 {em['bs']['crit']:.0f}%''')
                e_pb.configure(value = max(0, gctx['e_hp'][ei]), maximum = gctx['e_hp_max'][ei])
            _roster_line(None(gctx['enemy'], gctx['e_hp'], ei))
            if pi < len(gctx['player']):
                pm = gctx['player'][pi]
                tag = ' 💎' if pm.get('mega') else ''
                p_name_var.set(f'''{pm['name']}{tag} Lv.{pm['level']}''')
                p_stat_var.set(f'''체력 {max(0, gctx['p_hp'][pi])}/{gctx['p_hp_max'][pi]}   공 {pm['bs']['atk']}  방 {pm['bs']['def']}  크리 {pm['bs']['crit']:.0f}%''')
                p_pb.configure(value = max(0, gctx['p_hp'][pi]), maximum = gctx['p_hp_max'][pi])
            _roster_line(None(gctx['player'], gctx['p_hp'], pi))
            self._gym_render_sprites(gctx)

        gctx['ui']['refresh'] = _refresh
        gctx['ui']['set_log'] = log_var.set
        None()
        btn_row = None(bottom_bar)
        btn_row.pack()
        ult_btn = None(btn_row, text = '✨ 필살기', width = 10, command = (lambda : self._gym_action(gctx, 'ultimate')))
        ult_btn.grid(row = 0, column = 0, padx = 3, pady = 2)
        atk_btn = None(btn_row, text = '⚔ 공격', width = 10, command = (lambda : self._gym_action(gctx, 'attack')))
        atk_btn.grid(row = 0, column = 1, padx = 3, pady = 2)
        def_btn = None(btn_row, text = '🛡 방어', width = 10, command = (lambda : self._gym_action(gctx, 'defend')))
        def_btn.grid(row = 1, column = 0, padx = 3, pady = 2)
        give_btn = None(btn_row, text = '🏳 기권', width = 10, command = (lambda : self._gym_concede(gctx)))
        give_btn.grid(row = 1, column = 1, padx = 3, pady = 2)
    
        def _set_locked(locked):
            '''disabled'''
            state = 'disabled' if locked else 'normal'
            for b in (ult_btn, atk_btn, def_btn, give_btn):
                b.configure(state = state)
            return None
            except Exception:
                continue

        gctx['ui']['set_locked'] = _set_locked
    
        def _refresh_ult():
            '''p_active'''
            used = gctx['p_active'] in gctx['p_ult_used']
        
            try:
                if used:
                
                    try:
                        pass
                    if not used:
                    
                        try:
                            if gctx['flags']['locked']:
                            
                                try:
                                    pass
                                return None
                                except Exception:
                                    ult_btn.configure
                                    return None





        gctx['ui']['refresh_ult'] = _refresh_ult
        None()
        return None
    except Exception:
        continue
