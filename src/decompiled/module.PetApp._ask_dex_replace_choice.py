# module.PetApp._ask_dex_replace_choice
# source line 11230
# Recovered from bytecode; default argument values are not shown.

def _ask_dex_replace_choice(self, dex, prev_level, new_level):
    entry = POKEDEX.get(int(dex), { })
    old_rows = companion_synergy_breakdown([
        dex], {
        str(dex): {
            'level': prev_level } })
    new_rows = companion_synergy_breakdown([
        dex], {
        str(dex): {
            'level': new_level } })
    old_r = old_rows[0] if old_rows else {
        'crit_pct': 0,
        'def_pct': 0,
        'atk_pct': 0 }
    new_r = new_rows[0] if new_rows else {
        'crit_pct': 0,
        'def_pct': 0,
        'atk_pct': 0 }
    result = {
        'replace': False }
    win = None(self.root)
    win.title('도감 기록 선택')

    try:
        win.attributes('-topmost', True)
        resolve_species_win(win, 400, 320)
        None(win, text = f'''이미 도감에 있는 {entry.get('kr', '?')}를 이번엔 더 낮은 레벨로 잡았어요!''', font = ('맑은 고딕', 10, 'bold'), wraplength = 360, justify = 'left').pack(padx = 14, pady = (14, 4))
        None(win, text = "어느 쪽을 도감에 남길지 골라주세요. (어느 쪽을 고르든 '잡은 횟수'는 그대로 기록돼요)", font = ('맑은 고딕', 9), fg = '#666', wraplength = 360, justify = 'left').pack(padx = 14, pady = (0, 10))
        table = None(win)
        table.pack(padx = 14, pady = (0, 10))
        headers = [
            '',
            '레벨',
            '공격',
            '방어',
            '크리티컬']
        for None in enumerate(headers):
            c = ()
            h = None
        enumerate(headers)
        None(1, '기존', prev_level, old_r, '#1a4a8a')
        None(2, '새로 잡음', new_level, new_r, '#a05a1a')
        None(win) = tk.Frame
        btn_row.pack(pady = (4, 14))
    
        def _pick(replace):
            '''replace'''
            result['replace'] = replace
        
            try:
                win.grab_release()
                win.destroy()
                return None
            except Exception:
                continue


        None(btn_row, text = f'''기존 유지 (Lv.{prev_level})''', width = 16, command = (lambda : None(False))).pack(side = 'left', padx = 6)
        None(btn_row, text = f'''새로 교체 (Lv.{new_level})''', width = 16, command = (lambda : None(True))).pack(side = 'left', padx = 6)
        win.protocol('WM_DELETE_WINDOW', (lambda : None(False)))
        self._add_opacity_control(win)
        win.update_idletasks()
    
        try:
            win.grab_set()
            win.wait_window()
            return result['replace']
            except Exception:
                tk.Button
                continue
        except Exception:
            tk.Button
            continue
