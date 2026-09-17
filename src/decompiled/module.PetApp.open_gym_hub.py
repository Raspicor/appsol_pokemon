# module.PetApp.open_gym_hub
# source line 16767
# Recovered from bytecode; default argument values are not shown.

def open_gym_hub(self):
    win = None(self.root)
    win.title('체육관')
    resolve_species_win(win, 700, 620)

    try:
        win.geometry('700x620')
    
        try:
            win.attributes('-topmost', True)
            bottom = None(win)
            bottom.pack(side = 'bottom', pady = 10)
            top = None(win)
            top.pack(side = 'top', fill = 'x', padx = 14, pady = (12, 4))
            badges = gym_badges_held(self.state)
            None(top, text = f'''🏅 체육관 뱃지 {len(badges)}/{len(GYM_LEADERS)}   (최종공격력 +{gym_badge_atk_bonus_pct(self.state):.1f}%)''', font = ('맑은 고딕', 12, 'bold'), fg = '#1a4a8a').pack(anchor = 'w')
            None(top, text = '이전 체육관을 이겨야 다음 체육관에 도전할 수 있어요. 1번부터 순서대로 도전해보세요!', font = ('맑은 고딕', 8), fg = '#888').pack(anchor = 'w', pady = (2, 0))
            body_outer = None(win)
            body_outer.pack(fill = 'both', expand = True, padx = 10, pady = (6, 0))
            canvas = None(body_outer, highlightthickness = 0)
            vsb = None(body_outer, orient = 'vertical', command = canvas.yview)
            inner = None(canvas)
            inner_win_id = canvas.create_window((0, 0), window = inner, anchor = 'nw')
        
            def _on_gym_inner_configure(evt = None):
                '''all'''
                canvas.configure(scrollregion = canvas.bbox('all'))

            inner.bind('<Configure>', _on_gym_inner_configure)
        
            def _on_gym_canvas_configure(evt = None):
                canvas.itemconfigure(inner_win_id, width = canvas.winfo_width())

            canvas.bind('<Configure>', _on_gym_canvas_configure)
            canvas.configure(yscrollcommand = vsb.set)
            canvas.pack(side = 'left', fill = 'both', expand = True)
            vsb.pack(side = 'right', fill = 'y')
        
            def _gym_wheel(event):
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



        
            def _bind_gym_wheel(_e = None):
                '''<MouseWheel>'''
                canvas.bind_all('<MouseWheel>', _gym_wheel)
                canvas.bind_all('<Button-4>', _gym_wheel)
                canvas.bind_all('<Button-5>', _gym_wheel)

        
            def _unbind_gym_wheel(_e = None):
                '''<MouseWheel>'''
                canvas.unbind_all('<MouseWheel>')
                canvas.unbind_all('<Button-4>')
                canvas.unbind_all('<Button-5>')

            canvas.bind('<Enter>', _bind_gym_wheel)
            canvas.bind('<Leave>', _unbind_gym_wheel)
            win.bind('<Destroy>', (lambda e: if e.widget is win:
    None()))
            cols = 3
            for None in enumerate(GYM_LEADERS):
                i = ()
                g = None
                r = ()
                c = divmod(i, cols)
                idx in badges = None(inner, text = g['name'], padx = 8, pady = 6)
                challengeable = gym_challengeable(self.state, idx)
                type_kr = TYPE_KR.get(g['type'], g['type'])
                ace_dex = g['roster'][-1]
                ace_kr = POKEDEX.get(int(ace_dex), { }).get('kr', '?')
                None(card, text = f'''타입: {type_kr}''', font = ('맑은 고딕', 8)).pack(anchor = 'w')
                None(card, text = f'''에이스: {ace_kr}''', font = ('맑은 고딕', 8)).pack(anchor = 'w')
                if cleared:
                    badge_row = None(card)
                    badge_row.pack(anchor = 'w', pady = (4, 0), fill = 'x')
                    thumb = load_static_image(gym_badge_image_path(g), target_h = 26)
                    if thumb is not None:
                        thumb_photo = None(thumb)
                        thumb_lbl = None(badge_row, image = thumb_photo)
                        thumb_lbl.image = thumb_photo
                        thumb_lbl.pack(side = 'left', padx = (0, 6))
                    None(badge_row, text = f'''✅ 클리어! ({g['badge_kr']})''', font = ('맑은 고딕', 9, 'bold'), fg = '#1a7a3a').pack(side = 'left')
                    None(card, text = '🎮 재미로 재도전 (보상 없음)', font = ('맑은 고딕', 7), command = (lambda ix = idx: (win.destroy(), self._start_gym_challenge(ix, fun_mode = True)))).pack(fill = 'x', pady = (4, 0))
                    continue
                if challengeable:
                    None(card, text = '🟢 도전 가능', font = ('맑은 고딕', 9, 'bold'), fg = '#a8681a').pack(anchor = 'w', pady = (4, 0))
                    None(card, text = '⚔ 도전하기', command = (lambda ix = idx: (win.destroy(), self._start_gym_challenge(ix)))).pack(fill = 'x', pady = (4, 0))
                    continue
                None(card, text = f'''🔒 {idx - 1}번 체육관 클리어 필요''', font = ('맑은 고딕', 8), fg = '#aaa').pack(anchor = 'w', pady = (4, 0))
            tk.Button
            None(bottom, text = '닫기', command = win.destroy).pack()
            self._add_opacity_control(win)
            return None
            except Exception:
                tk.Label
                continue
        except Exception:
            continue
