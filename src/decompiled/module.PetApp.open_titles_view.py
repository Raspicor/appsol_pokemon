# module.PetApp.open_titles_view
# source line 14929
# Recovered from bytecode; default argument values are not shown.

def open_titles_view(self):
    self._backfill_missing_titles()
    win = None(self.root)
    win.title('🏆 칭호')
    resolve_species_win(win, 440, 580)

    try:
        win.attributes('-topmost', True)
        tab_var = None(value = 'equip')
        tab_row = None(win)
        tab_row.pack(fill = 'x', padx = 14, pady = (12, 0))
        equip_tab_btn = None(tab_row, text = '🏅 장착', font = ('맑은 고딕', 9, 'bold'), width = 12)
        list_tab_btn = None(tab_row, text = '📜 리스트', font = ('맑은 고딕', 9, 'bold'), width = 12)
        equip_tab_btn.pack(side = 'left', padx = (0, 4))
        list_tab_btn.pack(side = 'left')
        detail_frame = None(win, text = '칭호 상세 (지금 장착 중)', font = ('맑은 고딕', 8, 'bold'), fg = '#1a4a8a')
        detail_frame.pack(fill = 'x', padx = 14, pady = (10, 4))
        detail_var = None()
        None(detail_frame, textvariable = detail_var, font = ('맑은 고딕', 8), fg = '#333', justify = 'left', anchor = 'w', wraplength = 390).pack(fill = 'x', padx = 8, pady = 6)
    
        def _show_detail(tid, label, extra_head = ''):
            '''
    '''
            head = f'''{label}\n''' if label else ''
            txt = f'''{head}{extra_head}{title_effect_text(tid)}'''
            detail_var.set(txt)
            detail_frame.configure(text = '칭호 상세')

    
        def _show_equipped_default():
            '''장착 중인 칭호가 있으면 그 효과를, 없으면 안내 문구를 보여준다.
    창을 처음 열 때, 그리고 장착/해제할 때마다 다시 불러서 최신 상태로 맞춘다.'''
            eid = title_equipped_id(self.state)
            if eid:
                if not title_equipped_label(self.state):
                    title_equipped_label(self.state)
                elabel = eid
                detail_var.set(f'''👑 {elabel}\n{title_effect_text(eid)}''')
                detail_frame.configure(text = '칭호 상세 (지금 장착 중)')
                return None
            None.set('지금 장착한 칭호가 없어요. 아래에서 마스터 칭호를 장착하거나,\n칭호를 눌러보면 여기에 상세 효과가 나와요.')
            detail_frame.configure(text = '칭호 상세')

        outer = None(win)
        outer.pack(fill = 'both', expand = True)
        canvas = None(outer, highlightthickness = 0)
        vsb = None(outer, orient = 'vertical', command = canvas.yview)
        body = None(canvas)
        body.bind('<Configure>', (lambda e: canvas.configure(scrollregion = canvas.bbox('all'))))
        canvas.create_window((0, 0), window = body, anchor = 'nw')
        canvas.configure(yscrollcommand = vsb.set)
        canvas.pack(side = 'left', fill = 'both', expand = True, padx = (14, 0), pady = (4, 14))
        vsb.pack(side = 'right', fill = 'y')
    
        def _wheel(e):
            canvas.yview_scroll(-1 if e.delta > 0 else 1, 'units')

        win.bind('<MouseWheel>', _wheel)
    
        def _bind_click(widget, fn):
            '''<Button-1>'''
            widget.bind('<Button-1>', (lambda e: None()))

    
        def _refresh_equip_tab():
            bonus = title_atk_bonus_pct(self.state)
            stat_mult = title_stat_mult(self.state)
            stat_pct_extra = (stat_mult - 1) * 100
            equipped_label = title_equipped_label(self.state)
            equip_line = f'''\n👑 장착 중: {equipped_label} (아래 상세보기에서 정확한 장착효과를 볼 수 있어요, 이름 앞에도 표시돼요)''' if equipped_label else "\n👑 지금 장착한 칭호가 없어요. 장착 가능한 칭호 옆의 '장착하기' 버튼으로 골라보세요."
            extra_line = f'''\n총 스탯(HP/공격/방어) 배율: +{stat_pct_extra:.0f}% 적용 중''' if stat_pct_extra > 0 else ''
            None(body, text = f'''보유효과 합산: 최종공격력 +{bonus:.1f}% (체육관 뱃지 위에 별도로 곱해져요){extra_line}{equip_line}''', font = ('맑은 고딕', 9, 'bold'), fg = '#1a4a8a', wraplength = 380, justify = 'left').pack(anchor = 'w', pady = (0, 10))
            earned = self.state.get('titles_earned', [])
            if not earned:
                None(body, text = '아직 획득한 칭호가 없어요. 무한성장미터에 도전해보세요!', font = ('맑은 고딕', 9), fg = '#888', wraplength = 380, justify = 'left').pack(pady = 20)
                return None
            earned = tk.Label(earned, (lambda t: if isinstance(t, dict):
    t.get('id')))
            for t in earned:
                row = None(body, relief = 'groove', bd = 1, cursor = 'hand2')
                row.pack(fill = 'x', pady = 3)
                equippable = _is_equippable_title(tid)
                if equippable:
                    equippable
                is_equipped = title_equipped_id(self.state) == tid
                head = f'''🏆 {label}''' + ' 👑(장착 중)' if is_equipped else ''
                head_lbl = None(row, text = head, font = ('맑은 고딕', 9, 'bold'), anchor = 'w', justify = 'left', wraplength = 320, cursor = 'hand2')
                head_lbl.pack(anchor = 'w', padx = 6, pady = (4, 0))
                when_lbl = None
                if when:
                    when_lbl = None(row, text = when, font = ('맑은 고딕', 7), fg = '#999', cursor = 'hand2')
                    when_lbl.pack(anchor = 'w', padx = 6)
                effect_lbl = None(row, text = title_effect_text(tid), font = ('맑은 고딕', 7), fg = '#4a7a3a', justify = 'left', anchor = 'w', wraplength = 340, cursor = 'hand2')
                effect_lbl.pack(anchor = 'w', padx = 6, pady = (1, 0))
                for w_ in (row, head_lbl, effect_lbl) + (when_lbl,) if when_lbl else ():
                    None(w_, (lambda label = label, tid = tid: None(tid, f'''🏆 {label}''')))
                (row, head_lbl, effect_lbl) + (when_lbl,) if when_lbl else ()
                if not equippable:
                    continue
                btn_row = None(row)
                btn_row.pack(anchor = 'e', padx = 6, pady = (2, 4))
                if is_equipped:
                    None(btn_row, text = '장착 해제', font = ('맑은 고딕', 8), command = (lambda : (None(), _refresh, None()))).pack(side = 'right')
                    continue
                None(btn_row, text = '장착하기', font = ('맑은 고딕', 8), command = (lambda tid = tid: (None(), _refresh, None()))).pack(side = 'right')
            tk.Button

    
        def _refresh_list_tab():
            '''titles_earned'''
            earned_ids = set()
            for t in self.state.get('titles_earned', []):
                eid = t.get('id') if isinstance(t, dict) else t
                if not isinstance(eid, str):
                    continue
                earned_ids.add(eid)
            None(body, text = '게임에 있는 모든 칭호예요. 보유 중이 아니어도 번호와 조건을 볼 수 있어요.', font = ('맑은 고딕', 8), fg = '#888', wraplength = 380, justify = 'left').pack(anchor = 'w', pady = (0, 8))
            for None in enumerate(all_title_defs(), start = 1):
                tid = ()
                label = (i,)
                cond = None
                is_master = enumerate(all_title_defs(), start = 1)
                f'''{i}. {label}  [{status}]''' = '✅ 보유 중' if owned else '🔒 미보유'
                head_lbl = None(row, text = head, font = ('맑은 고딕', 9, 'bold'), fg = '#1a4a8a' if owned else '#888', anchor = 'w', justify = 'left', wraplength = 380, cursor = 'hand2')
                head_lbl.pack(anchor = 'w', padx = 6, pady = (4, 2))
                effect_lbl = None(row, text = title_effect_text(tid), font = ('맑은 고딕', 7), fg = '#4a7a3a', justify = 'left', anchor = 'w', wraplength = 380, cursor = 'hand2')
                effect_lbl.pack(anchor = 'w', padx = 6, pady = (0, 2))
                cond_lbl = None(row, text = f'''조건: {cond}''', font = ('맑은 고딕', 8), fg = '#666', anchor = 'w', justify = 'left', wraplength = 380, cursor = 'hand2')
                cond_lbl.pack(anchor = 'w', padx = 6, pady = (0, 4))
            
                def _on_click(tid = tid, label = label, cond = cond, owned = owned):
                    '''✅ 보유 중'''
                    head_txt = f'''{'✅ 보유 중' if owned else '🔒 아직 미보유'} - {label}\n조건: {cond}\n'''
                    None(tid, '', extra_head = head_txt)

                for w_ in (row, head_lbl, effect_lbl, cond_lbl):
                    None(w_, _on_click)
                (row, head_lbl, effect_lbl, cond_lbl)
            tk.Label

    
        def _refresh():
            '''equip'''
            for w in body.winfo_children():
                w.destroy()
            if tab_var.get() == 'equip':
                equip_tab_btn.configure(relief = 'sunken', bg = '#dbe7ff')
                list_tab_btn.configure(relief = 'raised', bg = 'SystemButtonFace')
                None()
                return None
            None.configure(relief = 'sunken', bg = '#dbe7ff')
            equip_tab_btn.configure(relief = 'raised', bg = 'SystemButtonFace')
            None()

    
        def _switch(tab):
            tab_var.set(tab)
            None()

        equip_tab_btn.configure(command = (lambda : None('equip')))
        list_tab_btn.configure(command = (lambda : None('list')))
        None()
        None()
        None(win, text = '닫기', command = win.destroy).pack(pady = (0, 14))
        self._add_opacity_control(win)
        return None
    except Exception:
        continue
