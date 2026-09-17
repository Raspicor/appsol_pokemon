# module.PetApp._open_legend_spin._reveal
# source line 13586
# Recovered from bytecode; default argument values are not shown.

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
