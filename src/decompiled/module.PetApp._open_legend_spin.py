# module.PetApp._open_legend_spin
# source line 13546
# Recovered from bytecode; default argument values are not shown.

def _open_legend_spin(self, candidates, gen, refresh_cb, level_range):
    winner = None(candidates)
    win = None(self.root)
    win.title(f'''🔮 {gen}세대 전설조우 토큰''')
    resolve_species_win(win, 300, 320)

    try:
        win.attributes('-topmost', True)
        win.protocol('WM_DELETE_WINDOW', (lambda : pass))
        None(win, text = '🌿 수풀이 부스럭부스럭...', font = ('맑은 고딕', 11, 'bold')).pack(pady = (14, 6))
        img_label = None(win, font = ('Segoe UI Emoji', 42))
        img_label.pack(pady = 10)
        name_var = None(value = '？？？')
        None(win, textvariable = name_var, font = ('맑은 고딕', 10, 'bold'), wraplength = 260, justify = 'center').pack()
        note_var = None(value = '')
        None(win, textvariable = note_var, font = ('맑은 고딕', 9), fg = '#555', wraplength = 260, justify = 'center').pack(pady = (2, 4))
        btn_row = None(win)
        btn_row.pack(pady = (4, 12))
        BUSH_FRAMES = [
            '🌿',
            '🌾',
            '🍃',
            '🌳']
        spin_state = {
            'idx': 0,
            'phase': 'spin',
            'job': None }
    
        def _tick_spin():
            '''phase'''
            if spin_state['phase'] != 'spin':
                return None
            jitter = random.randint * None(0, 2)
            img_label.configure(text = jitter + BUSH_FRAMES[spin_state['idx'] % len(BUSH_FRAMES)], image = '')
            win.after(140, _tick_spin) = None

    
        def _reveal():
            entry = POKEDEX.get(winner, { })
            img = self._sprite_preview_image(winner, size = 96, silhouette = False)
            img_label.configure(image = img, text = '')
            img_label.image = img
            name_var.set(f'''✨ {entry.get('kr', '?')} 등장!''')
            bundles = self._legend_bundles(gen)
            match = (lambda .0: for b in .0:
    if not int(b.get('dex', -1)) == int(winner):
    continueb.0)(bundles(), None)
            self.state[f'''legend_token_gen{gen}'''] = bundles
            self.save_state()
            if refresh_cb:
            
                try:
                    None()
                    note_var.set(f'''레벨 {level}! 이 전설에게 총 {attempts}번 도전할 수 있어요.''')
                
                    def _fight_now():
                        win.destroy()
                        self.open_battle(entry, level, legend_token_gen = gen)

                
                    def _close_only():
                        '''PikaPet'''
                        win.destroy()
                        None('PikaPet', f'''도감에서 \'{entry.get('kr', '?')}\' 항목을 열면 언제든 도전할 수 있어요.''')

                    None(btn_row, text = '바로 도전하겠습니다!', wraplength = 220, justify = 'center', command = _fight_now).pack(pady = (0, 4))
                    None(btn_row, text = '나중에 하겠습니다', wraplength = 220, justify = 'center', command = _close_only).pack()
                    return None
                except Exception:
                    None if level_range else random.randint
                    continue


    
        def _stop():
            '''phase'''
            if spin_state['phase'] != 'spin':
                return None
            spin_state['phase'] = None
            if spin_state['job'] is not None:
            
                try:
                    win.after_cancel(spin_state['job'])
                    spin_state['job'] = None
                    stop_btn.configure(state = tk.DISABLED, text = '멈추는 중...')
                    n_more = None(6, 9)
                
                    def _step(i):
                        if i >= n_more:
                            stop_btn.pack_forget()
                            None()
                            return None
                        jitter = random.randint * None(0, 2)
                        img_label.configure(text = jitter + BUSH_FRAMES[i % len(BUSH_FRAMES)], image = '')
                        frac = i / max(1, n_more - 1)
                        delay = 140 + int(420 * frac ** 2.2)
                        win.after(delay, (lambda : None(i + 1)))

                    None(0)
                    return None
                except Exception:
                    continue


        stop_btn = None(win, text = '🛑 지금 멈추기!', font = ('맑은 고딕', 10, 'bold'), command = _stop)
        stop_btn.pack(pady = (0, 4))
        self._add_opacity_control(win)
        None()
        return None
    except Exception:
        random.choice
        continue
