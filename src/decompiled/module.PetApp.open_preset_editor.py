# module.PetApp.open_preset_editor
# source line 15163
# Recovered from bytecode; default argument values are not shown.

def open_preset_editor(self, category, on_start_label, on_start):
    if category not in PRESET_CATEGORIES:
        category = 'gym'
    win = None(self.root)
    win.title('🎒 프리셋 관리 (상황별 동료 장착)')
    resolve_species_win(win, 760, 700)

    try:
        win.geometry('760x700')
        win.minsize(680, 560)
        win.resizable(True, True)
    
        try:
            win.attributes('-topmost', True)
            state_box = {
                'pending_dex': None,
                'category': category }
            top = None(win)
            top.pack(side = 'top', fill = 'x', padx = 10, pady = (10, 4))
            None(top, text = '상황:', font = ('맑은 고딕', 9, 'bold')).pack(side = 'left')
            cat_var = None(value = PRESET_CATEGORY_LABEL.get(category, category))
            for None in :
                pass
            cat_var('readonly', textvariable = PRESET_CATEGORIES, c, state = , [], , values = c,, width = 24) = top
            cat_combo.pack(side = 'left', padx = (6, 0))
            main = None(win)
            main.pack(side = 'top', fill = 'both', expand = True, padx = 10, pady = 6)
            left = None(main, text = '내 포켓몬 (세대별, 클릭해서 고르기)', padx = 6, pady = 6)
            left.pack(side = 'left', fill = 'both', expand = True, padx = (0, 6))
            preview_frame = None(left, height = 60)
            preview_frame.pack(side = 'top', fill = 'x', pady = (0, 6))
            preview_frame.pack_propagate(False)
            preview_img_label = None(preview_frame)
            preview_img_label.pack(side = 'left', padx = (2, 8))
            preview_name_var = None(value = '포켓몬을 누르면 여기에 미리보기가 나와요.')
            None(preview_frame, textvariable = preview_name_var, font = ('맑은 고딕', 9), fg = '#a8681a', justify = 'left', anchor = 'w', wraplength = 380).pack(side = 'left', fill = 'both', expand = True)
            left_canvas = None(left, highlightthickness = 0)
            left_vsb = None(left, orient = 'vertical', command = left_canvas.yview)
            left_inner = None(left_canvas)
            left_win_id = left_canvas.create_window((0, 0), window = left_inner, anchor = 'nw')
        
            def _left_configure(evt = None):
                '''all'''
                left_canvas.configure(scrollregion = left_canvas.bbox('all'))

            left_inner.bind('<Configure>', _left_configure)
        
            def _left_canvas_configure(evt):
                left_canvas.itemconfig(left_win_id, width = evt.width)

            left_canvas.bind('<Configure>', _left_canvas_configure)
            left_canvas.configure(yscrollcommand = left_vsb.set)
            left_canvas.pack(side = 'left', fill = 'both', expand = True)
            left_vsb.pack(side = 'right', fill = 'y')
        
            def _left_wheel(event):
                '''num'''
                delta = -1 if getattr(event, 'num', 0) == 5 or event.delta < 0 else 1
            
                try:
                    if left_canvas.winfo_exists():
                    
                        try:
                            left_canvas.yview_scroll(-delta, 'units')
                            return None
                            return None
                        except Exception:
                            return None



        
            def _bind_left_wheel(_e = None):
                '''<MouseWheel>'''
                left_canvas.bind_all('<MouseWheel>', _left_wheel)
                left_canvas.bind_all('<Button-4>', _left_wheel)
                left_canvas.bind_all('<Button-5>', _left_wheel)

        
            def _unbind_left_wheel(_e = None):
                '''<MouseWheel>'''
                left_canvas.unbind_all('<MouseWheel>')
                left_canvas.unbind_all('<Button-4>')
                left_canvas.unbind_all('<Button-5>')

            left_canvas.bind('<Enter>', _bind_left_wheel)
            left_canvas.bind('<Leave>', _unbind_left_wheel)
            win.bind('<Destroy>', (lambda e: if e.widget is win:
    None()))
            right = None(main)
            right.pack(side = 'left', fill = 'both', expand = True)
            slot_box = None(right, text = '동료 슬롯 (칸을 클릭하면 왼쪽에서 고른 포켓몬이 장착돼요)', padx = 6, pady = 6)
            slot_box.pack(side = 'top', fill = 'both', expand = True)
            slot_top_row = None(slot_box)
            slot_top_row.pack(side = 'top', fill = 'x', pady = (0, 4))
            None(slot_top_row, text = '※ 같은 포켓몬은 한 세팅에 중복으로 넣을 수 없어요.', font = ('맑은 고딕', 7), fg = '#888', wraplength = 180, justify = 'left').pack(side = 'left')
        
            def _unequip_all():
                '''category'''
                cat = state_box['category']
                if not None('PikaPet', f'''{PRESET_CATEGORY_LABEL.get(cat, cat)} 세팅에 장착된 동료를\n전부 해제해서 기존(기본) 세팅으로 되돌릴까요?'''):
                    return None
                cap = messagebox.askyesno._preset_cap(cat)
                for i in range(cap):
                    self._set_preset_slot(cat, i, None)
                None()
                None()

            None(slot_top_row, text = '↩ 전체 해제\n(기존 세팅으로)', font = ('맑은 고딕', 7), justify = 'center', command = _unequip_all).pack(side = 'right')
            slot_inner = None(slot_box)
            slot_inner.pack(fill = 'both', expand = True)
            effect_box = None(right, text = '장착 효과 (본체에 적용되는 시너지 보너스)', padx = 8, pady = 8)
            effect_box.pack(side = 'bottom', fill = 'x', pady = (10, 0))
            effect_var = None(value = '')
            None(effect_box, textvariable = effect_var, font = ('맑은 고딕', 9, 'bold'), fg = '#1a4a8a', justify = 'left', anchor = 'w').pack(anchor = 'w', fill = 'x')
            bottom = None(win)
            bottom.pack(side = 'bottom', pady = 10)
        
            def _caught_sorted_list():
                '''caught'''
                caught = self.state.get('caught', { })
                out = []
                for d_str in caught.keys():
                    out.append(int(d_str))
                out.sort()
                return out
                except Exception:
                    continue

        
            def _species_icon(dex, size = 32):
                e = POKEDEX.get(dex, { })
                frame = None
            
                try:
                    aset = None(sprite_folder_path(e.get('en')))
                    frame = aset.frame(e.get('idle', 'Idle'), 0, spriteanim.DIR_DOWN)
                    if frame is None:
                        return draw_pokeball_image(size)
                    frame = spriteanim.AnimSet.convert('RGBA')
                    s = size / max(1, frame.height)
                    return frame.resize((max(8, int(frame.width * s)), max(8, int(frame.height * s))), Image.NEAREST)
                except Exception:
                    frame = None
                    continue


            preview_photo_cache = []
        
            def _render_preview():
                '''pending_dex'''
                dex = state_box['pending_dex']
                if dex is None:
                    preview_img_label.configure(image = '')
                    preview_photo_cache.clear()
                    preview_name_var.set('포켓몬을 누르면 여기에 미리보기가 나와요.')
                    return None
                e = None.get(dex, { })
                lv = self.state.get('caught', { }).get(str(dex), { }).get('level', 1)
                img = None(dex, 48)
                photo = None(img)
                preview_photo_cache.clear()
                preview_photo_cache.append(photo)
                preview_img_label.configure(image = photo)
                preview_name_var.set(f'''👉 \'{e.get('kr', '?')}\' Lv.{lv} 선택됨 - 오른쪽 슬롯 칸을 클릭하면 그 자리에 장착돼요. (다시 누르면 선택 취소)''')

        
            def _pick_species(dex):
                '''pending_dex'''
                if state_box['pending_dex'] == dex:
                    state_box['pending_dex'] = None
                else:
                    state_box['pending_dex'] = dex
                None()

        
            def _mega_on(dex):
                '''caught'''
                if not mega_companion_ready(dex, self.state.get('caught', { })):
                    None('PikaPet', f'''이 동료는 메가진화 대상 종이 아니거나, 아직 최고 레벨(Lv.{MAX_PLAYER_LEVEL})로\n잡지 못했어요. 최고 레벨 개체를 잡아서 켜보세요.''')
                    return None
                mp = (lambda .0: for x in .0:
    int(x).0)(self.state.get('mega_party', [])())
                mp.add(int(dex))
                self.state['mega_party'] = list(mp)
                self._rebuild_companions()
                self.save_state()
                None()
                None()

        
            def _mega_off(dex):
                mp = (lambda .0: for x in .0:
    int(x).0)(self.state.get('mega_party', [])())
                mp.discard(int(dex))
                self.state['mega_party'] = list(mp)
                self._rebuild_companions()
                self.save_state()
                None()
                None()

        
            def _render_left():
                '''caught'''
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
            

            slot_photo_cache = []
        
            def _unequip_slot(idx):
                '''category'''
                cat = state_box['category']
                self._set_preset_slot(cat, idx, None)
                None()
                None()

        
            def _click_slot(idx):
                '''category'''
                cat = state_box['category']
                if state_box['pending_dex'] is not None:
                    pdex = int(state_box['pending_dex'])
                    if self._dex_is_taken_by_body(pdex):
                        None('PikaPet', '지금 본체(또는 2번 본체)로 쓰고 있는 포켓몬이에요. 이미 그\n능력치를 그대로 받고 있어서, 동료로 또 장착하면 중복이라\n넣을 수 없어요.')
                        return None
                    existing_slots = None._get_preset_slots(cat)
                    if False if any is <common_constant> else (lambda .0: for None in .0:
    i2 = ()s = Noneif not i2 != idx:
    continueif s is not None:
    s is not Noneint(s) == pdex)(enumerate(existing_slots)()):
                        None('PikaPet', '이 포켓몬은 이미 이 세팅의 다른 칸에 장착돼 있어요.\n같은 포켓몬을 한 세팅에 두 번 넣을 수는 없어요.')
                        return None
                    None._set_preset_slot(cat, idx, pdex)
                    state_box['pending_dex'] = None
                else:
                    slots = self._get_preset_slots(cat)
                    if  <= 0, idx or 0, idx < len(slots):
                        pass
                
                if slots[idx]:
                    self._set_preset_slot(cat, idx, None)
                None()
                None()

        
            def _render_slots():
                '''category'''
                for w in slot_inner.winfo_children():
                    w.destroy()
                slot_photo_cache.clear()
                cat = state_box['category']
                slots = self._get_preset_slots(cat)
                caught = self.state.get('caught', { })
                for None in enumerate(slots):
                    i = ()
                    dex = None
                    None(cell, text = f'''{i + 1}번''', font = ('맑은 고딕', 8), width = 4, anchor = 'w').pack(side = 'left')
                    cell.bind('<Button-1>', (lambda e, idx = i: None(idx)))
                    for child in cell.winfo_children():
                        child.bind('<Button-1>', (lambda e, idx = i: None(idx)))
                    tk.Button if dex else tk.Label
                tk.Label
                None()

        
            def _render_effect():
                '''category'''
                cat = state_box['category']
                customized = self._preset_is_customized(cat)
                dex_list = self._get_preset_dex_list(cat)
            
                try:
                    atk_pct = ()
                    def_pct = companion_synergy_bonus(dex_list, self.state.get('caught', { }), self.state.get('mega_party', []))
                    if customized:
                        effect_var.set(f'''{PRESET_CATEGORY_LABEL.get(cat, cat)}  (최대 {cap}마리, 현재 {len(dex_list)}마리)\n본체 공격 +{atk_pct:.1f}%   방어 +{def_pct:.1f}%   치명타 +{crit_pct:.1f}%''')
                        return None
                    self._preset_cap(cat).set(f'''{PRESET_CATEGORY_LABEL.get(cat, cat)}  (최대 {cap}마리)\n⚠ 아직 따로 설정 안 함 - 기본 세팅 동료({len(dex_list)}마리)로 대신 나가요\n본체 공격 +{atk_pct:.1f}%   방어 +{def_pct:.1f}%   치명타 +{crit_pct:.1f}%''')
                    return None
                except Exception:
                    crit_pct = 0
                    def_pct = 0
                    0 = None
                    continue


        
            def _on_category_change(evt = None):
                '''category'''
                label = cat_var.get()
                for None in PRESET_CATEGORY_LABEL.items():
                    c = ()
                    lb = None
                    if not lb == label:
                        continue
                None = None
                None()
                None()

            cat_combo.bind('<<ComboboxSelected>>', _on_category_change)
            None()
            None()
            None(bottom, text = '닫기', command = win.destroy).pack(side = 'left', padx = 6)
            if on_start and on_start_label:
            
                def _start():
                    win.destroy()
                    None()

                None(bottom, text = f'''⚔ {on_start_label}''', bg = '#ffd54a', command = _start).pack(side = 'left', padx = 6)
            self._add_opacity_control(win)
            return None
            except Exception:
                tk.Button
                continue
        except Exception:
            continue
