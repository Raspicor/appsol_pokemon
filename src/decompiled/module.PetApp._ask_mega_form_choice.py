# module.PetApp._ask_mega_form_choice
# source line 11115
# Recovered from bytecode; default argument values are not shown.

def _ask_mega_form_choice(self):
    conf = self.stage_conf()
    result = {
        'form': None }
    win = None(self.root)
    win.title('메가진화 형태 선택')

    try:
        win.attributes('-topmost', True)
        resolve_species_win(win, 340, 220)
        None(win, text = '어느 메가진화 형태로 할까요?', font = ('맑은 고딕', 10, 'bold')).pack(padx = 14, pady = (16, 4))
        None(win, text = '한 번 고르면 나중에 설정에서 다시 바꿀 수 있어요.', font = ('맑은 고딕', 8), fg = '#666', wraplength = 300, justify = 'left').pack(padx = 14, pady = (0, 10))
        btn_row = None(win)
        btn_row.pack(pady = (4, 14))
    
        def _pick(form):
            '''form'''
            result['form'] = form
        
            try:
                win.grab_release()
                win.destroy()
                return None
            except Exception:
                continue


        if not self.mega_display_name_for('x'):
            self.mega_display_name_for('x')
        name_x = 'X 형태'
        if not self.mega_display_name_for('y'):
            self.mega_display_name_for('y')
        name_y = 'Y 형태'
        None(btn_row, text = f'''🔴 {name_x}''', width = 16, command = (lambda : None('x'))).pack(side = 'left', padx = 6)
        None(btn_row, text = f'''🔵 {name_y}''', width = 16, command = (lambda : None('y'))).pack(side = 'left', padx = 6)
        dex_for_stats = conf.get('dex')
        if dex_for_stats in MEGA_XY_STAT_MULT:
            ax = mega_form_stat_mult(dex_for_stats, 'x', 'atk', MEGA_STAT_MULT)
            dx = mega_form_stat_mult(dex_for_stats, 'x', 'def', MEGA_STAT_MULT)
            ay = mega_form_stat_mult(dex_for_stats, 'y', 'atk', MEGA_STAT_MULT)
            dy = mega_form_stat_mult(dex_for_stats, 'y', 'def', MEGA_STAT_MULT)
            None(win, text = f'''X: 공격×{ax:.2f} / 방어×{dx:.2f}  (균형·방어 우위)\nY: 공격×{ay:.2f} / 방어×{dy:.2f}  (공격 특화·방어 약함)''', font = ('맑은 고딕', 7), fg = '#888', justify = 'center').pack(pady = (2, 0))
        win.protocol('WM_DELETE_WINDOW', (lambda : None(None)))
        self._add_opacity_control(win)
        win.update_idletasks()
    
        try:
            win.grab_set()
            win.wait_window()
            return result['form']
            except Exception:
                tk.Button
                continue
        except Exception:
            tk.Button
            continue
