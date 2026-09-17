# module.PetApp.open_evolution_tab._build_summary_bar
# source line 8836
# Recovered from bytecode; default argument values are not shown.

def _build_summary_bar():
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
